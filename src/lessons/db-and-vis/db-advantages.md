# Database Advantages

There are lots of advantages to using databases, for example:

- Fewer bugs
- Consistency
- Scalability
- Security
- Faster performance

## Fewer bugs
We already saw one advantage of using a database. The column names and table names are defined beforehand. From then on, any typos in the column or table name are detected instantly because an error will be occur. (This is better than the program silently not working).

In this way, modeling data using databases can prevent many kinds of subtle data corruption and integrity issues.

## Consistency 
Databases help ensure data consistency by enforcing constraints, such as data type and integrity rules, preventing invalid data from being entered. For example, if you try to enroll a student in a course that does not exist, a database can prevent such an error from happening.

## Scalability 
Databases can handle large amounts of data and can be scaled up or down to accommodate changing business needs. It can also be distributed across multiple machines.

## Security
Databases provide several security mechanisms to protect the data they store, including authentication, authorization, auditing, and backup and recovery. You can control who can see or edit data on all or part of the database.

## Faster Performance
Databases are optimized for performance when working with large data sets. While it's possible to write programs that manage data as quickly or more quickly as databases, it can take massive effort.

Let's measure the speed of the two versions of the Song program, to see the difference in speed between the database version and the JSON file. 

How long does it take to update the number-of-times-listened-to?

(The db file for this example can be found here, [songs-kibo.db](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/songs-kibo.db) and [songs-kibo.json](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/songs-kibo.json).)

We'll run each update 1000 times to get a better statistical sample size. (If we only compared the times a few times, it could give misleading results. For example, there could be a background process that runs at the same time, which happens to interfere with the test).

A first shot at a comparison is here:

```python
def bad_test_with_json():
    for _ in range(1000):
        song_list = SongListUsingJson('songs-kibo.json')
        song_id = song_list.get_song_id('Fatela')
        song_list.increase_times_listened_to(song_id)

def bad_test_with_db():
    for _ in range(1000):
        song_id = get_song_id('songs-kibo.db', 'Fatela')
        increase_times_listened_to('songs-kibo.db', song_id)
        
```

This isn't a good way to measure the speed difference. The database version has to reconnect for each iteration of the loop.

A more realistic test:

```python
def test_with_json():
    song_list = SongListUsingJson('songs-kibo.json')
    for row in song_list.data['songs']:
        if row['name'] == 'Fatela':
            row_found = song
    for _ in range(1000):
        row_found['times_listened_to'] += 1
        song_list.save()
    
def test_with_db():
    song_id = get_song_id('songs-kibo.db', 'Fatela')
    conn = sqlite3.connect('songs-kibo.db')
    for _ in range(1000):
        increase_times_listened_to_db(conn, song_id)

import time
start = time.time()
test_with_json()
end = time.time()
duration = (end - start)
print(f'Completed in {duration} seconds.')

import time
start = time.time()
test_with_db()
end = time.time()
duration = (end - start)
print(f'Completed in {duration} seconds.')
```

This time, it's a more realistic example because the connections are stored. In fact, for the json version the row is stored, which isn't very good programming practice but we're trying to see the maximum speed of the json version.

The results still show a signficant difference.

On my computer, the JSON version completes in `16.003` seconds. The database version completes in `3.987` seconds, which is more than four times faster.

Why is it faster? The Sqlite .db file is structured in a very specific way. Updating one row doesn't necessitate writing the entire file out again. The sqlite database code can move around inside the `.db` file and replace only a few bytes at a time.

This advantage gets better and better when the data sets are larger. Imaging working with a data set that is hundreds of megabytes. The json file approach of writing the entire file on every `save()` would be far too slow.

* Why do we need to call `save()` or `commit()` so often, if this is a slow part of the program?
* Could we move it to the end of the program?
* The issue is that we need to be careful about crashes,
* When using a database we want to call `save()` or `commit()` relatively often, because otherwise if a crash occurs, all of the recent changes would be gone - the changes wouldn't actually be written to the output file yet.

### Reflections

Database aren't magic. You could write a database system yourself, if you had enough time.

You could write a Python program that takes a string like `"insert into Students (firstname, lastname) values ('John', 'Anderson')"`. It could split apart the string, find the values, and recognize the meaning of the syntax. It could make a dictionary, and then save the dictionary to a JSON file on disk. When a program sent your program a string like `'select from Students where firstname="John"'`, your program could interpret the string, read the json file and get the result.

This is essentially what database programs do. 

Over the years, developers have optimized database programs to be faster and more resilient to errors. Database systems are careful about what data is stored in memory (e.g. in lists and dictionaries). For example, because data is stored on disk, it doesn't also need to be held in memory. The json version is inefficient because the entire data set is stored both on disk and in the in-memory lists and dictionaries. It doesn't necessarily need to be in both. So databases have an advantage for reduced memory usage, and can even store multi-gigabyte databases that would be too big to store in memory.

Databases can also use what is known as an index to make queries run quickly.

Databases often have a layer that coordinates access, so that many different programs can connect to the same data set at the same time. This would be hard to do with a JSON file. Even if two programs took turns accessing the file, it would be complicated to prevent one program from writing over the changes made by the other program.

So in summary, even though writing your own database system would be possible, it makes sense to use an existing system, because years of effort have gone into optimizing a system like SQLite.

Databases aren't always the perfect choice. It's easy to look inside a JSON file to see what the data looks like. To see inside a sqlite db file, one has to use a specialized tool, like the program `DB Browser for SQLite`. The code for databases is often more complex, and execution speed is often not needed. For small structured data, like program configuration, a JSON file is probably a better choice than a database.

# Database Advantages

There are lots of advantages to using databases:

- Fewer bugs
- Simpler code
- Faster performance

## Fewer bugs

We already saw one advantage of using a database. The column names and table names are defined ahead of time. From then on, any typos in the column or table name are detected instantly because an error will be occur. An error is better than the program silently not working, like the bug in the JSON version of the Songs program.

As you've learned, modeling data using databases can prevent lots of other kinds of subtle data corruption and integrity issues.

## Simpler Code

When using lists instead of a database, your program often needs many loops. Your program is simpler when you can use SQL's SELECT statements to get data, instead of looping through a list of objects. The sql statement `SELECT FROM Songs WHERE artist='Myley Cyrus' and name='Flowers'` is quite clear. The list implementation would need to loop through the list and check two conditions for each item. With a database, on the other hand, you don't need to write the loops.

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

Can we skip the `save()` method until the very end of the program? Wouldn't that make the program run a lot faster? Usually we can't - this would mean that if the program crashes, all of the progress and recent changes would be completely lost.

### Reflections

Database aren't magic. You could write a database system yourself, if you had enough time! 

You could write a Python program that takes a string like `insert into Students (firstname, lastname) values ("John", "Anderson") `. It could split apart the string, find the values, and recognize the meaning of the syntax. It could make a dictionary, and then save the dictionary to a JSON file on disk. When a program sent your program a string like `select from Students where firstname='John'`, your program could interpret the string, read the json file and get the result.

This is essentially what database programs do. 

Over the years, developers have optimized database programs to be faster and more resilient to errors. Database systems are careful about what data is stored in memory (e.g. in lists and dictionaries). For example, because data is stored on disk, it doesn't also need to be held in memory. The json version is inefficient because the entire data set is stored both on disk and in the in-memory lists and dictionaries. It doesn't necessarily need to be in both. So databases have an advantage for reduced memory usage, and can even store multi-gigabyte databases that would be too big to store in memory.

Databases can also use an **index** to make queries run quickly.

Databases often have a layer that coordinates access, so that many different programs can connect to the same data set at the same time. If doing this with a JSON file, even if the two programs took turns accessing the file, it'd be very hard to avoid the possibility of one program to mistakenly writing over the changes made by the other program.

Databases aren't always the perfect choice, though. It's easy to look inside a JSON file to see what the data looks like. To see inside a sqlite db file, one has to use a specialized tool, like the program `DB Browser for SQLite`. The code for databases is often more complex, and execution speed is often not needed. For small structured data, like program configuration, a JSON file is probably a better choice than a database.

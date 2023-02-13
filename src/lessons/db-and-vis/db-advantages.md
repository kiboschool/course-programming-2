
## Database Advantages

We already saw one slight advantage of using a database. The column names and table names are defined ahead of time. From then on, any typos in the column or table name are detected instantly because an error will be occur. (The error message is better than the program silently not working, like the bug that was in the json version).

Also, when using lists instead of a database, your program often needs many loops, at least one for each type of query. Your program is simpler when you can write `SELECT FROM Songs WHERE artist='Myley Cyrus' and name='Flowers'`. The list implementation would need to loop through the list and check for a row that matches. With a database, on the other hand, you don't need to write the loops.

### Measuring speed

Let's measure the speed of the programs. How long does it take to update the number-of-times-listened-to?

(The db file for this example can be found here, [songs-kibo.db](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/songs-kibo.db) and [songs-kibo.json](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/db-and-vis/songs-kibo.json).)

We'll run it 1000 times to get a better statistical sample size. (If we only compared the times a few times, it's not a good test. For example, there could be a background process happening to run at the same time that interferes with the test).

A first shot at a comparison is here,

```
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

This isn't a good way to measure how fast it is, because it has to reconnect every time in the loop.

A more realistic test:


```
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

On my computer, using json completes in `16.003` seconds. Using the database completes in `3.987` seconds, which is more than four times faster.

Why is it faster? The Sqlite .db file is structured in a very specific way. Updating one row doesn't necessitate writing the entire file out again. The sqlite database code can move around inside the `.db` file and replace only a few bytes at a time.

This advantage gets better and better when the data sets are larger. Imaging working with a data set that is hundreds of megabytes. The json file approach of writing the entire file on every `save()` would be far too slow.

Can we skip the `save()` method for the very end of the program? Wouldn't that make the program run a lot faster? Usually we can't - this would mean that if the program crashes, all of the progress and recent changes would be completely lost.

### Reflections

They aren't completely magical, though. You could write a database system yourself if you had enough time. You could write a Python program that takes a string like `insert into Students (firstname, lastname) values ("John", "Anderson") `. Your program could split apart the string and find the values. It could then make a dictionary, and then save the dictionary to a json file on disk. When a program sent your program a string like `select from Students where firstname='John'`, your program could interpret the string, read the json file and get the result.

This is essentially what database programs do. 

The difference is that over the years, companies have optimized the database programs to be faster and faster. One difference is that a database system is careful about what data is stored in memory (e.g. in lists and dictionaries). For example, because data is stored on disk, it doesn't also need to be held in memory. The json version is inefficient because the entire data set is stored both on disk and in the in-memory lists and dictionaries, it doesn't actually need to be in both. (So databases have an advantage for reduced memory usage, and can even store multi-gigabyte databases that would be too big to store in memory).

You also saw in the web applications course that databases can use an **index** to make queries run quickly.

Databases also have a layer that coordinates access, so that many different programs can connect to the same data set at the same time. (If doing this with a json file, even if the two programs took turns accessing the file, it'd be very hard to avoid the possibility of one program to mistakenly writing over the changes made by the other program).

Databases aren't always the perfect choice, though. It's easy to look inside a json file to see what the data looks like. To see inside a sqlite db file one has to use a specialized tool, like the program `DB Browser for SQLite`. The code for databases is often more complex, and execution speed is often not needed.

JSON files and databases are both useful tools, each can be better depending on the situation.


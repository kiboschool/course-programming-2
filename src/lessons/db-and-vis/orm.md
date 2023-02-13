
## ORM

### Sending SQL strings to the database considered harmful?

The SQLite code you saw worked like this: It built a string, and then sent the string to a connection. It didn't really feel like typical Python.

Also, because the program was building a string, there is the possibility of bugs occuring. There could be typos in table names, and VSCode could not show any misspellings.

Even worse, if the user could control what was put into the string, it can cause an even more serious bug.

Consider this line of code

```
sql = "UPDATE Songs SET name = " + name + " WHERE id = " + song_id;
cursor = conn.execute(sql)
```

This seems to work at first. But if the user were able to type in a `song_id` of `1 or TRUE`, the sql that would be executed would be  

```
UPDATE Songs SET name = changed WHERE id = 1 or TRUE
```

This would change the name on **every single row**. This is called [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) and malicious hackers can use it to break into computer systems!

By using the question marks,

```
conn.execute("UPDATE Songs SET nme = ? WHERE id=?", [song_name, song_id])
```

We are safe from SQL injection, but there is still the possibility that new code will forget to use a `?` question mark, and it's hard to be 100% sure that all of the right places have a question mark.

### An ORM

Instead of making a string and sending it to the database system, it would be better to work in terms of objects.

What if we thought of a database row as an object. The internal data would be the columns. The behavior would include modifying the data and saving it back to the database.

The syntax would now be very pythonic. It would look similar to working with other objects - it would look similar to the non-database versions of the program - and there would not be any need to see sql (a different language).

It's a bit of a stretch, but we can also kind of think of the database table as an object too. The internal data is the rows, and it has behavior like queries, inserts, and deletes.

We could write wrapping code like this, that converts sql code into more object-oriented easier-to-use code:

```python

# (this is just psuedocode sketching it out)

class SongsTable:
    def insert(self, new_row):
        sql = 'INSERT INTO Songs (id, name, artist, times_listened_to) values (?, ?, ?, ?)'
        self.conn.execute(sql, [new_row.id, new_row.name, new_row.artist, new_row.times_listened_to ])
        
    def query_by_name(self, name):
        sql = 'SELECT FROM Songs WHERE name = ?' 
        return SongsRow(self.conn.execute(sql, [name]))
        
class SongsRow:
    def __init__(self, initialrow=None):
        self.id = 0
        self.name = ''
        self.artist = ''
        self.times_listened_to = 0
        # read from initialrow...
        
    def update_name(self, new_name):
        self.name = new_name
        sql = 'UPDATE Songs set name=? where id=?'
        # ...
        return self.conn.execute(sql, [new_name id])
        
    def update_times_listened_to(self, times_listened_to)
        self.times_listened_to = times_listened_to
        sql = 'UPDATE Songs set times_listened_to=? where id=?'
        # ...
        return self.conn.execute(sql, [times_listened_to, id])
    
    # ...
    # ...
    # ...

```

Now the code will feel like Python. `row.update_name('new_name')`.

This is a great example of the object-oriented principle of hiding irrelevant details. Now that the program uses classes and objects, the calling code can simply call `update_times_listened_to`. It doesn't need to know any SQL, or even know that the class is interacting with a database at all. The program has defined an **interface** that has only the relevent details. The irrelevent details, like what SQL is being passed to the database, is nicely hidden so that calling code doesn't need to be concerned about it.

Imagine, though, if your database had dozens of tables. Would you need to write these full classes for each table? There would be a lot of duplicated work, and it would all do the essentially the same thing, building the same sql to send.

The answer is that if you use a system called an ORM, it will create the code for you. All you need to do is tell the ORM the table name and the columns, and it will generate all of the other methods automatically!

A good example of an ORM is called SQLAlchemy. When you set up SQLAlchemy it writes all of the sql for you, and all you need to do is tell it about your tables and columns. From then on, you can write nice object-oriented code.

This is a slow video, but it explains how to use SQLAlchemy,

https://www.youtube.com/watch?v=70mNRClYJko


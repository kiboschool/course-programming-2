# What is an ORM?

## Reconsidering sending SQL strings to the database

The SQLite code you saw worked like this: 
- it built a string
- then it sent the string to a connection

It didn't really feel like typical Python. It had a whole other language embedded in it!

Also, because the program was building a string, there is the possibility of bugs. There could be typos in the sql commands or the table names. Since the SQL is in a string, VSCode could not show any misspellings or syntax errors.

Even worse, if the user could control what was put into the string, it can cause an even more serious bug.

Consider this line of code

```python
sql = "UPDATE Songs SET name = " + name + " WHERE id = " + song_id;
cursor = conn.execute(sql)
```

This seems to work at first. But if the user were able to type in a song_id of `1 or TRUE`, the SQL that would be executed would be

```sql
UPDATE Songs SET name = changed WHERE id = 1 or TRUE
```

This would change the name on **every single row**. This is called [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) and malicious hackers can use it to break into computer systems!

You saw how to protect from SQL injection, using question marks to parameterize queries:

```python
conn.execute("UPDATE Songs SET nme = ? WHERE id=?", [song_name, song_id])
```

However, there is still the possibility that new code will forget to use parameterized queries, and it's hard to be 100% sure that all of the right places have a question mark.

### A better approach

Instead of making a string and sending it to the database system, it's often easier to work with objects.

What if we thought of a database row as an object. The Object's internal data attributes would be the columns. The behavior would include modifying the data and saving it back to the database.

The syntax would now be very pythonic. It would look similar to working with other objects - it would look similar to the non-database versions of the program - and there would not be any need to see or write the SQL by hand.

We can also kind of think of the database table as an object too. The internal data is the rows, and it has behavior like queries, inserts, and deletes.

Here is an unfinished pseudocode example of classes like this, that use an object-oriented style:

```python
class SongsTable:
    def insert(self, new_row):
        sql = 'INSERT INTO Songs (id, name, artist, times_listened_to)' + 
            'values (?, ?, ?, ?)'
        self.conn.execute(sql, [new_row.id, new_row.name, new_row.artist,
            new_row.times_listened_to])
        
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
```

This code would feel like Python. You would write `song.update_name('new_name')`, instead of writing out the UPDATE query.

This is a great example of the object-oriented principle of **Abstraction**: hiding irrelevant details. Now that the program uses classes and objects, the calling code can call `update_times_listened_to` instead of thinking about the database. It doesn't need to know any SQL, or even know that the class is interacting with a database at all. The program has defined an **interface** that has only the relevent details. The irrelevent details, like what SQL is being passed to the database, are hidden, so that calling code doesn't need to be concerned about it.

Imagine, though, if your database had dozens of tables. You would need to write classes for each table! There would be a lot of duplication, and it would all do the essentially the same thing, building the same SQL to send to the database.

Instead, you can use an Object-Relational Mapper (**ORM**). The ORM  will create the SQL code for you. All you need to do is tell the ORM the table name and the columns, and it will generate the other methods automatically!

One popular Python ORM system is SQLAlchemy. When you set up SQLAlchemy, it writes all of the sql for you, and all you need to do is tell it about your tables and columns. From then on, you can write nice object-oriented code.

## Video: SQLAlchemy

This video is a bit long, but it introduces how to use SQLAlchemy.

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/70mNRClYJko" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

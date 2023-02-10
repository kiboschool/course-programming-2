
### Writing a Python program to interact with databases

Today we will use the SQLite database system.

* It is simpler than other systems because it runs on your own computer, and saves its data to a file you can easily see.
* SQLite is already included as part of Python.

This is an example - let's build a database to keep a list of Songs on our computer, and store how many times we have listened to them.

The code to create a database file and a table named Tracks with two columns in
the database is as follows:
import sqlite3
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
conn.close()

The connect operation makes a **connection** to the database stored in the file
music.sqlite in the current directory. If the file does not exist, it will be created.
The reason this is called a connection is that sometimes the database is stored
on a separate database server from the server on which we are running our
application. In our simple examples the database will just be a local file in the
same directory as the Python code we are running.


A cursor is like a file handle that we can use to perform operations on the data
stored in the database. Calling cursor() is very similar conceptually to calling
open() when dealing with text files.

Once we have the cursor, we can begin to execute commands on the 
the database using the execute() method.

You'll remember that database commands are expressed in a special language, Structured Query Language or SQL for
short.

The first SQL command removes the Tracks table from the database if it exists.
This pattern is simply to allow us to run the same program to create the Tracks
table over and over again without causing an error. Note that the DROP TABLE
command deletes the table and all of its contents from the database (i.e., there is
no “undo”).

`cur.execute('DROP TABLE IF EXISTS Tracks ')`

The second command creates a table named Tracks with a text column named
title and an integer column named plays.

`cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')`

Now that we have created a table named Tracks, we can put some data into that
table using the SQL INSERT operation. Again, we begin by making a connection
to the database and obtaining the cursor. We can then execute SQL commands
using the cursor.

The SQL INSERT command indicates which table we are using and then defines a
new row by listing the fields we want to include (title, plays) followed by the
VALUES we want placed in the new row. We specify the values as question marks
(?, ?) to indicate that the actual values are passed in as a tuple ( 'My Way',
15 ) as the second parameter to the execute() call.

```
import sqlite3
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
('My Way', 15))
conn.commit()
print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()
cur.close()

```

First we INSERT two rows into our table and use commit() to force the data to be
written to the database file.

Then we use the SELECT command to retrieve the rows we just inserted from the
table. On the SELECT command, we indicate which columns we would like (title,
plays) and indicate which table we want to retrieve the data from.
After we
execute the SELECT statement, the cursor is something we can loop through in a
for statement. For efficiency, the cursor does not read all of the data from the
database when we execute the SELECT statement. Instead, the data is read on
demand as we loop through the rows in the for statement.

At the very end of the program, we execute an SQL command to DELETE the
rows we have just created so we can run the program over and over. The DELETE
command shows the use of a WHERE clause that allows us to express a selection
criterion so that we can ask the database to apply the command to only the rows
that match the criterion. In this example the criterion happens to apply to all the
rows so we empty the table out so we can run the program repeatedly. After the DELETE is performed, we also call commit() to force the data to be removed from
the database.

### Structured Query Language summary

```
CREATE TABLE Tracks (title TEXT, plays INTEGER)

To insert a row into a table, we use the SQL INSERT command:
INSERT INTO Tracks (title, plays) VALUES ('My Way', 15)

The SQL SELECT command is used to retrieve rows and columns from a database.
The SELECT statement lets you specify which columns you would like to retrieve
as well as a WHERE clause to select which rows you would like to see. 

SELECT title,plays FROM Tracks 

You can request that the returned rows be sorted by one of the fields as follows:
SELECT title,plays FROM Tracks ORDER BY title

``

<font size="-1">Uses material from Python for everybody. Dr. Charles R. Severance</font>
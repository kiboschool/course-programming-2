
## Databases in Python

You have already worked with databases, but here is a short reminder and review on what a database is.

A database system is a way to store data. There are many different database systems, including MySQL, PostgreSQL, and SQLite, each used for different purposes. Sometimes the database is running on the same computer your program is running on, and sometimes the database is running on a different computer, and your program accesses it over the internet. The database system, behind the scenes, places the data in specially structured files on disk.

Like a dictionary, database software is designed to keep the inserting and accessing of data very fast, even for large amounts of data.

You'll be working with a type of database called a relational database. This type of database has **tables**, **rows**, and **columns**.

```
(example image of rows and columns)
```

### Details

Database systems aren't magic. You could create your own if you wanted to, it would just take time! You could write a Python program that takes a string like `insert into Students (firstname, lastname) values ("John", "Anderson") `. Your program could split apart the string and find the values. It could then make a dictionary, and then save the dictionary to a json file on disk. When a program sent your program a string like `select from Students where firstname='John'`, your program could interpret the string, read the json file and get the result.

This is essentially what database programs do. 

One key difference between a database and a dictionary in Python is that for a relational database, the columns are set up in advance.

If you have a dictionary 

`student = {"firstname": "John", "lastname": "Anderson"}`

you can add a new section of data onto it

`student['age'] = 26`

But if you are working with a database,

`update students set age=26 where firstname='John' and lastname='Anderson'`

This won't work unless you have already created a column for `age`. All of the columns need to be specified ahead of time.

Why do databases have this difference?

* It's one of the reasons a database is faster at storing and retrieving a large amount of data.
* It can actually help prevent errors. For example, your code might have a typo, `student = {"firstnme": "John", "lastname": "Anderson"}`. Notice that there is a typo with `firstnme`. Using a dictionary, this is still a valid dictionary and so you might not find the problem until much later. Using a database, the typo will be caught right away.
* Not only can it catch typos in names, it can prevent the wrong type of data from being added. Let's say your database table has a column id of type int. If you tried to send this to a database, `update students set id='John' where lastname='Anderson'` it would catch the problem right away - the id cannot be a string like 'John'.



# SQL and Data Visualization

You have seen how we can save a program's data by writing to a file on disk, and later reading that file back in. Another way to save data is to save it to what we call a database. Using a database is sometimes more complicated, but it has advantages. Writing to a database is usually faster than writing an entire file to disk, and it also will enforce that the data is structured in the way that you want, because it will reject data that isn't in the right structure.

The way to communicate with a database is a different language called SQL.

Databases work very well when you have very large data sets, like if you are creating the next Facebook and you need a place to store every single comment that people have ever written. While we're on the topic of large data sets, we will talk about how to show visualizations of the data. This can help us see trends and understand the data. For our next-Facebook example we could create a data visualization of number-of-comments per day and if it looks like a line going up and to the right, this means our website is getting more and more active!

## Topics

* Write code that loops through data in lists to find the information that was requested.
* If there is a database, use a `select` in SQL to find information.
* Using an `insert`, `update`, and `delete` to modify the database.
* Using `limit`s (useful if we only need one piece of data) and `order` (useful to sort the results).
* Using a library called Matplotlib that makes it simple for us to visualize data.
* Being able to see interesting trends in data by drawing graphs with Matplotlib.


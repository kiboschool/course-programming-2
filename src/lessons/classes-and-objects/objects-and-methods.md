
# Objects and Methods

You might have come across the phrase "Object-Oriented Programming". What does this mean: in programming, what is an object?

## Objects

An **object** has **internal data** and **behavior**.

When you have a string in our program, for example by typing `name = 'Michael'`. `name` has some internal data (which stores the letters) and some behavior (it knows how to be joined onto another string, split into smaller strings, and so on).

When you have an int in our program, for example by typing `number = 5`. `number` has some internal data (which stores the value 5) and some behavior (it knows how to be added, subtracted and multiplied).

So, the strings and ints we use every day are examples of objects.

We can have a list in our program, for example by typing `list_of_names = []`. `list_of_students` has some internal data (which stores the names as strings) and some behavior (you can write `list_of_students.append(other_name)` to add a name).

So, lists are objects too.

As you may have noticed, an object can store other objects as part of the internal data. A list is an object, and it usually contains many other objects inside of it.

## Another example of an object

Remember when we retrieved information from the internet:

```python
url = 'https://www.7timer.info/bin/astro.php?lat=9.1&lon=7.4&output=json'
response = urllib.request.urlopen(url)
```

`response` is an object. It's not a list, and not a dictionary, but its own type of object. The internal data is the data that was sent back from the web server, and the behavior includes doing things like call `response.read()`, which converts that data into a structure we can work with.

An object can be very simple, like an int. Or it can be complicated, and contain thousands of other objects.

## Methods

Notice what happens when we write `list_of_students.append(other_name)`, or `response.read()`.

We are calling a function, but it is a function "attached" to an object.

This type of function that is attached to an object is called a **method**. Lists have certain methods, like `append`, and Responses have certain methods, like `read`.

We'll soon learn more about objects and methods, and how to use them.

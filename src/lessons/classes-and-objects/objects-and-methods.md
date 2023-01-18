# What is Object-Oriented Programming?

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/GscjD5I1L-I?rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

# Objects and Methods

By now, you have heard the phrase "Object-Oriented Programming".

What does this mean? In programming, what is an object?

## Objects

An **object** has _internal data_ and _behavior_.

When you have a string like `name = 'Michael'`, `name` has some internal data (which stores the letters) and some behavior (it knows how to be joined onto another string, split into smaller strings, and so on).

When you have an int, like `number = 5`, `number` has some internal data (which stores the value 5) and some behavior (it knows how to be added, subtracted and multiplied).

The strings and ints you use every day are examples of objects.

We can have a list, like `list_of_students = ['Ola', 'Mo', 'Keno']`. `list_of_students` has internal data (which stores the names as strings) and behavior (you can write `list_of_students.append(other_name)` to add a name).

Lists are objects too!

As you may have noticed, an object can store other objects as part of the internal data. A list is an object, and it usually contains other objects inside of it.

## Another example of an object

Remember when we retrieved information from the internet?

```python
url = 'https://www.7timer.info/bin/astro.php?lat=9.1&lon=7.4&output=json'
response = urllib.request.urlopen(url)
```

`response` is an object. It's not a list, and not a dictionary, but its own type of object. The internal data is the data that was sent back from the web server, and the behavior includes doing things like call `response.read()`, which converts that data into a structure we can work with.

An object can be very simple, like an int. Or it can be complicated, and contain thousands of other objects.

## Methods

Notice what happens when we write `list_of_students.append(other_name)`, or `response.read()`.

We are calling a function, but the function is "attached" to the object.

A function that is attached to an object is called a **method**.

Lists have certain methods, like `append`, and responses have certain methods, like `read`.

We'll soon learn more about objects and methods, and how to use them.

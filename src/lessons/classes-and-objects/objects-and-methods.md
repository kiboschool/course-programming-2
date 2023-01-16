
# Objects

You have probably seen the phrase "Object-Oriented Programming". Let's start by answering the question "What is an object?"

An **object** has **internal data** and **behavior**.

In the programs we've been writing, nearly everything we've worked with has been a type of object.

We can have an int in our program, for example by typing `number = 5`. `number` has some internal data (which stores the value 5) and some behavior (it knows how to be added, subtracted and multiplied).

We can have a string in our program, for example by typing `name = 'Michael'`. `name` has some internal data (which stores the letters) and some behavior (it knows how to be joined onto another string, split into smaller strings, and so on).

We can have a list in our program, for example by typing `list_of_names = []`. `list_of_students` has some internal data (which stores the names as strings) and some behavior (you can write `list_of_students.append(other_name)` to add a name).

As you may have noticed, an object can store other objects as part of the internal data.

Remember when we retrieved information from the internet,

```python
url = 'https://www.7timer.info/bin/astro.php?lat=9.1&lon=7.4&output=json'
response = urllib.request.urlopen(url)
```

`response` is an object. It's not a list, and not a dictionary, but its own type of object. The internal data is the data that was sent back from the web server, and the behavior includes doing things like call `read()`, which converts that data into a structure we can work with.

An object can be very simple, like an int. Or it can be complicated, and contain thousands of other objects.





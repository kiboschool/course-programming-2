# What is Object-Oriented Programming?

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/GscjD5I1L-I?rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

# Objects and Methods

## Objects

Objects are _specific_ instances of a class. Going back to our initial example, my car could be represented by an object, your car by a different object, but they are both _cars_ at the end of the day.

An **object** has _internal data_ and _behavior_.

The _internal data_ is what makes the object different from others. My car is red, yours is black. My car is manual, yours is automatic, etc.

The _behavior_ is what we can do with the object. My car can turn on, turn right, left, honk. Similarly, your car should be able to do the same.

This logic applies to code you have seen before: 

When you have a string like `name = 'Michael'`, `name` has some internal data (which stores the letters) and some behavior (it knows how to be joined onto another string, split into smaller strings, and so on).

When you have an int, like `number = 5`, `number` has some internal data (which stores the value 5) and some behavior (it knows how to be added, subtracted and multiplied).

The strings and ints you use every day are examples of objects. There is a class that defines the behaviour of all strings, and allows you to create specific strings you depending on the problem you are trying to solve. Similarly, there is a class defining the behaviour of all ints

If you run `print(type(5))` in the console, it will show `<class 'int'>`. And if you run `print(type('hello'))`, it will show `<class 'str'>`. This is a handy tool to use if you are unsure what kind of object you are dealing with.

We can have a list, like `list_of_students = ['Ola', 'Mo', 'Keno']`. `list_of_students` has internal data (which stores the names as strings) and behavior (you can write `list_of_students.append(other_name)` to add a name).

Every List you have created is also an object! This suggests that there is a class that defines the behaviour of all Lists. Unsurprisingly, `print(type(list_of_students))` shows `<class 'list'>`

## Methods and behaviour

Notice what happens when we write `list_of_students.append(other_name)`: In plain english, we are asking Python to append some variable `other_name` to the list `list_of_students`

What would happen if we were to just type `append(other_name)` in our code? It seems like there would be missing information: Where are we appending this new data? Go ahead and try it, Python will give you an error message.

**Methods** are special functions that are "attached" to an object. They only work when paired up with that object. This is how we get to design how objects of a given class get to behave.

## Check your understanding:

Look through your assignments and notes for Programming 1: Can you identify some methods and objects?

What will the result be for each line when the code is evaluated?

```python
>>> type(67.4)
>>> type(["hello"])
>>> type(None)
>>> [type([]), type({})]
```

First, try to predict the result. Then, enter each line in the Python console to
check your guess.


## What's next?

Many of the types you are familiar with are defined by a class behind the scenes. In the next section, we will learn how to create our own Classes, define Methods within them, then instantiate a new Object.

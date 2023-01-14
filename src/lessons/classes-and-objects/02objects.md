
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

## Classes and Instances

A **class** is a category of similar objects, with similar data and similar behavior. If you run `print(type(5))` in Python, it will show `<class 'int'>`. And if you run `print(type('hello'))`, it will show `<class 'str'>`.

When we create a particular object that belongs to the class, we call it an **instance** of the class. Every object is an instance of something. So for the class `int`, after running `number1 = 4` and `number2 = 5`, `number1` and `number2` each refer to objects that are instances of the class int. 

For the class `list`, after running `list_of_names = ['James', 'Jennifer']`, there is now an object that is instance of class list that contains two instances of strings.

Different instances are separate. If I wrote `other_list_of_names = []` and `other_list_of_names.append('John')`, the variable `list_of_names` would not be changed, because even though they are both lists, it's a separate list instance.

## Creating a class

In addition to using strings and lists, you can write your own class! 

Let's say we are writing a program that draws a point on the screen. To represent where to draw the point, we need to have the x coordinate and the y coordinate. (We could say that the x coordinate is the number of pixels from the left side of the screen, and the y coordinate is the number of pixels from the bottom of the screen).

This is an example of what it looks like to create a class for Points:

```python

class Point:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
    
    def moveUp(self):
        self.y += 1
        
    def moveDown(self):
        self.y -= 1
        
    def moveRight(self):
        self.x += 1
        
    def moveLeft(self):
        self.x -= 1
```

This does look different than the code we've looked at before - don't worry, we will explain what it means.

You can see that there are functions, the lines with `def`. Because of the indentation, these functions are inside of the class, and they act slightly differently. When a function is inside of a class like this, we call it a **method**. When we said that objects were about data and behavior, the behavior can be written using methods. Whenever we run code like this: `list_of_names = ['James', 'Jennifer']; list_of_names.append('John')`, the `.append` is calling a method. In this case our Point class has moveUp and moveDown methods that can be called.

First, I'll show what using the class could look like, to get a picture of what is happening:

```python

point = Point(0, 0)
print('the point is at x=', point.x, 'y=', point.y) # shows x=0, y=0
point.moveUp()
print('the point is at x=', point.x, 'y=', point.y)  # shows x=0, y=1
point.moveRight()
print('the point is at x=', point.x, 'y=', point.y)  # shows x=1, y=1

```

Now, going line by line through the class:

<!--Make this an embedded slide deck for better engagement. Can highlight the line we're talking about.-->

* `class Point` says that we are defining a class called Point.
* The indentation shows that the other lines below are inside this class and are part of it.
* You'll see `self` a lot of places. Self refers to the current instance of the class - when we run `my_point.moveUp()`, in that case `self` refers to `my_point`.
* The first method has a special name, __init__. This method is called the **initializer** and it will get called automatically whenever a new instance is made.
* By writing `self.x = initial_x`, we are putting internal data into the instance. This type of internal data is called a member variable. The rest of the methods can refer to `self.x` and it will act like a variable named x.
* Methods work very similarly to other functions, it's just that they are inside a class and the first argument is called `self`. We write the arguments including `self` as the first parameter. When you call a method it is like calling a function. It would make sense to call the function by writing `my_point.moveUp(my_point)`, since that is what the first argument will end up recieiving. Python chose to make it look redundant though, and, we only write `my_point.moveUp()` to call the method, passing the `my_point` into `self` is done invisibly.


A class is kind of like a template for creating objects.

We said that objects are **behavior** and **internal data**.

Our class describes what the behavior is (the methods) and what the internal data should start out with (the `__init__` method). 

(The name of the class with parentheses will act like a function that generates instances. We can now write `my_point = Point(0, 0); print(type(my_point))` and we'll see that we have made a new type of object, `<class '__main__.Point'>`)





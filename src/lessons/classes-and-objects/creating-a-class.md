# Creating a Class

## Classes and Instances

We saw earlier that lists have methods like `append()`, and responses have methods like `read()`. They have different methods because they are from different **classes**.

A **class** is a category of similar objects, with similar data and similar behavior. You can ask Python the type an object to see its class. If you run `print(type(5))` in the console, it will show `<class 'int'>`. And if you run `print(type('hello'))`, it will show `<class 'str'>`. 

When we create an object that belongs to a class, we call it an **instance** of the class. Every object is an instance of some class. After running `number1 = 4` and `number2 = 5`, `number1` and `number2` refer to objects that are instances of the class int. 

After running `list_of_students = ['Ola', 'Mo', 'Keno']`, there is now an object that is an instance of class list that contains two instances of strings. If you then run `other_list_of_names = []`, you have just created a new instance of the list class. The program now has two lists that can store their own items.

### Check your understanding

What will the result be for each line when the code is evaluated?

```python
>>> type(67.4)
>>> type(["hello"])
>>> type(None)
>>> [type([]), type({})]
```

First, try to predict the result. Then, enter each line in the Python console to
check your guess.

## Making your own class

If you want to define a new type of object, that isn't a list, dictionary, or anything built-in, you can create your own.

Let's say we are writing a program that draws points on the screen. To represent where to draw each point, we need to have the x coordinate and the y coordinate. The x coordinate will be the number of pixels from the left side of the screen, and the y coordinate will be the number of pixels from the bottom of the screen.

This is an example of what it looks like to create a class Point:

```python
class Point:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
    
    def move_right(self):
        self.x += 1
        
    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1
        
    def move_down(self):
        self.y -= 1
```

You can see that there are functions, the lines beginning with `def`. Because of the indentation, these functions are _inside of the class_, and they act slightly differently. They are _methods_.

Objects have data and behavior. 


The behavior can be written using methods. Remember that whenever we run code like: `list_of_names.append('John')`, the `.append` is calling a method. 

Our Point class has methods `move_left`, `move_right`, `move_up`, and `move_down`. 

The data for the x and y coordinates is stored on the Point instance using the `self` keyword. The `__init__` method sets the initial values, and the `move_` methods change the values.

Here's what it would look like to use the `Point` class:

```python
start = Point(0, 0) # create a point instance
print('x=', start.x, 'y=', start.y) # x=0, y=0
start.move_up()
print('x=', start.x, 'y=', start.y) # x=0, y=1
start.move_right()
print('x=', start.x, 'y=', start.y) # x=1, y=1
```

`start.move_up()` calls the `move_up` method defined in the class. It is like calling a function, it's just that this is a function attached to the object.

### Slides: Using instances

> Click through the slides to see how working with an instance of a Point is similar to working with an instance of a list

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSIuZDGkNh2XEEMtJYZkxPqXVfp5KzbL9s3vT30KioiCSKJbq6nAVGdnlg-YjNl1FwncaSJFfYTuPFA/embed?start=false&loop=false&delayms=60000" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Slides: `Point` class explanation

> Click through the slides to see an explanation for each line of the Point class

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRCq90ad0wfXUxI-PkR22m9Q91dJiSMQj3-z6Zg0QcE_C1qIJ4dApUKdWW1l9UnB0m-vkP98cQfMLsL/embed?start=false&loop=false&delayms=60000" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Templates for objects

A class is a template for creating objects.

Objects have **behavior** and **internal data**.

Our class describes what the **behavior** is (the methods) and what the **internal data** should start out with (the `__init__` method). 

To create a new instance, you can use the class like a function that makes an instance. It will call the `__init__` method with the arguments you pass in.

When you write:

```python
my_point = Point(0, 0)
print(type(my_point))
```

You are creating an object which is an instance of the new class we wrote. You now have a `<class '__main__.Point'>`.

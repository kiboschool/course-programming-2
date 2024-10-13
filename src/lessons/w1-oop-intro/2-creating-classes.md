# Creating a Class

## Class syntax

If you want to define a new type of object, that isn't a list, dictionary, or anything built-in, you can create your own. When you create a class you will need to provide python with the following information:

1. A *name* for your class.
2. What the _data_ that each object stores should be.
3. All the behavior we want the objects to be able to do. In other words, define **methods** for objects of your class. 

To define a class in Python we follow this pattern:

```python
class MyClass:
#<-> Note the indentation of all our code below 
    def __init__(self, param_1, param_2...):
        self.data_1 = param_1
        self.data_2 = param_2 * 7
        self.data_3 = "some_default_value"

    def method_1(self):
        # We can define a behavior in this method

    def method_2(self, param_1):
        # We can define a different behavior in this method.
```

Let's break this down:

- `class` is a keyword that should be followed by the name of the class. Note that everything related to our class is **indented** under the ```class MyClass:``` statement
- `__init__` is a *special method*, often called **the constructor**. This is the method that defines **what we need to create a new object of our class** We will dig a lot deeper into the`__init__` method soon.
- `self` is a keyword that you will see in all methods of our class. When you use the `self` variable within a method, you get to access **the data of the object the method was called upon**. This is a very crucial concept we will cover more in examples below. 

Let's build our first class.

## Our first class

Let's say we are writing a program that draws points on the screen. To represent where to draw each point, we need to have the x coordinate and the y coordinate. The x coordinate will be the number of pixels from the left side of the screen, and the y coordinate will be the number of pixels from the bottom of the screen.

Ideally, if `my_point` was a point object, I'd want it to know it's x and y coordinate. If I were to represent `my_point`, it would be convenient if I could type `print(my_point.x)` and see the x-coordinate of my point.

Let's do just that:

```python
class Point:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
```

With these few lines of code, it's now possible for us to define points: 

<iframe src="https://trinket.io/embed/python3/953c906fbe" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Let's dig deeper into what is going on here: We call _x_ and _y_ the attributes of Point objects. These represent the _data_ stored in each object and they can be accessed and manipulated directly. For example we can modify my_point's x coordinate: 

```python
my_point.x = 11
print(my_point.x) # prints 11
```

These attributes were defined and set up inside our **Constructor**, the `__init__` method. The line `self.x = initial_x` is telling python two different things:

- The object we are creating should have an *attribute* called `x`
- The value of that *attribute* should be the parameter `initial_x`

Similarly, we do the same for the y-coordinate of the point. 

It is up to you what the attributes of your objects should be, and how you will initialize them. This is part of the fun of programming in this style: Figuring out what you need to solve the problem at hand. 

You may be wondering, where is our constructor method called? It is not obvious at a first glance, but the constructor is used in this line:
```my_point = Point(4, 7)```. Using the name of your class, followed by all the parameters defined in `__init__` besides `self`, is how you create an object of a custon class. 

### Check your understanding:

What do you think would happen if you were to execute this line of code: 

<iframe src="https://trinket.io/embed/python3/d28b6f70f5" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Make a prediction about what will be printed, then test it out yourself.

<details> <summary>Solution:</summary>
    We will get an error! more specifically, an _AttributeError_, as the Point class does not have an attribute called _z_ defined in its constructor.
</details>

## Our first methods

The main thing we want to do with these points is move them around the screen, so let's build new behavior, new **methods** to achieve that.

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

Now on top of storing data, our objects have behaviour. Here's what it would look like to use the `Point` class now:

<iframe src="https://trinket.io/embed/python3/ebfe56913e" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

`start.move_up()` calls the `move_up` method defined in the class. It is like calling a function, it's just that this is a function attached to the object.

### Understanding `self`:
This section is not about self awareness, but about clarifying the use of the keyword `self`

Note that in our definition of the `move_right` method, `self` looks like a parameter, however we called the method as `start.move_right()` without providing any parameters. Here `self` refers to the **object we called the method upon**. When we execute `start.move_right()`, `self` is effectively `start`. If we call `my_point.move_right()`, `self` is effectively `my_point`. 

That's why we don't need to provide the parameter between parentheses, python knows what object to use in place of `self` by looking **at the object before the '.'**

How does it work in our **Constructor** though? Well there is no object *yet*, so inside our `__init__` method, `self` refers to **the object we are busy creating**

## Slides: `Point` class explanation

> Click through the slides to see an explanation for each line of the Point class

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRCq90ad0wfXUxI-PkR22m9Q91dJiSMQj3-z6Zg0QcE_C1qIJ4dApUKdWW1l9UnB0m-vkP98cQfMLsL/embed?start=false&loop=false&delayms=60000" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## What's next?

In the next section, we will go over some common bugs and errors you may encounter with your classes, before building another example class.
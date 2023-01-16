
# Creating a Class

## Classes and Instances

We saw earlier that lists have methods like `append()`, and Responses have methods like `read()`. They have different methods because they are from different **classes**.

A **class** is a category of similar objects, with similar data and similar behavior. We see the class by asking Python what type an object is. If you run `print(type(5))` in Python, it will show `<class 'int'>`. And if you run `print(type('hello'))`, it will show `<class 'str'>`. 

When we create an object that belongs to a class, we call it an **instance** of the class. Every object is an instance of something. After running `number1 = 4` and `number2 = 5`, `number1` and `number2` refer to objects that are instances of the class int. 

After running `list_of_names = ['James', 'Jennifer']`, there is now an object that is instance of class list that contains two instances of strings. If I then write `other_list_of_names = []` I have just created a new instance. The program now has two instances of lists that can store their own items.

## An example class

In addition to using strings and lists, you can create your own class.

Let's say we are writing a program that draws a point on the screen. To represent where to draw the point, we need to have the x coordinate and the y coordinate. (We could say that the x coordinate is the number of pixels from the left side of the screen, and the y coordinate is the number of pixels from the bottom of the screen).

This is an example of what it looks like to create a class for Points:

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

This looks different than the code we've seen before - don't worry, we will explain what it means.

You can see that there are functions, the lines beginning with `def`. Because of the indentation, though, these functions are inside of the class, and they act slightly differently. This is how to create a **method**. When we said that objects were about data and behavior, the behavior can be written using methods. Remember that whenever we run code like this: `list_of_names = ['James', 'Jennifer']; list_of_names.append('John')`, the `.append` is calling a method. In this case our Point class has move_up and move_down methods that can be called.

First, I'll show what using the class could look like, to get a picture of what is happening:

```python

point_instance = Point(0, 0)
print('the point_instance is at x=', point_instance.x, 'y=', point_instance.y) # shows x=0, y=0
point_instance.move_up()
print('the point_instance is at x=', point_instance.x, 'y=', point_instance.y)  # shows x=0, y=1
point_instance.move_right()
print('the point_instance is at x=', point_instance.x, 'y=', point_instance.y)  # shows x=1, y=1

```

Writing `point_instance.move_up()` will calling the `move_up` method that we wrote in the class.

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSIuZDGkNh2XEEMtJYZkxPqXVfp5KzbL9s3vT30KioiCSKJbq6nAVGdnlg-YjNl1FwncaSJFfYTuPFA/embed?start=false&loop=false&delayms=60000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>


Now, going line by line through the class:

<!-- Make this an embedded slide deck for better engagement. Can highlight the line we're talking about. -->

* `class Point` says that we are defining a class called Point.
* The indentation shows that the other lines below are inside this class and are part of it.
* You'll see `self` a lot of places. Self refers to the current instance of the class - when we run `my_point.move_up()`, in that case `self` refers to `my_point`.
* The first method has a special name, __init__. This method is called the **initializer** and it will get called automatically whenever a new instance is made.
* By writing `self.x = initial_x`, we are putting internal data into the instance. This type of internal data is called a member variable. The rest of the methods can refer to `self.x` and it will act like a variable named x.
* Methods work very similarly to other functions, it's just that they are inside a class and the first argument is called `self`. We write the arguments including `self` as the first parameter. When you call a method it is like calling a function. It would make sense to call the function by writing `my_point.move_up(my_point)`, since that is what the first argument will end up recieiving. Python chose to make it look redundant though, and, we only write `my_point.move_up()` to call the method, passing the `my_point` into `self` is done invisibly.


A class is kind of like a template for creating objects.

Remember that we said that objects are **behavior** and **internal data**.

Our class describes what the behavior is (the methods) and what the internal data should start out with (the `__init__` method). 

(The name of the class with parentheses will act like a function that makes an instance. It will automatically call the `__init__` method. We can now write `my_point = Point(0, 0); print(type(my_point))` and we'll see that we have made a new class of object, `<class '__main__.Point'>`)


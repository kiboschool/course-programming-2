# Why we chose this approach

There are others way we could have stored Points in our program. We could have used a list of length two,

```python
def make_point(initial_x, initial_y):
    return [initial_x, initial_y]

def moveUp(point):
    point[1] += 1

def moveDown(point):
    point[1] -= 1
    
def moveRight(point):
    point[0] += 1
    
def moveLeft(point):
    point[0] -= 1

```

An issue here is that we would have to always remember that [0] refers to x and [1] refers to y. And it could be hard to stop people from writing code incorrectly and accidentally add another number onto the list to give it a length different than two.

Alternatively, we could have used functions and a dictionary,

```python
def make_point(initial_x, initial_y):
    return {'x': initial_x, 'y': initial_y}

def moveUp(point):
    point['y'] += 1

def moveDown(point):
    point['y'] -= 1
    
def moveRight(point):
    point['x'] += 1
    
def moveLeft(point):
    point['x'] -= 1

```

We would refer to this as the non-object-oriented way to store Points. Using a class is the "object-oriented" way to store Points, because we are defining our own objects to solve the problem.

The non-object-oriented way would be similar. Instead of writing `my_point.moveUp()` we would write `moveUp(my_point)`.

Why didn't we just use a dictionary and use the non-object-oriented way?

* If we call `print(type(my_point))` it would just say `dict`. It would look like just any other dictionary, and in a large program it could be hard to know what data type we are looking at.
* The structure of the file is now flat. A good benefit of using a class is that the data and the methods are all organized together into one structure.
* It is much quicker to write code when you can type `point.x` instead of `point['x']`. And in fact, often in editors like VSCode, if there is a class instance and you begin to type `point.`, it will suggest `.moveUp()`,`.moveDown()` etc. as autocomplete options, which saves you time from going back to see what the methods are called.

In the introduction we discussed the benefits of modules, how gathering related code into one place is helpful for organization. Using a class also gathers related code into one structure in the python script and is similarly good for organization.



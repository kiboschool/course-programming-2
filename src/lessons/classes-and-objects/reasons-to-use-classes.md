# Reasons to use Classes

There are others way we could have stored Points in our program. We could have used a list of length two:

```python
def make_point(initial_x, initial_y):
    return [initial_x, initial_y]

def move_up(point):
    point[1] += 1

def move_down(point):
    point[1] -= 1
    
def move_right(point):
    point[0] += 1
    
def move_left(point):
    point[0] -= 1

```

An issue here is that we would have to always remember that [0] refers to x and [1] refers to y. And it could be hard to stop people from writing code incorrectly and accidentally add another number onto the list to give it a length different than two.

Alternatively, we could have used functions and a dictionary:

```python
def make_point(initial_x, initial_y):
    return {'x': initial_x, 'y': initial_y}

def move_up(point):
    point['y'] += 1

def move_down(point):
    point['y'] -= 1
    
def move_right(point):
    point['x'] += 1
    
def move_left(point):
    point['x'] -= 1
```

We would refer to this as the non-object-oriented way to store Points. Using a class is the "object-oriented" way to store Points, because we are defining objects to solve the problem.

The non-object-oriented code is similar. Instead of writing `my_point.move_up()`, we would write `move_up(my_point)`.

Why didn't we just use a dictionary and use the non-object-oriented way?

* If we call `print(type(my_point))` it would just say `dict`. It would look like just any other dictionary! In a large program, it would be hard to distinguish points from other dictionaries.
* The functions associated with a Point are now clear. The data and the methods are organized together into one structure, so any developer can tell which functions are related to Points, and which are not.
* It is quicker to write code when you can type `point.x` instead of `point['x']`. In fact, in editors like VSCode, when you type `point.`, it will suggest `.move_up()`,`.move_down()` etc. as autocomplete options. Autocomplete saves you from going back to see what the methods are called.

Because the data and methods are organized together into one structure, it will be easy for people adding on to your program will know what behavior is associated with which parts of data, and to know where to add new behavior.

In the introduction we discussed the benefits of modules. Gathering related code into one place makes code easier to understand and navigate. Using a class also gathers related code into one structure and makes code easier to understand.

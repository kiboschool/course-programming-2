# Aliasing and Copying

## Aliasing

Different instances are separate from each other. If I wrote  `list_of_names = []` and `other_list_of_names = []` and `other_list_of_names.append('John')`, the variable `list_of_names` would not be changed. They are both lists, but they are separate instances.

The same thing happens for instances of custom classes. If you generate two different instances:

```python
a = Point(0, 0)
b = Point(0, 0)
```

they are separate.

There are ways to make two names that point to the same object - where they are not separate. <span style="color:red">This is where things get dangerous</span>. If you assign an object to a different variable:

```python 
a = Point(0, 0)
b = a
```

`a` and `b` refer to *the same object*. Any changes to `a` will show up in b, and vice versa. This is called **aliasing**.  `a` and `b` are like two nicknames for the same person.

```python
a = Point(0, 0)
b = a

print(a.x) # 0
print(b.x) # 0
a.move_right()

# both a and b were changed!
print(a.x) # 1
print(b.x) # 1
```

Aliasing isn't always a problem. Sometimes, you want two names for the same object, but be careful. Aliasing is a common source of bugs!

## Function parameters

Aliasing will also happen when you pass an object as a parameter to a function. When you pass the object as a parameter, the object that the function operates on is the same.

```python
def move_right_twice(point):
    point.move_right()
    point.move_right()
    
a = Point(0, 0)
move_right_twice(a)
print(a.x) # 2
```

The object `a` gets changed, because the `point` in the function is the same as `a`. This is usually what we want, but we need to be aware of it.

## Example: Reflecting a point

Let's write a helper function that gets the reflected version of a point. 

We'll reflect across the y axis, flipping the point from left to right. We need a point that is the same as the original but with the x coordinate multiplied by -1, so that points on the left are reflected to the right, and points on the right are reflected to the left.

```python
# the code here is wrong!
def get_reflected_point(point):
    point.x *= -1
    return point
```

The `get_reflected_point` is not written correctly! It does return a reflected point as we wanted, but it has "side effects" - it modifies the original point. In this case, we don't want aliasing.

```python

a = (3, 3)
reflected = get_reflected_point(a)

print(reflected.x) # shows -3, just like we want
# but it also did something we didn't want
print(a.x) # this also shows -3. our original was modified.

```

`get_reflected_point()` should make a copy instead.

## Copying

This is a way to avoid aliasing.

```python
import copy
a = Point()
b = copy.deepcopy(a)
```

Now a and b are completely separate instances.

So, this is a better way to write `get_reflected_point`:

```python
def get_reflected_point(point):
    import copy
    copied_point = copy.deepcopy(point)
    copied_point.x *= -1
    return copied_point
```

It works as expected:

```python
a = (3, 3)
reflected = get_reflected_point(a)

print(reflected.x) # shows -3, just like we want.

print(a.x) # this also shows 3, our original is left intact.
```

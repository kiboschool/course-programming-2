# Aliasing and Copying

## Aliasing

Different instances are separate from each other. If I wrote  `list_of_names = []` and `other_list_of_names = []` and `other_list_of_names.append('Ola')`, the variable `list_of_names` would not be changed. They are both lists, but they are separate instances.

The same thing happens for instances of custom classes. If you generate two different instances:

```python
a = Point(0, 0)
b = Point(0, 0)
```

they are separate.

There are ways to make two names that point to the same object - where they are not separate. If you assign an object to a different variable:

```python 
a = Point(0, 0)
b = a
```

`a` and `b` refer to *the same object*. <span style="color:red">This is where things are dangerous</span>. Any changes to `a` will show up in b, and vice versa. This is called **aliasing**.  `a` and `b` are like two nicknames for the same person.

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

The object `a` gets changed, because the `point` in the function is the same as `a`. This is usually what you want, but you need to be aware of it.

## Example: Reflecting a point

Let's write a helper function that gets the reflected version of a point. 

We'll reflect across the y axis, flipping the point from left to right. We need a point that is the same as the original but with the x coordinate multiplied by -1, so that points on the left are reflected to the right, and points on the right are reflected to the left.

```python
# the code here is wrong!
def get_reflected_point(point):
    point.x *= -1
    return point
```

The `get_reflected_point` is not written correctly! The math is correct and it does return a reflected point as we wanted. But it has "side effects" - it modifies the original point. In this case, we don't want aliasing. The place that calls this function will probably not expect the original point to be changed - see what happens:

```python
first_point = (3, 3)
reflected_point = get_reflected_point(a)

print(reflected_point.x) # shows -3, just like we want
# but it also did something we didn't want
print(first_point.x) # this also shows -3. our original was modified.

```

The solution is that `get_reflected_point()` should make a copy first, and change the copy.

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

This time, the program works as expected:

```python
point = (3, 3)
reflected_point = get_reflected_point(point)

print(reflected_point.x) # shows -3, just like we want.

print(point.x) # this shows 3, our original is left intact.
```

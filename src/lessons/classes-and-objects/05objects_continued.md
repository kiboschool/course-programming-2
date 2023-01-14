
# Objects continued


PARSONS PROBLEM
<!--We are writing a class for Student in the enrollment 
Lines will appear scrambled and student will order them.
-->

```python
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.courses = []

john = Student(1, 'John')
```


### When are instances independent?

If you generate two different instances, 

a = Point()
b = Point()

they are separate.

If you assign it to a different variable,

a = Point()
b = a

This is called aliasing. a and b are actually referring to the same object now. Any changes to a will show up in b, and vice versa. You can think of a and b pointing to the same object.

Aliasing also occurs when the point is passed as a parameter to another function. Changes made in that function do stay there.

You can create a copy, or clone, of the object, if you need an independent copy. This is often a better approach because aliasing can cause bugs. <!-- example -->

<!-- illustrations from thinkpython -->


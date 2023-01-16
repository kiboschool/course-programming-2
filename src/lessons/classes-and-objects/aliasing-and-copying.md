
# Aliasing and Copying

## Aliasing

Different instances are separate. If I wrote `other_list_of_names = []` and `other_list_of_names.append('John')`, the variable `list_of_names` would not be changed, because even though they are both lists, it's a separate list instance.

The same thing happens for instances of classes we make.

If you generate two different instances, 

```python
a = Point()
b = Point()
```

they are separate.

Warning: this is where it gets dangerous: if you assign an object to a different variable,

```python
a = Point()
b = a
```

This is called aliasing. a and b are actually referring to *the same object* now. Any changes to a will show up in b, and vice versa. You can think of a and b as arrows pointing to the same object.

Sometimes aliasing is done intentionally, but it is important to be aware of.

## Example

getReflectedPoint()

Aliasing also occurs when the point is passed as a parameter to another function. Changes made in that function do stay there.

This program has "side effects". It modifies the point. This usually isn't what we want.

getReflectedPoint() should make a copy instead.


## Copying

This is a way to avoid aliasing.

```python
import copy
a = Point()
b = copy.deepcopy(a)
```

Now a and b are completely separate instances.


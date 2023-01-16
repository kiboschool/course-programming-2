# Video

Video 1: 

look at the same code from an object perspective

we have an INSTANCE and we can do ACTIONS with it

name_1 = 'John'
list_of_names = []
list_of_names.append(name_1)
list_of_names.sort()


response = urlopen.urlopen(a)
response.read()

talk through it and talk about how it is all methods


talk through it and talk about how it is all methods
a = Point()
a.moveUp()
a.moveDown()



type out the point class from scratch.
talk through each line
then at the bottom of the file put an example instance
put a few moveUp()
and a few moveDown() calls
run it.
you can't see what happened.
add a displayall() method. often useful for debugging.
now run it. can see the state change.

Show that two instances have separate state. 


Create instances of the Point class and show calling the methods.

Creating a displayall() method for debugging (like repr)
Writing render() methods. often useful to have one that shows state in the class.


Video 2:
----------------

Getting and setting Member variables, both from inside the class and outside.
one difference is that we can peek inside:
a.x and a.y
but it's better not to do that.
better to have a method


Create a new method moveUpBy() and show the `self` parameter disapearing. 


mutating vs copying
getReflectedVersion()
reflect()

Show common mistakes: attributeerror trying to reference something not on the class,
forgetting to add the first self param, spelling __init__ wrong, getting indendation right in the class, a = Point instead of a = Point(). 


What if you are half way through writing it, you hit F5 but it says an error.
Need to use `pass` to stub

what if you wrote point = point() too confusing what is happening...
is point a function?
that's why we capitalize
Casing conventions and file conventions.


Demo a higher level class, PointManager
has a createRectangleCorners method
has a createPointHalfwayBetween method

say that how we write the methods is like how we write functions...
there are lots of options, it is up to us...
all of these could be methods on the Point class too...
there's not always a right or wrong answer

--------------

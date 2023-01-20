
Inheritance and Error Handling
===================================

Exceptions
---------------------------------------------------------------
Errors will happen in our software even if it's not really a mistake,
it's just didn't anticipate invalid input.
We are reading a dictionary with json and the data is unreliable.
my_dict['nonexistant'] causes an exception.
We are writing the course manager, and we need the ID to be an integer.
We have an 'area of a circle' program.
User enters a radius. Need it to be a valid float.
Have the users run it, and see that it says ValueError.
Try running it.
So we have to be able to do something with these cases so that they don't cause crashes.


Exception handling
---------------------------------------------------------------
Use try and except to *handle* the exception.
Show a safe input int from user and a safe input float from the user
that use try and except.

Best video on exceptions I found,
https://www.youtube.com/watch?v=brICUKrzVR0&list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Phn
#63 Python Tutorial for Beginners | Exception Handling
Telusko
https://www.youtube.com/watch?v=6SPDvPK38tw
Can lets students opt in/opt out

this one is also ok but it goes into too much depth,
https://www.youtube.com/watch?v=brICUKrzVR0&list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Phn

Tools to help us in the process of working on classes
---------------------------------------------------------------
We are writing a complicated piece of code
We can write rough drafts of our code.
Kind of like when I added just a print statement to see it get called.
mention pass
mention the __str__ dunder


Modeling
---------------------------------------------------------------
Ben:
Explain Modeling. Picking parts of what's important to us and putting that in a class.
Imagine we are creating a video game where you are driving a car and racing against other cars.
It would make sense to have a class for the car - it has data and behavior.
Will the internal data for the car class compute all of the details for every piece of metal and molecule in the car? Will the code simulate how each part of metal in the car bends, and how the engine works?
No, that amount of detail isn't needed. We would include only the most simple attributes that we need.
In the game we are making, all we need is the position, speed, color, and max speed of the car.
So it only represents an abstract idea of the car, more than a car in the real world.
The process of taking something in the real world and only choosing a few parts of it to make attributes on a class is called Modeling.

Many examples that teach classes have an example class like Dog with an attribute number_of_legs set to 4. At first this doesn't really make sense
because there are so many important things about dogs that aren't included.
But this is just a model - the author took what was most important to the program they were writing and only included that.



Inheritance
---------------------------------------------------------------
Show SavedList

    First pull out the save into its own method

SavedList()
    method insert()
    method append()
        lst.append()
        self.save()
    method removeLastItem()
    method remove(which)
        lst
    method modify(which, newcontents)
Have one that saves as file lines
Have one that saves as json
First have all copypasted in two classes.
Want reuse.
Use inheritence.


        Could be handy to bring it back in the coursemanager!

madlibs example
Base class does substitution. One implementation asks input from user. One implementation pulls from random list.


Best video on inheritance I found,
https://www.youtube.com/watch?v=C8qE3mKiBrQ&list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Ph

Clothing store model
Article of clothing
some articles of clothing have own attributes, some are common
common methods like getprice

Useful for inheritance-adding logging.

And Drawing. pen, color.

--------------------
Create an aside: "subclass", "derived class", "child class" all similar terms

Composition
---------------------------------------------------------------
use some from the think python book

Helper instances
---------------------------------------------------------------
Set up having a class that contains other instances


(not included)
---------------------------------------------------------------
Explain callstacks



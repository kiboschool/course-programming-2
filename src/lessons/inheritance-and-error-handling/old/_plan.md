
Inheritance and Error Handling
===================================

Exceptions
---------------------------------------------------------------


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



Clothing store model
Article of clothing
some articles of clothing have own attributes, some are common
common methods like getprice

Useful for inheritance-adding logging.

And Drawing. pen, color.



Composition
---------------------------------------------------------------
use some from the think python book

Helper instances
---------------------------------------------------------------
Set up having a class that contains other instances


(not included)
---------------------------------------------------------------
Explain callstacks



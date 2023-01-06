# Introduction to Object Oriented Programming

Remember data types.

A list and a dict are also their own data types.

Remember that when we got data from the web api we saw a .response and a .text.


Remember that a list you can say a.function instead of function(a)

this means that they are an object.

We can make our own objects, our own data types.

Can think of a class as a template that defines what happens when you create a new object.

Point class

Note that they are independent: modifying one won't affect the other.

In fact, so far it's pretty similar to a dict {'x':2, 'y': 3}. We will see difference in next page.

<!--


Could be a list helper that always writes things to disk.
that way if the program crashes half way through it will always have a copy on disk
SavedList()
    method insert()
    method append()
        lst.append()
        self.save()
    method removeLastItem()
    method remove(which)
        lst
    method modify(which, newcontents)
    
    

use the student example.

why dicts aren't the best:
    you could have a typo?
    syntax is longer?
    
    no methods



examples of first class to have:
    student example?
    
    weather example?
    weather
        temperature
        windspeed
        cloudcover
        displayCloudCoverString()
        
    
    can have a weather-reader that reads from disk, or one that reads from the webapi
        
        1	0%-6%
        2	6%-19%
        3	19%-31%
        4	31%-44%
        5	44%-56%
        6	56%-69%
        7	69%-81%
        8	81%-94%
        9	94%-100%
                
        
clothing
    getprice() method
    
    



introduction-to-object-oriented-programming.md

------------------------------- in progress -------------------------------


Point class with 0 and 1.
Course with name and id?

student and class-
method

Introduce OOP. A class defines a ‘template’. Each instance behaves similarly to a dict with methods
A dict is also an ‘object’ that has state and methods, but there’s not a way to add your own .x .y .myMethod()
Point class (not perfect, but it does show how instances are independent)
(Having a point class also gives member names like x and y which is easier to read than [0] and [1])
You can make a list of Point instances
(Let’s say you have a list of points. having a point class vs a tuple makes it easier to not have bugs where only one coord is there, since tuples have no enforcement)
Recurring theme: better structuring the data is a way to have better constraints, which are a way to make code more resilient


Point example
    Point class
    Print-current-position method
    Get-distance-from-origin method
    Is-y-coordinate-greater-than-10 method


-->

# Introduction to Inheritence



<!--

------------------------------- content to mention this week -------------------------------
Larger classes, origanizing the program to put everything in classes.


write a helper function that creates two points.


Take
    Add pass ?

Discuss *model*. very simplified computer representation of data+behavior.
Take a clothing store model, ArticleOfClothing
methods getPrice()

talk about the bug
putting a=[] at the top

class mylist:
    my_list = []



Show SavedList and have students add to it.
a list helper that always writes things to disk that way if the program crashes half way through it will always have a copy on disk.
(helps connect concepts, lists are objects)
SavedList()
    method insert()
    method append()
        lst.append()
        self.save()
    method removeLastItem()
    method remove(which)
        lst
    method modify(which, newcontents)

    briefly mention that hiding details is good. people calling into it don't need to care that it uses json.
    we'll pick up on that theme later


Weather example
    Demos composing classes.
    Have a larger weatherlookup class with methods for retrieving it from the api.
    Why is it more useful to use classes this way?  weather_helper.getByCity(‘lagos’).getUpcomingDay(‘3’).temperature() is easier to read than looping through the raw data.
    

ListScrambler
    Demos avoiding mutation by copying.

------------------------------- in progress -------------------------------



Introduce inheritance. 

The persistedlist class-what if we also wanted to add logging.

version one of the code:
no save method, everything is duplicated

then a version with a save method

then a version with a shouldLog 

but this can gum up the functionality-what if sometimes you need to log to a file, sometimes you need to log to console, sometimes you need to include the time in a different format. sometimes you only need to log on deletes, not on adds. needs a lot of if/thens.

one way to do this is with composition-
show example-
but this is inflexible and needs a lot of typing, kind of fragile and you'd have to update it when any of the methods change

one solution for this is called inheritence!

by default it does what the parent class does.
-->

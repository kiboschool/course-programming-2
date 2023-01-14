
# Exercises

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


file helper and/or directoryhelper
File('test.txt')
method setContentsTo('abc')
method appendToFile('abc')
method getContents()
method deleteFile()
    nice that it hides some details.


# Tools when Making Classes

You already have experience writing programs, and so you've gotten a feel for how to what steps to take when working on a larger project. Here we will introduce some new tools specific to classes and objects.

When we're writing complicated programs, sometimes we write the program in multiple steps.

1) First, we'll type down our ideas of what the program will do, e.g. our goals.

1) Then, we can type down some ideas for functions and classes. We're dividing the program into different parts.
    * (We'll see how **pseudocode** can help during this step)
    
1) Next, we will write code that can be run as Python, but isn't complete. Maybe some of the functions aren't written yet.
    * (We'll see how **pass** can help during this step)
    
1) The next step could be to write simple pieces of test code that checks if the program is working.
    * (We'll see how **\_\_str\_\_** can help during this step)
    
1) After more and more working and revising, and putting all of the pieces together, the program is complete.


## Pseudocode (helps with step 2)

> 📗 Pseudocode is an informal description of what a program does. It uses the structural conventions of a normal programming language, but is intended for human reading rather than machine reading.

You can write it in a .py file, but it intentionally won't run. It is a way to type down your thoughts about how the program could work.

Pseudocode is a simple way of writing programming code in English. Pseudocode is not an actual programming language. It uses short phrases to write ideas for programs before you actually create them in a real programming language. Later, once you know what the program is about and how it will function, eventually you can translate pseudocode into Python.

An example:

```
Get student id from user
Get student's grade from data
If student's grade is greater than or equal to 60
    Print "passed"
Else
    Print "failed"
End

```

This could be psuedocode for a class:

```
Class named WeatherData
Stores an attribute temperature
Stores an attribute wind speed
Stores an attribute wind direction
Has a method display which
    prints the temperature
    prints the wind speed
    prints the wind direction

```

You can just write in the way that communicates the details that matter most, but you don't need all of the details.

Pseudocode can also help you communicate your ideas quickly to a classmate or coworker.

Your program can evolve from rough pseudocode:

```
Get data from the api
```

to more precise pseudocode, as you work on your program:

```
Determine the url for the api
Get a response from the api
Use json.loads to turn the data into a dictionary
Read data from the dictionary
```


## The pass statement (helps with step 3)

Let's say we are working on our PersistedList example. (This is a list class we showed, it saves the contents into a text file whenever modifications are made).

```python
import os

class PersistedList:
    def __init__(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                file_contents = f.read()
                self.internal_list = file_contents.split('\n')
        else:
            self.internal_list = []
    
    def persist(self):
        with open(filename, 'w') as f:
            new_file_contents = '\n'.join(self.internal_list)
            f.write(new_file_contents)    
    
    def append(self, incoming_string):
        self.internal_list.append(incoming_string)
        self.persist()
```

Imagine that we are now writing a very advanced PersistedList that stores information onto the internet. It could, say, send a POST to an API to save the list on a server.

But, we haven't written the code to connect to the API yet.

First, we write it in pseudocode.

But when it is in pseudocode, we can't try running the program. It would cause syntax errors, because the pseudocode is not valid Python syntax.

We can comment it out:

```python
import os

class PersistedListInternet:
    def __init__(self, filename):
        # connect to the api and download the data
    
    def persist(self):
        # connect to the api and send the data
    
    def append(self, incoming_string):
        self.internal_list.append(incoming_string)
        self.persist()
```

But we get syntax errors still because Python will not run the script if any methods are empty. Even with the comments there, they are too empty, there needs to be more code.

A good approach for this intermediate phase, where you don't have working code yet, but you at least want to be able to run a few small snippets of code, is to **add pass statements**.

The **pass** statement helps us avoid syntax errors, but it does not do anything.

```python
import os

class PersistedListInternet:
    def __init__(self, filename):
        # connect to the api and download the data
        pass
    
    def persist(self):
        # connect to the api and send the data
        pass
    
    def append(self, incoming_string):
        self.internal_list.append(incoming_string)
        self.persist()
```

With `pass` there, we no longer get a syntax error, and we can run the program again.

It's just a helpful tool. `pass` is good whenever we want an empty function or empty method, which is especially useful in a half-finished program where we intentionally don't have anything written there yet.


## The \_\_str\_\_ method (helps with step 4)

When debugging, we often want to see what the contents of our object are. It's very common to write test code that does a few things, then prints all of the attributes of the class, then we visually look and see if it looks right.

(When we're done with the program we'll delete these little test snippets.)

If we run 

```python

list_of_names = []
list_of_names.append('Michael')
list_of_names.append('Keno')
print(list_of_names)

```

we see the names printed. But if we run:

```python

list_of_names = PersistedList()
list_of_names.append('Michael')
list_of_names.append('Keno')
print(list_of_names)

```

using our own PersistedList class, the `print` doesn't work very well. It just says `<__main__.PersistedList object at 0x0000023CA16D13A0>`, which is not very useful for debugging.

We could write a `display` method, which would work fine. This is what we've used before, and it has worked. But it is convenient to be able to send everything to `print`, as if it were a list, dict, or string.

Please read the page [here](https://www.pythontutorial.net/python-oop/python-__str__/) which talks about a special method named `__str__`.

With `__str__`, you can customize what `print(my_object)` will show.

> ### Challenge
> What code would you write so that `print(list_of_names)` is more helpful, when list_of_names is a PersistedList instance?

<font size="-1">Sources: Wikipedia, [Pseudocode](https://en.wikipedia.org/wiki/Pseudocode).</font>

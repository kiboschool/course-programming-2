# Exceptions

Errors happen. The first version of a program usually has issues that get resolved 
when testing, refining, and debugging the program. Sometimes, issues don't get
resolved, and errors happen in production applications.

But... not every error is a bug!

Let's explore what is going on behind the scenes when an error occurs.

## Errors

In the *Bugs to Watch Out For* video last week, the code was intentionally 
written incorrectly, to show common mistakes when writing classes. 

Several times in the video, an error occurs when running the program.

The program stops running, and a box pops up on the screen with details about 
the error. One of the messages included a phrase `line 45 of main.py`. This is 
useful because you can open `main.py` and go to line 45. This might tell you 
what went wrong.

(You can watch the *Bugs to Watch Out For* video again, on [this page](/lessons/classes-and-objects/bugs-to-watch-out-for.html).)


There are three large categories of errors:

### Category #1: Syntax Errors


The first error that showed up in *Bugs to Watch Out For* showed an 
`IndentationError`. The code was like this:

```python
print('starting the script')

class WeatherData:
def display(self):
print('display is called')
```

The `def` and `print` lines need to be indented to the right.

The interesting thing is that this code is so incorrect that Python does not run 
anything! Instead, it shows the error immediately. 

Usually, the message `starting the script` would still show up, even if there 
were problems later in the file. After all, Python runs programs in order, 
line by line from the top, right? 

But an `IndentationError` is a type of `SyntaxError`. And for a `SyntaxError`, 
none of the code in the file is run.

### Behind the Scenes: Syntax Errors

When you enter `python main.py` on the Terminal, Python takes a series of steps. 
First, it reads the code for the _structures_. It finds out where the classes 
are, where the functions are, and where the loops, conditions, statements, and 
expressions are. This step is called _parsing the syntax_.

Only _after_ parsing does Python actually execute the code from top to bottom. 

When Python can't understand the syntax (like when the indentation is wrong), 
it stops everything early.

Syntax problems cause syntax errors. If a `:` is missing when it should be there, 
or a class, function, or loop does not have the correct form, this will usually 
cause some type of syntax error.

Fortunately, syntax errors are usually the easiest to fix! Python will tell you 
the line number that has the problem. Editors like VSCode can also show red 
lines underneath likely syntax errors.

### Category #2: Runtime Errors

In _Bugs To Watch Out for_ , one of the problems was forgetting to include `self` 
as the first parameter in a method definition. 

```python
print('starting the script')

class WeatherData:
    def __init__():
        print('init is called')

weather_data = WeatherData()
```

In this case, the structure is okay! The lines are indented correctly, and
Python can recognize each part of each line as real Python code. No Syntax
error.

However, when the file is run, it does not work! It shows a message, with the 
line `takes 0 positional arguments but 1 was given`.

This isn't a type of syntax error, so the `starting the script` message will
show up. Code before the problem still gets run. Python doesn't see the issue
until it hits this line: `weather_data = WeatherData()`.

The `__init__` method is called -- it is always called when we create a new
object from a class -- and, like always, it will get the `self` argument passed
in. But, in the definition, it doesn't include the self parameter. Python raises
an exception any time the number of _arguments_ does not match the number of
_parameters_.

Here's the fix:

```python
print('starting the script')

class WeatherData:
    def __init__(self):
        print('init is called')

weather_data = WeatherData()
```

That way, the number of arguments matches what `__init__` is expecting.

Runtime errors are a very common category of problem. They happen when:

* Trying to read data from a file that doesn't exist.
* Trying to get the 4th element from a list that only has 3 elements in it.
* Trying to call a method that doesn't exist. `my_list.read()` does not work, because lists do not have a read method.
* Trying to divide a number by 0 - Python will cause an error if that happens, because in math it's not possible to do that.

> What other runtime errors have you encountered?
> Are there any other situations you can think of where there _should_ be a
> runtime error?

### Category #3: Logic Errors

A clear example of a mistake in a program:

```python
def get_temperature(weather_data):
    return weather_data.wind_speed
```

When someone calls this, they will get the wrong data back!

The program runs smoothly, and will not have any error messages or warnings.

But, it isn't correct. We call this category of problem **logic errors**. It's a type of bug in a program. 

It might be completely silent, and not show any visible errors or warnings. Unless 
you are carefully paying attention (and carefully testing your code), you might 
not even notice anything is wrong. But it is still wrong!

Logic errors can be subtle. The output could be slightly wrong, and hard to 
notice. Or, the program could give the correct output in same cases, but not 
all cases. This is the hardest category of problem to track down and fix.

Consider another example from last week's video:

```python
class WeatherData:
    def init(self):
        print('init is called')

weather_data = WeatherData()
```

We wanted `init` to be the initializer, so that it is called when we create a 
new object. To be the initializer, it must be written as `__init__(self)`, not 
`init(self)`, so the `init is called` message never showed up. 

This is why we write tests: to confirm that the program is working as expected.

## Exceptions

Let's go back to category 2, Runtime Errors.

Every runtime error in Python has a specific _error type_.

This is what shows up in the message. Sometimes the name of the error type 
helps you realize what went wrong, like `FileNotFoundError`. Sometimes it isn't 
as clear, though, like when forgetting to add `self` causes a `TypeError`.

### Try it: Investigation

> Write a program that uses a variable that does not exist. What error type is shown?

## Behind the scenes: Runtime Exceptions

When Python runs into a problem, it follows these steps:

* Python encounters a problem, like dividing by 0
* Python creates a new Exception object, which stores:
  * an attribute with the file name
  * an attribute with line that was being run
  * a string with a message
* Python stops the program completely
* Python shows the error type, for example `DivideByZeroError`.
* Python shows the information from the Exception object

This type of object, which stores information about an error that occurred, is called an **exception object**.

This sequence of events is known as **raising an exception**.

Runtime Errors have lots more to explore. In the next lesson, you'll see how to
create and handle them.

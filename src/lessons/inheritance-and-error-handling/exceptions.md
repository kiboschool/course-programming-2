# Exceptions

Exceptions and errors happen often when we are developing a program. Let's explore more information about what is going on behind the scenes when an error happens.

## Errors

Let's recall the *Bugs to Watch Out For* video from last week. The code there was intentionally written incorrectly, to show the common mistakes that occur when making classes. 

Very often in the video, when running the program, an error occurred.

The program stops running, and a box pops up on the screen with details about the error. For example, the message might say `line 45 of main.py`. This is useful because you can open the `main.py` and go to line 45. This might give information about seeing what went wrong.

There are three large categories of errors:

### 1) Syntax Errors

Remember that the first error that showed up in the *Bugs to Watch Out For* video popped up a message saying "IndentationError". This is because there was code like this,

```python

class WeatherData:
def init(self):
print('init is called')

```

The `def` and `print` lines need to be indented to the right.

The interesting thing is that this code is so incorrect, that Python does not run anything, it shows the error immediately. For example, if you wrote:


```python

print('starting the script')

class WeatherData:
def init(self):
print('init is called')

```

(Do you remember how to fix this?)

Usually, the message `starting the script` would still show up, even if there were problems later in the file. After all, Python is running the program in order, line by line from the top, right? But an IndentationError is a type of Syntax Error. And for Syntax Errors, none of the code in the file is run.

(What's happening behind the scenes is that when you run `python main.py`, Python has an earlier step that determines the structures in the file: figuring out where are the classes, where are the functions, and where are the loops. Only after this step does it run through the file from top to bottom. Python couldn't figure out the structure of the class because the indentation was wrong, and so it stopped everything early).

Structural problems generally cause Syntax Errors. So if a `:` is missing when it should be there, or a class, function, or loop does not have the correct form, this will usually cause a type of Syntax Error.

Fortunately, Syntax Errors are usually the easiest to fix because Python will tell you the line number that has the problem. Editors like VSCode sometimes show red lines underneath likely syntax errors.

### 2) Runtime Errors

In the Bugs To Watch Out for video, one of the problems was forgetting to have `self` as the first received in a method. 


```python

print('starting the script')

class WeatherData:
    def __init__():
        print('init is called')

weather_data = WeatherData()
```

In this case, the structure is correct. The lines are indented correctly, and there are no problems with loops or functions. But when the file is run, a message pops up that says `takes 0 positional arguments but 1 was given`.

This isn't a type of syntax error, so the `starting the script` message still shows up (code before the problem still gets run).

The correct way to write it is this,


```python

print('starting the script')

class WeatherData:
    def __init__(self):
        print('init is called')

weather_data = WeatherData()
```

Runtime errors are a very common category of problem.
* Trying to read data from a file that doesn't exist.
* Trying to get the 4th element from a list that only has 3 elements in it.
* Trying to call a method that doesn't exist. `my_list.read()` does not work, because lists do not have a read method.
* Trying to divide a number by 0 - Python will cause an error if that happens, because in math it's not possible to do that.

What runtime errors can you think of?


### 3) Silent Errors

Consider another example from the video,

```python

class WeatherData:
    def init(self):
        print('init is called')

weather_data = WeatherData()
```

The program runs fine, and doesn't pop up any errors or warnings.

But it isn't correct! We wanted init to be the initializer, and it must be written as `__init__(self)`, not as `init(self)`. The `init is called` message never showed up.

We can call this a **silent error**. Unless you are carefully paying attention, you might not even notice anything is wrong, but it is still wrong.

A very clear example:

```python

def get_temperature(weather_data):
    return weather_data.wind_speed

```

When someone calls this, they will get the wrong data back.

Silent errors can also be subtle. They can be the hardest to track down and fix.


## Exceptions

Let's go back to category 2, Runtime Errors.

Every runtime error in Python has a more specific error type.

This is what shows up in the message. Sometimes the name of the error type helps you realize what went wrong, like `FileNotFoundError`. And sometimes it isn't as clear, like when forgetting to add `self` causes a `TypeError`.

Write a program that reads from a variable that does not exist. What error type is shown then?

It turns out that when Python runs into a problem, it does these steps behind the scenes:

* A problem is hit, like dividing by 0
* Python creates a new object
  * on the object it stores an attribute with the file name
  * on the object it stores an attribute with line that was being run
  * on the object it stores a string with a message
* Python then stops your program completely
* Python then shows the error type, for example `FileNotFoundError`.
* Python then shows the information on the newly created object.

This sequence of events is known as **raising an exception**.

This type of object, that stores information about an error that happened, is called an **exception object**.

As you have seen, Runtime Errors, in category 2, are interesting to explore. We will talk about them further in the next page.


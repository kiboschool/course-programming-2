# Exception Handling

We'll continue talking about the second category we discussed on the previous page, Runtime Errors.

Runtime errors will happen in software. Watching the video, we wrote a program 
that read data from the weather API. What if the server was down, or there was 
no internet connection?

Or, if our program takes in input from the user and then does division, the 
program might run into a divide-by-zero error. Often in CLI projects, you'll
encounter a ValueError when trying to convert input from a user into an `int` or
`float`.

You don't really want your program to crash in these cases. You need a way to 
*catch* a Runtime Error and not let it stop the program entirely.

The video below will show how to do this in Python.

## Video

Please watch the first 5 minutes of this video:

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/brICUKrzVR0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Summarizing the video

You are writing a program that divides candy into pieces. Your program asks "how 
much candy?" and "how many people?" This program works:

```python
amount_of_candy = 2.3
number_of_people = 3
candy_per_person = amount_of_candy / number_of_people
```

What if the value for how many people is 0?

```python
amount_of_candy = 2.3
number_of_people = 0
candy_per_person = amount_of_candy / number_of_people
```

This program will crash, because Python will raise a DivideByZeroError!


```python
amount_of_candy = 2.3
number_of_people = 0
try:
    candy_per_person = amount_of_candy / number_of_people
except:
    print('We could not determine the amount of candy per person.')
```

Now the program will not crash. It will run the code under `except` and keep going.

## Behind the scenes: Exception handling

As you saw in the video above, if there is a `try` and an `except`, there will 
still be a runtime error. The program will stop, but it will jump to the `except`
block instead of stopping entirely.

Here's what Python does behind the scenes:

* Python encounters a problem, like dividing by 0
* Python creates a new Exception object, which stores:
  * an attribute with the file name
  * an attribute with line that was being run
  * a string with a message
* _IF IT WAS INSIDE OF A `try` block:_
  * Jump to the `except` block and keep running the program.
* _OTHERWISE:_
    * Python stops your program completely
    * Python shows the error type, for example `DivideByZeroError`.
    * Python shows the information from the Exception object.

We call this **handling** the exception.

It's similar to how people talking about "handling" a problem. 

## Example: exception handling

Getting input data from a user is often a case for exception handling.

When data has to be an integer or a float, you can try converting and use 
exception handling to deal with situations where the input isn't right. 

```python
def get_which_student_id():
    student_id_string = input('Please enter a student id')
    try:
        student_id = int(student_id_string)
    except:
        print('A student id must be an integer')
        return None

    return student_id
```

In this case, the `except` block returns `None` if the input cannot be converted
to an int. In lots of CLI projects, it's common to ask the user to enter input
again.

## Should all exceptions be handled?

In the video, we wrote a program that read data from the weather API. What if 
there was a problem with the weather API server, so that one in a hundred times, 
it ommitted the temperature in the json data? The dictionary would not contain 
`temp2m`. So our program would crash with a runtime error.

In these cases, it's not clear if it we would call this a *bug* in the program. 
Yes: the program shouldn't crash. But the program was also making a reasonable 
assumption that it was being given valid input.

It is possible to write programs that thoroughly check all of the input before 
running, and then exit with a message saying exactly what went wrong if some of 
the input isn't right. There is a tradeoff though, because it takes a lot of time 
to write the code that checks every possibility.

For example, if you had a program that saves a file to disk, and then a few 
seconds later, reads the file back from disk. A very cautious program would say
"what if in those few seconds another program deleted the file? I should check 
if it still exists before reading it back in." 

It's true that this exception could be handled, and a descriptive message could 
be shown. In most cases though, you only need to handle exceptions that are 
reasonably likely to happen.

The tradeoff also depends on how *reliable* the software needs to be. Software 
in medical devices or vehicles actually _does_ need to handle errors for 
everything. There are severe consequences to the program malfunctioning!

The best plan is often to write specific handlers for the typical cases where 
exceptions happen, e.g. the cases where there is no internet connection. For the 
rare cases, you may have a general handler at the beginning of the program that 
shows a general message that "something went wrong". That way, if of these rare 
scenarios does happen, at least the user won't see a crash message.

> In professional software development, programs often can run in a *debug* mode
> that shows more information about errors, or a *release* mode, that shows 
> friendly error messages with less detail. 

## Reasons for runtime errors

Now that you know about `try` and `except`, why wouldn't you use them everywhere? 
Wouldn't this mean that your program would _never_ crash?

This might sound like a good idea at first.

It's true that all runtime errors would not show up. But, if the program is 
doing something wrong, it's usually a _good thing_ for it to be stopped. In 
this [scene from Fantasia (Youtube)](https://www.youtube.com/watch?v=oPDSoFgivPA), 
Mickey Mouse is tired of getting water, and so makes a spell for broomsticks to 
get water for him. As you can see in the video, things would have turned out a
lot better if the brooms had stopped with a Runtime error!

(This cartoon reminds me of programming. It's like there is a bug in a 
`while loop` and the program keeps going past where it should stop.)

Runtime errors are beneficial because they stop the program. If you added 
try/except everywhere, the program would keep going, even if it were doing the 
wrong thing. Just like the cartoon, if the program keeps going, it can create
more problems!

Adding try/except in too many places isn't a good way to improve a program. It risks turning Category 2 runtime errors 
(which are annoying, but at least stop the program and show the line where the 
failure is) into Category 3 logic errors (which do not stop the program, and are 
harder to track down).

## Asserting the correct behavior

In fact, it can be a good idea to raise runtime errors yourself. 

Let's say you had a program that deletes old log files that have the extension 
`.log`. It's a complicated program with a lot of loops and `if` statements. 

Right when you get to the `delete()` part of the code that deletes the file, 
you would write something that checks again that the filename ends with `.log`. 
If it doesn't, you could intentionally raise and exception and crash the program, because 
if the filename does not end with `.log`, there is definitely a problem! Instead 
of continuing (and potentially deleting important files), you would rather stop 
everything and limit the damage.

If we lived in a perfect world, code would have no bugs, and the assert would not be needed. In reality, though, 
programs do have bugs. Even if there are not many bugs now, they might be introduced over time as the program changes.

One tool for intentionally creating an exception when something isn't right, is 
writing an **assert**. It looks like this:

```python
def complicated_delete_log_function(file):
  assert file.name.endswith('.log')
  # ... the rest of the function
```

If the file name does not end with `.log`, the program will crash with an
AssertionError. That is much better than deleting an important file.

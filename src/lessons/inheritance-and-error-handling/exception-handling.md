
# Exception Handling

We'll continue talking about the second category we discussed on the previous page, Runtime Errors.

Runtime errors will happen in software. Watching the video, we wrote a program that read data from the weather API. What if the server was down, or there was no internet connection.

Or if our program takes in input from the user and then does division, the program might run into a divide-by-zero error.

We don't really want our program to crash in these cases. We need a way to *catch* a Runtime Error and not let it stop the program entirely.

The video below will show how to do this in Python.

## Video

Please watch the first 5 minutes of this video:

https://www.youtube.com/watch?v=brICUKrzVR0

You are writing a program that divides candy into pieces. Your program asks "how 
much candy?" and "how many people?" This program works:

```python

amount_of_candy = 2.3
number_of_people = 3
candy_per_person = amount_of_candy / number_of_people

```

What if the user types in 0 for how many people?

```python

amount_of_candy = 2.3
number_of_people = 0
candy_per_person = amount_of_candy / number_of_people

```

This program will crash with a DivideByZeroError!


```python

amount_of_candy = 2.3
number_of_people = 0
try:
    candy_per_person = amount_of_candy / number_of_people
except:
    print('We could not determine the amount of candy per person.')

```

Now the program will not crash. It will run the code under `except` and keep going.

As we saw in the video above, if there is a `try` and an `except`, there will still be a runtime error. The program will stop, but it will jump to the except block instead of stopping entirely.

Python is doing this behind the scenes:

* A problem is hit, like dividing by 0
* Python creates a new object
  * on the object it stores an attribute with the file name
  * on the object it stores an attribute with line that was being run
  * on the object it stores a string with a message
* IF WE WERE INSIDE OF A TRY
  * Jump to the `except` and keep running the program.
* OTHERWISE
    * Python then stops your program completely
    * Python then shows the error type, for example `DivideByZeroError`.
    * Python then shows the information on the newly created object.

We call this **handling** the exception.

It's similar to how people talking about "handling" a problem. 

## Example uses of exception handling

When you get data that has to be an integer, or has to be a float (decimal number), this is a good place to use exception handling. You can write code that looks like this:

```python
def get_student_data(all_student_data):
    student_id_string = input('What student id to look at?')
    try:
        student_id = int(student_id_string)
    except:
        print('Please enter an integer')
        return None

    student_data = all_student_data[student_id]
    return student_data

```

## Should all exceptions be handled?

Watching the video, we wrote a program that read data from the weather API. What if there was a problem with the weather API server so that it ommitted the temperature in the json data? The dictionary would not contain `temp2m`. So our program would crash with a runtime error.


In these cases, it's not clear if it we would call this a *bug* in the program. Yes, the program shouldn't crash. But the program was also making a reasonable assumption that it was being given valid input.

It is possible to write programs that thoroughly check all of the input before running, and then exit with a message saying exactly what went wrong if some of the input isn't right. There is a tradeoff though, because it would take too much time to write the code that checks every possibility.

For example, if we had a program that saved a file to disk, and then a few seconds later, read the file back from disk. A very cautious program would say - "what if in those few seconds another program deleted the file? I should check if it still exists before reading it back in." It's true that this exception could be handled, and a descriptive message could be shown. In most cases though, we only need to handle exceptions that are reasonably likely to happen.

The tradeoff also depends on how *reliable* the software needs to be. Software in, say, medical devices does need to handle errors as well as it can!

The best plan is often to write specific handlers for the typical cases where exceptions happen, the cases like no internet connection. But for the rare cases, is to have a general handler at the beginning of the program shows a general message that "something went wrong". That way, if one of these rare scenarios does happen, at least the user won't see a crash message.

> In professional software development, commonly programs can be run in either a *debug* mode (that shows a lot of information about errors) or a *release* mode (that shows friendly error messages with less detail). 

## Reasons for runtime errors

On a related note, now that we know about `try` and `except`, why don't we use them everywhere? Wouldn't this mean that our program would never crash?

This might sound like a good idea at first.

In this cartoon, Mickey Mouse is tired of getting water, and so makes a spell for broomsticks to get water for him.

https://www.youtube.com/watch?v=oPDSoFgivPA

(This cartoon reminds me of programming. It's like there is a bug in a `while loop` and the program keeps going past where it should stop.)

Runtime errors are beneficial in a sense because they stop the program. If you added try/except everywhere, the program might keep going, even if it were doing the wrong thing. Just like the cartoon, if the program keeps going, it can create problems!

> In fact, it can even be a good idea to put intentional runtime errors in. Let's say you had a program that deletes old log files that have the extension `.log`. It's a complicated program with a lot of loops and `if` statements. Right when you get to the `delete()` part of the code that deletes the file, you would write something that checks again that the filename ends with `.log`. If it doesn't, you would write code to intentionally crash the program - because there is definitely a problem somewhere and we want to stop everything and limit the damage. This strategy, of intentionally creating an exception when something isn't right, is called writing an **assert**.




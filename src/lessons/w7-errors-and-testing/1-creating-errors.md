# Exceptions

Despite it's title, this section is not about writing bad code, quite the opposite! Throughout our experience as programmers, we will run into plenty of **Runtime Errors.** Time to understand a bit more about them: How do they work, how do we handle them, and how do we customize them?

## Behind the scenes: Runtime Exceptions

When Python runs into a problem, it follows these steps:

* Python encounters a problem, like dividing by 0
* Python creates a new `Exception` object, which stores:
  * an attribute with the file name
  * an attribute with the line that was being run
  * a string with a message
* Python **stops the program completely**
* Python shows the error type, for example `DivideByZeroError`.
* Python shows the information from the Exception object

This type of object, which stores information about an error that occurred, is called an **exception object**.

This sequence of events is known as **raising an exception**.

So once again, we run into a practical example of *Object Orienter Programming*. The **exception object** already has data and methods to help us deal with a bad situation:

1. The file name and line number help us pinpointwhere the exception comes from.
2. The name of the error and the message that comes with it _hopefully_ help us understand why the error occured. 

As frustratingas seeing many lines of red text is, think of the alternative: What would we do if our program just crashed, without any kind of information? Being able to work with these exceptions is powerful. Let's get more acquainted with them:

#### Try it: Investigation

> Write a program that uses a variable that does not exist. What error type is shown?

> Write a program that causes another type of error of your choice: Just do something you expect to break. What's the _type_ of the **exception object** you've encountered? What message is provided? Does it seem helpful?

## Handling errors:

You are writing a program that divides candy into pieces. Your program asks "how 
much candy?" and "how many people?" Test the program: If you provide 10 candies and 5 people the result should be 2

<iframe src="https://trinket.io/embed/python3/bac541226f" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

What happens however if the user inputs "seven" or "twenty two" instead of numbers?

Even if the users know to type in numbers, what if they provide a negative number? what if they provide 0 as the number of people?

In the first scenario, we will get a `ValueError` as we are trying to convert arbitrary strings to integers.
In the second scenario, we will get an negative result, but no error.
In the final scenario, we will get a `ZeroDivisionError` Error. 

The second scenario may lead to logical errors, but it is not **immediately halting our program**. There may be other things we want to do within our programs: data to store, other questions to ask, APIs to call. None of those would happen in the first and third scenari as **exceptions immediately halt the program**

What if we don't want to do that? well we can **handle** an exception. The way python approaches this is by using the keywords `try` and `except`. The video below is a solid introduction to the new syntax you should watch:

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/brICUKrzVR0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

So bringing the ideas from the video, here is how we can improve our code to handle the errors we saw before:

<iframe src="https://trinket.io/embed/python3/e9a85e2d34" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Behind the scenes: Exception handling

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

We call this **handling** the exception: We know it could happen, but we won't let our program stop because of it. 

It is a matter of debate, and experience, whether or not an exception should be handled though. You should not **always** default to using `try` `except` whenever you run into an exception. 

Handling these two exceptions, we have made our program more **resilient**: It will not randomly crash when a user gives a bad input, but it's up to us to make sure that the experience remains good and useful - perhaps we can put our function in a loop that keeps asking until we get good input?

Some programs really want to be **resilient**: If you are writing software for planes, or for banking systems, or medical applications, crashing the program could be terrible! if you can think of a scenario where an exception would occur, you better handle it!

There are other scenarios though where we may want to be **strict**: If an exception would occur, let the program crash, because that is better than the alternative: Imagine for example that our program is supposed to save our work in a file, and opens that file whenever we run the program. If we find the file is missing, we should freak out! Let's raise an exception! nothing can move forward if we don't have that key file.

## Creating Exceptions:

Now how about if we wanted to make our candy program more **strict**. How do we treat the scenario where someone puts a negative number with the same level of **seriousness** as the other two scenarios? Python is perfectly fine with it, we can convert '-2' to an integer, and divide negative and positive numbers. 

Let's create a new exception that we want to trigger whenever someone inputs a negative number as an input. Our goal is to:
- Interrupt the program whenever we realize the user gave us a negative number as input.
- Point out where the issue occurs.
- Show a helpful message - let's say a `NegativeInputError` with instructions on how we do not want negative inputs.

Many of these behaviors are similar to other exceptions we have seen. We know these exceptions are objects that belong to a class...let's try to inherit from them!

The `Exception` class is straightforward. its `__init__` method takes a single parameter: A message to be displayed. Let's use that information to create a new child of `Exception`:

<iframe src="https://trinket.io/embed/python3/487806abe1" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here we create a `NegativeInputError` class that inherits from `Exception`. `NegativeInputError` takes a value in its `__init__` method, uses it to create a message that it provides to its parent's `__init__` method, and done. Try running the code and providing a negative input. 

Nothing happened! this is part of the catch with creating your own exceptions: You have to decide when they should be raised. We do that using the `raise` keyword

<iframe src="https://trinket.io/embed/python3/8e802d1708" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Note that we add two if statements to check our input. If any of the inputs is negative, we `raise NegativeInputError(input_value)`, which triggers an exception in the code: If we raised with the first input, we never ask for the second, the program ends right then and there. 

## Recap:

- `Exception` is a class that you can inherit from to create your own custom exceptions and error messages. 
- Built in classes for exceptions also inherit from `Exception`, you can read more about them [here](https://blog.airbrake.io/blog/python/class-hierarchy)
- You can trigger your new exceptions by using the `raise` keyword
- You can make your program more **resilient** to exceptions by using `try`, `except`, and `finally`:
	- `try` includes the code that _could_ trigger an exception.
	- `except` if an exception happens within a `try` block, the code in `except` will run
	- if provided, the code in a `finally` block will always run, whether or not an exception was handled.
- `except` can also be customized to handle only a specific kind of error by using `except ExceptionClass`  






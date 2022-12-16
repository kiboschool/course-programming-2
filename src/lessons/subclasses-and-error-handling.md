# Subclasses and Error-handling

In this week, we will continue last week's topic of Classes. There is a way to create a class that uses information from another class. This is called making a "subclass", also referred to as a "child class". Subclasses can be used to model cases where the program should sometimes run in a slightly different mode, with different behavior or added features. We will go through what subclasses mean and how to use them.

You have probably seen that when something goes wrong in your program, Python will say there was an "Error" or "Exception" when it dumps out information to your screen when the program crashes. In this week we will talk about precisely what is happening when a program crashes this way. In fact, there is even a way to intentionally cause the program to "crash", by using a statement called `raise`.

And there is also a way to stop the program from crashing by intercepting an error. The statements to do this are called `try` and `except`. 

Raising errors is a useful tool when writing subclasses. For example, a subclass might have specific requirements about the type of data being passed in, like one of the parameters must be a number between 1 and 5. If we can check that the parameter is valid early on, and intentionally say "you gave me bad data!" this is better than having the program run into complicated issues later on.

## Learning Objectives

* Be able to read and write code that uses subclasses.
* Understand how subclasses inherit methods from the parent class
* Learn about some specially named methods called "dunders".
* Be able to use `raise` to cause an error.
* Be able to use `try` and `catch` to recover from an error. In particular, this structure is used as part of the standard way to go from a text string to a number.
* Begin to learn when, and when not to, use classes to implement a program.
 

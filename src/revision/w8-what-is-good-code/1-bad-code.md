# Bad Code

As we are having a conversation about code quality, let's take a moment to study some _absolutely terrible code_. 

<iframe src="https://trinket.io/embed/python3/0fc4596e58" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I want you to take a moment to read through the code and think about what it will do. Don't take more than 5 minutes on this, as this code may hurt your head. 

Now I want you to state what the code does. What do you predict will happen when you run it? Run it and see if your prediction was correct. 

Now let's take a moment and read through this other example of code in the same way. Read for 5 minutes, think about what it will do, then run it. 

<iframe src="https://trinket.io/embed/python3/47f35a7352" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

You may have seen this coming. The two programs produce the exact same output! They both display a time, in this case `13:59:47`, then display the following 29 possible timestamps, adding one second each time.

Reflect for a moment: What made the first example hard to understand? and how does the second address it? 

Imagine if you were given a task to modify this code to add new functionality  Where would you like to start from? example 1 or example 2?

Let's dig into what makes example 2 better code

## Make your code easy to read.

Let's start with the most obvious challenge of example 1: The developer did not do us any favors explaining what's going on:
* We have meaningless names: What do `x`, `y`, and `z` actually mean? 
* We have magic numbers: Why are we looping 30 times?
* We use functions without explanations: what is `zfill?` do I really have to open google every time I read code?
* We have nested logic: The deeper you nest your logic - in other words the more if statements you have inside other if statements inside loops inside try/except etc. The harder it is to make sense of all the ways your code could execute.

We have been able to address this in example 2 by applying ourselves and communicating clearly:
* There is a `Clock` class. This probably has to do with time!
* it's init method takes on 3 parameters called hours, minutes, and seconds. Now we know at a glance that the code has to do with time.
* The `Counter` class has some tricky elements, but at least it has comments to explain the `zfill` method and how the `tick` is designed.
* We have very few numbers directly used in code. When we do, they can be understood from context (The upper limit for the value of minutes is 60). The duration we want to simulate a clock is stored in a variable so it's clear what would happen if we modify it.
* While we still have a little bit of nested logic, it's made more understandable: Tick the seconds, if they reset (returning True) then tick the minutes. If they reset then tick the hours!

## Make your code easy to reuse. 
Beyond immediate readability, let's think about future reuse: In example 1, nothing can be readily reused! there is no function, no method, no class. Where do we begin if we wanted to make changes?

Example two puts the code together in a more organized way: We now have a `Clock` class which we can use in many scenarios. We can initialize to the current time and use it to simulate time passing. We can initialize it as 00:00:00 and use it as a stopwatch. It's versatile. 



With the basic building block of the `Counter` class, we could make easy modifications by using our knowledge of OOP: What would a counter that counts "down" instead of counting "up" look like? that way we could have a timer instead of a clock! We could inherit some aspects of the `Counter` class, and just change the `tick` method to advance the clock.

Beyond using methods and classes, one of the big benefits of our approach is that **we have built useful abstractions**. If we needed to build a `Stopwatch` class for example, we can think of ways to use a `Clock` that don't even require us to _know_ how the `Clock` class works in depth, how it's methods are implemented. We know we can set a clock, print it, and make it advance correctly. We can use that!

## Make your code focused:
As much as possible, focus on having each function, each method, perform one job only. Moreover, if a function peforms a particular task, we shouldn't have other parts of the code doing the exact same thing! let's just reuse the same function.

This unlocks a lot of benefits for us:
	1. It's easier to think about a function when it's goal is small and focused.
	2. It's easier to know where to make a change, then trust that it will be applied accross our program.
	3. It's also easier to test the function if it only does one thing.
The demo_function performs the main task. The tick method moves the clock forward, etc. This also makes it easier to reuse a function in other parts of the project when it does _exactly_ one thing. You don't have to worry about unwanted side effects.

The same thinking can apply at a higher level: We can think of a program as having has different layers. Code in the higher layers imports and uses classes that are written in lower layers. The highest layers are generally the user-interface code, and the lowest layers are the simple helper functions that do not need to call into any other modules.

Think of it this way, the user-interface has a lot of specific problems it needs to solve: What does the UI look like? what do we write? what do we do? This means a lot of code focusing on this. For our command line programs, this is equivalent to all the code we write to print instructions and gather user input from our users, testing if the input is correct, etc. 

So what then? once we have the right user interface, what should we do with the information we get from the users? that's where the deeper layer can come in, and all the code for it. All the code that has to do with our **business logic** (Deciding if a transaction should go through. Creating a new account. Checking our inventory to see if we can sell an item. Saving some data to a file etc..) does not need to know about our **presentation logic** (What do we display? where? how do we get input?). They each have their own challenges. 

A way to think about abstraction is that it involves splitting code into higher and lower layers, and moving details from the higher layer into the lower layer. These layers can get very deep!

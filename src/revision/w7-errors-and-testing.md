# ERROR! ERROR! ERROR!

We are nearing the end of the course, and we have read, analyzed, and written quite a bit of code so far. This week we will deal with errors and exceptions in our code in a couple new ways:

First of all, we will talk about the `Exception` class itself, and see how to handle errors in code as well as create our own custom errors! Why would we want to do that? we will explore it more in the content, but this ultimately has to do with communication: The same way `Python` teaches you how to use its syntax and tools safely (for example, don't divide by 0. Don't try to index into a location where we have no data), you can convey that same information to users of the code you create.


We will then get proactive with our code: In week 2 we spoke about debugging - a reactive way to deal with runtime errors or logical bugs - this week we will focus on **automated testing**. You've been _using_ automated tests ever since programming 1! That is the code that you ran to check your assignments before submiting them. Turns out writing code that confirms that another piece of code works correctly is very, very valuable. So valuable in fact that for on average, for every hour of coding, a professional developer expects an extra half an hour testing that code. [[1]](https://www.microsoft.com/en-us/research/uploads/prod/2019/04/devtime-preprint-TSE19.pdf). We will learn the mindsets and tools needed to be able to write our own test moving forward.


## Preview:
Here is what we will be exploring this week:
* How can we prevent exceptions from triggering in our code?
* How can we create custom exceptions to handle our specific logic?
* How do we define a unit test? What are other kinds of testing?
* How can we use the unittest framework to write unit tests?

## Why does this matter?
Getting more familiar with exceptions: How they are made, handled, and raised, is important for a new developer as it is a way we communicate our ideas in code. If something raises an exception, then it is serious!

Similarly, testing is a key part of professional development and you will inevitably spend hours testing your code in the future. This is time to learn the fundamentals.


> [1]: A. N. Meyer, E. T. Barr, C. Bird and T. Zimmermann, ["Today Was a Good Day: The Daily Life of Software Developers,"](https://www.microsoft.com/en-us/research/uploads/prod/2019/04/devtime-preprint-TSE19.pdf) in IEEE Transactions on Software Engineering, vol. 47, no. 5, pp. 863-880, 1 May 2021, doi: 10.1109/TSE.2019.2904957.
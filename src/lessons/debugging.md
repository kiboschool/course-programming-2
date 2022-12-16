# Debugging

If a program isn't working, how do we know what's going wrong? When there are hundreds of lines of code, do we need to look at each line to find the problem, or are there faster ways of seeing where the problem is? This process is called debugging.

We will introduce some tips and techniques for finding out what is happening in a malfunctioning program, whether it is a program you wrote or another program you are using.

## Learning Objectives

* You will know some tips for `print` debugging, for example, a way to display the values of all local variables.
* There is a way to freeze a program at a certain point and look at the exact line of code that the program was about to run. This type of stopping the world debugging requires special tools, and isn't always needed, but can sometimes be very helpful. With this type of debugging you can step line-by-line to see exactly where the program goes, like in the PyTutor website.
* We will talk about organizing code to make future debugging easier.
* You will be able to better document your code. For example, "docstrings" are like multi-line commemnts that can be used to type an explanation of what a function does.
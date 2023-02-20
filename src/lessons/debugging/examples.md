# Types of Bugs

## Video: Intro to Debugging

> This video from Linkedin Learning gives an overview of bugs and debugging in Python.

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/b7VbiZBg-dA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Types of Bugs

The video introduces terms for different kinds of bugs:

- Syntax Errors
- Runtime errors
- Logic errors

**Syntax errors** are (usually) easy: the program won't run at all, and it often tells you where the mistake is.

**Runtime Errors** are a little harder: the program runs, but crashes, and prints out a bunch of information about the error and what was happening up to that point. This means you have to recreate the bug to figure out how it happened, but 1) it's clear there is a bug and 2) you have a starting point for investigating.

**Logic errors** are harder still. First, it's not obvious that you have a bug at all. Next, if you only have the erroneous results of the program, you have to go find more information in order to figure out where the error is in your code.

The video also mentions some of the tools and processes of debugging. Specifically, the process is about _finding information_, _forming hypotheses_, and _testing your hypotheses_. That's (more or less) the scientific method!

## Types of Python Errors

Not every bug will crash with an error! But, knowing the types of errors can be really helpful for understanding what is happening when you see one.

This [Python Errors flowchart](https://pythonforbiologists.com/29-common-beginner-errors-on-one-page.html) can help you diagnose an error if you are seeing one.

## Test Failures

In your courses, you are often writing code to solve a pre-defined task, with automated tests to check your work. Test failures are a specific kind of bug. 

Each test has an expectation for exactly what should happen when the code runs. If the code does something else -- even if what it does makes sense to you -- the test will fail.


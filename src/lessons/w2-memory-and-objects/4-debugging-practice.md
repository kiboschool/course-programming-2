# Stop the World!

As an aside, you may be looking at some of our earlier examples and wondering how come we can see all these variables and objects and frames etc. Wouldn't this be helpful while working on assignments and projects?

It indeed would be, and that's exactly why we have access to a **debugger**

A debugger stops the execution of the program at a _breakpoint_, and you can view variables and step the code forward step by step to see how things change. Since it stops the execution of the program, it's also called 'stop the world' debugging.

## Video: Breakpoints and pdb

> This video gives a quick intro to the `breakpoint()` function and the basics of the pdb debugger

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/aZJnGOwzHtU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Key points:
- add a breakpoint with `breakpoint()`
- Python will stop at the breakpoint when you run the program
- Basic pdb commands: help, where, print, next, step, continue, quit

For a more in-depth tutorial, see this [Python debugger crash course](https://www.youtube.com/watch?v=0LPuG825eAk)

## Debugging in the IDE

As an alternative to running pdb in the terminal, you can also run an interactive debugger from your IDE.

> This video from NeuralNine explains how to use an interactive debugger from the IDE Python.

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/4jRfXluDmKY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

- Set a _breakpoint_ by clicking on the sidebar
- Run the program in 'debug' mode
- The program stops at the breakpoint
- While it is stopped, you can look at the variables, evaluate expressions, or run the code forward step by step to see how the variables change after each line executes.

This can help us solve all kinds of problems. In fact, this is a good time to define the kind of problems we can run into in this video: 

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

## Finding information:

The first question you should be able to answer clearly, for yourself and whoever might be helping you, is: "What is wrong?"

Are we dealing with a Syntax error? A runtime error? or a Logic error?

Where in the code is it happening? Luckily syntax and runtime errors tend to come with error messages that point at a specific line. Logic errors, however are harder to track. This is where using the debugger we introduced above is very helpful: Step through the code with the debugger, saying outloud what you expect would happen each step: Where do you find a difference between your expectation and what the code did?

## Forming Hypotheses

After you've gathered information, you need to make a guess about what is going wrong. Sometimes, it's easy to come up with lots of potential ideas. Other times, it's hard to come up with any guesses at all.

If you get stuck, it's worth checking your assumptions again and gathering more data, and seeing if that helps. If you're still stuck, it's often helpful to share your bug with a friend, or take a break and come back to the bug fresh.

## Testing your Hypothesis

Remember: Science is about **disproving** hypotheses. Not proving them! The key question is "What evidence would show that this idea is _false_?".

When you are debugging, you will find information about your program and how it runs. As you do, you'll come up with hypotheses for how it might be going wrong. When you do, you can't trust that you know for sure that you have correctly identified the error. You have to try to _disprove_ that it is the error.

Testing your hypothesis usually means _changing the code_ and _running it again_. It's really helpful to have a _minimal reproducible example_ when you do. If it's easy to repeat the bug, then you can quickly check the results of your change.

Tips for experiments:
- Test only one thing at a time
- Say out loud (or write down) what your hypothesis is, and why you think your change will help you tell if your hypothesis is wrong.
- Make experiments quick and repeatable

Often, beginners will try changing random things (or nothing at all) and rerun the code to see what happens. This is _not_ testing a hypothesis! Your changes should help you find out if your hypothesis about your code is correct.

This [blog post from CS Professor John Regehr](https://blog.regehr.org/archives/199) lays out a scientific approach to debugging, and is a strongly recommended read.

## Practice: Python debugger

Follow these 5 mini-exercises to practice navigating code using the Python debugger:

> [Five exercises to master the Python debugger](https://www.tjelvarolsson.com/blog/five-exercises-to-master-the-python-debugger/)

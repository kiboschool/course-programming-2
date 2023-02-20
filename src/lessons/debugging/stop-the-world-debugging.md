# Stop the World Debugging

The big alternative to print debugging is using an interactive debugger.

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

## Practice: Python debugger

Follow these 5 mini-exercises to practice navigating code using the Python debugger:

> [Five exercises to master the Python debugger](https://www.tjelvarolsson.com/blog/five-exercises-to-master-the-python-debugger/)

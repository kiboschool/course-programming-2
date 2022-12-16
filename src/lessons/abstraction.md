# Abstraction

Abstraction is an important concept in computer science, it isn't easy to describe, but by the end of this course you will gain an understanding of it. Imagine a game that has a save() method to save the current progress, and a load() method that looks for the saved information and restores it to resume where you were. We'll talk about how the program can treat save() and load() as "abstractions" that don't have assumptions aobut the internals of what save and load do internally.

This is a good way to write a program because in the future we can easily add features. We could make a new save() and load() that write to a database for very fast save times. Or even make a save() and load() that store information on the internet.

## Learning Objectives

* First, we'll talk about "helper functions", which is writing a simpler-to-use function instead of needing to have copies of complicated code in many places.
* An "interface" refers to the methods on a class. If two different classes implement the same methods with the same parameters, we can say that they share the same "interface".
* Even if the program gets the right answer and functions correctly, it still might not be written in the best way possible. For example, it might be hard to read and understand the code, which in the world of computer science, is still important. This is part of what it means to have code quality.
* You will see in a hands-on example how abstraction helps us make changes to a program more quickly.


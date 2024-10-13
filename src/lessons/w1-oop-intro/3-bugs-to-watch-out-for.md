# Bugs to Watch Out For

## Video

A video with warnings about common bugs that we might accidentally run into:


<div style="position: relative; margin-top:1em; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/3OWb-DYTBww?rel=0" title="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

What we saw in the video:

* If the indentation isn't right,  errors can happen. For example, methods need to be indented to the right to be inside the class.
* If the name of the initializer method is `init()`, or anything that's not `__init__()`, it won't be called and won't work.
* If a method doesn't have `self` as the first argument, this can cause the error message `takes 0 positional arguments but 1 was given`.
* If you don't spell all attributes correctly, you might get an attribute not found error.
* If you forget to add parentheses when creating a class, it won't work.
* If you don't use capital letters for a class, the code will be harder to understand.

## It's not always easy

It isn't always easy to know how to make classes and methods. It's like how for functions, there isn't a clear way to decide what should be inside a function, and what the function should be called. Programmers often ask themselves questions like:

* "What should this class be called?"
* "Should I add the code as a method on this class, or a method on another class?"
* "Should these lines of code be a method, or should they be a function in another file?"
* "Should the method do both of these things, or should there be two different methods?"

It's normal to find it difficult answering these questions. The goal is for the program to be understandable by other people. We will do our best and keep working!

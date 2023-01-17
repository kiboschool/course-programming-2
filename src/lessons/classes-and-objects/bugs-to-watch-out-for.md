# Bugs to Watch Out For

## Video

A video with warnings about common bugs that we might accidentally run into:


<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/3OWb-DYTBww?rel=0" title="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

The most important tips from the video:

* If the indentation isn't right,  errors can happen. For example, methods need to be indented to the right to be inside the class.
* If the name of the initializer method is `init()`, or anything that's not `__init__()`, it won't be called and won't work.
* If a method doesn't have`self` as the first argument, this can cause the error message`takes 0 positional arguments but 1 was given`.
* If you don't spell all attributes correctly, you might get an attribute not found error.
* If you forget to add parentheses when creating a class, it won't work.
* If you don't use capital letters for a class, the code will be harder to understand.

## Sometimes it's not easy!

Choosing how to make classes and methods is like writing functions, or like programming in general. There isn't a clear right and wrong way to decide what should be inside a function and what the function should be called. Programmers often ask themselves questions like:

* "What should this class be called?"
* "Should it be a method on this class, or a method on another class?"
* "Should this be a method, or should it be a function in another file?"
* "Should the method do both of these things, or should there be two different methods?" 

It's normal to find it difficult answering these questions. We will do our best and keep working!

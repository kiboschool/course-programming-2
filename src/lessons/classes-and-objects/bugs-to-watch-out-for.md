# Bugs to Watch Out For

## Video

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/3OWb-DYTBww?rel=0" title="Weather - Reading from Dictionaries" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

A video with warnings about common bugs that we might accidentally run into:



The most important tips from the video:

* Need to indent correctly
* Needs to be exactly `__init__`, not `init`
* All methods need `self` as the first argument
    * Forgetting `self` might cause the error message`takes 0 positional arguments but 1 was given`.
* Spell all attributes correctly
* Make an instance of a class by writing the class name with parens after it

## Sometimes it's not easy!

Choosing how to make classes and methods is like writing functions, or like programming in general. There isn't a clear right and wrong way to decide what should be inside a function and what the function should be called. Programmers often ask themselves questions like:

* "What should this class be called?"
* "Should it be a method on this class, or a method on another class?"
* "Should this be a method, or should it be a function in another file?"
* "Should the method do both of these things, or should there be two different methods?" 

It's normal to find it difficult answering these questions. We will do our best and keep working!

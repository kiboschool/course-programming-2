# Video on Inheritance

Please watch the first 5 minutes of this video. It contains detailed information about inheritance in Python.

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/C8qE3mKiBrQ?start=0&end=300" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Fun fact (optional)

<details>
<summary><strong>Runtime errors use inheritance (optional)</strong></summary>

Remember what we showed a few pages ago, when we talked about all of the types of exception objects for the errors in Python?

The exception objects that Python creates when a runtime error gets hit - the ones that capture the line number where the exception was raised, the current file, and so on. 

A `ZeroDivisionError` is a type of `ArithmeticError`, which is a type of `Exception`, which is a type of `BaseException`.

Fun fact: Python internally uses inheritance for this! The objects are instances of classes.  For example, there is a class `ZeroDivisionError` that is a child of a class named `ArithmeticError`. You can glance at the list [here](https://blog.airbrake.io/blog/python/class-hierarchy) to learn more. 
</details>

## Conclusions

* Inheritance is the ability to define a new class that is a modified version of an existing class.

* This relationship between classes—similar, but different—is one of the reasons to use inheritance, because otherwise the code would be duplicated. To define a new class that inherits from an existing class, you put the name of the existing class in parentheses. When a new class inherits from an existing one, the existing one is called the parent and the new class is called the child.

* It's possible that, if used excessively, inheritance can make programs difficult to read. When a method is called, it is sometimes not clear where to find its definition. The relevant code may be spread across several files.

* In some cases, though, you can express a child class as being *a type of* the base class. For example, a `PersistedListJson` *is a type of* a `PeristedList`. For cases like this, inheritance reflects the natural structure of the concepts, which makes the design easier to understand.

<!-- a couple sentences here borrowed from Think Csci -->


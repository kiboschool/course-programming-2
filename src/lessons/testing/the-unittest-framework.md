
# The Unittest Framework

## Creating tests in Python

Watch this video to see how to use the `unittest` framework in Python:

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/Oz0Z2tNuvDw?start=10&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

(You don't need to work on the example from 10:10 onwards in the video).


## Frameworks

You have noticed that when we have a test file, we have used the `unittest` module. Why didn't we just write some functions with asserts, and call them at the bottom of the file?

A few reasons why it is helpful to use a **testing framework** like `unittest`:

* Shows a console UI when running the tests, with a count of passes and failures.
* Useful methods like `self.assertEqual`. This is similar to the `assert` keyword, but if the values are not equal, the values are shown to the console as part of the error message.
  * For example, your test might say `self.assertEqual(result, '4')`
  * The error message will say something like `expected '4' but got '5'.` instead of just `AssertionError`.
  * This makes it quicker to debug/discover the problem.
  * Sometimes the bug is a real bug in the program, and sometimes it is simply a bug in the test.
* Because `unittest` is a common framework, other programs connect to it. For example, there are VSCode extensions that make it convenient to work with `unittest` tests.

## Test Classes

It might seem confusing to need to create a class that inherits from unittest.TestCase. Why did we have to write `class TestMultiply(unittest.TestCase)`?

We're mostly just using a class to organize all of the tests into one structure. We don't really have a need to create instances of the class or really use object-oriented features. One benefit of the class structure is that if your test needs helper methods, they can be part of the structure of the class instead of being floating as functions outside (which is less organized, especially if you have one test file with several test classes).

Also, if you add methods called `setUp` or `tearDown` to the class, `setUp` will run before each test, and `tearDown` will run after each test. Behind the scenes, these are overriding methods on the base `unittest.TestCase` class.

One way to organize test classes is to create one test class for each corresponding class in your source code. And then for each method on your real class, create several test methods in the test class to cover the different scenarios for that method.


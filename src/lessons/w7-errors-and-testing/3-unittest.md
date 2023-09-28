# The Unittest Framework

As mentioned, testing is important, so you can imagine that the hundreds of thousands of python developers have been writing tests for years now. This means that we, as a community, have a sense for how tests should be run: 

- We need to make assertions and know where they fail and where they succeed.
- We want to test a lot of logic at once, so even if something fails we shouldn't stop the test.
- We want to not have to write a ton of code.
- We want the tests to run fast

And many other notions. Usually, when the community starts getting strong opinions about how things should be done, members of the community will create a **framework**: A library or modules that implement their opinion. unittest is the most common testing framework for Python. There are others, that behave slightly differently, but let's just focus on this one for now.

## Unittest in practice

Watch this video to see how to use the `unittest` framework in Python:

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/Oz0Z2tNuvDw?start=10&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


## Frameworks

You have noticed that when we have a test file, we have used the `unittest` module. Why didn't we just write some functions with asserts, and call them at the bottom of the file?

A few reasons why it is helpful to use a **testing framework** like `unittest`:

* Shows a console UI when running the tests, with a count of passes and failures.
* Useful methods like `self.assertEqual`. This is similar to the `assert` keyword, but if the values are not equal, the values are shown to the console as part of the error message, saving you time.
  * For example, your test might say `self.assertEqual(result, '4')`
  * The error message will say something like `expected '4' but got '5'.` instead of just `AssertionError`.
  * This makes it quicker to debug/discover the problem.
  * Sometimes the bug is a real bug in the program, and sometimes it is simply a bug in the test.
* Because `unittest` is a common framework, other programs connect to it. For example, there are VSCode extensions that make it convenient to work with `unittest` tests.

## Test classes

It might seem confusing to need to create a class that inherits from unittest.TestCase. Why did we have to write `class TestMultiply(unittest.TestCase)`?

We're mostly just using a class to organize all of the tests into one structure. We don't really have a need to create instances of the class or really use object-oriented features. One benefit of the class structure is that if your test needs helper methods, they can be part of the structure of the class instead of being floating as functions outside (which is less organized, especially if you have one test file with several test classes).

Also, if you add methods called `setUp` or `tearDown` to the class, `setUp` will run before each test, and `tearDown` will run after each test. Behind the scenes, these are overriding methods on the base `unittest.TestCase` class.

One good way to organize test classes is to create one test class for each corresponding class in your source code. And then for each method on your real class, create several test methods in the test class to cover the different scenarios for that method.

## A hidden benefit to writing tests

If you write tests only a long time after developing your program, it might be tricky to add tests. Your program might have classes and methods that perform many actions, and so one method might need 5 or more tests to cover what it does. You also might need to write extensive `setUp` and `tearDown` helpers, because some classes expect complex state to be present.

As a program grows over time, it is natural for your program to begin to depend on the precise interaction between multiple classes. This is called coupling, and it can be fragile because adding future changes can cause the program to stop working in hard-to-debug ways.

But if you are writing tests around the same time as developing the program, writing the tests can influence the way you write the program code too. The tests might influence you to write shorter methods that do fewer actions. And the tests might influence you to have smaller classes that are more focused on one part of the program. These traits are beneficial to making a flexible program that can be changed and repurposed in the future, which is an important benefit for professional software.

Because unit tests focus on just one method of one class, it helps you avoid coupling because it encourages you to write classes that can work more independently.

You are still learning as a programmer, so don't worry if you don't yet feel how writing tests can help in this way. It's just something to keep in mind: in larger scale projects, a hidden benefit to writing tests is that they help organize your program structure.

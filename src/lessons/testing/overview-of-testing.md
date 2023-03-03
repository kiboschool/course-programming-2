# Overview of Testing

Let's say you've written a program that runs processor instructions, like you did in the project earlier this year. How can you know if the program is running correctly or not?

- You could write a little bit of code at the bottom of the file. The code will run the program with some example input, and print the results. You'll then look at the results to see if they match what you expect.

There's nothing wrong with using temporary print statements like this to check the program as you are writing it.

Once your program gets bigger, though, you'll find yourself wanting to check the results often. (Each time you make a change to the program, you'll often want to confirm it still works). It takes time for you to have to manually look at the printed output!

- You can save a step. Instead of printing the results, you could write an `if` statement that compares the results to the expected output. If the results do not match what was expected, print a message like "warning: did not get the expected result".

- An even better way to check the results is to use Python's `assert` keyword. `assert` is built in to the language. This shortens the code because it can now be all on one line. For example, if you expect the result to be `123`, you would write the line `assert run_processor('example.json') == 123`.

- Another benefit of assert is that it will raise an `AssertionError` if the value does not match. That way you'll know right away that it came from an assert, and that the error isn't another type of problem in your program like a ValueError or a TypeError.

The next step is to write more checks. For example, if your program can run in two different modes, you should test each mode separately.

Over time, you will add more and more checks. You've now written what is known as "test code".

Your source code will get longer and longer. Also, when someone is reading your program's code and is trying to find a class, they will be distracted by seeing a lot of test code instead. For these reasons, it is good to move the tests into their own file. For example, for the OOP Jukebox project, the program was in `jukebox.py`, and the tests were in their own file, `test_jukebox.py`.

**The most important part:** If you didn't have tests, whenever you changed your program, there would be a chance that your change might introduce a bug. When you do have tests, there is a feeling of confidence - as long as the tests give the expected results, you know it is likely that your program is still working.

# Types of tests

Over the years, software developers have come up with different types of testing strategies. In professional software development, a project often has at least a few tests of each type.

> Note that the definitions below are the standard definitions, but when people talk, they sometimes use the terms more loosely: even though technically the term "unit tests" refers to a specific type of test, when people chat they'll sometimes refer to just about any test as a unit test.

Some common types of tests:

### Automation tests

A high level test that involves simulating user input. For example, an automation test for a website could simulate moving the cursor, clicking on buttons, and inserting text into the text boxes as if a user were typing there.

A related term is _end-to-end test_. An end-to-end test for a program that interacts with an api will communicate with a real server, and follow essentially the same code paths that would occur if a customer were using the program.

### Integration tests

Tests that focus on connecting the different parts of the program.

For example, your program might have a class that records student registration and a class that saves the results to a database. An integration test would confirm that the classes are interacting in the expected way, and that the changes actually make it to the database.

You typically don't need as many integration tests, because there typically isn't as much variability. As long as a few records make it into the database successfully, you can be pretty sure that the database connection code is correct, and that any bugs would be coming from other parts of the program.

### Component tests

These test a component of your program. For example, there could be part of your program that computes information and writes a result file to disk. A component test could import only that part of the program, send it input, and check that the file was written.

These are similar to integration tests, but instead of the focus being on the connection between the pieces of the program, the focus is on the functionality+end result. There are often many, to test each supported feature.

### Unit tests

Unit tests focus just on one small piece of your program. You would write a unit test to check just one method of a class. The idea is to isolate just one small piece of the code to test - not allowing any other code to be involved.

This does have a benefit - one of the frustrations with automated tests is knowing what to do if a test fails. Because unit tests only look at one place, that is the place causing the problem.

For a software project, there can easily be thousands of unit tests. So it is important for the tests to run quickly. It is also important for the tests to be reliable. You will be running unit tests frequently and should never be distracted by random failures that aren't caused by actual bugs.

For these reasons, a unit test should never communicate with an api - making an internet call is slow, unreliable (the server might be down or throw a transient error), and potentially expensive (the api might have a limit of the number of calls allowed before blocking you or charging money).

You will read later more about unit tests, including how to write unit tests for a program that relies on an api to work.

<!--
### Comparisons

You can think of these categories on a spectrum from lower level (unit tests) to higher level (automation tests). In professional software development, tests are usually somewhere around the unit test or component test level.

<details><summary>Higher level tests -- See the Pros/Cons</summary>

* Pro: test reflects closer-to-real-world conditions
* Pro: in some cases, can be faster to write the tests
* Con: slow to run, for example, they might need to launch a real web browser
* Con: are the most fragile. a common problem in automation tests. sometimes an automation test simulating clicking on a button will fail because the button has moved, or hasn't loaded yet.

</details>


<details><summary>Lower level tests -- See the Pros/Cons</summary>

* Pro: if there is a failure, it's more clear where to investigate
* Pro: run very quickly, and they help you catch issues right away.
* Pro: guides you to structure your program in a more flexible way (more on this later)
* Con: many bugs are caused by problems in the interaction between parts of the program. those bugs can't be caught by unit tests.
* Con: for very simple methods, can feel like a waste of time+redundant, even though it is usually worth it.
* Con: catches problems in your classes. but can make it slower to refactor (make structure changes) to your program because the unit tests all need to be updated.

</details>



Tests are a good addition to any program. They not only help you to discover errors, but also make it easier for you to modify code – you can run the tests after making a change to make sure that you haven’t broken anything.


This is vital in any large project, especially if there are many people working on the same code. Without tests, it can be very difficult for anyone to find out what other parts of the system a change could affect, and introducing any modification is a potential risk.

-->

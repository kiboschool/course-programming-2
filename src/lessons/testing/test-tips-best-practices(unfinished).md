
# Test Tips: Best Practices

(Ideally, show negative examples for as much as possible, to show the pitfalls of not following the advice).

### Test Coverage

cover different branches
tools to measure line coverage

### Detecting Exceptions

use with catch errors


### What makes a good unit test?

(These are ideally what a good unit test looks like. In the real world, we sometimes have to make tests that are more like component tests (they don't perfectly mock out all dependencies) and won't always be like this.)

* If you discover a bug in your program, and there isn't a test case that would have caught it, add test(s) that would have caught the problem.
   * This will help prevent similar problems from happening in the future.
* If a method has side effects, test those too

Thinking of tests like a scientific experiment. The first part is to arrange everything in place. The second part is to run the experiment. The last part is to read the results. That part uses an 'assert'.
    
    Just like in science, we want the steps to be repeatable. They shouldn't depend on the current time or what database is installed. A true unit test won't even depend on files on the disk.
    



One Assert Per Test Method

Avoid Test Interdependence-Each test should handle its own setup and tear down.

Keep setup very short

If setup has to be big, you'll have to refactor your program-that's ok

negative example: api example


If you write code that stuffs things into a database or that reads a file from disk, you have not written a unit test.  Unit tests don’t deal with their environment and with external systems to the codebase.  If it you’ve written something that can fail when run on a machine without the “proper setup,” you haven’t written a unit test.

Unit tests don’t generate random data and pepper your application with it in unpredictable sequences. 

And, finally, unit tests don’t exercise multiple components of your system and how they act.  If you have a console application and you pipe input to it from the command line and test for output, you’re executing an end-to-end system test — not a unit test.

In C#, you can think of a unit as a method.  You thus write a unit test by writing something that tests a method.  Oh, and it tests something specific about that method in isolation.  Don’t create something called TestAllTheThings and then proceed to call every method in a namespace.

One assert per test method

Avoid Test Interdependence

Use short tests.

It's OK to copy/paste some code when writing tests. Usually we want to refactor, but tests are the one place it is ok to repeat code.

If a test requires a bunch of setup, you'll need to refactor. But that's ok. In fact one of the main benefits of the requirements of unit tests is that it does influence you to split your code into separate units.


A unit of work is the sum of actions that take place between the invocation of a public method 


tests should run quickly-you'll need several per method, so there might be thousands
tempted to re-use the setup, but that's dangerous because you should test everything with a clean slate

Ben:tests should try to silence the logs if possible, so as not to clutter the test output
this is especially important when testing a failure case, otherwise you'll see the failure in the logs and think something went wrong

sometimes tests use an assertEquals that conveniently shows what was expected

tests must run in a simple context-no interaction between threads, no network calls,. should not depend on operating system-use integrations for that. so you can even run unit tests for something that isn't on your system. for example, you could have a program uses the windows api to create lnk shortcut files. if you mock out those api calls, you should be able to have your tests pass even on a mac.
this helps you write your program in a re-usable way. maybe in the future you will want to support other os, and you've now structured your program to make that possible.
note that as your program grows it gets harder and harder to change.

what about testing the db? that should be in an integration test. my own opinion is that it's ok to have accompianing non-unit tests that truly talk to the db

why unit tests focus on just one piece of the program? they can be slower to write because it needs more setup. if they ended up using a lot of the program, they would run slower, and if they fail it would be harder to track down where the problem is.

higher level tests are sometimes called integration tests or component tests.
when different pieces of a program are put together, this can be referred to as integration. so an integration test will check that the connections between.
an integration test has real dependencies, not mocked out.










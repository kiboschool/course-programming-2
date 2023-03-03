
# Test Tips: Mocks and Boundaries

(Ideally, show negative examples for as much as possible, to show the pitfalls of not following the advice).

Example for mocks: use an APICaller mock

Example for boundaries: when reading json from a file. when reading json from a file it makes more sense to test for None/test for invalid data types. for typical methods in your code, especially non-public methods, you usually don't need unit tests to check invalid data types/None.

Example for transitions: make the max length of a string 20, adding "..." if truncated. This has non-trivial transition cases.


### Reliability

You will be running your unit tests very often. It would be frustrating if a test failed for no good reason, even if this was a rare occurrence. You need the test to run exactly the same way each time.

Imagine you are writing a test that 

### Structuring your program

This is an other reason to write tests as you write your program, instead of waiting until the end.
 Also, it might take a lot of time to write the tests at that point because your code might be stuck.

In order for our code to be suitable for automated testing, you need to organise it in logical subunits which are easy to import and use independently from outside the program. You should already be doing this by using functions and classes, and avoiding reliance on global variables.

If a function relies only on its input parameters to produce the result, we can easily import this function into a separate testing module.


this is why we return strings instead of print. side effects are harder to test.

use an api call example

divide into an apicaller class

if you need to you can override
test input boundaries for malformed input
(within a program not as important to test for None,
but from outside a program should)

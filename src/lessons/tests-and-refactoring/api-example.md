
This is an other reason to write tests as you write your program, instead of waiting until the end.
 Also, it might take a lot of time to write the tests at that point because your code might be stuck.

In order for our code to be suitable for automated testing, you need to organise it in logical subunits which are easy to import and use independently from outside the program. You should already be doing this by using functions and classes, and avoiding reliance on global variables. If a function relies only on its input parameters to produce some kind of result, we can easily import this function into a separate testing module, and check that various examples of input produce the expected results. Each matching set of input and expected output is called a test case.
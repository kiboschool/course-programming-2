# Tests and Refactoring

One of the best things about being able to write software is that we can write programs to help us solve any problem that comes up. Let's say we've written a program that runs processor instructions, like we did in the midterm project. How do we know if the program is running correctly or not? We could give it an example input and look at the output results, and then we could go through and read the output and see if it matches what we expect. But instead of looking at the output ourselves, we can write a program to automate it and look at the output for us.

Writing a test means writing a program to call the program, give it input where we know the answer, and see if the outputs look right. 

This is the process behind your projects in GitHub showing up with a green checkmark, it's how the system knows your program is working.

This isn't perfect. Your program could still have bugs, and it's just that the test input didn't happen to hit them. This is one of the topics we'll discuss this week, how to write tests that don't leave gaps.

We will also talk about refactoring. This means to change the program in a way where it will  still compute the same output and still does the same thing. For example, changing the name of a variable from 's' to 'user_name' does not change what the program does, but is still a worthwhile change because it makes the code easier to read.

## Course Objectives

* Write tests to confirm a program works.
* Learn ways refactoring can make code easier to read.
* Use an `assert`, a way to intentionally cause the program to error, for example if there is bad data given.  
* Use named parameters as a way to refactor code. If a function takes a lot of parameters, this can be a good refactoring step. 
* Learn tips to reduce the chances of having a scenario where the tests all pass but the program still has bugs.


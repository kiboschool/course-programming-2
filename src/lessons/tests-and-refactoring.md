# Tests and Refactoring

Let's say you've written a program that runs processor instructions, like you did in the project earlier this year. How can you know if the program is running correctly or not? You could give it an example input and look at the output results, and then you could go through and read the output and see if it matches what you expect.

It's fine to do this early on in the process of writing the program, but it takes time. Later on, when you make changes to the program, it would be very slow to have to manually confirm each change did not break some other part of the program.

Writing a test means writing a program to call the program, give it input where we know the answer, and see if the outputs look right. 

This is the process behind your projects in GitHub showing up with a green checkmark. It's how the system knows your program is working.


This isn't perfect. Your program could still have bugs, and it's just that the test input didn't happen to hit them.

We will also talk about refactoring. This means to make changes to the code, while still having it compute the same output in essentially the same way. For example, changing the name of a variable from 's' to 'user_name' does not change what the program does. Changing code from using functions to using methods on a class is a common type of refactoring. Even though refactoring does not change the functionality of the program, it is often a worthwhile change as long as the resulting code is easier to read or easier to make future modifications to. 

## Course Objectives

* Write tests to confirm a program works.
* Learn tips to write effective test cases. The goal is to reduce the chances of having a scenario where the tests all pass, but the program still has bugs.

<!--
* Learn ways refactoring can make code easier to read.
* Use named parameters as a way to refactor code. If a function takes a lot of parameters, this can be a good refactoring step. 
-->



# Testing

In the introduction to this week's material, you read about a big benefit of creating automated tests: manually testing a program takes too much time.

Automated tests are a good addition to any program. They not only help you to discover errors, but also make it easier for you to modify code – you can run the tests after making a change to make sure that you haven’t broken anything. 


This is vital in any large project, especially if there are many people working on the same code. Without tests, it can be very difficult for anyone to find out what other parts of the system a change could affect, and introducing any modification is a potential risk.

Adding automated tests can seem like a waste of time in a small project. But they are important if the project becomes larger or if you have to return to it to make a small change after a long absence. They can also serve as a form of documentation – by reading through test cases you can get an idea of how the program is supposed to behave. 

>> Some people even advocate writing tests first, creating a plan for what the program is supposed to do, and filling in the actual program code afterwards.

You may find this approach a little extreme, but you shouldn’t go too far in the opposite direction – if you wait until you have written the entire program before writing any tests, you might discover that core parts of the program aren't working.

It is a good idea to write portions of our code and the tests for them at approximately the same time – then you can test our code while you are developing it. Most programmers write at least temporary tests during development to make sure that a new function is working correctly – programmers often use print statements as a quick, but impermanent form of debugging. It is better practice to write a permanent test instead – once you have set up the testing framework, it really doesn’t require a lot more effort.



Tests which are applied to individual pieces of code are known as unit tests – they check that one specific "unit" working correctly, instead of the entire program.


```python

def divide(a, b):
    return a / b
    

import unittest

class TestMultiply(unittest.TestCase):

    def test_divide(self):
        assert divide(1, 3) == 1 / 3


```

Testing the interaction between different components in a system is a separate type of test. This is known as integration testing.

When you are writing unit tests, you should have at least one test for every function in the code (including each method of each class).

It is also good practice to write a new test whenever you fix a bug – the test should specifically check for the bug which you have just fixed. If the bug was caused by something which is a common mistake, it’s possible that someone will make the same mistake again in the future – the test will help to prevent that.

<font size="-1">Adapted from: https://python-textbok.readthedocs.io/</font>


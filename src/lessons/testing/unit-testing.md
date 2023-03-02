# Unit Testing

In this page we'll focus on unit tests.



Adding low-level tests can seem like a waste of time in a small project. But they are important if the project becomes larger or if you have to return to it to make a small change after a long absence. They can also serve as a form of documentation – by reading through test cases you can get an idea of how the program is supposed to behave. 

> Some people even advocate writing tests first, creating a plan for what the program is supposed to do, and filling in the actual program code afterwards.

You may find this approach a little extreme, but you shouldn’t go too far in the opposite direction – if you wait until you have written the entire program before writing any tests, you might discover that core parts of the program aren't working.

It is a good idea to write portions of your code and the tests for them at approximately the same time – then you can test our code while you are developing it. Most programmers write at least temporary tests during development to make sure that a new function is working correctly – programmers often use print statements as a quick, but impermanent form of debugging. It is better practice to write a permanent test instead – once you have set up the testing framework, it really doesn’t require a lot more effort.


Unit tests check that one specific "unit" is working correctly, instead of the entire program.


```python

def multiply(a, b):
    return a * b
    

import unittest

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        assert multiply(2, 3) == 6


```


To follow best practices, when you are writing unit tests, you should have at least one test for every function in the code (including each method of each class).

It is also good practice to write a new test whenever you fix a bug – the test should specifically check for the bug which you have just fixed. If the bug was caused by something which is a common mistake, it’s possible that someone will make the same mistake again in the future – the test will help to prevent that.


Please watch this video to learn about Unit Testing in Python:

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/Oz0Z2tNuvDw?start=10&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

<font size="-1">Sources include: https://python-textbok.readthedocs.io/</font>


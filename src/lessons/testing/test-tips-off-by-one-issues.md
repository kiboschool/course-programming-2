
# Test Tips: Off-by-one Errors

### Introduction

Unit tests will never really be able to catch all bugs. It's not realistic to write millions or billions of tests that would check every single input.

If all of your tests pass, your program can still have bugs, and it's just that the test input didn't happen to hit them.

This is OK, though. Over time as you gain experience as a programmer, you will learn what bugs tend to come up in software. You will use this experience to write unit tests to detect these bugs. This means your tests will be more effective in knowing if there are problems or not.

Being talented at writing unit tests means writing tests that anticipate the type of bug that might appear in your program - and to write a test to make sure that doesn't happen! 

### Tests are still useful

It is worthwhile to write tests, because realistically, even just one test can still give you confidence that a lot of behavior is correct.

Say you are testing a function that finds the sum of a list of numbers that are passed in.

```python
def get_sum(the_list):
    total = 0
    for item in the_list:
        total += item
    return total

```

You write a test for a list of 5 items. It's very likely that if the program works for a list of length 5 items, it will also work for a list of 6 items. And so, you don't need to write tests covering everything from length of 1 to length of 6.

<!--(It is usually a good idea to write a test for a length of 0, though.)-->

### Off-by-one errors


Consider a function that computes the price for selling bagels. The bakery sets up a discount where bagels are cheaper if you buy one dozen (12 bagels) or more.

So, you write a function:

```python

normal_bagel_price = 2.00
cheaper_bagel_price = 1.90
discount_if_this_many_bagels = 12

def get_total_cost(number_of_bagels):
    if number_of_bagels >= discount_if_this_many_bagels:
        return number_of_bagels * cheaper_bagel_price
    else:
        return number_of_bagels * normal_bagel_price
    
```

Some functions have **transitions** where the behavior changes. In this case there is a transition at 12.

Transitions are a common place where bugs can occur. What if someone accidentally wrote

```
    if number_of_bagels > discount_if_this_many_bagels:
```

the program might not obviously look incorrect. But the functionality would be wrong because 12 bagels would still get the non-discount price.

This is called an "off by one" bug!

Whenever there is a transition, it is good to write tests around the special transition values:

```python
import unittest

class TestGetTotalCost(unittest.TestCase):
    def test_not_eligible_for_discount(self):
        assert get_total_cost(11) == 22
        
    def test_is_eligible_for_discount(self):
        assert get_total_cost(12) == 22.80
    
    def test_is_also_eligible_for_discount(self):
        assert get_total_cost(13) == 24.70

```

This will help catch bugs caused by off-by-one problems.

### Side note on assert comparisons

Try running the code

```
assert 1.1 + 1.1 + 1.1 == 3.3
```

Surprisingly, this fails with AssertionError, even though 

```
assert 1 + 1 + 1 == 3
```

works completely fine.

This is because unlike with integers, when calculating with floats you don't always get the perfectly exact number you expected. (Try running `print(1.1 + 1.1 + 1.1)` and depending on your computer, you might see something like `3.3000000000001`.)

The minor difference isn't a big deal because the discrepency is so small. Essentially the only time it causes a problem is when trying to compare with `==`.

The solution is to always write `self.assertAlmostEqual` when comparing floats. 

So, an improved version of the above test is
```python
import unittest

class TestGetTotalCost(unittest.TestCase):
    def test_not_eligible_for_discount(self):
        self.assertAlmostEqual(get_total_cost(11), 22)
        
    def test_is_eligible_for_discount(self):
        self.assertAlmostEqual(get_total_cost(12), 22.80)
    
    def test_is_also_eligible_for_discount(self):
        self.assertAlmostEqual(get_total_cost(13), 24.70)

```
because it is comparing floats, not integers.

This version of the test class is sure to work on all computers.

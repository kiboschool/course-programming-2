
# Test Tips: Off-by-one Errors

### Introduction

Unit tests will never really be able to catch all bugs. It's not realistic to test every single input.

This isn't perfect. Your program could still have bugs, and it's just that the test input didn't happen to hit them. But say you are testing a function that finds the sum of a list of numbers that are passed in. If you write a test for a list of 14, statistically speaking, if the program works for a list of 14 items it will work for a list of 15 items. And so you don't need to write tests covering everything from length=1 to length=15.

Over time as you gain experience as a programmer, you will learn what buggy behavior is most common. At the same time, you will learn to write unit tests to detect these bugs.

Being talented at writing unit tests means writing tests that anticipate the type of bug that might appear in your program - and make sure that doesn't happen! 

### Off-by-one Errors

first the throw if > 4 items

then the ... example

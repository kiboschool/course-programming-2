# Abstraction

Earlier in this course, you read a page about what it means to make a <a href="/lessons/inheritance-and-error-handling/models.html">model</a>. You saw how programs often have representations of something in the real world, like a car. In a software program it is common to create a model, a simplified representation of that concept, which contains only the parts of that concept that are relevant to the program.

For example, a model of a car in a simple video game, all the game needs to keep track of was the position and speed.

### Introduction to Abstraction

Abstraction is a related idea about simplification.

When we use the `math` module, we don't need to know how the computer calculates the square root of a number. We just need to know to use the `sqrt()` function.

```python
import math

x = 25
y = math.sqrt(x)
print(y)
```

There are several different algorithms and ways to compute a square root. Some are faster for certain types of computer processors. Some algorthms are slower, but return a more accurate answer. If ever time we wrote a program, we had choice which type of square root algorithm to use, it would slow us down. Mentally, we would have to think about 

The idea of abstraction is that in our program we just write "get the square root of a number". The choice of what algorithm internally to use, we leave up to somewhere else.



-----------------

Abstraction is similar to making a model


Abstraction is a fundamental concept in programming that is used to simplify complex systems by focusing on their essential characteristics or features while hiding their unnecessary details from the users.

## Learning Objectives

- Understand what abstraction is and how valuable it is.
- Start thinking about how to abstract your code.

## Abstraction in a Car

In the real world, a car is a complex system that has many different parts. But when you drive a car, you don't need to know how the engine works or how the brakes work. You just need to know how to use the steering wheel and the pedals to drive the car. This is abstraction.

### Available for Use

<img align="center" src="../../images/w9/car_tablue.jpeg">

### Abstracted

<img align="center" src="../../images/w9/car-abstracted.webp">
<img align="center" src="../../images/w9/car-engine.jpeg">

## Abstraction In Code

In programming, when we use the `print()` function, we don't need to know how the computer prints things to the screen. We just need to know how to use the `print()` function.

```python
name = "Alice"
age = 25
height = 1.75

print("My name is", name, "and I am", age, "years old.")
print("My height is {:.2f} meters.".format(height))

```

Another example is the `math` module. We don't need to know how the computer calculates the square root of a number. We just need to know how to use the `sqrt()` function.


save/load

# Abstraction

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

```python
import math

x = 25
y = math.sqrt(x)
print(y)
```

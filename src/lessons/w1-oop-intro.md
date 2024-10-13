# Object Oriented Programming

You have never seen my car, but if I gave you the keys and asked you to do me a favor and move my car, you can probably imagine what that process would look like. You'd enter the door, put the keys in the ignition, hit the gas and use the wheel to direct the car to its destination. 

You would probably be very surprised if my car had 7 wheels, or had a stirring wheel in the backseat, or had two wings - as cool of a feature as that would be.

In other terms, without knowing any details about my specific car, what you can imagine **is good enough for you to plan how to use it.** While all cars can be different, they all fit into some *abstract idea of what a car is, and what a car should be able to do*

What does this have to do with software? It turns out a whole lot! So far, we have been focusing on writing small solutions to small problems. As you move forward in your learning journey, you will see that developers around the world are tackling extremely complex challenges, and creating a lot of code to help each other out.

A lot of code is written only to be used by other developers - we've started benefiting from that last term by *importing* other modules, for example being able to create random numbers by using `import random` then calling `random.randint`

We can go beyond that by using a technique called Object-Oriented-Programming, or OOP for short. In OOP we define a **class** to capture abstract ideas about what we are trying to model. A `Car` class would define information about all cars: What can they do? what information should we know about them?

An **object** is a specific instance of a class, in other words, it's how we would represent my car in code, your car would require a different object, but they would both be able to do similar things since they are both instances of the `Car` class. We will spend plenty of time this week practicing this concept

## Preview

Here is what we will be exploring this week:

* How can we define a **class** in Python?
* How do we customize the data and behaviour of **objects?**
* What are some common pitfalls when writing OOP code?


## Why does this matter?

OOP as a style of programming is widespread in all modern languages, and helps us define *How other developers should use our code*. Getting familiar with OOP is crucial to be able to read, understand, and contribute to most of modern code that is written today.

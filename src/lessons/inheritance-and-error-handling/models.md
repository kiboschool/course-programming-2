# Models

Imagine that you are creating a video game, where you are driving a car and racing against other cars.

It's a simple game like Mario Kart, where you can press Left on your keyboard to steer left, and Right on your keyboard to steer right.

There are many ways to write the code for the game. It would really make sense to have a class for `Car`, though, because a `Car` has its own data and behavior. The data could include attributes like the color, graphics files, max speed, and so on. Depending on the way you chose to write the program, you could also include the current state in the class as attributes, like the current position and current speed. This would be a good way to design the class, because there could be an instance for your car and an instance for each of the other cars you are racing against.

<img src="../../images/w3/cars.png" width="75%" height="75%" />

When you write the program, should you compute all of the details for every piece of metal and molecule in the car? Should the program simulate how the gasoline ignites, how the engine works, and how each part of the car bends and compresses as it moves?

No, this would be too much effort. And even if you did go to all of the effort to write the code for all of this, it wouldn't really make the game more fun. Adding the details wouldn't make it a better class. Writing programs takes a lot of time. The more code there is, the harder the program is to read and the probability of having bugs increases. The best programs only include the code that is necessary.

**This means that writing good classes involves an extreme amount of simplification.**

We call the class `Car`. But in the real world there are thousands of attributes, and thousands of behaviors, that we won't include in the program. The car class doesn't have a `number_of_wheels` attribute, or a `seatbelt_clicked_in` attribute, or a `doors_locked` attribute.

It is still OK to call the class Car, though.

When you take a concept, and only choose a few parts of it to include in your class, this is called making a **model**. Making a car class that only has the position and speed would be a good example of modelling a car. The car class is simple, but that is completely fine for our game, because that is all that is needed in the game. The model is a simplified (and often extremely simplified) version of a concept.


It's like in the weather program from last week. The current weather has much more complexity than the temperature and wind speed. But it is fine for the WeatherData class to be a simple model, because that is all the program needed to have for the goals it was trying to achieve.

When you read about Python on other websites, you might come across other people's example classes. For example, people might show a `class Animal` or a `class Dog`. These are just highly-simplified models. A simplified model like this could still be useful in a program. Maybe this is part of a program that only needs to have a few attributes and behaviors for each animal.

A model sometimes includes attributes that are different than anything you would see in the real world. For example, a car class might have an `id` attribute. This is an attribute that is useful to have for the program, but doesn't really correspond with anything in the real world.

> **Try out your understanding:** you are making a program that is a student course enrollment manager. You have a `Student` class. Can you think of a few attributes of students that are attributes of people in the real world, but don't need to be included in the class? What attributes should be included in the model?


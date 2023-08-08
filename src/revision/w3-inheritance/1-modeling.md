# Models

Imagine that you are creating a video game, where you are driving a car and racing against other cars.

It's a simple game like Mario Kart, where you can press Left on your keyboard to steer left, and Right on your keyboard to steer right.

There are many ways to write the code for the game. It would really make sense to have a class for `Car`, though, because a `Car` has its own data and behavior. The data could include attributes like the color, graphics files, max speed, and so on. Depending on the way you chose to write the program, you could also include the current state in the class as attributes, like the current position and current speed. This would be a good way to design the class, because there could be an instance for your car and an instance for each of the other cars you are racing against.

<img src="../../images/w3/cars.png" width="75%" height="75%" />

When you write the program, should you compute all of the details for every piece of metal and molecule in the car? Should the program simulate how the gasoline ignites, how the engine works, and how each part of the car bends and compresses as it moves?

No, this would be too much effort. And even if you did go to all of the effort to write the code for all of this, it wouldn't really make the game more fun. Adding the details wouldn't make it a better class. Writing programs takes a lot of time. The more code there is, the harder the program is to read and the probability of having bugs increases. The best programs only include the code that is necessary.

**This means that writing good classes involves an extreme amount of simplification.**

We call the class `Car`. But in the real world there are thousands of attributes, and thousands of behaviors, that we won't include in the program. The car class doesn't have a `number_of_wheels` attribute, or a `seatbelt_clicked_in` attribute, or a `doors_locked` attribute.

Let's think about what a car model would entail. What matters depends a lot on your goal:
- If you are building a game, then some information about how a specific car differs from another one in the game would be important.
- If you are building a platform to sell cars, then information about price, age, etc. becomes very important.
- If you are building a ride-sharing platform like Uber, then information about drivers and passengers may be very important. 

In all cases, It is still OK to call the class Car, though.

When you take a concept, and only choose a few parts of it to include in your class, this is called making a **model**. Making a car class that only has the position and speed would be a good example of modelling a car. The car class is simple, but that is completely fine for our game, because that is all that is needed in the game. The model is a simplified (and often extremely simplified) version of a concept.

When you read about Python on other websites, you might come across other people's example classes. For example, people might show a `class Animal` or a `class Dog`. These are just highly-simplified models. A simplified model like this could still be useful in a program. Maybe this is part of a program that only needs to have a few attributes and behaviors for each animal.

A model sometimes includes attributes that are different than anything you would see in the real world. For example, a car class might have an `id` attribute. This is an attribute that is useful to have for the program, but doesn't really correspond with anything in the real world.

> **Try out your understanding:** you are making a program that is a student course enrollment manager. You have a `Student` class. Can you think of a few attributes of students that are attributes of people in the real world, but don't need to be included in the class? What attributes should be included in the model?

## Commonalities between models:

Let's work on a `Car` class from the perspective of a ride sharing application. Our car will have a few attributes:
- A license number, which uniquely identifies the car.
- An attribute called `available`, which is a boolean that tells us whether or not someone could hail the car. For now we will base this on whether or not we have space in the car.
- A list of passengers, which tells us how many people are currently in the car. We'll only want to have 3 passengers at most.

<iframe src="https://trinket.io/embed/python3/b7720e8922" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Let's think about this though, imagine that our rideshare application takes off, and we suddenly realize that we have some additional use cases:
- Some people really want BIG cars, where they could put up to 6 people instead of our limit of 3.
- Some people are fine just getting on the back of a motor bike. They can only take 1 passenger.

We could create a `MotorBike` class that is similar to our `Car` class, and another `BigCar` class as well. 

What would happen if we wanted to change our print statements for all our vehicles to say "We have now picked up the lovely Fatima" instead of just saying "Picking up Fatima"? We would have to go change that in three different methods, in three different classes, possibly in three different files. I don't know about you, but I feel too lazy to do all of that!

Luckily there is a hint here about what we _really_ want to model. We care about `Vehicles`, so let's create a `Vehicle` class. We haven't given up on our `Car` and `BigCar` and `MotorBike` classes, but the next section will showcase a new trick for this kind of modeling
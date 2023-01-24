# Overriding Methods

> <a href="https://replit.com/team/kibo-programming-2/MadLibs-Override-Demo" target="_blank">**Click here to follow along on Replit!**</a> Please sign up for an account and request to join the team if you haven't already.

> Once you are in Replit, click `Shell` on the right, type in `python v1.py`, and press Enter to run one of the scripts.

> <img src="../../images/w3/replit3.png" width="80%" height="80%" />


## Madlibs

First, let's look at a Madlibs game.

Like the project from Programming 1, this is a game where people get asked to enter a *noun* or *verb*, and then they type in any word that come to mind. In the end, the program prints out a silly story. Try running this code in replit, and understand how it works.

We'll walk through see 6 versions of the program, from v1 to v6.

In the replit shell on the right, run `python v1.py`.

> ### Practice
> * Create another `template` array to create another Madlibs template.
> * (The only supported word types are NOUN, VERB, and NUMBER).
> * There is a fun phrase: "the quick brown fox jumps over the lazy dog". You could make a short template with this, for example replacing "jumps" with "VERB".

### Making the game object-oriented

In the past, we've mostly worked with smaller classes that represented simple things.

Classes can represent larger concepts, too, though.

We can put the code that runs the Madlibs game into a class. Just like other objects, there is **behavior** (asking the user for words, showing the result) and  **internal data** (the results and the game template, which in this case are just held in variables). 

One benefit is that we can have two separate games going independently, just by making two objects that are instances of the `MadLibsEngine` class.

You can run `python v2_class.py` to run this version of the game.

### Adding a feature

What if your friends have a hard time thinking of words to choose, and the game takes too long to get to the end?

We can add a feature to the game: 

🤖 An automatic mode that picks words at random from a list - playing the game automatically.

The `random` module will be perfect for us - it has a useful function called `random.choice` that returns a random element from a list. Also, we can use `random.randint(1, 100)` to get a random number between 1 and 100.

We'll make a new class `MadLibsEngineRandom` that still has a method called `get_noun`, but this time gets the word from a list. We'll keep both classes around because we still want to be able to play the traditional game sometimes too.

Please run `python v3_two_classes.py` to run this version of the game.

### Overriding

The two classes have a lot in common. The `play` method is the same for both of them. Repeated code isn't good in general, it takes up space and clutters up the program.

You may have anticipated what to do - we have two classes that act similarly - the solution is to use inheritance!

See the code in `v4_override.py.`

We can make a parent class called `MadLibsEngineParent`. It can have the play method there and the child classes will inherit it.

There are two child classes. One of them is the MadLibsEngineInteractive class that plays the traditional game, and one of them is the MadLibsEngineRandom class that chooses words randomly.

All three of the classes have methods with the same name (get_noun, get_verb, and get_number), but they do different actions. <!-- A computer scientist would use a technical term and say that the methods have different **implementations**.-->

* We know that inheriting from a class will let a child class use methods from the parent class.

* So what happens when a child class defines a method with the same name as a method on the parent class?

* We say that the child class's method **overrides** the parent class method. The parent class method doesn't get called.

You can think of the method call as looking where to go, starting from the child class. If it doesn't find anything there, it will go up to the parent class and try looking there. Only if it has reached the top and not found any method with that name, then will Python raise an error.

> ### Practice
> * Add testing `print` calls to all methods in `MadLibsEngineParent`.
> * Then run the game, by calling play on an instance of the child class.
> * By looking for the print call you added, notice which method(s) on the parent do get called, and which method(s) do not get called because they have been overridden by a child class.

### Adding bigger words

We have another feature. We'd like to use a different word list if the user wants, a word list with longer words to use for nouns. We need to make a `MadLibsEngineRandomWithBigNouns` class.

Inheritance works great for this, because we only need a few lines of code. 

The resulting program is in `v5_override_broken.py`. But the program doesn't work, and it isn't really clear why. It's true that only one of the methods was overridden - but that isn't the problem, when get_verb and get_number are called they'll just use the versions in `MadLibsEngineRandom`.

Everything looks right, why doesn't the program work?

### Calling into the parent class

It turns out that the `__init__` method can be overridden.

The `__init__` on MadLibsEngineRandomWithBigNouns is overriding the `__init__` on MadLibsEngineRandom, so that one is never getting called!

In this case we want both the child and the parent version of the method to be called - not like the default behavior with overriding where only the child version is called.

The solution is in `v6_override_fixed.py.`

There's a special line of code, `super().__init__()`, that ends up calling `__init__` on the parent class. This way both are run, like we want.

> The term *super class* means essentially the same thing as *parent class*.

The program works! We now have a good demonstration of inheritance and method overriding.

<p>&nbsp;</p>

## Video

Please continue the video here, from 5 minutes onward, for more information about overriding.

<div style="position: relative; padding-bottom: 56.25%; height: 0; margin-top:1.6em"><iframe src="https://www.youtube.com/embed/C8qE3mKiBrQ?start=325&end=888;rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Be careful overriding 

Notice that when we override methods, we need to be careful. We want the overridden method in the child class to do conceptually the same action. It should receive the same parameters and act like the the method from the parent class. If the child class needs a method that has a different meaning, it'd be better to not override and to create a different method.

You have a class that retrieves weather forecast data from an API on the internet. You write a `get_temperature()` method that returns the current temperature in degrees celsius. We then find another API for weather forecast data that has different features - in addition to the wind speed and wind direction you were already getting, it will give you more precipitation information, and so you'd like to add it to your program too.

This is a good case for inheritance. The other API could be in an inherited class, because it has similar behavior. The `get_wind_speed()` and `get_wind_direction()` methods could be overridden and take data from the new source. Imagine, though, that this new API doesn't provide the current temperature, it gives the estimated daily high temperature and daily low temperature. Shouldn't you override `get_temperature()` and put the data there, since it's still returning a temperature?

💡No, this would not be a good idea. Bugs will appear in your program if two classes both have a method with the same name, but they aren't actually referring to the same concept.

You could instead add a new method with a name such as `get_daily_high_temperature()`, to show that it isn't the same type of temperature being returned.


## Inherited classes are linked

You can visualize a child class as being linked to a parent class.

A class can inherit from a class that itself inherits from a different class - there can be a link to a link to a link. This is an *inheritance tree*.

<img src="../../images/w3/tree.gif" width="50%" height="50%" />


When you call a method on an object, if the method is there, it will be run. But if it isn't there, Python will follow the link upwards to look for methods that got inherited from the parent class. It's following links, hopping from one class to another. (It is only at the end, if the method isn't there, when Python raises an error.)

A structure with links like this is sometimes called a *tree* or a *hierarchy*.

Seeing at the structure, and visualizing Python looking upwards, explains why overriding a method blocks the parent version of the method from being called. The child version is there and there's no need to look further.



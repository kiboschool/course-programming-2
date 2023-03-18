
# Introduction To Abstraction

### Remembering models

Earlier in this course, you read a page about what it means to make a <a href="/lessons/inheritance-and-error-handling/models.html">model</a>. You saw how programs often have representations of something in the real world, like a car. In a software program it is common to create a model, a simplified representation of that concept, which contains only the parts of that concept that are relevant to the program.

For example, for a model of a car in a simple video game, all the game needs to keep track of is the position and speed.

Abstraction is a related idea. It is also a way to simplify code to make it easier to work with.

### <img src="../../images/midterm/calc.png" width="8%" height="8%" style="border:none, border-width: 0, border: 0; box-shadow: 0px 0px;" /> Calculating a square root

When we use the `math` module, we don't need to know how the computer calculates the square root of a number. We just need to know to use the `sqrt()` function.

```python
import math

x = 25
y = math.sqrt(x)
print(y)
```

There are several different algorithms and ways to compute the square root of a number. Some are faster for certain types of computer processors. Some algorithms are slower, but return a more accurate answer. When we write code in Python, though, it doesn't really matter what method is used to compute the square root, because the differences are so small that they do not meaningfully affect what the program does.

We could imagine a world where to compute a square root we would have to choose between different algorithms, like `math.sqrt_linear_estimate_algorithm`, `math.sqrt_heron_algorithm`, and `math.sqrt_babylonian_algorithm`.

But this would be confusing to read! It would be distracting to think about the choice of algorithm when the differences have no real impact on what the program does.

The idea of abstraction is to **hide the unimportant details**.

What matters most for a high level language like Python is to have code that is easy to read and understand. And so Python gives us just one choice, `math.sqrt`. Behind the scenes, Python will use one of the algorithms. Because we don't need to know about that detail when we write our program, we can say that detail is hidden.

### 🚗 Driving a car

Here is a depiction of abstraction in our life:

Different car engines work in different ways. An electric engine is significantly different than a combustion engine, and an all-wheel-drive car is internally different than a two-wheel-drive car.

But when you drive, the car designers have **hidden the unimportant details**.  You only need to focus on *what* to do, not the type of engine or how the engine works. And there is a very similar interface -- no matter what type of engine the car has, you just need to know how to use the steering wheel and the pedals.

If there weren't abstraction, we'd have to think about this when we drove:

<img align="center" src="../../images/w9/car-abstracted.webp" width="70%" height="70%">
<img align="center" src="../../images/w9/car-engine.jpeg" width="70%" height="70%">

But because of abstraction, we only need to think about this:

<img align="center" src="../../images/w9/car_tablue.jpeg" width="70%" height="70%">



<!-- 
Could potentially add in the future if we explain enough,
Image of a black box - hide the complexity within the box
Video "Abstraction Can Make Your Code Worse"
https://www.youtube.com/watch?v=rQlMtztiAoA -->

### 🏙️️ Another benefit of abstraction


Imagine a program where you enter the name of a city, and it displays information about that city. For example, if the user enters Accra, the program would output `Country: Ghana, Population 284,000, Coordinates: 5°33′N 0°12′W`. The goal is for the same program to run in different modes:

* as a command-line text program
* as a visual program with menus and buttons, running in Windows (this type of program is known as GUI)
* running within a web browser as part of a website

If the program wrote its output by having a lot of `print` statements everywhere, this would be limiting. It would work in VSCode and as a command-line text program that runs in a console. But visual programs in Windows have a different way to display text - not print, but a function called SendMessage. And programs running on a web browser also have a completely different way to have text show on the website. `print` will not work in those cases.

Instead of the program calling `print` in a lot of places, the solution is to have the program instead call a helper function `display_text`. We can think of `display_text` as a *generalized* or *abstract* action that represents the idea of displaying text. Changing the code from calling print to calling display_text is *abstraction*.

We are focusing on what the program does, and not the specifics of how it is achieved. The benefit is that the same program can now be easily run in different modes, without needing to make any changes. (Over in the `display_text` function, the program can determine what mode it is running in, and call the appropriate function to actually show the text).

So, another benefit of abstraction, besides simplication, is that your program can be more adaptible. Abstraction will help you write a program that runs in different situations without needing modification.

### 🏷️	 Other examples

The examples so far have shown abstraction for programs that use classes and methods.

A program that just uses functions can also be thought of as having abstraction, like in this example:

```python
import lower_layer_helpers

def calculate_total_price(item, quantity):
    price = lower_layer_helpers.get_price(item)
    total_price = price * quantity
    return total_price
```

We are calling a function called `get_price`.

In the background, the `get_price` function might be using a database to get the price of the item, or it might be using a dictionary to get the price of the item.

The details of the `get_price` function are hidden from us, and we don't need to know how it works. This is abstraction.





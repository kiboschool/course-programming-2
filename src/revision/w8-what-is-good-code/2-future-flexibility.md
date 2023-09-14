# Abstraction & Flexibility


## Examples of Abstraction in practice

### 🚗 Driving a car

Here is a depiction of abstraction in our life:

Different car engines work in different ways. An electric engine is significantly different than a combustion engine, and an all-wheel-drive car is internally different than a two-wheel-drive car.

But when you drive, the car designers have **hidden the unimportant details**.  You only need to focus on *what* to do, not the type of engine or how the engine works. And there is a very similar interface -- no matter what type of engine the car has, you just need to know how to use the steering wheel and the pedals.

If there weren't abstraction, we'd have to think about this when we drove:

<img align="center" src="../../images/w9/car-abstracted.webp" width="70%" height="70%">
<img align="center" src="../../images/w9/car-engine.jpeg" width="70%" height="70%">

But because of abstraction, we only need to think about this:

<img align="center" src="../../images/w9/car_tablue.jpeg" width="70%" height="70%">

### Square roots:

When we use the `math` module, we don't need to know how the computer calculates the square root of a number. We just need to know to use the `sqrt()` function.

```python
import math

x = 25
y = math.sqrt(x)
print(y)
```

There are several different algorithms and ways to compute the square root of a number. Some are faster for certain types of computer processors. Some algorithms are slower, but return a more accurate answer. In the vast majority of cases though, those differences are irrelevant. It doesn't really matter what method is used to compute the square root, because the differences are so small that they do not meaningfully affect what the program does.

We could imagine a world where to compute a square root we would have to choose between different algorithms, like `math.sqrt_linear_estimate_algorithm`, `math.sqrt_heron_algorithm`, and `math.sqrt_babylonian_algorithm`.

But this would be confusing to read! It would be distracting to think about the choice of algorithm when the differences have no real impact on what the program does.

When we write code with abstraction in mind, we **hide the unimportant details**.

What matters most for a high level language like Python is to have code that is easy to read and understand. And so, Python gives us just one choice, `math.sqrt`. Behind the scenes, Python will use one of the square root algorithms. Because we don't need to know about that detail when we write our program, we can say that detail is hidden.

In this case, the author of Python's `math` library thought about abstraction and realized that people computing the square root of a number don't need to know the details. So they hid the details, like the choice of which algorithm to use, by only providing one simple `sqrt` function.

### 🏷️   Example: getting the price

This is a way to use abstraction in your code: find a piece of complicated code, create a new Python module, and move the complicated code there.

For example, you are working on a store program where items being sold have prices. The way to get the price of an item was complicated and had dozens of lines of code. The solution is to create a file called `get_price_helpers.py` and move all of that complicated code into a `get_price` function in that file.

The existing code that needed to get the price of an item is now simple and easy to read. For example, there is a function that calculates the total price when there are many of one type of item. `calculate_total_price` is now very simple because it does need to see any of the complexity of the `get_price` function.

```python
import get_price_helpers

def calculate_total_price(item, quantity):
    price = get_price_helpers.get_price(item)
    total_price = price * quantity
    return total_price
```

In this case, the detail being hidden is the detail of how the price is being retrieved from the item. `get_price` might be using a database to get the price of the item, or it might be using a dictionary, or even reading from the internet. From the point of view of the calculate_total_price function, it doesn't matter.

The details of the `get_price` function are hidden from us, and we don't need to know how it works. This is abstraction.

## 💾 Saving data

Now with all these new concepts in mind, let's try to improve some code ourselves!
When a program has good abstraction, it is more flexible.

This means that when, in the future bug fixes or new features are needed, the code is easier to change.

Imagine that you are creating a game, and you need a feature where the player can save their progress.

There are several places in the code that need to save the game - when the player clicks save, after completing a level, every 5 minutes just in case, and so on.

You know you want saving to be a separate method, since you definitely don't want to have duplicated code in all of those places.

Imagine that calling the method looks like this: 

```python
class Game:
    ...
    def on_complete_level(self):
        ...
        self.save_to_json(self.data, 'saved_game.json')
        ...
    def on_every_five_minutes(self):
        ...
        self.save_to_json(self.data, 'saved_game.json')
        ...
    def on_user_click_save(self):
        ...
        self.save_to_json(self.data, 'saved_game.json')
        ...
    ...
```

This strategy will work in the short term.

But in the future, it will probably need to change. You might need a feature to store more than one game file. Or you need to store the game in a database. Or you need a feature to save to an online server. Each time a change like this is made, you would need to update each of the several calls - which takes time.

The problem is that **the details are not hidden**. To improve the code, the high level code should not have details about how the save is occurring!

Let's creat a new class with a single job, a  **single responsibility**: Saving a game.

```python
class GameSaver:
    def __init__(self, filename):
        self.filename = filename
    
    def save(self, data):
        # saves to self.filename
        ...

# Every game that wants to save some data should use an object of the GameSaver class
class Game:
    ...
    def __init__(self):
        self.game_saver = GameSaver('saved_game.json')
        
    def on_complete_level(self):
        ...
        self.game_saver.save(self.data)
        ...
    def on_every_five_minutes(self):
        ...
        self.game_saver.save(self.data)
        ...
    def on_user_click_save(self):
        ...
        self.game_saver.save(self.data)
        ...
    ...
```

The save method is now well abstracted, because the details are hidden. 

And the program is more **flexible** because it is easier to adapt to future changes. If any changes need to be made, they only need to be made once in the creation of the `game_saver` object instead of several times. (In this small example, it's not a big deal. But in a large professional software project, having to search for each place that calls a method and making the correct updates can end up being days of work, especially once testing and code review are taken into account).

Also, the program is **clearer**, because we just see the action `save` and we are not distracted by seeing the filename and format.

> 💡 For a program that uses abstraction well, the higher layers only describe *what* the program does. It is the lower layers that have the details on *how* the program works.

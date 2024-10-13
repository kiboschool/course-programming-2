# Sharing an Interface

We will continue with the  `GameSaver` class: We are asked to make the program
run in two modes - in one mode the game is saved to a file on disk, and in
another mode the game needs to save the data online to a server. The goal is to
keep the program's flexibility, where if anything about saving needs to change,
the changes only need to be in **one place** and not all of the locations that
call the save method.

One approach would be to modify the `GameSaver` class:

```python
class GameSaver:
    def __init__(self, filename, is_online_mode):
        self.filename = filename
        self.is_online_mode = is_online_mode
    
    def save(self, data):
        if self.is_online_mode:
            # saves to the server
        else:
            # saves to self.filename
        ...
        
    def load(self):
        if self.is_online_mode:
            # loads from the server
        else:
            # loads from self.filename
        ...
        
class Game:
    def __init__(self):
        self.game_saver = GameSaver()
        ...
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
```

This would work, and it keeps our `Game` class clean and tidy.

Think about all the future work we might have to do on the `GameSaver` class:
Every method would start with an `if` `else` statement, depending on the mode.
If we introduce a third way to save, then we have to **update every single
method to add a new scenario**. That sounds annoying before we even got to it!

So while the code is clear, and fairly well abstracted, there are some
complications if we think about how we would keep improving it.

Object-oriented-programming provides a perfect solution to this:

## Thinking about interfaces

A solution is to have two classes with the same **interface**. They have the
same `save` and `load` methods.

This will mean making some small changes to the `Game` class, but that's ok. The
`Game` should tell us what mode it's operating under, and we will set up one of
the two classes to save the game correctly.

From the calling code's perspective, it just needs to say `save`, and the
calling code does not need to know which class is actually being used!

```python
class GameSaverToFile:
    def __init__(self, filename):
        self.filename = filename
    
    def save(self, data):
        # saves to self.filename
        ...
        
    def load(self):
        # loads from self.filename
        ...
        
class GameSaverOnline:
    def __init__(self):
        ...
    
    def save(self, data):
        # saves to the server
        ...
        
    def load(self):
        # loads from the server
        ...

class Game:
    def __init__(self):
        # This is the slight change we need to make: The game should know what mode it's running with
        # But let's just make one decision with that information
        if is_online_mode:
            self.game_saver = GameSaverOnline()
        else:
            self.game_saver = GameSaverToFile('saved_game.json')
    
    # All the methods just ask the game_saver object to save()
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

When we speak of **interfaces** in this context, we mean "the things you
interact with". It's nice when interfaces are consistent: Pretty much every
phone you've held in the last 5 years has 2 buttons, next to each other, to
indicate the volume going up or down. It would be pretty confusing if a phone
manufacturer changed that.

The **interface** of a class is the set of method names that are intended to be
called from **outside** the class. When different classes share the same
**interface**, that means they _should be interchangeable_.  

In this example, we say that the classes have the same interface because they
both have methods (save and load) with the same names and which take the same
parameters.

When the game is started, it determines which class to make an instance of. From
then on, everything in Game just works - it just calls `save()` and it doesn't
need to worry about which class is actually there!

## Making our interface more sturdy

If someone makes changes to the methods in `GameSaverToFile`, it might not be
clear to them that they need to also update `GameSaverOnline`.

Our previous changes work because the two classes both implement the exact same
**method signatures**. How can we make sure a fellow developer wouldn't change
the `save` method of one of the classes to take on new parameters and break this
nice setup we have?

This concept is very important to structuring OOP code - so important in fact
that many languages give you built in ways to **prevent classes from breaking
their interface**.

Python is not as strict, but we can achieve the same goal all the same -
Remember: This is not about syntax, this is about concepts that will serve you
throughout your studies and career.

Wouldn't it be nice that if another developer broke our interface by modifying
the classes we just made, the program itself would tell them? Well we can achieve
that!  First, we will create a class to `define` what our interface should be:

```python
class GameSaver:
    def save(self, data):
        raise Exception("Children of GameSaver MUST implement this method")
        
    def load(self):
        raise Exception("Children of GameSaver MUST implement this method")
```

The point of this class is not to ever be instanced. We will never create a
`GameSaver` object directly. Instead, this is here almost as a safeguard: If for
some reason we call the `save` or `load` method of this class, we will raise an
error! This is our alarm bell!

```python
# NOTE: This now inherits from GameSaver
class GameSaverToFile(GameSaver):
    def __init__(self, filename):
        self.filename = filename
    
    def save(self, data):
        # saves to self.filename
        ...
        
    def load(self):
        # loads from self.filename
        ...

# NOTE: This now inherits from GameSaver    
class GameSaverOnline(GameSaver):
    def __init__(self):
        ...
    
    def save(self, data):
        # saves to the server
        ...
        
    def load(self):
        # loads from the server

```

Remember what we learned in inheritance. If `GameSaverOnline` implements the
`save(self, data)` method, that is the code that will run. If we modify that
method to make it have a different signature, say `save(self, data, server)`,
but the rest of our code still has calls to `save` with only one parameter, it
will call the method from the parent class - `GameSaver` and will raise an
error!

This helps us maintain that GameSaverToFile and GameSaverOnline, and any other
class that inherits from GameSaver, need to have the same save() and load()
methods.

The child classes GameSaverToFile and  GameSaverOnline we refer to as an
**implementation**. Each child class is an implementation class that has methods
that override the interface methods.

This new version of the program doesn't really change the functionality. But it
does convey to anyone working on the program that `GameSaverToFile` and
`GameSaverOnline` need to share the same interface. And, if the child class has
forgotten to add a method, or modifies its signature over time, the exception in
`GameSaver` will remind us to fix it.

This was a lot to digest, let's look at some other tactics to improve code
quality.

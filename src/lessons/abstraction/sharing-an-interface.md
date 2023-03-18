

# Sharing an Interface

Let's say we are working on the `GameSaver` class in the previous example.

It ends up being the case that we are asked to make the program run in two modes - in one mode the game is saved to a file on disk, and in another mode the game needs to save the data online to a server. The goal is to keep the program's flexibility, where if anything about saving needs to change, the changes only need to be in one place and not all of the locations that call the save method.

One approach would be to write the code like this:

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

This would work, but the class would feel more complex than it needs to be. All of the methods would need to check the mode. This would be slightly fragile too, because if one of the methods forgot to check the mode, there could be a bug.

Object-oriented-programming provides a perfect solution to this:

### Using the same interface

The solution is to have two classes with the same **interface**. They have the same `save` and `load` methods. From the calling code's perspective, it just needs to say `save`, and the calling code does not need to know which class is actually being used!

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
        ...
        if is_online_mode:
            self.game_saver = GameSaverOnline()
        else:
            self.game_saver = GameSaverToFile('saved_game.json')
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
    ...
```

The **interface** of a class is the set of method names that are intended to be called from outside the class. 

In this example, we say that the classes have the same interface because they both have methods (save and load) with the same names and which take the same parameters.

When the game is started, it determines which class to make an instance of. From then on, everything in Game just works - it just calls `save()` and it doesn't need to worry about which class is actually there!

### Depicting the interface

If someone makes changes to the methods in `GameSaverToFile`, it might not be clear to them that they need to also update `GameSaverOnline`. For example, someone needs to change the `save` method so that it receives two data parameters in. They would update the save method on the GameSaverToFile class. If they forgot to update the save method on the GameSaverOnline class, the classes would no longer have the same interface, and the program would stop working. (The problem would be that if the object was a GameSaverOnline instance, the program would get a not-enough-parameters error as soon as the save method was hit).

We can indicate that the classes need to have the same interface by writing code like this:

```python

class GameSaver:
    def save(self, data):
        raise NotImplementedError
        
    def load(self):
        raise NotImplementedError

class GameSaverToFile(GameSaver):
    def __init__(self, filename):
        self.filename = filename
    
    def save(self, data):
        # saves to self.filename
        ...
        
    def load(self):
        # loads from self.filename
        ...
        
class GameSaverOnline(GameSaver):
    def __init__(self):
        ...
    
    def save(self, data):
        # saves to the server
        ...
        
    def load(self):
        # loads from the server

```

A programmer looking at the code will see this and know that it means that GameSaverToFile and GameSaverOnline need to have the same save() and load() methods.

In this example, the parent class GameSaver depicts the **interface**. The child classes GameSaverToFile and  GameSaverOnline we refer to as an **implementation**. Each child class is an implementation class that has methods that override the interface methods.

This new version of the program doesn't really change the functionality. But it does convey to anyone working on the program that GameSaverToFile and GameSaverOnline need to share the same interface. And, if the child class has forgotten to add a method,  the NotImplementedError will fire to remind us to fix this.
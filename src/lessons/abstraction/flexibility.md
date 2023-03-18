
# Flexibility

When a program has good abstraction, it is more flexible.

This means that when, in the future bug fixes or new features are needed, the code is easier to change.

### Layers

A program typically has different layers. Code in the higher layers imports and uses classes that are written in lower layers. The highest layers are generally the user-interface code, and the lowest layers are the simple helper functions that do not need to call into any other modules.

This is like how in this course's final project, the higher-layer `EventCreatorAndRetriever` relies on the lower-layer `EventBriteAPIHelper` and `EventDBHelper` classes.

A way to think about abstraction is that it involves splitting code into higher and lower layers, and moving details from the higher layer into the lower layer. The example below will demonstrate what this looks like.

### 💾 Saving data



Imagine you are creating a game, and you need a feature where the player can save their progress.

There are several places in the code that need to save the game - when the player clicks save, after completing a level, every 5 minutes just in case, and so on.

You know you want saving to be a separate method, since you definitely don't want to have duplicated code in all of those places. (You write a method that builds a dictionary, calls json.dumps to convert to a json string, and puts the json string into a text file. You then write a load method that can read that file to restore the game progress).

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

A good solution would be to instead have code that looks like this:

```python
class GameSaver:
    def __init__(self, filename):
        self.filename = filename
    
    def save(self, data):
        # saves to self.filename
        ...

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


Also, the program is simpler to read, because we just see the action `save` and we are not distracted by seeing the filename and format.


> 💡 For a program that uses abstraction well, the higher layers only describe *what* the program does. It is the lower layers that have the details on *how* the program works.


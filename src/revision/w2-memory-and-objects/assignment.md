# Exercises

---

> 💡 This is your chance to put what you’ve learned into action.
>

# Object-Oriented Jukebox

## Intro

A Jukebox is an old music player (see https://en.wikipedia.org/wiki/Jukebox).
In the time before mp3 players or smartphones, bars and restaurants would have a
music player that allowed minimal song selection.

In this project, we will do something different: We will provide you code! it's 
however up to you to figure out if it works well. You will have to read methods,
understand what they _should_ do, as well as what they _actually_ do, and fix 
any errors you find in your way. You will have to write a little bit of code, 
but this assignment mostly tests your ability to read code and debug it.

### Provided code:
`jukebox.py` is where our JukeBox class is defined. This is where you are expected 
to do your work. 

`test_jukebox.py` is a test file. Your aim will be to make sure all the tests pass. Unfortunately, very few of them do at the moment. To help you focus, most of the tests are *commented out*. Each step in the assignment will ask you to bring back some of the tests.

`main.py` is a demo of the JukeBox class. It should run perfectly by the end of the assignment, and you can find what the output of this file should look like further down these instructions. Feel free to add some of your own code here to test the class, but changes to this file will not influence your grade.

#### Testing

Run the unit tests with `python -m unittest` or `pytest`.

You can inspect or run `main.py` to see an interactive use of the Jukebox class.

A working sample run of `main.py` has this output:

```
❯ python main.py
Paused
Playing: Kuna Kuna
Playing: Inauma
Paused
Playing: Vaida
Playing: Sasa Hivi
Playing: McMca
Playing: Dai Dai
Playing: Woman
Playing: Mbona
Playing: Toto
Playing: Kanairo dating
Playing: Wanjapi
Playing: Kuna Kuna
Playing: Kuna Kuna
Playing: Wanjapi
Playing: Kanairo dating
Playing: Toto
Playing: Mbona
Playing: Woman
```

## Requirements

Before we get into the code, let's understand what we want the `Jukebox` class to do. **Pay attention here, understanding this is key to you being able to complete this assignment**

A Jukebox needs to keep track of the following data:
- `songs`: This is a list of strings that represent the song titles
- `current_song`: This is the index of the currently playing song
- `is_playing`: This is a Boolean that represents if the jukebox currently playing or paused. 

A Jukebox should have the following methods:
- `play()`: starts playing the Jukebox. This method should make the `is_playing` attribute `True`
- `pause()`: pauses the Jukebox. This method should make the `is_playing` attribute `True`
- `next()`: goes to the next song. This modifies the `current_song` attribute
- `previous()`: goes to the previous song. This modifies the `current_song` attribute
- `current_state()`: returns a message indicating whether the jukebox is playing or
  paused. If it's playing, it should also return the current song that's playing.
  - If paused: return `"Paused"`
  - If playing: return `"Playing: [Song name]"` with the name of the current song
- `copy_song_list()`: returns a **copy** of the JukeBox's song list.

When created, a JukeBox should **not** start playing.

The first song to play should be the first song in the list.

Our song list should loop. This means that:
- Calling the `next()` method when we are on the last song should take us to the first song
- Calling the `previous()` method when we are on the first song should take us to the last song

Take your time reading the above, then let's get started testing and fixing the provided code

### Step 1: Do we even have a jukebox? (1 point)
Our first milestone is to make sure that we can create a `JukeBox` object. 

Run the unit tests with `python -m unittest` or `pytest`. You should see that 1 test ran. The test creates a `JukeBox` object and checks that all its attributes were initialized correctly.

Unfortunately this test **failed!** 

You will be shown an error message: `NameError: name 'self' is not defined`

Use your intuition and the debugger to figure out what could be wrong with our `JukeBox` class definition. 

Work on this until you see that the test passes, then move on to the next milestone.

### Step 2: Playing/Pausing (1 point)
In this milestone we want to make sure that we can change the **state** of the `JukeBox` object. 

Open the `test_jukebox.py` file, and remove the comments between lines **16 and 26**, then run the tests again

Run the unit tests with `python -m unittest` or `pytest`. You should see that 3 tests ran in total, with one new failure:

`    assert player.current_state() == "Paused"
AssertionError`

When we expected our current_state() to be "Paused", we got something different. Once again, investigate and debug the class to find the issue.

Work on this until you see all 3 tests passing, then move on to the next milestone.

### Step 3: Please don't stop the music (2 points)
In this milestone we want to make sure that we can move through our song list. 

Open the `test_jukebox.py` file, and remove the comments between lines **21 and 41**, then run the tests again. Luckily everything should pass now! This tells us that we can move to the next song, and go back to the previous song. 

**Note that if these new tests failed, that means you modified the next() and previous() method incorrectly, make sure they pass before moving forward**

But wait. `next()` and `previous` sound easy to handle, but remember we want our song list to loop around, so when we hit `next()` on the last song we go to the first. When we hit `previous()` on the first song we go to the last. 

Remove the comments between lines **45 and 59**, then run the tests again. Both new tests will fail. How can we improve the `next()` and `previous()` methods to make them pass?

Work on this until you see all 7 tests passing, then move on to the next and final milestone.

### Step 4: Reference problems (2 points)
We are almost there! comment out the final test, from lines **62 to 66**, and run tests again. You should see it fail.

The issue with this final test is that while our `copy_song_list()` method returns a list that is indeed similar to the song list, it is not returning **a different object**. Based on what we learned this week, how can we make sure that the method returns a **copy** of the song list, not a **reference** to it?

Work on this until you see all 8 tests passing.

## Submitting an assignment

When you are done, `commit` and `push` your code. Submit a link to your work on
Github using this form: **[Programming Exercise log](https://forms.gle/UbWLpo86JsWxrpNe9)**.

Be sure that the link you submit will take the instructor directly to your code.

<aside>

**If you get stuck**
1. Read the instructions again.
2. Remember **G**o **C**limb **K**ibo - first Google, then ask the Community on Discord, then reach out to Kibo instructional team.

</aside>

<!--meta exposure: initial -->
<!--meta assessmentFormat: ProgrammingAssignment, GitHubClassroom -->
<!--meta submissionVia: GradeScope -->
<!--meta instructionType: specific -->
<!--meta submissionFormatFlexibility: no -->
<!--meta submissionTopicFlexibility: no -->
<!--meta rubricAvailable: yes -->
<!--meta rubricShared: yes -->
<!--meta groupWork: no -->
<!--meta automatedGrading: 80 -->
<!--meta studentInstructionsLink: https://github.com/kiboschool/programming2-w2-debugging -->
<!--meta topics: memory, oop, debugging -->

# Assignment 2: Jukebox

## Introduction

A Jukebox is an old music player (see [https://en.wikipedia.org/wiki/Jukebox](https://en.wikipedia.org/wiki/Jukebox)).
In the time before mp3 players or smartphones, bars and restaurants would have a
music player that allowed minimal song selection.

In this project, we will do something different: We will provide you code! It is,
however, up to you to figure out if it works well. You will have to read methods,
understand what they _should_ do, as well as what they _actually_ do, and fix
any errors you find in your way. You will have to write a little bit of code,
but this assignment mostly tests your ability to read code and debug it.

### Provided Code

Clone your repo using this link: [https://github.com/kiboschool/programming2-w2-debugging](https://github.com/kiboschool/programming2-w2-debugging)

`jukebox.py` is where our JukeBox class is defined. This is where you are expected
to do your work.

`test_jukebox.py` is a test file. Your aim will be to make sure all the tests pass. Unfortunately, very few of them do at the moment. To help you focus, most of the tests are _commented out_. Each step in the assignment will ask you to bring back some of the tests.

`main.py` is a demo of the JukeBox class. It should run perfectly by the end of the assignment, and you can find what the output of this file should look like further down these instructions. Feel free to add some of your own code here to test the class, but changes to this file will not influence your grade.

#### Testing

Run the unit tests with `python -m unittest` or `pytest`.

You can inspect or run `main.py` to see an interactive use of the Jukebox class.

A working sample run of `main.py` has this output:

```prompt
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

### Step 1: Do we even have a jukebox?

Our first milestone is to make sure that we can create a `JukeBox` object.

Run the unit tests with `python -m unittest` or `pytest`. You should see that 1 test ran. The test creates a `JukeBox` object and checks that all its attributes were initialized correctly.

Unfortunately this test **failed!**.

You will be shown an error message: `NameError: name 'self' is not defined`

Use your intuition and the debugger to figure out what could be wrong with our `JukeBox` class definition.

Work on this until you see that the test passes, then move on to the next milestone.

### Step 2: Playing/Pausing

In this milestone we want to make sure that we can change the **state** of the `JukeBox` object.

Open the `test_jukebox.py` file, and remove the comments between lines **16 and 26**, then run the tests again

Run the unit tests with `python -m unittest` or `pytest`. You should see that 3 tests ran in total, with one new failure:

```text
assert player.current_state() == "Paused"
AssertionError
```

When we expected our `current_state()`` to be "Paused", we got something different. Once again, investigate and debug the class to find the issue.

Work on this until you see all 3 tests passing, then move on to the next milestone.

### Step 3: Please don't stop the music

In this milestone we want to make sure that we can move through our song list.

Open the `test_jukebox.py` file, and remove the comments between lines **21 and 41**, then run the tests again. Luckily everything should pass now! This tells us that we can move to the next song, and go back to the previous song.

**Note that if these new tests failed, that means you modified the next() and previous() method incorrectly, make sure they pass before moving forward.**

But wait. `next()` and `previous` sound easy to handle, but remember we want our song list to loop around, so when we hit `next()` on the last song we go to the first. When we hit `previous()` on the first song we go to the last.

Remove the comments between lines **45 and 59**, then run the tests again. Both new tests will fail. How can we improve the `next()` and `previous()` methods to make them pass?

Work on this until you see all 7 tests passing, then move on to the next and final milestone.

### Step 4: Reference problems

We are almost there! comment out the final test, from lines **62 to 66**, and run tests again. You should see it fail.

The issue with this final test is that while our `copy_song_list()` method returns a list that is indeed similar to the song list, it is not returning **a different object**. Based on what we learned this week, how can we make sure that the method returns a **copy** of the song list, not a **reference** to it?

Work on this until you see all 8 tests passing.

## Grading

| Criteria                            | Proficient                                        | Competent                                          | Developing                                       |
|-------------------------------------|---------------------------------------------------|----------------------------------------------------|--------------------------------------------------|
| **Coding Style (20%)**   ||||
| 1. Indentation and Formatting       | Code is consistently well-indented and follows PEP 8 formatting guidelines. | Code is mostly well-indented and follows PEP 8 guidelines with minor deviations. | Code lacks consistent indentation and does not follow PEP 8 guidelines. |
| 2. Naming Conventions               | Meaningful and consistent variable/function/class names following PEP 8 conventions. | Mostly meaningful names, with occasional inconsistencies. | Variable/function/class names are unclear or inconsistent. |
| 3. Comments and Documentation       | Comprehensive comments and clear documentation for major functions and complex logic. | Adequate comments explaining major sections of code. | Lack of comments or insufficient documentation. |
| 4. Appropriate Use of Language Constructs | Demonstrates advanced understanding and appropriate use of Python language constructs (e.g., list comprehensions, generators). | Generally applies language constructs correctly, with occasional lapses. | Misuses or misunderstands key language constructs. |
| **Persistence (50%)**                    |                                                   |                                                    |                                                  |
| 5. Completeness                     | Evidence that all components of the assignment were attempted.  All functionality present. | Evidence that most elements of the assignment were attempted. Most functionality present. | Little evidence of completion of work.  Incomplete or major functionality missing.        |
| 6. Timeliness                       | Assignment started early (based on GitHub data).  GitHub commits show steady progress. Submitted on time. | Assignment is submitted late but GitHub data demonstrates an early or reasonable start date, with significant iteration on arrival to solution (i.e., multiple commits showing progress) | Submitted late. GitHub repository data shows late start and minimal iteration. |
| 7. Use of Resources                 | Assignment is fully complete and provides all functionality. If assignment is not fully complete, student attended office hours (or additional help sessions) and/or asked high quality and timely questions on Discord. | Assignment is not fully complete and there is minor evidence of effort to get assistance on assignment (e.g., office hours attendance or Discord discussions). | Assignment is incomplete and no evidence of seeking assistance. |
| **Correctness (30%)**               |                                                   |                                                    |                                                  |
| 8. Test Cases                       | Percentage of automated test cases that pass. |||

> **Evidence of Persistence:**
>
> In the event that you are unable to get your program fully functional, you will receive partial credit based on your evidence showing the amount
> of effort that went into learning the underlying concepts to complete the assignment or that you persistently sought appropriate assistance. Examples of persistence may
> include, but is not limited to, the following: Git commit history showing evolution of your program, attendance to office hours (Instructor or TA), asking
> thoughtful questions in the appropriate Discord forums, formation of study groups, completion of additional practice exercises, reading of third-party
> resources, etc.  
>
> To receive partial credit, you **must** create a file called `PERSISTENCE.md` in your GitHub repo alongside the `README.md` file, and include your evidence of
> persistence, for example, links to your Discord questions, narrative explaining dates and times of office hour sessions that you attended and what you learned, links to resources that you referenced,
> links to ChatGPT conversations that you initiated (focusing on concepts not just getting answers), etc. The better you can demonstrate your work on learning, the
> easier it will be to provide partial credit, so be thorough. Make sure that file is properly committed to your repo, and included in your Gradescope submission.

## Submitting Your Work

Your work must be submitted Anchor for degree credit and to Gradescope for grading.

**For coding tasks involving Github Classroom:**

1. Ensure that you `commit` and `push` your local code changes to your remote repository.  (Note: In general, you should commit and push frequently, so that you have a backup of your work, so that there is evidence that you did your own work, and so that you can return to a previous state easily.)
2. Upload your submission to [Gradescope](https://www.gradescope.com) via the appropriate submission link by selecting the correct GitHub repository from the drop-down list.
3. Export a zip archive of your GitHub repository by visiting your repo on [GitHub](https://www.github.com), clicking on the green `Code` button, and selecting "Download Zip".
4. Upload the zip file of your repository to Anchor using the form below.

**For cases where you answer questions on Gradescope:**

1. Complete the work in [Gradescope](https://www.gradescope.com) by navigating tot he appropriate link.
2. Export it as a pdf using th Google Chrome plugin: [https://gofullpage.com/](https://gofullpage.com/).  This plugin will do multiple screen captures while scrolling through your document, and then stitch them into a pdf that you can download.
3. Upload the generated pdf to Anchor using the form below.

**For any work completed outside of GitHub or Gradescope:**

1. Take either screen captures of your work or export a pdf showing your complete work.
2. Submit the materials to [Gradescope](https://www.gradescope.com) via the appropriate submission link for the course.
3. Upload the screen captures or pdf files to Anchor using the form below.

> **Note:** Anchor submissions can occur at any time during the term, but it is **critical** that you upload all of your work to
> Anchor before the last day of the term.  Gradescope submissions must be submitted before the deadline (or the late deadline, if applicable).

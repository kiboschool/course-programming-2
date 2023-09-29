# Refactoring

The video here will explain what refactoring is, and why it can be helpful:

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/8D2RHhJ0794" title="Programming 2: Refactoring" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

To follow along with the video, you can download the source code by using the links below. You can pause the video every few minutes and look through the code.

<a href="https://github.com/kibo-programming-2-jan-23/walkthroughs/tree/main/phonebook-refactoring/1-before-refactoring" target="_blank">Part 1: Before refactoring</a>

<a href="https://github.com/kibo-programming-2-jan-23/walkthroughs/tree/main/phonebook-refactoring/2-after-refactoring" target="_blank">Part 2: After refactoring</a>

<a href="https://github.com/kibo-programming-2-jan-23/walkthroughs/tree/main/phonebook-refactoring/3-after-changing-implementation" target="_blank">Part 3: After changing the data structure</a>


### Details on refactoring

In large projects, software developers read through the code often. This means that it is valuable to have code that is easier to understand and work with.

Improving code in any of these ways is considered a type of refactoring:

* Naming
    * Improving the variable names, method names, and file names
* Readability, intention
    * Making the purpose of the classes and methods more clear to people reading the code
* Readability, implementation
    * Making the implementation - how the program works - more clear to people reading the code
* Testability
    * Restructuring the program so that automated tests can be written
* Flexibility
    * Making the pieces of the program not be tangled to the details of other pieces of the program

Why should we spend time organizing code in a way that allows us to make changes in the future?

Because in the world of professional software development, code is always changing. Some reasons why a program will need to change:

* New requirements
    * Realizing that the program needs to have different capabilities
* Feature requests
    * Needing to add or modify a feature
* Reuse
    * Taking code from one project and repurposing it to use in another project
* Bug fixes
    * Needing to fix bugs and errors
* Platform changes
    * Maintaining compatibility with the newest versions of Python, and newest versions of the Python modules being used


## Wrap up

This brings us to the end of new content for the course. Next week we will focus on revision of content: Make sure to come prepared to discuss topics you still feel unsure about. 

We will also release your final project early next week! You will have two weeks to work on it, and it will be your biggest coding exercise yet. Organize your time to start as early as possible, and use office hours wisely!

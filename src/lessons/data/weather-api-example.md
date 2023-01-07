# Weather API Example

Watch the video below to see how I update the weather program we've been working on to read real weather information from the internet.

## Part 1, Calling the API

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe width="560" height="315"  src="https://tempclip.com/embed/krFhqubVS8KrsuN"  frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Part 2, Completing the Program

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe width="560" height="315"  src="https://tempclip.com/embed/p4TsmtCfdFUxtXX"  frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Exercise:

Currently the program saves the json information to a file, and then reads the information back in from the file. This is unnecessary, there is a way to get the information without needing to save to a file. Modify the program so that it doesn't save to a file.

Hint: remember that there is a function `json.loads()` that loads from a string instead of a file. And the data type returned by the `decode()` method is a string.




# Practice

---

> 💡 This is your chance to put what you’ve learned into action.

### Submission

You are required to submit documentation for 10 practice exercises over the
course of the term. Each one will count for 1/10 of your practice grade, or 1%
of your overall grade.

To log your practice for credit:

> **[Submit a link using this form](https://forms.gle/UbWLpo86JsWxrpNe9)**

* Practice exercises will be graded for _completion_ not _correctness_. You have
to document that you did the work, but we won't be checking if you got it right.
* You are welcome to log practice that is not one of the exercises listed on the 
practice page.
* You can submit a link to a github repo, a replit, a Google doc, or some other 
resource.

Your log will count for credit as long as it:
- is accessible to your instructor
- shows your own work

## Setup

Click Open Project here to get a copy of the code. Just like the videos, we will be adding to the weather API example!

<a href="https://classroom.github.com/a/PCUb7tFJ" target="_blank"><img src="https://img.shields.io/static/v1?label=Open%20Project&message=Weather%20API%20Exercise&color=blue" alt="weather-api-exercise" /></a>

<!-- link to https://github.com/kibo-programming-2-jan-23/show-weather-from-api-exercise -->

## Part 1: A new city

Add a new city. You can usually find the coordinates for a city on the wikipedia page for a city, then look on the panel on the right side for "coordinates". 

Once you have the coordinates, format them the same way that the existing entries are written. Note that "S" or "south" is negative and "N" or "north" is positive. Add the new city to the list in `map_city_to_coords` and try it.

## Part 2: Wind direction

Add a feature to the program, so that it shows the wind direction alongside the temperature. Show the wind direction in a descriptive way, for example display "From the southwest" instead of "SW" and "From the north" instead of "N".

Hint: open the `api_output.json` file and look for wind. Remember that a dictionary can contain other dictionaries. It's sometimes easier to get the data in two steps.

## Part 3 (optional): Avoiding saving the file

Currently the program saves the json information to a file, and then reads the information back in from the file. This is unnecessary - isn't there a way to get the information without needing to save to a file first? Modify the program so that it doesn't save to a file.

Hints:
* Right now the `get_api_results` function does not need to return anything, but you can change it so that it will `return` a value at the end. 
* The data type returned by the `decode()` method is a string.
* And remember that there is a function `json.loads()` that loads from a string instead of a file.

## Submitting the assignment

When you are done, `commit` and `push` your code. Submit a link to your work on
Github using this form: **[Programming Practice log](https://forms.gle/UbWLpo86JsWxrpNe9)**

<image src="../../images/w1/cool_library_snake.png" height="25%" width="25%" style="border:none, border-width: 0, border: 0; margin-top:2em; box-shadow: 0px 0px;" />

<aside>

**If you get stuck**
1. Read the instructions again.
2. Remember **G**o **C**limb **K**ibo - first Google, then ask the Community on Discord, then reach out to Kibo instructional team.

</aside>



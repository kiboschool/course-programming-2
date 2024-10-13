<!--meta exposure: initial -->
<!--meta assessmentFormat: ProblemSet -->
<!--meta submissionVia: CodeCheck -->
<!--meta instructionType: specific -->
<!--meta submissionFormatFlexibility: no -->
<!--meta submissionTopicFlexibility: no -->
<!--meta rubricAvailable: yes -->
<!--meta rubricShared: yes -->
<!--meta groupWork: no -->
<!--meta automatedGrading: 100 -->
<!--meta studentInstructionsLink: https://codecheck.io/assignment/23111422363sxun8e3pdh568v81zmmliey1 -->
<!--meta topics: exceptions, testing -->

# Practice: Exceptions and Testing

## Required Practice

Complete the exercises using the link below.

[https://codecheck.io/assignment/23111422363sxun8e3pdh568v81zmmliey1](https://codecheck.io/assignment/23111422363sxun8e3pdh568v81zmmliey1)

When you start the exercise, you will be given a `CodeCheck ID`.  You must **save this ID and the private URL** so that you can return to your work later!  If you don't save the private URL (which contains the `CodeCheck ID`), you will have to start the exercise from the beginning.  We will re-use this site throughout the term, so I recommend creating a document on your computer where you will save the private URLs for the whole term.

After you have completed the exercise, submit your `CodeCheck ID` to GradeScope using the following link:

[/assignments/practice__exceptions_/assignments/practice__exceptions_/assignments/practice__exceptions_/assignments/practice__exceptions_https://www.gradescope.com/courses/544003/assignments/3597316_testing.pdf_testing.pdf_testing.pdf_testing.pdf](/assignments/practice__exceptions_/assignments/practice__exceptions_/assignments/practice__exceptions_/assignments/practice__exceptions_https://www.gradescope.com/courses/544003/assignments/3597316_testing.pdf_testing.pdf_testing.pdf_testing.pdf)

For submission to Anchor, please take a screen capture of each of your solutions (5 in total for this assignment) and submit them below.  

## Additional Practice

### Pagination Testing

Imagine a "pagination" function that takes a list as a parameter. The goal is to take a long list and split it into pages of length 5 or less. The result is a list of lists that all need to be less than 5 items. For example, if the input is [1, 2, 3, 4, 5, 6, 7], the output would be [[1, 2, 3, 4, 5], [6, 7]].

This type of function would be used, for example, if a search engine gave you 90 results, and you needed to display them to the user one page at a time.

* What test cases would you write to test this function?
  * Make a list of at least 3 test cases you would write if you were to write unit tests for this function.

### Testing Show Weather From API

Recall our "show-weather-from-api" program that we worked on earlier in the course. You can see the source code at the link  [here](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/show-weather-from-api/end/program.py).

Right now, the `show_weather_to_user` function is not as easily testable because it prints the result instead of returning it as a string.

#### Making the program more testable

* Modify `show_weather_to_user` so that it returns a string instead of using `print`.
  * This can be done while still leaving the program looking the same. Just take any place that calls `show_weather_to_user` and add a `print` at that point instead, that will print the return value from `show_weather_to_user`.
  
#### Writing test cases

* Make a list of at least 3 test cases you would write if you were to write unit tests for this function.

#### Creating a test (optional challenge)

* Create a file named `program.py` on your computer,
* Copy the `show_weather_to_user` function into that file,
* Create a file in the same folder named `test_show_weather_from_api.py`,
* Add test methods that call the `show_weather_to_user` function. For example,

```python
import unittest
import program

class TestShowWeatherFromApi(unittest.TestCase):
  def test_when_hour_number_is_24(self):
     fake_weather_data_list = ...
     result = program.show_weather_to_user(fake_weather_data_list)
     assert result == ...

```

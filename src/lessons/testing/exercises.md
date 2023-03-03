
# Exercises

> 💡 This is your chance to put what you’ve learned into action.

### Submission

> **[Use this form](https://forms.gle/UbWLpo86JsWxrpNe9)**

You are required to submit documentation for 10 exercises over the
course of the term. Each one will count for 1%
of your overall grade.

* You are welcome to log work that is not one of the exercises listed on the 
exercises page.
* You can submit a link to a github repo, a replit, a Google doc, or some other 
resource.

Your log will count for credit as long as it:
- is accessible to your instructor
- shows your own work

<!--## Pagination test cases

Imagine a "pagination" function that takes a list as a parameter. The goal is to take a long list and split it into pages of length 5 or less. The result is a list of lists that all need to be less than 5 items. For example, if the input is [1, 2, 3, 4, 5, 6, 7], the output would be [[1, 2, 3, 4, 5], [6, 7]].

This type of function would be used for example if a search engine gave you 90 results, and you needed to display them to the user one page at a time.

* What test cases would you write to test this function?
  * Make a list of at least 3 test cases you would write if you were to write unit tests for this function.
-->

<hr/>

Recall our "show-weather-from-api" program that we worked on earlier in the course. You can see the source code at the link  [here](https://github.com/kibo-programming-2-jan-23/walkthroughs/blob/main/show-weather-from-api/end/program.py).

Right now, the `show_weather_to_user` function is not as easily testable because it prints the result instead of returning it as a string.

### Making the program more testable

* Modify `show_weather_to_user` so that it returns a string instead of using `print`.
   * (This can be done while still leaving the program looking the same. Just take any place that calls `show_weather_to_user` and add a `print` at that point instead, that will print the return value from `show_weather_to_user`.)
   
### Writing test cases

* Make a list of at least 3 test cases you would write if you were to write unit tests for this function.




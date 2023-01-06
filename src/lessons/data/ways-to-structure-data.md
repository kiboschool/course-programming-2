# Ways to Structure Data

Let's start with a quick reminder of some basics from the Programming 1 course.

### Reminders from Programming 1

When you write `score = 100`, you are taking the *value* 100, and putting it into a *variable* named score.

Every value is a specific type.

* Values can be of type **int**. This is short for integer. These are whole numbers like 1, 0, 8, and 12.
* Values can be of type **float**. These are any type of number, including decimals like 1.0, 4.32, or 10.189.
* Values can be of type **str**. This is short for string. These are used to store groups of letters in order, for example a piece of text like`"hello"`. When you create a string you use quote marks. It's good to remember the term string -- we'll refer to the term string often, and each time just think of it as a piece of text.

We can modify variables, by writing something like `score = 200`. Writing `score += 50` will add 50 to score. Writing `message = f'The score is {score}."` will create a new string that displays the score. You could write `message += ' Good job'` to add to the string, and `print(message)` to display the string.

In programming-1 we used `print()` to display strings and `input()` to let the user enter a string into the program. When you write something like `input()` we call this "calling into a function". We even learned how to create our own new functions by writing `def my_own_function()`.  Then other places in the code we could call into the function by writing `my_own_function()`.

We used `if` and `else` to direct the program to do different things in certain cases. We used loops like `while` and `for` to run a few lines of code more than once. We learned to check the loops by adding a temporary `print` inside them to see what was happening, something we do all of the time when writing programs.

Remember that you can create lists. You can write `countries = ['Kenya', 'Ghana', 'Ethiopia']` and then write `print(countries[0])` and `print(countries[1])` to show the first two elements in the list. To change something there is `countries[2] = 'Nigeria'` and to add something to the end of the list there is `countries.append('Cameroon')`. There is `len(countries)` to get the number of elements. We can write a loop like `for country in countries: print(country)` to do something for each element in the list. It might have been a while since we talked about this, so if there is anything mentioned you don't remember, please go back to the programming 1 website and read about it for a few minutes to refresh your memory.

Towards the end, we talked about splitting a task into separate functions, where each function does one piece of the program. Reading a file is accomplished with `open()` and `read()`, writing a file is accomplished with `open()` and `write()`, and `os.listdir()` gets a list of files in a given directory (aka a folder on your computer).

Most importantly, we talked about "dictionaries". Dictionaries are useful for so many purposes - they can be a mapping from one piece of data to another,

```
capitals = {
  "Kenya": "Nairobi",
  "Ghana": "Accra",
  "Ethiopia": "Addis Ababa",
  "Zimbabwe": "Harare",
}
print(capitals["Kenya"]) # "Nairobi"
```

and they can be used as a counter,

```
statistics = {
    "count_how_many_at_least_ten": 0,
    "count_how_many_less_than_ten": 0,
}
data = [5, 9, 11, 4, 18]
for element in data:
    if element > 10:
        statistics['count_how_many_at_least_ten'] += 1
    else:
        statistics['count_how_many_less_than_ten'] += 1
```

and a dictionary can even contain other dictionaries,

```
country_data = {
  "Kenya": {"capital: "Nairobi", "currency": "shilling"},
  "Ghana": {"capital: "Accra", "currency": "cedi"},
  "Ethiopia": {"capital: "Addis Ababa", "currency": "birr"},
}

print(country_data["Ghana"]["currency"])
```

In all of these cases the dictionary is connecting each "key" to a "value".

### Data structures

It is very useful for a list to contain dictionaries, or for a dictionary to contain other dictionaries. This is an important way to keep data organized.

Let's go back to one of the final projects from the Programming-1 course, the Student Enrollment Management project. We were asked to build a project that had a list of student data,

```
Student Records

 - Must keep a list of the students
 - Student records include a student ID, a student name, and the courses they are enrolled in.
 - Must be able to Add or Remove students
 - Must be able to look up students and see their information as well as their course enrollments.
```

There are many ways to store this information. There could be a group of different `list`s. There could be a `dict` from student id to a `list` or `dict` of student information. When we talk about the shape of the data, like whether it is a dictionary of dictionaries or a list of dictionaries, this is called talking about the data structure.

This would be one way to structure the student records:

```
student_ids = [35434, 67768, 17768, 45645]
student_names = ['Joshua', 'Michael', 'Jessica', 'Rapheal']
student_course_ids_enrolled = [[], [567567], [78979, 567567], []]
```

(In this example solution I came up with, all of the ids are fake numbers I came up with as an example, and the lists in student_course_ids_enrolled are lists of the course ids that student is enrolled in. Don't worry about the courses, right now we're just thinking about the students).

This structure does work to solve the problem. But it isn't ideal for a few reasons. First of all, if a new student is added, a new element has to be added to all three lists, and if there is any place in the code that forgets to add an element to one of the lists, this is a bug that will cause errors. It is the same for deleting a student - all three lists would have to be updated. We'd have three different variables to keep track of and pass around to the different functions. 

This data structure would be better in some ways,

```
student_records = [
    ['Joshua', 35434, []],
    ['Michael', 67768, [567567]],
    ['Jessica', 17768, [78979, 567567]],
    ['Rapheal', 45645, []],
]
```

(notice that this is the same data as before, just moved to a different structure).

The advantage is that we are down to one variable. And so when a student is added or deleted, there isn't a chance to forget to update one of the variables. But now, to get the name of the first student, we would write `student_records[0][0]` and to get the id we would write `student_records[0][1]`. This code is hard to read and understand because it's hard to remember that [0] refers to the name and [1] refers to the id. We could add comments to help explain, but it's still not great.

In general, a better data structure would be to use dictionaries,

```
student_records = [
    { 'name': 'Joshua', 'id': 35434, 'courses_enrolled_in': [] },
    { 'name': 'Michael', 'id': 67768, 'courses_enrolled_in': [567567] },
    { 'name': 'Jessica', 'id': 17768, 'courses_enrolled_in': [78979, 567567] },
    { 'name': 'Rapheal', 'id': 45645, 'courses_enrolled_in': [] },
]
```

Our code will now be much easier to read, because we can write code like `student_records[0]["id"]` to refer to the id of the first student in the list. 


<!--

------------------------------- in progress -------------------------------


quiz: data structure?

Review programming-1, walk through an example reading file from disk
Structuring data: could put it all in a list. But a dict of dicts is better to deal with. Weather api– if searching a list, you would need to traverse everything, which is less organized than weather[‘seattle’][‘12-06-2022’]
Data, like a list of temperatures in the forecast for the next few days

Warm-up with Dictionaries
    We provide map of some capital cities to lat/long, student adds a new entry to the map
    
Warm-up with Reading from a list of weather data

Warm-up with Reading from a dict of weather data

-->
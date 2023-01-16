# Data types and Dictionaries

Let's start with a reminder of some topics from the Programming 1 course.

## Values and types

When you write `score = 100`, you are taking the **value** 100, and putting it into a **variable** named score.

Every value is a specific type.

* Values can be of type **int**. This is short for integer. These are whole numbers like 1, 0, 8, and 12.
* Values can be of type **float**. These are any type of number, including decimals like 1.0, 4.32, or 10.189.
* Values can be of type **str**. This is short for string. These are used to store groups of letters in order, for example a piece of text like`"hello"`. You can have a string that contains numeric digits, like `"123"`. When you create a string you use quote marks. It's good to remember the term string -- we'll refer to the term string often, and each time just think of it as a piece of text.

# Reviewing the basics

We can modify variables, by writing something like `score = 100` and then later on in the code writing `score = 200`. Writing `score += 50` will add 50 to the variable score.

---

If we write `message = f'The score is {score}.'` it will create a new string that displays the score - the `f''` tells Python to look for variables inside the string and put the contents in.

---

You could write `message += ' Good job!'` to add text to end of the string.

---

In Programming 1 we used `print(f'The score is {score}.')` to display the contents of the variable store. And we can write many extra prints like that when we are creating a program to check what is happening to all of the variables. 

---

We used `input('please type your name')` to let the user enter a string into the program.


---

When the code that says `some_function(some_input)` runs, we call this "calling the function `some_function`". For example, `input` and `print` are functions that your programs will call all the time. We learned how to create our own new functions. For example, if we wrote a function that added two numbers, we could start by writing `def add_numbers(num1, num2)`.  Then somewhere else in the code we could call into the function by writing `add_numbers(1, 2)`.

---

We talked about how splitting a task into separate functions, where each function does one piece, is a great way to build a program.

---


We used `if` and `else` to direct the program to do different things in certain cases. We used loops like `while` and `for` to run a few lines of code more than once. We learned to check the loops by adding an extra `print` inside them to see what was happening, something we do all of the time when writing programs.

# Lists

Remember that you can create lists. You can write `countries = ['Kenya', 'Ghana', 'Ethiopia']` and then write `print(countries[0])` and `print(countries[1])` to show the first two elements in the list.

To change something there is `countries[2] = 'Nigeria'` and to add something to the end of the list there is `countries.append('Cameroon')`.

There is `len(countries)` to get the number of elements.

We can write a loop like `for country in countries: print(country)` to do something for each element in the list.

It might have been a while since we talked about this, so if there is anything mentioned you don't remember, please go back to the programming 1 website and read about it for a few minutes to refresh your memory.

# Files

Towards the end, we opened and wrote files.

* Reading a file is accomplished with `open()` and `read()`
* Writing a file is accomplished with `open()` and `write()`
* `os.listdir()` gets a list of files in a given directory (aka a folder on your computer).

# Dictionaries

Most importantly, we talked about "dictionaries". Dictionaries are useful for so many purposes.

They can be a mapping from one piece of data to another:

```python
capitals = {
  "Kenya": "Nairobi",
  "Ghana": "Accra",
  "Ethiopia": "Addis Ababa",
  "Zimbabwe": "Harare",
}

print(capitals["Kenya"]) # "Nairobi"
```

and they can be used as a counter:

```python
statistics = {
    "count_how_many_at_least_ten": 0,
    "count_how_many_less_than_ten": 0,
}

data = [5, 9, 11, 4, 18]
for element in data:
    if element >= 10:
        statistics['count_how_many_at_least_ten'] += 1
    else:
        statistics['count_how_many_less_than_ten'] += 1
```

and a dictionary can even contain other dictionaries:

```python
country_data = {
  "Kenya": {"capital": "Nairobi", "currency": "shilling"},
  "Ghana": {"capital": "Accra", "currency": "cedi"},
  "Ethiopia": {"capital": "Addis Ababa", "currency": "birr"},
}

print(country_data["Ghana"]["currency"])
```

In all of these examples, the dictionary is connecting keys (like the name of the country) to values (like the corresponding data for the country).

## Practice: Dictionaries

Write a `for` loop to show all of the currencies in `country_data`.

<iframe src="https://trinket.io/embed/python/67f058762c" width="100%" height="300" frameborder="0" style="margin-top:2em"  allowfullscreen></iframe>

### Solution

Here is a good way to show all of the currencies:

<details><summary>See the Solution</summary>

```python

def show_currencies():
    for country_name in all_country_data:
        # each time through the loop, we'll get a different country_name.
        country_data = all_country_data[country_name]
        print(country_data['currency'])

show_currencies()

```

</details>

## Review: Dictionaries

Dictionaries do take a bit of time to understand. You can [review the material on dictionaries from Programming 1 here](https://programming-1.vercel.app/lessons/data_structures/dict-basics.html).



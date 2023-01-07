
# Data Types, Dictionaries

Let's start with a reminder of some topics from the Programming 1 course.

### Data Types, and Other Programming 1 Topics

When you write `score = 100`, you are taking the **value** 100, and putting it into a **variable** named score.

Every value is a specific type.

* Values can be of type **int**. This is short for integer. These are whole numbers like 1, 0, 8, and 12.
* Values can be of type **float**. These are any type of number, including decimals like 1.0, 4.32, or 10.189.
* Values can be of type **str**. This is short for string. These are used to store groups of letters in order, for example a piece of text like`"hello"`. When you create a string you use quote marks. It's good to remember the term string -- we'll refer to the term string often, and each time just think of it as a piece of text.

We can modify variables, by writing something like `score = 200`. Writing `score += 50` will add 50 to score. Writing `message = f'The score is {score}."` will create a new string that displays the score. You could write `message += ' Good job'` to add to the string, and `print(message)` to display the string.

In programming-1 we used `print()` to display strings and `input()` to let the user enter a string into the program. When you write something like `input()` we call this "calling into a function". We even learned how to create our own new functions by writing `def my_own_function()`.  Then other places in the code we could call into the function by writing `my_own_function()`. (We talked about how splitting a task into separate functions, where each function does one piece, is a great way to write a program.)

We used `if` and `else` to direct the program to do different things in certain cases. We used loops like `while` and `for` to run a few lines of code more than once. We learned to check the loops by adding a temporary `print` inside them to see what was happening, something we do all of the time when writing programs.

### Lists and Files

Remember that you can create lists. You can write `countries = ['Kenya', 'Ghana', 'Ethiopia']` and then write `print(countries[0])` and `print(countries[1])` to show the first two elements in the list. To change something there is `countries[2] = 'Nigeria'` and to add something to the end of the list there is `countries.append('Cameroon')`. There is `len(countries)` to get the number of elements. We can write a loop like `for country in countries: print(country)` to do something for each element in the list. It might have been a while since we talked about this, so if there is anything mentioned you don't remember, please go back to the programming 1 website and read about it for a few minutes to refresh your memory.

Towards the end, we opened and wrote files. Reading a file is accomplished with `open()` and `read()`, writing a file is accomplished with `open()` and `write()`, and `os.listdir()` gets a list of files in a given directory (aka a folder on your computer).

### Dictionaries

Most importantly, we talked about "dictionaries". Dictionaries are useful for so many purposes.

They can be a mapping from one piece of data to another,

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
    if element >= 10:
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

In all of these examples, the dictionary is connecting keys (like the name of the country) to values (like the corresponding data for the country).

Dictionaries do take a bit of time to understand. You can read the informatation from Programming 1 [here](https://programming-1.vercel.app/lessons/data_structures/dict-basics.html), if it would be helpful.

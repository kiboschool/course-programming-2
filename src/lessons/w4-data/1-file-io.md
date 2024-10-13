# Saving and Reading Data

## Following along in the code

> The next few lessons walk through the steps to build a project using files and nested data structures.
>
> When there is a tutorial video, you can click the "Open Project" link to see the code, open it in VSCode, and follow along with the video.
>
> You will learn much more if you type out the code along with the tutorial.

### Weather forecast

Let's write a program to display the weather forecast for a city. We'll show the estimated temperature and wind speed.

For the first version of our program, the user will type in a city name, and we will show them the estimated temperature for the next 3 days.

<image src="../../images/w1/weather.png" height="25%" width="25%" style="border:none, border-width: 0, border: 0; box-shadow: 0px 0px;" />

This is the data structure we will use for the weather forecast for a city:

```python
forecast = [
    { 
        "day" : 1,
        "temperature": 23,
        "wind_speed": 1.37
    },
    {
        "day" : 2,
        "temperature": 20,
        "wind_speed": 0.25
    },
    {
        "day" : 3,
        "temperature": 21,
        "wind_speed": 0.83
    },
]
```

_`forecast` is a **list**. Each entry is a dictionary that contains 3 keys: "day", "temperature", "wind_speed"_

Our program stores the location data with GPS latitude and longitude coordinates, like 2.1° North, 5.6° West. GPS coordinates are similar to x and y coordinates on a graph, but are coordinates for a globe. Every location on the planet can be referred to by its latitude and longitude coordinates.

Software programs often use GPS coordinates like this to identity a location.

The full data structure looks like this,

```python
all_forecasts = {
    "9.02N,7.31E" : [
        { 
            "day" : 1,
            "temperature": 23,
            "wind_speed": 1.37 
        },
        { 
            "day" : 2,
            "temperature": 20,
            "wind_speed": 0.25 
        },
        { 
            "day" : 3,
            "temperature": 21,
            "wind_speed": 0.83
        }
    ], 
    "1.3S,36.85E":
    [
        { 
            "day" : 1,
            "temperature": 20,
            "wind_speed": 0.73 
        },
        { 
            "day" : 2,
            "temperature": 18,
            "wind_speed": 0.96 
        },
        { 
            "day" : 3,
            "temperature": 19,
            "wind_speed": 1.29
        }
    ],
    "5.63N,0.39W":
    [
        { 
            "day" : 1,
            "temperature": 15,
            "wind_speed": 1.31 
        },
        { 
            "day" : 2,
            "temperature": 13,
            "wind_speed": 0.24 
        },
        { 
            "day" : 3,
            "temperature": 16,
            "wind_speed": 0.83 
        }
    ]
}
```

_`all_forecast` is a dictionary. It uses a GPS coordinate as a key, and a forecast, as shown previously, as its entry_

### Walkthrough Part 1: Showing the Forecast

This walkthrough demonstrates retrieving data from the nested structures, and
displaying it.

Click Open Project to get the code and follow along in VSCode.

<a href="https://github.com/kiboschool/programming2-walkthroughs" target="_blank"><img src="https://img.shields.io/static/v1?label=Open%20Project&message=Code%20for%20the%20weather%20file%20video%20(not%20graded)&color=blue" alt="weather-from-file-example--not-graded" /></a>

<!-- link to https://github.com/kibo-programming-2-oct-23/show-weather-from-file -->

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/crdXLylaxQo?rel=0" title="Weather - Reading from Dictionaries" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

### Walkthrough Part 2: Saving the current city

This walkthrough demonstrates reading and writing json files.

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/vO-wHSf9Tko?rel=0" title="Weather - Reading from JSON" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

### Practice: Change the current city (Optional)

At the end of the program, ask the user if they would like to change the current city. If they type yes, let them type in a city, and then store that as the current city.

### Syntax Summary

Opening a file is simple with the `with open()` syntax.

```python
with open('path/to/your/file', mode) as f:
```

- mode is a string that tells python what we want to do with the file. Setting mode to `'r'` means we want to **read** the file.
- setting mode to `'w'` means we want to **write** to the file. You should think of this as **overwriting!** any existing content will be removed!
- seting mode to `'a'` means we want to **append** to the file. This will add whatever you write to the end of the file.
- `f` here is just a variable name that represents our file, we can replace that `f` with anything that would make more sense!

Reading and writing from a file is straightforward:

- `f.read()` returns the entire content of a file.
- `f.write("some content")` will write the string "some content" to the file. If our mode was `w` that would be all what the file says. If the mode was append, we would add it to the bottom of the file.

You can also read the content of the file line by line. The simplest way to do so is with the following syntax:

```python
with open('path/to/your/file', 'r') as f:
    for line in f:
        # line will contain the first line in the first iteration of the loop, the second line in the next, etc.
```

Alternatively, you can use the `readline()` method. `f.readline()` returns the first line of the file the first time you call it, the second line the second time you call it, etc.

There are many more methods you can use for handling files you can read about [here](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

Now handling json is a bit different. You could open a json file the same way as above, but in the case of json we **know** the data is structured, so we can get a data structure out of the file - for example a dictionary - instead of going through a list of strings!

```python
import json
with open('my_json_file.json', 'r') as example:
    example_content = json.load(example)
```

Note here that we first must import the json library - this contains many useful methods beyond the ones we cover here to deal with jsons. You can read the json documentation [here](https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json)

Once we open the file, we can use the `load` method of the `json` library to directly turn its content into a data structure! If the json in the file represented a list, we would get a list! if it represented a dictionary, we would get a dictionary!

This also means that we should be able to directly store lists or dictionary as json files, and we can!


```python
import json
with open('json_output.json', 'w') as example:
    example_content = json.dump(example)
```

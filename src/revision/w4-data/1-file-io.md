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

Our program stores the location data with GPS latitude and longitude coordinates, like 2.1° North, 5.6° West. GPS coordinates are similar to x and y coordinates on a graph, but are coordinates for a globe. Every location on the planet can be referred to by its latitude and longitude coordinates.

Software programs often use GPS coordinates like this to identity a location.

The full data structure looks like this,

```python
all_forecasts = {
    "9.02N,7.31E" : [
        { "day" : 1,
        "temperature": 23,
        "wind_speed": 1.37 },
        { "day" : 2,
        "temperature": 20,
        "wind_speed": 0.25 },
        { "day" : 3,
        "temperature": 21,
        "wind_speed": 0.83 }
    ], 
    "1.3S,36.85E":
    [
        { "day" : 1,
        "temperature": 20,
        "wind_speed": 0.73 },
        { "day" : 2,
        "temperature": 18,
        "wind_speed": 0.96 },
        { "day" : 3,
        "temperature": 19,
        "wind_speed": 1.29 }
    ],
    "5.63N,0.39W":
    [
        { "day" : 1,
        "temperature": 15,
        "wind_speed": 1.31 },
        { "day" : 2,
        "temperature": 13,
        "wind_speed": 0.24 },
        { "day" : 3,
        "temperature": 16,
        "wind_speed": 0.83 }
    ]
}
```

### Walkthrough Part 1: Showing the Forecast

This walkthrough demonstrates retrieving data from the nested structures, and
displaying it. 

Click Open Project to get the code and follow along in VSCode.

<a href="https://classroom.github.com/a/bqXfOdqE" target="_blank"><img src="https://img.shields.io/static/v1?label=Open%20Project&message=Code%20for%20the%20weather%20file%20video%20(not%20graded)&color=blue" alt="weather-from-file-example--not-graded" /></a>

<!-- link to https://github.com/kibo-programming-2-jan-23/show-weather-from-file -->

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/crdXLylaxQo?rel=0" title="Weather - Reading from Dictionaries" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

### Walkthrough Part 2: Saving the current city

This walkthrough demonstrates reading and writing json files.

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/vO-wHSf9Tko?rel=0" title="Weather - Reading from JSON" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

### Practice: Change the current city (Optional)

At the end of the program, ask the user if they would like to change the current city. If they type yes, let them type in a city, and then store that as the current city.



# Saving and Reading Data In Files

### Weather forecast

Let's imagine that we are writing a program to display the weather forecast for a city. We'll be showing the estimated wind speed, temperature, and the percentage of cloud cover in the sky.

For the first version of our program, the user will type in a city name, and we will show them the estimated temperature for the next 3 days.

This is the data structure we will use for the weather forecast for a city, it will be a list of dictionaries,

```
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

Our imagined program stores the location data with GPS latitude+longitude coordinates (if you haven't seen these before, like 2.1° North, 5.6° West, they are similar to x and y coordinates on a graph, but are coordinates for a globe. Every location on the planet can be referred to with latitude+longitude coordinates). This will make the program realistic, because real weather data uses these coordinates.

The full data structure looks like this,

```
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

Tutorial 1: Writing a program that shows the weather forecast

(Shows how to retrieve information from dictionaries)

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe width="560" height="315"  src="https://tempclip.com/embed/U39GzGgC2otu2HR"  frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Tutorial 2: Writing a program that remembers the current city

(Shows how to read and write json files)

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe width="560" height="315"  src="https://tempclip.com/embed/9wSHCjudZUkjZpk"  frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>



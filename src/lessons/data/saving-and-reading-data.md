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
        "wind_speed": 1.3
    },
    {
        "day" : 2,
        "temperature": 20,
        "wind_speed": 0.2
    },
    {
        "day" : 3,
        "temperature": 21,
        "wind_speed": 0.8
    },
]
```

Our imagined program stores the location data with GPS latitude+longitude coordinates (if you haven't seen these before, like 2.1° North, 5.6° West, they are similar to x and y coordinates on a graph, but are coordinates for a globe. Every location on the planet can be referred to with latitude+longitude coordinates). This will make the program realistic, because real weather data uses these coordinates.

The full data structure looks like this,

```
all_forecasts = {
"9.02°N,7.31°E" : [
    { "day" : 1,
    "temperature": 23,
    "wind_speed": 1.3 },
    { "day" : 2,
    "temperature": 20,
    "wind_speed": 0.2 },
    { "day" : 3,
    "temperature": 21,
    "wind_speed": 0.8 },
], 
"1.3°S,36.85°E":
[
    { "day" : 1,
    "temperature": 20,
    "wind_speed": 0.7 },
    { "day" : 2,
    "temperature": 18,
    "wind_speed": 0.9 },
    { "day" : 3,
    "temperature": 19,
    "wind_speed": 1.2 },
],
"5.63°N,0.39°W":
[
    { "day" : 1,
    "temperature": 15,
    "wind_speed": 1.3 },
    { "day" : 2,
    "temperature": 13,
    "wind_speed": 0.2 },
    { "day" : 3,
    "temperature": 16,
    "wind_speed": 0.8 },
]
}


```


<!--

Get the repo going and open `part1/program.py`.

First try running the program (showcurrentweather) and confirm that it works.

Then add support for the city Accra, which has the coordinates "5.63°N,0.39°W". 

Now open `part2/program.py`. (showcurrentweather) Notice how now we are reading from a json file on disk.

walk them through it:
making a json
reading the json

adding current location to the json
adding current location to the code
adding set current location--no, set metric or ferenhieght--no, set 
saving the json


Initial:
Please enter a city name to see the current weather:

New:
The current weather for your saved location is abc.
Please enter a city name to change your saved location.

--------------

add ghana which has the coordinates  
add current city load
add current city save

weather example

------------------------------- in progress -------------------------------

Warm up Read data from a provided simple json with weather data (just a list of numbers)
Read data from a provided realistic json with weather data (complex structure)

save as favorite

-->

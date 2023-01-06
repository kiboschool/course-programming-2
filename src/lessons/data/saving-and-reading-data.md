# Saving and Reading Data In Files

### Quiz

Can a dictionary contain other dictionaries?

TRUE/FALSE
Answer=TRUE
We can even have a dictionary that contains lists, and a list that contains dictionaries. Consider an example like this,

```
country_data = {
  "Kenya": {
        "capital: "Nairobi",
        "currency": "shilling",
        "parks": [
            {
            "park_name": "Aberdare National Park",
            "size_km": 767
            },
            {
            "park_name": "Meru National Park",
            "size_km": 870
            }
        ]
    },
  "Ghana": {
        "capital: "Accra",
        "currency": "cedi",
        "parks": [
            {
            "park_name": "Kakum National Park",
            "size_km": 375
            },
            {
            "park_name": "Mole National Park",
            "size_km": 4840
            }
        ]
    },
}
```
It sounds complicated to have a dictionary containing lists of dictionaries. But that is what is happening in this example, and it actually is not hard to understand. The example shows that this type of "nested" structure can actually be a great way to store data.

Someone else wrote a version of a program that uses a list to compute the answer, and I wrote a version of the program that uses a dictionary to solve the answer. So, our programs use different ________.
a) formats 
b) data structures
c) data libraries
d) modules
Answer=b

When we run the line of code `my_variable = "1.25"`, what is the type of my_variable?
a) int
b) float
c) str
d) number
Answer=c. This is a tricky one. If it were `my_variable = 1.25`, the answer would be float, it would be a floating point number. But because there are quotation marks, "1.25" is actually a string and just treated as text. Why does this difference matter? Writing `+` will add two floats, but if the inputs are strings, it will join two strings together. Open up Python and try showing the results of 1.25 + 1.25, and then show the results of "1.25" + "1.25" - the results are different!

Warmup exercise in replit:
```
country_data = {
  "Kenya": {
        "capital: "Nairobi",
        "currency": "shilling",
        "parks": [
            {
            "park_name": "Aberdare National Park",
            "size_km": 767
            },
            {
            "park_name": "Meru National Park",
            "size_km": 870
            }
        ]
    },
  "Ghana": {
        "capital: "Accra",
        "currency": "cedi",
        "parks": [
            {
            "park_name": "Mole National Park",
            "size_km": 4840
            },
            {
            "park_name": "Kakum National Park",
            "size_km": 375
            }
        ]
    },
}

# write a function that uses the data above to get a list of park names
def get_park_names(city_name):
    results = []
    # write your code here
    return results


print(get_park_names('Ghana'))
# when the program works it will show ['Aberdare National Park', 'Meru National Park']
```

### Weather forecast

Let's imagine that we are writing a program to display the weather forecast for a city. We'll be showing the estimated wind speed, temperature, and the percentage of cloud cover in the sky.

For the first version of our program, the user will type in a city name, and we will show them the estimated temperature for the next 3 days.

Just like how we talked about data structures on the previous page, we will use dictionaries to hold the data for a specific location,

```
forecast = [
{ "day" : 1,
"temperature": 23,
"wind_speed": 1.3 },
{ "day" : 2,
"temperature": 20,
"wind_speed": 0.2 },
{ "day" : 3,
"temperature": 21,
"wind_speed": 0.8 },
]
```

Our imagined program stores the location data with GPS latitude+longitude coordinates (if you haven't seen these before, like 2.1° North, 5.6° West, they are similar to x and y coordinates on a graph, but are coordinates for a globe). We'll do this to make the program realistic, because real weather data uses these coordinates.

So we'll have a dictionary containing lists of other dictionaries, which is often the best way to store the data. The full data structure looks like this,

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

def get_forecast_by_city(city_name):
    map_city_to_coords = {
        '': 
    }
```

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



<!--

add ghana which has the coordinates  
add current city load
add current city save

weather example

------------------------------- in progress -------------------------------

Warm up Read data from a provided simple json with weather data (just a list of numbers)
Read data from a provided realistic json with weather data (complex structure)

save as favorite

-->

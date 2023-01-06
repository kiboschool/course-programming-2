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

Tutorial 2: Saving the current city

(Shows how to read and write json files)




<!--
Tutorial video:
* run and try it. with city that matches. with city that does not match
* write a show_weather function that shows it better
def show_weather(weather_data_list):
    for weather_data in weather_data_list:
        day_number = weather_data['day']
        temperature = weather_data['temperature']
        wind_speed = weather_data['wind_speed']
        print(f'On day {day}:')
        print(f'temperature = {temperature}:')
        print(f'wind speed = {wind_speed}:')
        
        
* add accra to the list
5.63°N,0.39°W

video part 2

# We now have a working program that shows the weather.
# In a real-world version of the program,
# we would be reading the data from another place.


# Let's load the data from a file.
# We'll use the "json" format mentioned in Programming 1.
# json is a format to store dictionaries and lists into a file, 
# and when we read from the file,
# we'll get the dictionaries and lists back.


# First we'll change the program to read from a json file.

copy to all_forecasts.json
make all_forecasts have quotes

import json
with open('all_weather_data.json', 'r') as f:
    all_weather_data = json.load(f)
    all_forecasts = all_weather_data['all_forecasts']

# Check that the program still works

# We've now learned how to read the data from a json file.
# Now we'll learn how to write data to a json file.
# We'll add a feature to the program.
# We will store the current city so that the user doesn't have to type it in each time.

if 'current_city' not in all_weather_data:
    current_city = input('What is the current city where you want to see the weather?')
    all_weather_data['current_city'] = current_city
    with open('all_weather_data.json', 'w') as f:
        json.dump(all_weather_data, f)
else:
    current_city = all_weather_data['current_city']

# now, the next time we run the program, it will remember the city.

open json to see it there

# An exercise for you:
# At the end of the program, ask the user if they would like to change the current city.
# if they type yes, let them type in a city, and store that as the current city.


* 

* add saved

# add it to the xml
    # temporary, just for testing, we will delete later
add "saved_city": "Nairobi" to the top
add a print statement saying 
    saved_city = all_weather_data['all_weather_data']
    print(f'the saved city is {saved_city}')
    all_weather_data['saved_city'] = city_name
    with open('all_weather_data.json', 'w') as f:
        json.dump(all_weather_data, f)


def show_weather():
    with open('all_weather_data.json', 'r') as f:
        all_weather_data = json.load(f)
        
    saved_city = all_weather_data['saved_city']
    if city_name not in map_city_to_coords:
        print('We do not have coordinates for that city.')
    else:
        coords = map_city_to_coords[city_name]
        print(all_forecasts[coords])
    
    should_change_city_name = input('Change current city? yes/no')
    if should_change_city_name == 'yes':
        city_name = input('Please enter a city name:')
        if city_name not in map_city_to_coords:
            print('We do not have coordinates for that city.')
        else:
            all_weather_data['saved_city'] = city_name
            with open('all_weather_data.json', 'w') as f:
                json.dump(all_weather_data, f)

-->

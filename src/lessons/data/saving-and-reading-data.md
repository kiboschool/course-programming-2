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


Tutorial 1: Writing a program that shows the weather forecast

(Shows how to retrieve information from dictionaries)

<iframe width="560" height="315"  src="https://tempclip.com/embed/b5bqNF8jR1eCnzV" title="weather 1" frameborder="0" allowfullscreen></iframe>

Tutorial 2: Saving the current city

(Shows how to read and write json files)





```


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

copy to all_forecasts.json
import json
with open('all_weather_data.json', 'r') as f:
    all_weather_data = json.load(f)
    all_forecasts = all_weather_data['all_forecasts']

ensure it still works

add "saved_city": "Nairobi" to the top
add a print statement saying 
    # temporary, just for testing, we will delete later
    saved_city = all_weather_data['all_weather_data']
    print(f'the saved city is {saved_city}')



* 

* add saved

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

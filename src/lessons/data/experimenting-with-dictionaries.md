
### Experiment

You can experiment with dictionaries here. Try creating a for loop to show all of the currencies in country_data.

<iframe src="https://trinket.io/embed/python/67f058762c" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Solution

Here is a good way to show all of the currencies:

```python

def show_currencies():
    for country_name in all_country_data:
        # each time through the loop, we'll get a different country_name.
        country_data = all_country_data['country_name']
        print('Currency is')
        print(country_data['currency'])

show_currencies()

```


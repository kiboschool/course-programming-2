#Dictionary Refresher

We are familiar with dictionaries already, but let's refresh the basic syntax and learn some new tricks with them. 

First of all, what is the purpose of a `dictionary`? whereas a `list` collects entries that are related to each other. A `dictionary` is really about relationships: This is a mapping from _some_ data to _some_ other data. A dictionary consists of a set of _keys_ - the term _set_ here matters: Keys can't be repeated - and a variable that relates to each _key_

## Looping over dictionaries

Let's consider a simple example of a dictionary `capital_cities` where we keep track of countries and their capital cities. Our keys will be strings for the country name, and the value will be a string representing the capital city. 

We can identify the `keys` of the dictionary by using the `capital_cities.keys()` method. Note that looping over the dictionary's keys and looping over the dictionary itself are equivalent:

<iframe src="https://trinket.io/embed/python3/c5cbfa87b5" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

We can also access the values stored in a dictionary by using `capital_cities.values()`, which we can also loop through:

<iframe src="https://trinket.io/embed/python3/e0ea879a34" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

It's important to be able to access the keys and the values when needed, but really dictionaries are about relationships, so how can we show both the key and the value easily? 

We can always try to access the data in the dictionary since it's easy to find the keys, but there is also a handy shortcut:

<iframe src="https://trinket.io/embed/python3/7636042d8b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

the `capital_cities.items()` method returns a list of `tuples`. Each `tuple` contains a key and value pair, which we can unpack!

## Dictionary comprehension:
Similarly to lists and sets, we can use dictionary comprehension to quickly create dictionaries. Let's use that to "reverse" our `capital_cities` dictionary: We want the capitals to be the key now, and the country to be the city. We could do this via a loop, building up an empty dictionary in the process, but it's a lot faster and easier to read to use comprehension:

<iframe src="https://trinket.io/embed/python3/967340c043" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Note that dictionary comprehension looks similar to set comprehension, in both cases we use curly braces `{}` to indicate the collection we are building. The main difference is that in dictionary comprehension we will always care about two values and how they connect. We'd need to see a `:` character to represent the mapping. In the example above, we set the capital as the key because it is to the left of the `:`, and country becomes the value since it is to the right. 

We can process the data as well if need be. Say that in our application we want all names of countries and capitals to be lowercase:

```python
capitals = {'Morocco': 'Rabat', 'Senegal': 'Dakar', 'Nigeria': 'Abuja'}
lowercase_dict = {coutry.lower():capital.lower() for country,capital in capitals.items()}
print(lowercase_dict) # {'morocco': 'rabat', 'senegal': 'dakar', 'nigeria': 'abuja'}
```

We also don't have to start from a dictionary as the source of our data. We can start from lists or sets or anything else we can loop through:

```python
squares = {number:number*number for number in range(4, 12)}
print(squares) # {4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121}
```

Finally, we can also include if statements if need be. Take a moment and read through this example as it is a bit more complex: We have a large dictionary mapping countries to their capitals. We also have sets to indicate what country belongs to what continent. We want to use this information to create a dictionary of only African countries and capitals:

<iframe src="https://trinket.io/embed/python3/080f75fa65" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Avoiding Key Errors:
Similarly to lists who break when the index is larger or equal to the length of the list, dictionaries will also raise a `KeyError` when you try to access a key that does not exist. Consider this example:

<iframe src="https://trinket.io/embed/python3/5c3bb01972" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Take a few minutes and convince yourself that we can access the data in our dictionary. I also want you to intentionally break this code! how can you trigger an error? 

If we want to shield ourselves from such errors, we have a few options:

### Option 1: Check first, then index:
<iframe src="https://trinket.io/embed/python3/ce3570fd33" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In this example, we check if the user provided input is a key first, and only if it's a valid key do we use it to index.

### Option 2: Use the Get method:
<iframe src="https://trinket.io/embed/python3/639b2d9203" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

the `get` method is very convenient! It takes two parameters:
* The first parameter is the key you want to use.
* The second parameter is a default value. If we don't find the key, we will just return this default value. Note that this is an optional parameter, if you don't provide it, the method will return `None`

We will see a new, more generic way of handling errors, but for now let's keep going with our dictionary study.

## DefaultDict:
A similar issue we often run into involves dictionaries that connect a key to a collection. Consider the following dictionary:
```python
continent_to_countries = {'Africa': ['Ghana', 'South Africa', 'Ethiopia'], 'Asia': ['South Korea', 'Singapore', 'Mongolia']}
```

How would we add "Ivory Coast" to our dictionary? well we know we want to add it to the entry for 'Africa', so we'd need code that:
* Finds the list associated with the key 'Africa'
* Appends "Ivory Coast" to that list

```python
continent_to_countries['Africa'].append("Ivory Coast")
```

What about adding "Brazil" to our dictionary? Brazil is a country in South America, but We don't have "South America" as a key yet, so there is no list for us to append to yet. Could we perhaps use the `get` method we saw earlier to do this? let's try:

<iframe src="https://trinket.io/embed/python3/0e565f302e" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

We are not getting an error, but let's analyze this line:
```python
continent_to_countries.get('South America', []).append("Brazil")
```

We use the `get` method to look up the `String` "South America" in the dictionary's keys without triggering an error.
As we don't find it, we return the default value, an empty list.
We then append "Brazil" to that list, but we never put the list in the dictionary!!

We have to be more cautious: Let's look at a new example
<iframe src="https://trinket.io/embed/python3/e09ba5e641" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
Now we check first! if we can't find our new continent, then we create a new entry for it, with a new list, containing our new country input. 

This pattern is very common whenever you are dealing with a mapping from a value to a collection. So common in fact that we have a subclass of dictionaries that specializes in handling these kind of scenarios. It is called defaultdict: A dictionary that has a default value for its keys.
<iframe src="https://trinket.io/embed/python3/dff90aaa5f" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Counting
One of the most common use cases for dictionaries is counting. The keys represent some repeating data, and the value becomes the count of it. Let's look at an example: 
Say we are voting for a class representative. We receive a list of everyone's votes, and we would like to create a dictionary that tells us how many votes each candidates got. Let's think about a moment how we can approach this:

* We will need a dictionary mapping a person to a number indicating how many votes that person received.
* We can go trough our list of votes. For each name we see we can do one of two things:
** If it's the first time we see the name, add it to the dictionary with a value of 1
** If it's already in the dictionary, we can increase its value by 1.

Let's see it in action:

<iframe src="https://trinket.io/embed/python3/d6cdb1817e" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Now this is quite a bit of code. This is also such a common use case that we have a specialized type of dictionary just for this in our collections library: The Counter class. Let's see how easy it makes this whole process:

<iframe src="https://trinket.io/embed/python3/bc80e50552" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

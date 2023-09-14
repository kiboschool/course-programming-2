# List Refresher

Let's start with lists, the very first data structure we studied. We know we can instantiate a list like this:

```python
empty_list = []
list_of_numbers = [1,2,3]
```
We know we can add things to a list using append:
```python
empty_list.append("Hello") # empty_list is now ["Hello"]
list_of_numbers.append(1) # list_of_numbers is now [1,2,3,1]
```

## Indexing:
We know we can use indeces to access **and modify** data within a list. The index of the first element is 0

```python
list_of_numbers[3] = 4 #list_of_numbers is now [1,2,3,4]
```

We also know that we should be careful with this index, as it can not be equal or higher than the length of the list:

```python
empty_list[127] = "Would this work?" #This would trigger an IndexError
```

Interestingly though, indeces are allowed to be negative! That is absolutely not intuitive, but you'll wrap your head around it:

An index of -1 represents the final element of the list. This is convenient as it's easier to type `list[-1]` instead of `list[len(list)-1]`if you know you want to interact with the last element of the list.

Similarly, an index of -2 represents the element before last, -3 the element before that, etc. This is our first example of **Syntactic Sugar!**

So to summarize consider the example below:
```python

alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
## Indeces    0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6
#also valid: -7 , -6 , -5 , -4 , -3 , -2 , -1
```

## Manipulating Lists:
Sometimes we want to extract only some elements from a list. For example, let's build a function that takes a list, and returns a new list that contains all the same content as the input list, except the first and last element. 

Think about creating this function -which we will call _chop_ - for a few minutes before checking out the implementation below:

<iframe src="https://trinket.io/embed/python3/1ca6ef9e0c" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In our function here we use the `pop` method. (_we know it's a method because we see the pattern list.pop(), and we know that a list is an object._)
- `some_list.pop()` removes and returns the last element from a list
- `some_list.pop(i)` removes and returns the element at index `i` from the list, or raise an error if `i` is not a good index

Now in our example above, we didn't quite care for the value returned, we just needed to delete the first and last element from a copy of the input list. 

Let's pause for a moment: you may or may not know about the `pop` method, but what can we do with lists really? Remember that you have access to the [official python documentation!](https://docs.python.org/3/tutorial/datastructures.html#data-structures)

### Splicing
Now turns out, creating a list that is a smaller version of an existing list is such a common problem that python gives us some nice **syntactic sugar again**. Check out this new version of the chomp method:

<iframe src="https://trinket.io/embed/python3/48286f9b5f" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Now this syntax will look weird, but it really saves us some time. To take a sublist from a list you can follow this pattern:

```python
sublist = original_list[start_index:end_index]
```
Do note that the **start_index is included**, and that the **end_index is excluded**. 

There is even a third parameter that lets you do more interesting sublists:
<iframe src="https://trinket.io/embed/python3/e0747c1d81" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

As you can probably tell from the example, our third parameter lets us skip some elements. Generally, the rule is:

```python
sublist = original_list[start_index : end_index : step]

sublist = [original_list[start_index], original_list[start_index + step], original_list[start_index + 2*step], original_list[start_index + 3*step]....] 
# This will stop whenever we reach or exceed end_index
```

## List comprehension

Splicing is very handy, and a lot of problems can be quickly resolved using it, but we wouldn't have been able to use it to solve problems where we want to base our logic on something more complex than just _where_ the data is in the list. Sometimes we want to modify all the values in a copy of a list or filter the data. This is where **List Comprehension** comes into play. 

The idea with **List Comprehension**is that you can **describe** the values in the list, and let python process the list for you. Let's look at the most basic example: using list comprehension to copy a list

```python
celsius_temperatures = [12.5, 18.7, 20.9, 28.3]
copy_list = [ temperature for temperature in celsius_temperatures ]
```

`copy_list` is defined using list comprehension: The square brackets [] tell python we are making a list. The elements of the list are defined by an internal for loop: for each element in celsius_temperatures, put that element in copy_list. I named that element _temperature_ as that makes sense, but this would've worked the same if we said: `copy_list = [ temp for temp in celsius_temperatures ]` or `copy_list = [ element for element in celsius_temperatures ]` or any other name for the variable.

This syntactic sugar is not very sweet though, we could copy the list faster using the `deepcopy()` method we learned about in week 2. Things get more interesting when we get to **manipulate the data**. Instead of just copying the list, let's make a list of farenheit temperatures. The formula to convert is that `farenheit = celsius * (9/5) + 32`. We could build a loop to do this, but list comprehension is easier to read and implement. Take a look:

<iframe src="https://trinket.io/embed/python3/7b8209cf1e" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This brings us back to our initial challenge: Finding all the positive numbers that are multiples of 3, but not multiples of 4, and are less than 100. We can imagine a for loop that lets us create such a list. If we can put it in a for loop, we can ***probably*** put it in list comprehension format!

<iframe src="https://trinket.io/embed/python3/315f690f17" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The general pattern for list comprehension therefore is:

```python
list_comprehension = [ some expression with element for element in input_list if some conditions are true ]
```

The expression can be as simple as leaving the element as is, you can call functions with it as an input etc.
The if statement can be skipped if you do not need filtering. 

# An important aside: Comparing lists and objects. 

If you are **really** paying attention, then some of our last examples should leave you scratching your heads. In the last two examples we created two different lists, then compared them and found a result of `True`. 

Now if you recall week 2, we said that comparing objects means comparing their **references**. Regardless of the value of the object, if the references are pointing to two different objects in memory then they are different. Lists are objects, so how come we could compare two different lists and still get `True`? 

The answer lies deep. When we compare two objects, there is a specific method that gets called. The method is name `__eq__`. This is similar to how the `__str__` method gets called when we print an object. 

**By default**, `__eq__` compares the references of two objects to see if they are the same. Thanks to inheritance and what we know of object oriented programming, this is something we can override. Look at these two examples with the simple `Point` class we had made way back in week 1:

<iframe src="https://trinket.io/embed/python3/d1dc0aabdb" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In this first example, you can see that despite having similar instance variables, our two point objects are not seen as the same. Let's now override the `__eq__` method and see:

<iframe src="https://trinket.io/embed/python3/3c13b7f615" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

We get to define for ourselves if the objects are the same! 

You may be wondering: Well how can I tell what happens when I compare two objects if it's all based on whether or not `__eq__` is implemented? The only true answer to this question is to read the documentation! 
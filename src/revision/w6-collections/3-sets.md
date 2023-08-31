# Set definition

You should be very familiar with the idea behind sets from the mathematical thinking course. We will take this section to focus on how to bring all those concepts together in Python code. But first, a refresher: A `set` is a collection of unique elements. Similarly to `lists`, a `set` can grow to arbitrary sizes. 

`set` objects can be set up very similarly to `lists`, we just use curly braces `{}` instead of square brackets `[]`.

```python
vowels = {'a', 'e', 'i', 'o', 'u'}
```

We can also loop over sets using for loops:

```python
for vowel in vowels:
	print(vowel)
```

but we can't access an element using a specific index. vowels[0] returns an error

As we've just learned this week, we can also use set comprehension in a very similar way to list comprehension - simply swap the square brackets for curly braces. For example, here is a quick way to find all the unique characters in a word or sentence:

```python
unique_letters = {character for characters in 'anticonstitutionally' if character not in 'abc'}
```

We can add and remove individual elements as well, by using the `add()` and `remove()` methods:

```python
vowels.add('y')
print(vowels) # shows {'a', 'e', 'i', 'o', 'u', 'y'}

vowels.remove('y')
print(vowels) # shows {'a', 'e', 'i', 'o', 'u'}
``` 

Note that adding the same element a second and third time does nothing really: A Set only contains unique elements:
```python
vowels.add('y')
print(vowels) # shows {'a', 'e', 'i', 'o', 'u', 'y'}

vowels.add('y')
print(vowels) # still shows {'a', 'e', 'i', 'o', 'u', 'y'}
```

Removing an element that does not exist in the set will raise a `KeyError` - this is very similar to trying to use the wrong key in a dictionary!

```python
vowels.remove('x')
# Raises KeyError!
```

## Set operations

Let's get into set operations, as we have seen them in mathematical thinking! the provided set class would not be complete if it could not perform unions, substractions, and intersections! Let's look at an example that covers all three of these operations

<iframe src="https://trinket.io/embed/python3/1b09050f36" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

We also very commonly use sets to check if some data _belongs_ to the set or not. We use the `in` keyword for that test, as shown in this example:

<iframe src="https://trinket.io/embed/python3/43ab14767a" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Set to List and List to Set

Sometimes we have to work with functions and libraries that use data structures that are not ideal for what _we_ are trying to build. For example you may receive lists as an output of a function, then realize that what you really want to do is find the intersection of all those lists. Let's look at a scenario where we are forced to have lists as an input and output

<iframe src="https://trinket.io/embed/python3/73fdd5b993" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Life would be so much easier if we had sets instead of lists! Well life can be that easy: We can quickly convert between data structures using their constructors. Let's consider this example:

<iframe src="https://trinket.io/embed/python3/d2a21e339e" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

We get the exact same result, and we still stick to our constraint in terms of the input and output. Our code became more concise and clear: Turn the inputs into sets, take the intersection of the sets, turn that into a list!

This is possible thanks to the `list()` and `set()` methods, which take a different collection as an input, and convert it into a `list` and a `set` respectively. 

As you can imagine, there is also a `tuple()` method if you ever need to turn a list or set into a tuple, but that's a rarer usecase.

## What can we put in a Set?

Let's consider a simple example: Imagine we are writing software to help retail stores track their expenses. We build up a big list of data throughout the day, keeping track of items sold and how much they were sold for. We want to turn that list into a set.

<iframe src="https://trinket.io/embed/python3/e0355ab915" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Run the code above to see that everything runs as expected: We turned the list of tuples into a set of tuples, which means we no longer see two entries for `('T-shirt', 45)`

Now let's look at a slightly different example. Read through this code carefully, and before running it think of what changed in comparison with the previous example. Then run it and see what the output is:

<iframe src="https://trinket.io/embed/python3/a123d06568" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In the first example, we are building a set of tuples, and it works.

In the second example, we are building a set of lists, and it does not work. We get the error message `TypeError: unhashable type: 'list'`

Let's try to make sense of this situation. Here is what we know:
- Lists and Tuples are different. The main difference is that **tuples are immutable**
- We briefly spoke about hashing in the mathematical thinking course: It's a process to turn some data into a numerical value.

We will cover this in more depth in our data structure course, but for now the takeaway is that sets use hashes to be efficient at what they do. Hashing some data depends on its value, so we can't hash data that can always change! Imagine for a second that we could allow lists inside a set:

```python
test_set = {[1,1], [1,2], [1,3]} 

new_list = [1,4]
test_set.add(new_list)
```

So far so good right? we have 3 different lists within the set, then we add a new, fourth list that is different from them. Bear in mind though that in this scenario, we still have a **reference** to our new_list in the new_list variable. This means we can do the following:

```python
new_list[1] = 2 
# We have just made new_list equal to [1,2]
# This is one of the lists that are already in our set?
```

How should we handle this? does that mean that our set now has duplicate elements? if so then it's no longer a set!!

Should we raise an error instead, saying we can't change this list because it's in a set? That would be a lot of information to keep track off at all times!

This is a simplified explanation for why sets can only store data that is **immutable**. The same idea applies for the keys of a dictionary, which we will study in more depth in the next section.
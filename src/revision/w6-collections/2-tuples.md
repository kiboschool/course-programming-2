# Tuple definition
Tuples are an odd cousin of lists, but with a crucial difference: tuple objects are immutable! This means that once you create a Tuple, you can not change it, expand it, shrink it, replace items within it, etc. 

Why would we want a data structure like that? we will explore that later in the notes, but first let's get used to the basic Tuple syntax

## Tuples Syntax:
You can instantiate a tuple the same way you'd instantiate a list, except we use parentheses `()` instead of the list's square brackets `[]`:

```python
my_tuple = (1, 2, 3)
```

At this point we can access our data as with a list using indexing. Note that we are back to using square brackets now!

```python
print(my_tuple[0]) ### prints 1
```

Note however that we can't assign a new value to that index:
```python
my_tuple[0] = 7
### Raises a TypeError: 'tuple' object does not support item assignment
### In other words, you can't assign to a tuple after it's been instantiated.
```
There is also no `append` for tuples. The size of a tuple can not be changed once we create it. Our example tuple has three elements, and will always have the **same** three elements. 

We however can still use some other convenient functionality similar to lists:

We can loop over the elements of a tuple using `for` loops:

```python
for element in my_tuple:
	print(element) # prints 1, then 2, then 3
```

We can check for the length of a tuple using `len`:

```python
print(len(my_tuple))
```

And we can mix and match various types within the tuple:

```python
scorecard = ('Mathematics', 80, True, "Solid Effort!")
```

Now on this last point, we can do the same with a list. Python does not stop us from appending elements of any type in a list. The community however tends to _prefer_ to keep lists _of the same type_ as much as possible. If you find yourself needing a few elements of various types stored together in a variable, then a _tuple_ may come in handy. 

This is a matter of style, of preference, so don't hold on to it too strongly. That being said, let's dig into why tuples matter. 

## Unpacking

One of the most common use cases for using tuples is scenarios where you want to return more than one value from a function. For example, let's say we build a program for a quizz. We could have a function that provides us both a question and its answer, that way the rest of our program would both know what question to show a learner, as well as how to validate their answer.

A tuple is a good structure to use to return both data at once - An object may be overkill, while trying to use two different functions that each return one of the values would make our code messy.

```python
def get_question():
	# This is a simplified function. In practice it would read from a file, database, or make an API call.
	return ("What is the OOP principle by which we can connect classes together in a hierarchy?", "Inheritance")
```

We can use this in practice by indexing into the result:

```python
question = get_question()[0]
answer = get_question()[1]
```

This is a bit redundant however, as we make the call to our function twice. Better to save the result:

```python
result = get_question()
question = result[0]
answer = result[1]
```

This is a bit better, but it could be farther improved: We're writing a few lines for what should be a simple assignment, and we also have no context for what other data could be in the `result` variable. Is `result[2]` valid? who knows?

There is a handy feature of Python that helps a lot: Unpacking. This is valid syntax:

```python
question, answer = get_question()
```

You can assign a tuple of size two to two variables at once. By default, the first variable will get the entry at index 0, and the next variable the entry at index 1. 

Variable unpacking only works when the number of variables on the left side of the `=` sign is exactly equal to the length of the `collection` on the right, otherwise you will encounter an error. 

Note that this works with many `collections`: Lists, Tuples, Sets, etc. We mention it here as it is a very common pattern to see with tuples in particular.

## Why does immutability matter?

Our first motivation in covering tuples is making sure you can read as much python code as possible. Beyond that, let's think as to why we would ever want an immutable data structure? Why would we ever choose to lose the flexibility of a list? after all a list's value can keep changing! and the list can keep growing as long as we need it to!

These two observations are exactly why, in some specific cases, tuples end up being a better choice:

### Sometimes we don't need data structures to grow:

Think about what we discovered on week 3: Every variable, every piece of data we use takes some space in memory. 

With a `tuple` having a limited size, we know exactly how much space it will take in memory, and most importantly, **we know that will never change**. There is no work for us to do to manage this tuple after it's been created.

In contrast, a `List` can grow to any arbitrary size. This is useful, but bear this in mind in general: **if it's useful, you are paying for it somehow**: In practice, it means that it would take some work - we would have to execute some code - to grow our `List`: What's the element we are putting in? where in memory do we put it? do we even have space for that? 

This means that in specific scenarios where your code would:
- Need to keep track of a large amount of collections.
- Not care about modifying them.

You would get a much better performance using `tuples`, meaning your code would be likely to run faster, and use less memory.

Now at our stage of learning, we will not run into situations like that yet, but it's important to build up the intuition for it. This is also likely one of the reasons you'll see tuples used in code.

### Sometimes we don't want values to change:

If you want to communicate to a fellow engineer that some values are _critical_ for your code to works and therefore _should not be modified_, then it is good to use an immutable value. If they try to directly modify the collection you provided them the code would error out.

There is something very powerful about immutable data as well that we will explore in the next section.

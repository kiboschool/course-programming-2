# Organizing Data

This week, we will revisit some familiar data structures: Lists and Dictionaries, as well as introduce two other Data Structures: Sets and Tuples. 

Let's be clear about what a **Data Structure** is before we move forward:
- A data structure is a data **organizations**, **storage**, and **management** format that is usually chosen for efficient access to data.

When should we use a specific data structure over another? well it helps to really understand the problem at hand. You may have already built an intuition for when to use a list or a dictionary, so we will add a few additional tools to your belt with sets and tuples. 

Python provides many data structures for us to use, and we will learn in future courses how to build our own. This week we will revisit old known structures and introduce new ones. These are:

* [Lists](https://docs.python.org/3/tutorial/datastructures.html)
* [Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
* [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
* [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

This is also an important week to get used to the official python documentation. Each of the links above provides useful information about data structures, and was created by the community that creates and maintains Python!. The link above lists **all the methods of the classes**. As you think about tackling a specific challenge with a list or a set, you should get into the habit of consulting the documentation to see if there is a solution to that problem already, or at least something that would make your life easier.

We will also look at some advanced tips and tricks with lists and dictionary, so you get more effective at using them, and can read Python code written by others more reliably. 

For example, consider this problem: Create a list of all the multiples of 3 that are not also multiples of 4 and are less than 100

<iframe src="https://trinket.io/embed/python3/7d6b1b8d41" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Well what if I told you we could achieve the same result in one concise line of code? Try the following yourself:

```python
result = [ number for number in range(100) if number % 3 == 0 and number % 4 != 0 ]
```

This should yield the exact same result!

The above is an example of what we call **Syntactic Sugar** - a complicated phrase, but the main thing to remember about it is that it is sweet! examples of syntactic sugar in a language are **shortcuts**, ways to do a very common operation faster, with fewer lines of code. We will cover a lot of these features of Python this week, alongside new tricks for you to learn.


## Preview:
Here is what we will be exploring this week:
* How can we efficiently create lists and dictionary using comprehension syntax?
* How can we recognize what simple data structure is best for a given problem? 
* How can we use tuples, sets, counters, and default dictionaries in Python?

## Why does this matter?
Next term, we will have a whole class dedicated to data structures. Understanding what data structure to use to tackle the problem you are facing can save you a lot of time and headaches. Being aware of the basic data structures already provided by Python is key to your growth as a developer, and will allow us to tackle more complex problems over the next few weeks!
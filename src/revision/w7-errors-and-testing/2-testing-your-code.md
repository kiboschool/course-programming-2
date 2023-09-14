# Testing your code
We've written code and submitted many assignments over the last few months. Hopefully, this means you've spent quite a bit of time thinking through whether or not your code was correct, and testing it. In this section, we will try to formalize some thinking about how to effectively test our code.

## What to look out for:
First and foremost, testing really benefits from organizing your code in functions. If all the functions work correctly, it's likely that our program overall will work fine (but it's not guaranteed! testers are pessimistic by nature!)

Start by making sure your code is as organized as possible. Testing a function that has exactly one goal, returns one value, is much easier than testing functions that do multiple things. Once you have your code sorted into multiple functions, let's consider how we will test each one. 

Start with functions that do not call any of your other functions, then once they are tested and you trust that they work fine, start testing functions that combine them together. 

The same logic applies for methods if you are working on an OOP project. Let's focus on what to test:

### Confirm the obvious results:
Make sure that the function handles the ideal scenario. If you give it correct input, does it give you correct output? If we don't have this achieved then that should be our main focus: Making sure the function does its job.

For example consider:

```python

def reverse(input_list):
	### This function should return a new list that
	### reverses the content of the input list.
	### The first element of the output list is the last element of the input list, etc.
```

What's an example of a test to confirm that the obvious result is correct?

You'll probably want to set up a small list, say `[1,2,3]`, then pass it to the function. When you print the result, you want to see `[3,2,1]`

Does seeing that result make the function correct? well take a look at the following implementation:

```python
def reverse(input_list):
	return [3, 2, 1]
```

**Technically,** this function passes the test above, but is it correctly reversing? no! it always returns `[3, 2, 1]` no matter what. 

The lesson here is that you often want to test more than one scenario, so let's look into how we to find other scenarios

### Think about branches:
If your code includes multiple _branches_, you should have tests that you know will go through all of them. 

For example consider this function that determines 

```python
### Returns "beginner league" if the user's age is between 10 and 14, and if the user has an authorization from their parent
### Returns "junior league" if the user's age is between 15 and 18, regardless of autorization
### Returns "Not Allowed" in all other scenarios
def check_if_eligible_for_entry(age, has_authorization):
	if 10 <= age <= 14 and has_authorization:
		return "Beginner League"
	elif 15 <= age <= 18:
		return "Junior League"
	else:
		return "Not Allowed" 
```

We want to make sure to set up tests that explore each branch of the if statement above. Testing `check_if_eligible_for_entry(11, True)` should trigger the first return. 

Testing `check_if_eligible_for_entry(16, True)` and `check_if_eligible_for_entry(17, False)` should trigger the second return.

Testing with an age under 10, an age over 18, and with age between 10 and 14 without authorization, should all trigger the else statement. This fairly simple function already lead us to think about **5 different test cases** if we want to be thorough.

Think of it like playing hide and seek with potential bugs. If we are playing hide and seek in your house. You will want to check every room looking for me. If you just decide to never check the kitchen, you'd be making it a lot more likely to lose the game!

The same idea applies: We want to write tests that _visit_ as much of our code as possible. As many methods and functions, and as many branches as possible.

### Think about exceptions

Another way we just learned we can create a branch in the way our code runs is with `try` and `except` statements. This means that we should check what happens with input that does not trigger exceptions, as well as what happens with input that triggers them, because that's what gets us to **actually run the code we defined in `except`**

Similarly, if you build custom exceptions, you want to make sure that your program **raises** them in scenarios when they should be.

### Think about types

Take a moment and think about the _type_ of the inputs you provide to your function. What _type_ do you want your input to be? What happens if it is not? You hopefully already caught a lot of that in the previous section thinking about exceptions. 

More interestingly, think very hard about the _type_ you want to see...are there any broad categories of it? any weird exceptions?

When thinking about numbers for example, we have negatives and positives. Does it matter for your function? if so it's worth testing both! We have whole numbers and fractions, do they matter? Zero is a very special case, and would break division, does that matter?

Similarly for lists: What if the input list to our function is empty? do things stil work well?

## What is unit testing?

If you look at all the previous sections we covered, clearly we have a lot to think about! If we wanted to manually test our code each time we've worked on it for a while we would have to:
- document all our test cases somewhere.
- set up a test by running our program, or starting the console and importing a specific function to run it.
- do it over and over again going through all these scenarios
- document whenever a test fails or gives us incorrect output.
- this means we need to already know with 100% confidence what the output to each test should be given our changed code. 

I don't know about you but that seems like way too much work. We can get the benefits of thorough testing without all these headaches by setting up **Automated Unit Tests** for our project. We will explore the automation in the next section, but for now let's define Unit Tests:

A Unit Test is a function that checks if another function correctly performs a specific task. Unit tests are what we would use to explore all the concerns we've been reading about so far. Before we jump into it though, let's introduce some new `Python` syntax that will be helpful here:

```python
assert True

assert False
```

`assert` is a `Python` keyword that except a `Boolean` after it. If you assert a `True` statement, nothing happens!

However if you try to assert a `False` statement, an `exception` will be raised!

Optionally, you can provide a second parameter that contains a message that can be displayed when the assertion fails:

<iframe src="https://trinket.io/embed/python3/e8b875a451" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Now, how can we put what we learned together. Let's build some unit tests for the `check_if_eligible_for_entry` function

<iframe src="https://trinket.io/embed/python3/a5eefb89dc" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Take your time and read through each of the functions we created: Each one aims to test a specific scenario.

Now make a small change to the `check_if_eligible_for_entry` function: Imagine as we were working, we didn't notice a typo, and instead of typing 18 as the age limit we typed 189! 

Make the change and run your code, you should see an error.

This is the beauty of unit testing: This is not about making sure your code is correct **now**. This is about making sure your code is correct **forever**. As you keep working on the project, making small changes to functions as new problem pop up, it's easy to sometimes take a step back, and introduce a bug or lose some functionality that worked well before. 

Unit tests help your future self, and collaborators on your project, build confidence that **you will not go backwards!**, and this is very, very valuable in the business world.

Now you may be thinking that you are still far from that business world, and that is true. We still recommend you think carefully about unit tests, and put effort into writing tests for you code, as it is a great way to push yourself to really understand every function you work on. 

That being said, our example tests were a bit tedious to write, and that approach doesn't fit well into a project, so let's look at a better way to write Unit Tests!
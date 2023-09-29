# Be Lazy!

Coding is hard. We will all get better at it over time, and this week's topic will very much be about making ourselves more efficient in our coding. 

Since programming 1, we have looked at scenarios where we can save ourselves time and headaches by using good coding practices. For example, imagine some banking code that relies on knowing an interest rate ratio:

```python
new_balance = balance * 1.05
 
loan_interest_rate = 1.05 * 3

def is_legal_interest_rate(rate):
	return 0 < rate <= 1.05
```
If we wanted to update the rate from 1.05 to 1.07, we'd have to look all around our code for 1.05 and change it to the new value. And what if there was some calculation that used the number 1.05 but it had nothing to do with the interest rate? We save ourselves time and headaches by shifting the code to something like this:

```python
interest_rate = 1.05

new_balance = balance * interest_rate
 
loan_interest_rate = interest_rate * 3

def is_legal_interest_rate(rate):
	return 0 < rate <= interest_rate
```
That way we can update many aspects of our code by modifying a single variable.

The same advantages are achieved by using functions cleverly: compare this code snippet:

```python
# We compute the average of two numbers provided by the user
number_1 = ""
while not number_1.isnumeric():
	print("Please provide the first number")
	number_1 = input()

number_1 = int(number_1)

number_2 = ""
while not number_2.isnumeric():
	print("Please provide the second number")
	number_2 = input()

number_2 = int(number_2)

print((number_1 + number_2) / 2)
```
with this code snippet:

```python
# We compute the average of two numbers provided by the user
def keep_asking_until_number(message):
	result = ""
	while not result.isnumeric()
		print(message)
		result = input()
	return int(result)

number_1 = keep_asking_until_number("Please provide the first number")
number_2 = keep_asking_until_number("Please provide the second number")

print((number_1 + number_2) / 2)
```
The second example is much easier to maintain over time: we have a function we can modify, and suddenly many parts of our code get new functionality, instead of us trying to look for every loop we've created in our code to get a number from our user.

So good variable usage help us be effective with our data. Good functions help us be effective with our logic. 

Well. Classes are a nice combination of data and logic. How can we be efficient with using them? This week will focus on **Inheritance**, one of the most common strategies for being able to reuse classes effectively.

## Preview
Here is what we will be exploring this week:

* How can we think about modeling real world ideas into classes?
* How can we model related things without repeating our code by using inheritance?
* How do we customize our subclasses and override the behaviour of their parent classes?

## Why does this matter?
Being efficient with the code you are writing, minimizing repetition, is something all developers aspire to. OOP is a key feature of not only Python, but nearly all the other languages you will encounter in your studies and career. 

Learning to be efficient with OOP code, and using **Inheritance** smartly, will be key to your ability to write code, read code, and collaborate with other developers.
# How does our code remember?

Let's think about this code snippet:

```python
limit = 10
result = []
for i in range(limit):
	result.append(i)
```

What do you think it would produce? We will get a list of 10 elements, going from `0` to `9`. This should be similar to code you've seen a lot since you started with Kibo.

What happens if I change the limit to 100? We would go from `0` to `99`. What about a limit of 1000? We would go from `0` to `999`

How about a limit of 1 billion? how about 1 trillion? 1 quintillion?? Logically, we know what numbers should be there, but could our computers keep track of all of that? 

**I strongly recommed you do not try to run this loop with a large limit. it will crash your computer!**

Every variable our code keeps track of takes a tiny bit of space in memory. We need to store this data so we can use it later, manipulate it, return it as a result of a function call, and so many other things.

This week, we will introduce some high level concept of how Python handles memory, and see how it impacts our ability to code with objects. After all, an object could be _anything_. It could contain numbers and booleans and strings and other objects. How does Python manage all of that information?

## Preview
Here is what we will be exploring this week:

* How do objects differ from built-in types like Boolean or int in how they are stored?
* How can we look into our code more deeply, and understand exactly what Python is storing in memory at any point in time?
* How can we leverage object references, and what are some issues we should avoid?

## Why does this matter?

In the scope of our learning, we will rarely try to solve problems that risk us running out of memory. Nevertheless, it is important as a developer to understand that **while we have a lot of resources, they are still limited.** We will have other courses dedicated to these issues, but for now, we will focus on a few core and simple concepts.

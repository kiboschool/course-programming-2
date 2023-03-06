## Other forms of Abstraction

Abstraction is not only related to Object-Oriented Programming (OOP), it is also a concept in other programming paradigms such as functional programming and procedural programming.

In procedural programming, for example, abstraction is achieved through the use of functions and procedures, which encapsulate a group of instructions and provide a level of abstraction over them. Procedures allow programmers to write code that is easier to read, understand, and modify.

Take a look at the following example:

```python
def calculate_price(item, quantity):
    price = get_price(item)
    total_price = price * quantity
    return total_price
```

Read the above code carefully. Do you feel the abstraction?

We want to know the price of an item, so we call the `get_price` function. We don't need to know how the function works, we just need to know how to use it.
The code of the `get_price` function is hidden from us, and we don't need to know it. This is abstraction.

In the background, the `get_price` function might be using a database to get the price of the item, or it might be using a dictionary to get the price of the item. We don't need to know how it works, we just need to know how to use it.

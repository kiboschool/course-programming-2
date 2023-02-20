# Print Debugging

## Video: 5 Debugging Tips

> This video from CS Dojo walks through solving a particular bug in a Django server, and illustrates print debugging.

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.youtube.com/embed/K6WGRBhacq8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Print debugging

Print debugging involves adding `print` statements to show values as your program runs. It can help you find out

- what parts of your code run
- what functions are called in what order
- what the values of your variables are

These clues can frequently lead to understanding your bugs.

## Print debugging tips

**Print out meaningful strings**

If you print out the same string multiple times when debugging, it's hard to tell which `print` the string is coming from.

`print('inside Product.calculate_tax')` makes it clear which print statement it is.

**Print relevant variables**

It's often helpful to print out variables. You can print variables with their names:

```python
print("self.price", self.price)
print("tax_rate", tax_rate)
```

**Print function arguments**

It's often helpful to print the arguments a function is called with, right at the start of a function.

```python
def self.calculate_tax(self, tax_rate):
  print("inside Product.calculate_tax")
  print("tax_rate", tax_rate)
```

**Print all local vars**

You can access a dictionary of all the local variables by calling `locals()`.

```python
print(locals())
```

Sometimes this is more noise than is helpful, but it can be handy.

<!-- 
- dump object’s `__dict__`
- `repr` to see whitespace chars
- pretty-print
-->

**Clean up your prints afterwards**

After you are done debugging (or if earlier print statements are no longer in use), remember to clean up after yourself and remove them.

Sometimes, cluttered print output can make it harder to see the relevant information from other print statements.

## Logs and Error reports

In live applications, you can't necessarily add print statements. You aren't necessarily running the code on your machine! Print statements that you can't see won't help you debug.

It's common to have alternatives for monitoring and inspecting values for running applications. _Logs_ are a more sophisticated print statement. Instead of printing to the terminal, logs are written to a file and stored for later review. Sometimes, logs have additional structure, like information about what process was running, and when the log was written.

Log-based debugging is in many ways similar to print-debugging. You inspect the output, show more information if desired, and find out about the source of your bugs.

## When does print debugging fail?

Print debugging is very powerful, but there's also situations where it doesn't work as well.

- If you don't know what variable or value to look for
- If you need to run some code in order to explore the system
- If you aren't sure what step of the code isn't working as you expect
- If you have complicated or slow setup, and it takes a long time to get feedback from print statements

Next, you'll learn about debugging with an interactive "stop the world" debugger.

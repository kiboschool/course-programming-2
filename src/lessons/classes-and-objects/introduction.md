
# Introduction

In Programming 1, we had a week dedicated to learning about Organizing Code. We talked about splitting code into functions, adding comments, and using good variable names. This type of a change to a program is about more than writing code that functions correctly: it is a type of change that improves readability and organization. 

We also talked about modules in Programming 1, when we wrote `import` at the top of the Python file to use a module. For example, once we have written `import random` we can call `random.randint` and get a random number.

Imagine what it would be like if you didn't have any modules!

All your code would be in one long file. If you wanted to pick a random number, you would have to look up some code to generate a random number, read through it and make sure it works the way you expect, and then copy and paste it into your program. Then when you want to save data to json, you couldn't use `import json` and `json.dump`, you would again have to copy and paste a function into your program. When writing a program, your `.py` file would quickly become very long and disorganized.

Modules gather together related functions into one group, and then move that group of functions out into another file. Once that group of functions is in another file, your program is easier to read because it is shorter, and you don't have to constantly see and think about those other functions anymore. It is so much simpler to just use a module, by writing `random.randint`, rather than having randint in your program.

In this week, we will talk about another way to gather related code together into one place.


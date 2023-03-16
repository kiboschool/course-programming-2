
# Summary

Abstraction is a concept that allows us to hide unnecessary details from the user. It allows us to reduce complexity and isolate impact of changes.

You can achieve abstraction in your classes, functions, and modules.

In your code, you should try to use abstraction to reduce complexity and make your code easier to read, understand, and modify.

Here are a few tips to help you achieve abstraction in your code:

- The higher levels of your code should be concerned with *what* the program is doing, and not the details of *how* the program achieves the result. 
- Move the details (like are we writing to a json format or a csv format) to the lower levels of your code. It would usually be better to have a method called `save_to_file` instead of `save_to_json`, because the choice of json format is an implementation detail.
- This way, method names and parameters can stay similar even if the lower levels change. And, the code will be easier to read because you won't be distracted by details.


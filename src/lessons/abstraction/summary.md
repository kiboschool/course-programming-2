
# Summary

In your code, it's good to use abstraction to reduce complexity and make your code easier to read, understand, and modify.

A concise path towards having better abstraction in your code:

- The higher levels of your code should be concerned with *what* the program is doing, and not the details of *how* the program achieves the result. 
- Move the details (like are we writing to a json format or a csv format) to the lower levels of your code. For example, it would usually be better to have a method called `save_to_file` instead of `save_to_json`, because the choice of json format is an implementation detail.
- When your code is written this way, method names and parameters can remain the same, even if there are changes made to the lower levels. And, the code will be easier to read because you won't be distracted by details.


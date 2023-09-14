# Persistence

In our previous example, we deliberately saved our data at the end of the process. We can create an even smoother experience for our users in some cases. Instead of waiting for them to save, we auto-save their work for them as they do it. That way, if something were to go wrong and the program or the machine it's running on crashes, they won't use much work. 

We will approach this in a bit of an abstract way: Many programs use lists right? Let's create a new class, `PersistedList`, which works exactly like a `List`, but always saves its content to a file.

<a href="https://replit.com/team/kibo-programming-2/PersistedList-Inheritance-Demo" target="_blank">**Click here to follow along on Replit!**</a> _Please sign up for an account and request to join the team if you haven't already._

> Once you are in Replit, click `Shell` on the right, type in `python main_v1.py`, and press Enter to run one of the scripts.

> <img src="../../images/w3/replit2.png" width="80%" height="80%" />


```python
# main_v1.py

class PersistedList:
  def __init__(self, filename):
    self.filename = filename
    self.internal_list = []
    
    if os.path.exists(filename):
      with open(self.filename, 'r') as f:
        file_contents = f.read()
        if file_contents:
          self.internal_list = file_contents.split('\n')

  def append(self, incoming_string):
    self.internal_list.append(incoming_string)
    with open(self.filename, 'w') as f:
      new_file_contents = '\n'.join(self.internal_list)
      f.write(new_file_contents)
    
  def insert(self, position, incoming_string):
    self.internal_list.insert(position, incoming_string)
    with open(self.filename, 'w') as f:
      new_file_contents = '\n'.join(self.internal_list)
      f.write(new_file_contents)    
```

This code does work, but it's not as good as it could be.

Let's add some improvements. There is some repeated code. We can add a helper method to reduce the repetition.

We don't expect outside users of the class to need to call this `persist()` method. It's an internal method to help the other methods work.

```python
# main_v2_helper.py

class PersistedList:
  def __init__(self, filename):
    self.filename = filename
    self.internal_list = []
    
    if os.path.exists(filename):
      with open(self.filename, 'r') as f:
        file_contents = f.read()
        if file_contents:
          self.internal_list = file_contents.split('\n')
      
  def persist(self):
    with open(self.filename, 'w') as f:
      new_file_contents = '\n'.join(self.internal_list)
      f.write(new_file_contents)
    
  def append(self, incoming_string):
    self.internal_list.append(incoming_string)
    self.persist()
    
  def insert(self, position, incoming_string):
    self.internal_list.insert(position, incoming_string)
    self.persist()  
```

The program doesn't work, though, if one of the items has a newline (\n) character in it. We can make a new version of the persistedlist that saves to `json`, which is a good way of solving the problem. Imagine that we still need to keep the original PersistedList around though, because there are older parts of the program that still need to use that format.

> In professional software development, *backwards compatibility* is something to be aware of. If this is a program running on a customer's device, it can be hard to change the way data is stored on disk, even if it's not stored in the best way. This is because customers on their own devices will already have a lot of data stored in the old format.

So we only need to change the name of our existing class to make it a bit more clear what it does:
```python
# main_v3_two_classes.py

import os
import json

class PersistedListIntoLines:
  def __init__(self, filename):
    self.filename = filename
    self.internal_list = []
    
    if os.path.exists(filename):
      with open(self.filename, 'r') as f:
        file_contents = f.read()
        if file_contents:
          self.internal_list = file_contents.split('\n')
      
  def persist(self):
    with open(self.filename, 'w') as f:
      new_file_contents = '\n'.join(self.internal_list)
      f.write(new_file_contents)
    
  def append(self, incoming_string):
    self.internal_list.append(incoming_string)
    self.persist()
    
  def insert(self, position, incoming_string):
    self.internal_list.insert(position, incoming_string)
    self.persist()  
```

And we can create a new, very similar class to that can persist lists into Json
```python
class PersistedListIntoJson:
  def __init__(self, filename):
    self.filename = filename
    self.internal_list = []
    
    if os.path.exists(filename):
      with open(self.filename, 'r') as f:
        self.internal_list = json.load(f)
      
  def persist(self):
    with open(self.filename, 'w') as f:
      json.dump(self.internal_list, f)
    
  def append(self, incoming_string):
    self.internal_list.append(incoming_string)
    self.persist()
    
  def insert(self, position, incoming_string):
    self.internal_list.insert(position, incoming_string)
    self.persist()  
```

Our program is pretty long, now, and there's again repeated code. Our two classes are very similar, so perhaps we can leverage **inheritance?**

First we create a class that carries all the shared logic
```python
# main_v4_inheritance.py

import os
import json

class PersistedListGeneral:
  def append(self, incoming_string):
    self.internal_list.append(incoming_string)
    self.persist()
    
  def insert(self, position, incoming_string):
    self.internal_list.insert(position, incoming_string)
    self.persist()
```

Now we can inherit from it! The children classes only need to define the `persist` method
```python  
class PersistedListIntoLines(PersistedListGeneral):
  def __init__(self, filename):
    self.filename = filename
    self.internal_list = []
    
    if os.path.exists(filename):
      with open(self.filename, 'r') as f:
        file_contents = f.read()
        if file_contents:
          self.internal_list = file_contents.split('\n')
      
  def persist(self):
    with open(self.filename, 'w') as f:
      new_file_contents = '\n'.join(self.internal_list)
      f.write(new_file_contents)
  

class PersistedListIntoJson(PersistedListGeneral):
  def __init__(self, filename):
    self.filename = filename
    self.internal_list = []
    
    if os.path.exists(filename):
      with open(self.filename, 'r') as f:
        self.internal_list = json.load(f)
      
  def persist(self):
    with open(self.filename, 'w') as f:
      json.dump(self.internal_list, f)
```

Now, we no longer have the repeated code.

An instance of `PersistedListIntoLines` will still have the `append` and `insert` methods, because it has **inherited** those methods from the GenericPersistedList class.

An instance of `PersistedListIntoJson` will still have the `append` and `insert` methods, because it has **inherited** those methods from the GenericPersistedList class.Inheritance can be used for many purposes. It's often useful when there are two classes that have the same set of methods, but are in different modes and end up implementing the methods differently.

> ### Practice
> Open `main_v4_inheritance.py` in replit. (There is a link to replit at the top of this page).  
> * At the bottom of the file, create an instance of the `PersistedListIntoLines` class that saves into the file "fruit.txt"
> * Use the `append` method to add the string "apples" to the list
> * Use the `append` method to add the string "bananas" to the list
> * (Notice that the append method works even though `PersistedListIntoLines` does not have that method. This is because it is using the method from `PersistedListGeneral`).
> * Open "fruit.txt" and see the contents.

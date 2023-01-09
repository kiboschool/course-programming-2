# Ways to structure data

Let's look back to one of the final projects from Programming 1, 
the Student Enrollment Management project. 

Here were some of the project requirements:

```
Student Records

 - Must keep a list of the students
 - Student records include a student ID, a student name, and the
        courses they are enrolled in.
 - Must be able to Add or Remove students
 - Must be able to look up students and see their information as
        well as their course enrollments.
```

There are many ways to store this information.
* a group of different `list`s.
* a `dict` with student id keys, and `list` or `dict` values, with student information

When we talk whether it is a dictionary of dictionaries or a list of dictionaries, 
we're talking about the "shape" of the data, and which **data structures** we're
using.

<image src="../../images/w1/marble.png" height="25%" width="25%" style="border:none, border-width: 0, border: 0; box-shadow: 0px 0px;" />

This would be one way to structure the student records:

```python
student_ids = [35434, 67768, 17768, 45645]
student_names = ['Joshua', 'Michael', 'Jessica', 'Rapheal']
student_course_ids_enrolled = [[], [567567], [78979, 567567], []]
```

(The numbers here are just example IDs, this is just an example of what the data would look like.)

In this example, the lists in student_course_ids_enrolled are lists of the course ids the student is enrolled in. 

This structure does work to solve the problem. 

But, it isn't ideal for a few reasons:
- if a new student is added, a new element has to be added to all three lists
- if there is any place in the code that forgets to add an element to one of the lists, there will be errors
- It is the same for deleting a student: all three lists have to be updated.
- We have three different variables to keep track of, and to pass to different functions. 

---

Let's look at an improved way to structure the data.

```python
student_records = [
    ['Joshua', 35434, []],
    ['Michael', 67768, [567567]],
    ['Jessica', 17768, [78979, 567567]],
    ['Rapheal', 45645, []],
]
```

This is the same data as before, just structured differently.

What are the advantages?
- We are down to one variable, so there's only one thing to pass into each
    function
- When a student is added or deleted, there's no way to forget to update one of the lists.

Now, to get the name of the first student, the code is `student_records[0][0]`. 
To get the id, we would write `student_records[0][1]`. 

Accessing the values that way is hard to read and understand. It's hard to 
remember that `[0]` refers to the name and `[1]` refers to the id. 

We could add comments to help explain, but it's still not great.

---

A better data structure would be to use a list of dictionaries.

```python
student_records = [
    { 'name': 'Joshua', 'id': 35434, 'courses_enrolled_in': [] },
    { 'name': 'Michael', 'id': 67768, 'courses_enrolled_in': [567567] },
    { 'name': 'Jessica', 'id': 17768, 'courses_enrolled_in': [78979, 567567] },
    { 'name': 'Rapheal', 'id': 45645, 'courses_enrolled_in': [] },
]
```

Our code will now be much easier to read and write, because we can write access 
values like `student_records[0]["id"]` to refer to the id of the first student.

## Practice: Dictionaries

A dictionary can contains lists, and a list can contain dictionaries. 

As you saw in the example, this type of "nested" structure can be a great way to 
organize data for a given problem. 

Write a function that takes a country name, navigates the nested dictionary, and 
returns a list of park names.

<iframe src="https://trinket.io/embed/python/a99715e86f" width="100%" height="400" frameborder="0"  style="margin-top:1em" allowfullscreen></iframe>

Remember that if you use a for loop to iterate through the items in a dictionary, 
each time through the loop you will get one of the keys (in this case, a country 
name).

If you use a for loop on a list, each time through the loop you will get one 
element in the list (the element could be a string, dictionary, or another list).


### Solution

Here is a one way to get the list of park names:

<details><summary>See the Solution</summary>

```python
def get_park_names(country_name):
  ''' a function that uses the data above 
  to get a list of park names'''
  results = []
  
  if country_name not in all_country_data:
    print('Could not find this country')
  else:
    country_data = all_country_data[country_name]
    parks = country_data['parks']
    for park in parks:
      results.append(park['park_name'])
    
  return results

get_park_names()
```

</details>

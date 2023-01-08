
## Data structures

It is very useful for a list to contain dictionaries, or for a dictionary to contain other dictionaries. This is an important way to keep data organized.

Let's go back to one of the final projects from the Programming-1 course, the Student Enrollment Management project. We were asked to build a project that had a list of student data,

```
Student Records

 - Must keep a list of the students
 - Student records include a student ID, a student name, and the
        courses they are enrolled in.
 - Must be able to Add or Remove students
 - Must be able to look up students and see their information as
        well as their course enrollments.
```

There are many ways to store this information. There could be a group of different `list`s. There could be a `dict` from student id to a `list` or `dict` of student information. When we talk about the shape of the data, like whether it is a dictionary of dictionaries or a list of dictionaries, this is called talking about the data structure.

This would be one way to structure the student records:

```
student_ids = [35434, 67768, 17768, 45645]
student_names = ['Joshua', 'Michael', 'Jessica', 'Rapheal']
student_course_ids_enrolled = [[], [567567], [78979, 567567], []]
```

(In this example solution I came up with, all of the ids are fake numbers I came up with as an example, and the lists in student_course_ids_enrolled are lists of the course ids that student is enrolled in. Don't worry about the courses, right now we're just thinking about the students).

This structure does work to solve the problem. But it isn't ideal for a few reasons. First of all, if a new student is added, a new element has to be added to all three lists, and if there is any place in the code that forgets to add an element to one of the lists, this is a bug that will cause errors. It is the same for deleting a student - all three lists would have to be updated. We'd have three different variables to keep track of and pass around to the different functions. 

This data structure would be better in some ways,

```
student_records = [
    ['Joshua', 35434, []],
    ['Michael', 67768, [567567]],
    ['Jessica', 17768, [78979, 567567]],
    ['Rapheal', 45645, []],
]
```

(notice that this is the same data as before, just moved to a different structure).

The advantage is that we are down to one variable. And so when a student is added or deleted, there isn't a chance to forget to update one of the variables. But now, to get the name of the first student, we would write `student_records[0][0]` and to get the id we would write `student_records[0][1]`. This code is hard to read and understand because it's hard to remember that [0] refers to the name and [1] refers to the id. We could add comments to help explain, but it's still not great.

In general, a better data structure would be to use dictionaries,

```
student_records = [
    { 'name': 'Joshua', 'id': 35434, 'courses_enrolled_in': [] },
    { 'name': 'Michael', 'id': 67768, 'courses_enrolled_in': [567567] },
    { 'name': 'Jessica', 'id': 17768, 'courses_enrolled_in': [78979, 567567] },
    { 'name': 'Rapheal', 'id': 45645, 'courses_enrolled_in': [] },
]
```

Our code will now be much easier to read, because we can write code like `student_records[0]["id"]` to refer to the id of the first student in the list.

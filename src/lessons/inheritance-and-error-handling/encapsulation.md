# The Four OOP Pillars

Recall that object-oriented programming is a programming paradigm that is based on the concept of objects. The 4 pillars of OOP are: encapsulation, inheritance, abstraction, and polymorphism. In this lesson, we will learn about encapsulation and inheritance. But first, let's go over what these four pillars are.

**Encapsulation**: This refers to the practice of hiding the internal state and behavior of an object, and exposing only a public interface for interacting with it.

**Inheritance**: This allows one class to inherit the properties and methods of another, allowing for a hierarchical relationship between classes.

**Polymorphism**: Polymorphism means that different classes can respond to the same method call in different ways by overriding and overloading methods.

**Abstraction**: This is the process of making complicated systems easier to understand by breaking them up into smaller, more manageable parts. In OOP, this is often achieved through the use of abstract classes and interfaces.

This might be a lot to take in, but no worries! We will go over each of these pillars in detail in this lesson and the following ones.

## Encapsulation

Encapsulation is the process of bundling (encapsulating) data and behavior and protecting or hiding an object's elements from external access. Creating good classes is an example of encapsulating data and behavior together. We can also hide the internal state and behavior of an object, and expose only a public interface for interacting with it.

### Why would we want to prevent access to an object's attributes or methods?

One reason is that we want to prevent users from changing the state of an object in a way that is not intended. Let's say we have a variable that represents the number of students in a class. We don't want users to be able to change this variable to a negative number, or to a number that is not an integer. In code, this would look like this:

```python
class Class:
    def __init__(self, name, number_of_students):
        self.name = name
        self.number_of_students = number_of_students

    def get_name(self):
        return self.name

    def get_number_of_students(self):
        return self.number_of_students

    def set_number_of_students(self, number_of_students):
        if type(number_of_students) != int:
            raise TypeError("Number of students must be an integer")
        if number_of_students < 0:
            raise ValueError("Number of students must be positive")
        self.number_of_students = number_of_students
```

Unwanted changes to the number of students could be made like this:

```python
classK23 = Class("Class Oct23", 10)
classK23.number_of_students = -1
```

To prevent this, we can make the `number_of_students` attribute private, so that it can only be accessed through the `get_number_of_students` and `set_number_of_students` methods which also known as getters and setters or accessors and mutators.

## Encapsulation in Python

Python does not have a built-in way to make attributes private. The Python culture is to make developers responsible.This means that we should not rely on the language to prevent us from doing something that we shouldn't. Instead, develoeprs should use conventions to indicate that something is private, and then they should be responsible for not accessing it.

The most common convention to follow to indicate a member is private is to prefix it with an underscore or double underscores.

### Using a Single Underscore

```python
class Class:
    def __init__(self, name, number_of_students):
        self.name = name
        self._number_of_students = number_of_students

    def get_name(self):
        return self.name

    def get_number_of_students(self):
        return self._number_of_students

    def set_number_of_students(self, number_of_students):
        if type(number_of_students) != int:
            raise TypeError("Number of students must be an integer")
        if number_of_students < 0:
            raise ValueError("Number of students must be positive")
        self._number_of_students = number_of_students
```

The above code is the same as the previous example, except that the `number_of_students` attribute is prefixed with an underscore. This is a convention that is used to indicate that the attribute is private, and **should not** be accessed directly. However, it is still possible to access the attribute directly. Yes, it is not so useful, but it is a step.

Also members that start with a single underscore are not imported when using the `from module import *` syntax.

### Using a double underscore

```python
class Class:
    def __init__(self, name, number_of_students):
        self.name = name
        self.__number_of_students = number_of_students

    def get_name(self):
        return self.name

    def get_number_of_students(self):
        return self.__number_of_students

    def set_number_of_students(self, number_of_students):
        if type(number_of_students) != int:
            raise TypeError("Number of students must be an integer")
        if number_of_students < 0:
            raise ValueError("Number of students must be positive")
        self.__number_of_students = number_of_students
```

This way, the interpreter will raise an error if we try to access the attribute directly.

```python
classK23 = Class("Class Oct23", 10)
classK23.__set_number_of_students(-1) # Raises AttributeError: 'Class' object has no attribute '__set_number_of_students'

```

Little bit better, but still not perfect. The reason is that the attribute `__set_number_of_students` is still accessible through `Class.__set_number_of_students` . This is the best we can do in Python.

In other programming languages, we can use access modifiers to control access to private members. In Java, for example, the `private` keyword can be used like this:

```java
public class Class {
    private int number_of_students;

    public int getNumber_of_students() {
        return number_of_students;
    }

    public void setNumber_of_students(int number_of_students) {
        if (number_of_students < 0) {
            throw new IllegalArgumentException("Number of students must be positive");
        }
        this.number_of_students = number_of_students;
    }
}
```

## Hiding the implementation details

Another reason to hide the internal state and behavior of an object is to prevent users from relying on the implementation details of an object. For example, let's say we have a class that represents a list of students. We want to be able to add and remove students from the list. We also want to be able to get the number of students in the list. We don't want users to be able to access the list directly, because we might want to change the implementation of the list in the future. For example, we might want to change the list to a dictionary. If we allow users to access the list directly, they might start relying on the implementation details of the list, and we will have to change their code when we change the implementation. This is why we should hide the implementation details of an object.

A typical example in python that implements the above:

```python
class StudentList:
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student):
        self.__students.remove(student)

    def get_number_of_students(self):
        return len(self._students)
```

Users of the above code can access students list like this:

```python
student_list = StudentList()
student_list.add_student("John")
student_list.add_student("Mary")
student_list.remove_student("John")
print(student_list.get_number_of_students()) # Prints 1
```

and **not** like this:

```python
student_list = StudentList()
student_list.students.append("John")
student_list.students.append("Mary")
student_list.students.pop("John")
```

In the second example, the user is relying on the implementation details of the `StudentList` class `student_list.students.append`. If we change the implementation of the `StudentList` class to use a `dict` instead of a `list`, users will have to change their code. That describes really bad code and program design.

## What Should We Do?

There is a debate in the software market about whether or not we should make all members of a class private and use accessors and mutators. The answer is that it depends on the situation and the culture of the language we use.

In Python, we are going to follow the common culture of the language by keeping the members' default to public and only changing when needed.

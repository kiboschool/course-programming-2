
# Abstract Methods And Classes

We'll continue with the Game Saver example from the previous page.

In this page, we'll describe what an abstract method is, and what an abstract class is.

### Abstract methods

In the latest version of the Game Saver example, this is what the parent class looks like:

```python
class GameSaver:
    def save(self, data):
        raise NotImplementedError
        
    def load(self):
        raise NotImplementedError
```

The methods do not have any code, all they do is raise a NotImplementedError because they are just depictions of the interface.

These methods only exist to say that child classes should have a method that looks like this. This is called an **abstract method**, because the implementation details have been moved away to a lower level.

### An abstract class

A class with one or more abstract methods is called an **abstract class**. A child class that implements the empty abstract methods is called an **implementation class**.



In a sense, an abstract class is not "ready to use" yet, because part of the functionality is missing. Only child classes that fill in the missing functionality are ready to use. 

> 💡 If someone using the code tried to make an instance of GameSaver, it wouldn't be very useful because the methods do nothing but raise an error!


So this is a big reason why we care about which classes are abstract classes versus which classes are implementations. We shouldn't make an instance of abstract classes - we instead need to instantiate the implementation classes, where all of the methods work.

<details><summary>Optional: Marking a class as abstract</summary>

Python has a way to mark a class as abstract. This shows people that you should not make an instance of it.


(This isn't used in Python as often as it is in other languages, though. In other languages it's more useful because your program stops right away if you've accidentally created an instance of a abstract class anywhere instead of a child class).

<b>Python syntax for abstract classes</b>

```python
from abc import ABC, abstractmethod

class GameSaver(ABC):
    @abstractmethod
    def save(self, data):
        pass
        
    @abstractmethod
    def load(self):
        pass
```

(The ABC stands for Abstract Base Class).

</details>

<details><summary>Optional: Terminology</summary>

Because object-oriented programming has been around for so many years, there are many different terms. You might come across these terms as you read about object-oriented programming:

* A base class means essentially the same thing as a parent class.
* A concrete class means essentially the same thing as an implementation class (that is to say, a child class of a parent class that has some abstract methods).  
* (Remember that an abstract method is an empty placeholder method). People sometimes use the term interface to refer to a class where all methods are abstract methods. You could say that an interface is a completely-abstract abstract class.


</details>


<details><summary>Optional: Another example</summary>

Here is another example of an abstract class in Python:

```python
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, query_string):
        pass

class MySQLDatabaseConnection(DatabaseConnection):
    def connect(self):
        # Code to connect to a MySQL database
        ...

    def query(self, query_string):
        # Code to execute a query on a MySQL database
        ...

class MongoDBDatabaseConnection(DatabaseConnection):
    def connect(self):
        # Code to connect to a MongoDB database
        ...

    def query(self, query_string):
        # Code to execute a query on a MongoDB database
        ...
```

DatabaseConnection is an abstract class that defines two abstract methods: connect and query. Any implementation  child class of DatabaseConnection must implement them.

MySQLDatabaseConnection and MongoDBDatabaseConnection are **implementation** child classes of DatabaseConnection that implement the connect and query methods. Each implementation has different code according to their specific database systems. By inheriting from DatabaseConnection, they **must** implement these methods or they will not be compatible with the abstract DatabaseConnection class.

Example code that uses the DatabaseConnection class:

```python
def connect_and_run_query(database, query_string):
    database.connect()
    result = database.query(query_string)
    return result
```


The function is able to connect to and run queries on any databases without actually knowing how the database works or what type of database it is. It just needs to know that the database has a connect method and a query method (which are defined by the DatabaseConnection abstract class).


</details>



<!--
## Interfaces

Interfaces are another way to achieve abstraction in OOP. An interface is a contract that defines the behavior of a class. It is a collection of abstract methods. A class implements an interface by providing the implementation of all the abstract methods defined in the interface. You can think of an interface as a 100% abstract class. That means an interface contains only abstract methods and no concrete methods (methods with implementation).

In some programming languages, interfaces are declared using the `interface` keyword. In Python, interfaces are defined the same way as abstract classes. They are declared using the `ABC` module.

Here is an example of an interface in Python:

```python
from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass

    @abstractmethod
    def deserialize(self, serialized_data):
        pass
```

As you can see, the Serializer interface looks like an abstract class. The only difference there is that it does not contain any concrete methods. It only contains abstract methods.
-->


### Ending notes

<blockquote>
<b>Optional exercise:</b>

We touched on similar concepts when we discussed inheritence and the PersistedList classes [here](/lessons/inheritance-and-error-handling/inheritance.html). We gave the PersistedListIntoLines and PersistedListIntoJson classes the same interface. The benefit is that code that saves lists can be flexible, it can just save the list without needing to know which of the classes it is using.)

Write an abstract base class depicting the interface for `PersistedListIntoJson`.

(Hint: in this class, all of the methods will just raise an NotImplementedError).
</blockquote>


Abstraction is one of the core concepts in object-oriented programming (OOP). It is the process of simplifying complex real-world entities into their essential characteristics or features while hiding their unnecessary details from the users. In other words, it focuses on what an object does rather than how it does it.

If this confuses you with encapsulation, don't worry. A good encapsulation is a good abstraction too. In encapsulation, when we make the implementation details of an object less accessible from the outside, that is related to hiding details. So, good encapsulation is good abstraction too.

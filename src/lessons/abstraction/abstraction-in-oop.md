# Abstraction in OOP

Abstraction is one of the core concepts in object-oriented programming (OOP). It is the process of simplifying complex real-world entities into their essential characteristics or features while hiding their unnecessary details from the users. In other words, it focuses on what an object does rather than how it does it.

If this confuses you with encapsulation, don't worry. A good encapsulation is a good abstraction too. In encapsulation, when we hide the implementation details of an object, that's hiding unnecessary details from the users. So, good encapsulation is good abstraction too.

## Abstract Classes

An abstract class is a class that contains one or more abstract methods. An abstract method is a method that is declared but contains **no implementation**. Abstract classes cannot be instantiated, and their abstract methods must be implemented by their subclasses.
Here is an example of an abstract class in Python:

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, query_string):
        pass

class MySQLDatabase(Database):
    def connect(self):
        # Code to connect to a MySQL database
        pass

    def query(self, query_string):
        # Code to execute a query on a MySQL database
        pass

class MongoDBDatabase(Database):
    def connect(self):
        # Code to connect to a MongoDB database
        pass

    def query(self, query_string):
        # Code to execute a query on a MongoDB database
        pass
```

In this example, Database is an abstract class that defines two abstract methods: connect and query. These methods do not have any implementation in the abstract class, but their presence **ensures that any concrete subclass of Database must implement them**.

MySQLDatabase and MongoDBDatabase are **concrete** subclasses of Database that implement the connect and query methods according to their specific database systems. By inheriting from Database, they **must** implement these methods, making them compatible with the abstract Database class.

Now here is a client code that uses the Database class:

```python
    class Client:
    def __init__(self, database):
        self.database = database

    def run_query(self, query_string):
        self.database.connect()
        result = self.database.query(query_string)
        self.database.disconnect()
        return result
```

## Abstraction in the Client Class

The above class is able to connect to and run queries on any databases without actually knowing how the database works or what type of database it is. It just needs to know that the database has a connect method and a query method (which are defined by the Database abstract class). This is abstraction achieved by using abstract classes.

Here is how different people can use the Client class on different databases:

```python
    # sample usage with mysql database
    mysql_database = MySQLDatabase()
    client1 = Client(mysql_database)
    result1 = client1.run_query("SELECT * FROM customers")

    # sample usage with mysql database
    mongodb_database = MongoDBDatabase()
    client2 = Client(mongodb_database)
    result2 = client2.run_query("db.customers.find()")

    print(result1)
    print(result2)
```

The `Database` class code uses the ABC module to define an abstract class. ABC stands for Abstract Base Class. It also provides the `@abstractmethod` decorator to define abstract methods. The `@abstractmethod decorator` is used to mark a method as abstract. An abstract method is a method that is declared, but contains **no implementation**. Abstract classes can not be instantiated, and their abstract methods must be implemented by their subclasses.

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

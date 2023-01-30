# Inheritance

## Review: Inheritance

Try to guess what each toggle will say underneath before reading the answer.

<details><summary>Inheritance allows you to </summary>

reuse the code from one class in another class

</details>

<details><summary>The syntax for inheriting from a class is</summary>

You put the parent class in parentheses when you define the class.

like this: 

```python
class SQLiteDatabase(Database):
  # SQLiteDatabase inherits all the behaviors of Database
```
</details>

<details><summary>If you define a method on a child class with the same name as a method on the parent class, that's called </summary>

overriding

It's one of the main ways that you can customize and extend the behavior of a parent in a child class.
</details>

<details><summary>To create a class variable, you </summary>

add a variable at the top level of the class, like
```python
class SQLiteDatabase(Database):
  max_connections = 1 
```
</details>

<details><summary>To call a parent class method from a child class method, you use the keyword </summary>

`super`. It effectively gives you access to the parent class's methods.

here's an example:

```python
class SQLiteDatabase(Database):
  def connect(self, connection_string):
    if len(self.connections) < self.max_connections:
      return super().connect(connection_string)
    else:
      raise DatabaseConnectionError("Max connections exceeded.")
```

Instead of rebuilding the `connect` method, this code reuses the parent class's implementation, but also does additional logic.
</details>

<details><summary>What does it look like to call the `super` function in the initializer?</summary>

Initializing in a child class means passing through any args for the parent class as well as performing any specific initialization for the child class.

```python
class SQLiteDatabase(Database):
  def __init__(self, options):
    self.connections = []
    super().__init__(options)
```
</details>

<details><summary>To check if an object is an instance of a class, you can use the function</summary>

`isinstance`

```python
isinstance(db, SQLiteDatabase)
isinstance(db, Database)
```

It returns True if the object is an instance of the class, or if the class is an ancestor of its class.
</details>

## Bonus: Inheritance vs. Composition

One aspect of Object-oriented design is deciding when to use Inheritance to share functionality, and when to use some other strategy.

This video on [Inheritance vs. Composition](https://www.youtube.com/watch?v=hxGOiiR9ZKg) sums up the choice well.

# Error handling

## Review: Error handling

Try to guess what each toggle will say underneath before reading the answer.

<details><summary>This kind of error is raised when Python does not recognize a keyword</summary>

`SyntaxError`
</details>

<details><summary>To handle errors in a Python program, we use a __________ statement.</summary>

`try`/ `except`
</details>

<details><summary>This kind of block always runs, even if there is an error.</summary>

`finally`
</details>


<details><summary>To catch specific errors, you can</summary>

specify the type of error when you write an `except`:

```python
try:
  100 / int(input("number: "))
except ZeroDivisionError:
  print("you have to enter a non-zero number.")
```

</details>


<details><summary>To create an error explicitly, you can use the keyword</summary>

`raise`

```python
x = input("enter a number: ")

if not x.isnumeric():
  raise TypeError("Only numbers are allowed")
```
</details>

<details><summary>You can define a custom error class by </summary>

defining a class that inherits from `Exception` or another error class,

```python
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
```

</details>

<details><summary>You can raise an error if a particular condition is not met using the keyword</summary>

`assert`

```python
def check_age(age):
  assert age > 18
```
</details>

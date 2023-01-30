# Class syntax

## Review: Defining a class

Try to guess what each toggle will say underneath before reading the answer.

<details><summary>A class is a</summary>

  blueprint or template for an object. 
</details>

<details><summary>You define a class using the keyword</summary>

`class`

like this: 

```python
class Request:
  # ... the rest of the definition indented here
```
</details>

<details><summary>Functions associated with an object are called </summary>

methods
</details>

<details><summary>In a class definition, the first argument to a method is usually named </summary>

`self`. It represents the current instance.
</details>

<details><summary>The way you store data on an instance is</summary>

to use the `self` keyword in a method, like

```python
class Request:
  def set_url(self, url):
    self.url = url
```
</details>

<details><summary>The method that is called when you create an instance is</summary>

The `__init__` method.

```python
class Request:
  def __init__(self, url):
    self.url = url
```
</details>

<details><summary>To create an instance of the `Request` class with an 'example.com' url, you'd write:</summary>

```python
request = Request("https://example.com")
```
</details>

<details><summary>To define a method on the Request class that sets the response, you would write</summary>

```python
class Request:
  # ... other Request methods
  def set_response(self, response):
    self.response = response
```
</details>

<details><summary>To use the `set_response` method on an instance of Request, you would write</summary>

```python
request = Request("https://example.com")
request.set_response("HTTP/1.1 200 OK")
```
</details>

Did you get all of the answers right? If not, it's worth going back and practicing defining classes.

# Inheritance Syntax:

Let's make some tweaks to our class to make it a bit more generic: We now have a `Vehicle` class that looks very similar to our `Car` class.

<iframe src="https://trinket.io/embed/python3/143dd811fa" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In our `__init__` method, we've added a `capacity` parameter, that way a vehicle object can keep track of how many max passengers they can have. 

This means that we can create `Vehicles` that have a capacity of 3 passengers, or 1, or 6, or 20! They will all use the same logic. 

How about the types of `vehicles` we have? Cars and BigCars and MotorBikes? It seems like we could just add another attribute to the `Vehicle` class to track that, something like:

```python
class Vehicle:
	def __init__(self, license, capacity, vehicle_type):
		self.license = license
		self.capacity = capacity
		self.available = True
		self.passengers = []
		self.vehicle_type = vehicle_type
```

But what happens if we want to add functionality to some types of vehicles, but not others? Say for example that we let our users order food in our apps. We're happy to let cars and bikes deliver that order, but we don't want to use bigcars for that. 

```python

def order(self):
	if self.vehicle_type == 'car' or self.vehicle_type == 'bike':
		# place the order
	else:
		# ignore the order
```

With every new functionality though, we'd have to ask ourselves: Does this apply to all the vehicle types we support? which ones allow it, which ones don't?

Things can get even more annoying if we introduce a new type of vehicle. Imagine if we also want to support `Bikes`. We'd have to go through all our methods and see if a `Bike` should or shouldn't be able to perform that action. 

There has to be a better way! and there is. Let's talk about **Inheritance**

## Inheritance 

Inheritance is one of the pillars of Object-Oriented Programming. It enables us to create a new class that already has all the data and functionality of another class. In this case, we may want to create a `Car` class that inherits from the `Vehicle` class. 

<iframe src="https://trinket.io/embed/python3/1d02118902" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

We leave our `Vehicle` class unchanged, but we create two new classes: `Car` and `MotorBike`.

You will notice that those class definitions are very light: No `__init__`, only an `__str__` method we added to help us demonstrate differences between the various classes. 

Here we say that `Car` is a **subclass** of `Vehicle`. We can also say that `Car` is a children class of `Vehicle`, or that `Car` extends `Vehicle`

Similarly, we say that `Vehicle` is a parent class to `Car`.

As you can tell however, the two objects we create for our new classes are able to add passengers and drop them off. That is because a `Car` object **is a `Vehicle` object**, and can do everything a `Vehicle` can. 

This is very helpful! if we make a change to the `Vehicle` class, all its subclasses will be able to benefit, while we also keep our ability to customize each subclass.

Let's focus on the syntax once again:

```python
def my_subclass(ParentClass):
	# define custom code for the subclass

	# All methods of your parent are by default methods of the subclass
```

Let's look into this code in Python Tutor to get a sense for what's going on in-memory. To simplify our analysis, we only look at `Vehicle` and `Car`:

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=class%20Vehicle%3A%0A%20%20%20%20def%20__init__%28self,%20license,%20capacity%29%3A%0A%20%20%20%20%20%20%20%20self.license%20%3D%20license%0A%20%20%20%20%20%20%20%20self.capacity%20%3D%20capacity%0A%20%20%20%20%20%20%20%20self.available%20%3D%20True%0A%20%20%20%20%20%20%20%20self.passengers%20%3D%20%5B%5D%0A%0A%20%20%20%20%23%20Passenger%20is%20requesting%20a%20ride%0A%20%20%20%20%23%20Return%20true%20if%20the%20car%20is%20available,%20and%20add%20them%20to%20the%20passenger's%20list%0A%20%20%20%20%23%20Return%20false%20if%20the%20car%20is%20not%20available%0A%20%20%20%20def%20request%28self,%20passenger%29%3A%0A%20%20%20%20%20%20%20%20if%20self.available%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.add_passenger%28passenger%29%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20else%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%0A%20%20%20%20%23%20We%20have%20a%20passenger%20that%20successfuly%20joined%20the%20car.%20We%20add%20them%20to%20the%20list%0A%20%20%20%20%23%20If%20that%20means%20we%20got%203%20passengers,%20then%20we%20are%20no%20longer%20available%20to%20add%20new%20passengers%0A%20%20%20%20%23%20so%20we%20set%20self.available%20to%20be%20False%0A%20%20%20%20def%20add_passenger%28self,%20passenger%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22Picking%20up%20%20%7Bpassenger%7D%22%29%0A%20%20%20%20%20%20%20%20self.passengers.append%28passenger%29%0A%20%20%20%20%20%20%20%20if%20len%28self.passengers%29%20%3D%3D%20self.capacity%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.available%20%3D%20False%0A%0A%20%20%20%20%23%20To%20simplify,%20we'll%20say%20that%20passengers%20are%20always%20first%20come%20first%20serve,%20so%20the%20first%20passenger%20we%20added%0A%20%20%20%20%23%20Will%20be%20the%20first%20passenger%20we%20drop%20off%0A%20%20%20%20def%20drop_off_passenger%28self%29%3A%0A%20%20%20%20%20%20%20%20if%20len%28self.passengers%29%20%3E%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20passenger%20%3D%20self.passengers.pop%280%29%20%23%20remove%20the%20first%20entry%20in%20the%20list,%20shrinking%20the%20list%20in%20the%20process%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22Dropping%20off%20%7Bpassenger%7D%22%29%0A%0A%0Aclass%20Car%28Vehicle%29%3A%0A%20%20def%20__str__%28self%29%3A%0A%20%20%20%20return%20f'Car%20license%3A%20%7Bself.license%7D'%0A%0Atest_car%20%3D%20Car%28%22A11%22,%203%29%0Aprint%28test_car%29%0A%0Atest_car.request%28%22Fatima%22%29%0Atest_car.drop_off_passenger%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=2&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

After Step 1 and Step 2, we see 2 classes defined in our global frame. Note how it's clear to Python that the `Car` class *extends* the `Vehicle` class.

In Step 3, as we create a new `Car` object, you can see that we call the `__init__` method of the `Vehicle` class. This makes sense because we did not define a specific `__init__` for `Car`, and a `Car` **is** a `Vehicle` so we can rely on that constructor.

In Step 10, we want to print our object. Step 11 takes us to the `__str__` method we defined for `Car`. If we hadn't defined this method, we would look for the `__str__` method of the parent class, etc.

In Step 14, we want to use the `request` method. In Step 15 we see the code jump into the `Vehicle` class' method definitions and executing the code there!

## Conclusion:
We can use inheritance to save ourselves from repeating a lot of similar code.

Inheritance is ideal in scenarios where we have many related models to implement, particularly if `model_A` is a kind of `model_B`. We can define `model_B`, and have `model_A` inherit methods and data from it.

We can customize our subclasses with their own methods, and we can also call methods from their parent classes. This also applies for grandparent classes, or great-grandparent classes! you can keep this going as much as needed.
 
What happens in scenarios where we don't want to inherit _everything_ the parent class has to offer? Let's find out in the next section.

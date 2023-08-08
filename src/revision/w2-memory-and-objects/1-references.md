## Memory and boxes

Let's consider a simple scenario. We have two variables, and we want to swap their values. 

For example:

<iframe src="https://trinket.io/embed/python3/6b2199aa4a" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Give it a try for a few minutes before continuing with the notes.

If you tried a direct assignment, like 
```python3
current_player = next_player
```
then it will be challenging to achieve our goal, as we have lost information. At this point in time, `current_player` was *assigned* the valu of `next_player`. They are both "Dipo", and we lost the information about who the `current_player` was.

Let's look at the solution using a new tool, Python Tutor. This tool lets us watch our code's execution step by step, and lets us see what's happening in our memory as the code runs. Click the **Next** button to go through your code line by line

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=current_player%20%3D%20%22Tomi%22%0Anext_player%20%3D%20%22Dipo%22%0A%0A%23%20Save%20the%20value%20of%20current%20player%20in%20a%20new%20variable%0A%23%20i.e%20a%20new%20location%20in%20memory%0Atemp%20%3D%20current_player%0A%0A%23%20Now%20we%20can%20safely%20overwrite%20the%20value%20of%20current_player%0Acurrent_player%20%3D%20next_player%0A%0A%23%20Then%20we%20use%20the%20variable%20we%20stored%20to%20update%20next_player%20as%20well%0Anext_player%20%3D%20temp%0A%0Aprint%28current_player%29%0Aprint%28next_player%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

We can see after executing the first 3 steps that we have 3 different variables - effectively 3 different places in memory that hold some information. 

We store the information for who the `current_player` is in the `temp` variable. The two variables have the same **value**: If we were to ask Python if the two variables were equal the answer would be `True`

But the two variables are two separate boxes. They represent two different places in our computer's memory, they just happen to have the same data in them.

We can then carry on copying the data around and get to our objective. 

## Primitives vs Objects
Let's look at another example. Here we have two variables that are meant to track two different concepts (My birthday is the 11th of the month, and I have 11 players on my football team) but they just happen to have the same value. Let's see what happens when we modify one:

<iframe width="1200" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=number_of_players%20%3D%2011%0Abirthday%20%3D%20number_of_players%0A%0Aprint%28number_of_players%29%0Aprint%28birthday%29%0A%0Anumber_of_players%20-%3D%201%0A%0A%23%20This%20should%20change%0Aprint%28number_of_players%29%0A%0A%23%20This%20should%20not%0Aprint%28birthday%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Step through the code step by step: Notice here that as we modify one of the variables, the other one remains unchanged. This might feel very obvious, and I agree! you'd hope that modifying one variable wouldn't have side effects on other variables. 

We do have to be careful though, let's look at another example.

This examples is very similar: We have two variables that serve different purposes - in this case I have one list for the people I want to invite to my birthday party, and another list for the people who play on my team - but they share the same value.

Step through the code and observe what happens as we modify one of these variables:

<iframe width="1200" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=players_on_the_team%20%3D%20%5B%22Eddie%22,%20%22JJ%22,%20%22Omar%22%5D%0Aparty_guests%20%3D%20players_on_the_team%0A%0Aprint%28players_on_the_team%29%0Aprint%28party_guests%29%0A%0Aplayers_on_the_team.append%28%22Messi%22%29%0A%0A%23%20This%20should%20change%0Aprint%28players_on_the_team%29%0A%0A%23%20should%20this%20change%3F%0Aprint%28party_guests%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Notice that after we append "Messi" to the list of players, we also end up adding him to the list of party guests! What's going on?

The visualization is what gives us a hint here: the `players_on_team` variable and `party_guests` variable both show arrows **going to the same place**: An object, more specifically a list. 

**There is only one list object in the code we shared**

We however, have two variables that **point** to that same object, which is represented by the arrow in the visualization.

The arrow makes sense as a symbol, but behind the scenes, both our `players_on_team` and `party_guests` hold the location in memory where the object is stored. They are not the object itself, they are the address where we can find the object.

Different programmin languages and communities refer to this kind of variable in diffrent ways, they are all effectively equivalent: You can call these "arrows" an object **reference**, or a **pointer** to an object, or **the address** of the object

 When we say: 

```python
party_guests = players_on_team
```

We are creating a new variable. The value of the variable is going to be the same as `players_on_team`. So the value will be a **reference to the list players_on_team is referencing as well**. 

Note that we can easily avoid this issue by **making sure we create two different objects**: Observe how differently this code behaves:

<iframe width="1200" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=players_on_the_team%20%3D%20%5B%22Eddie%22,%20%22JJ%22,%20%22Omar%22%5D%0Aparty_guests%20%3D%20%5B%22Eddie%22,%20%22JJ%22,%20%22Omar%22%5D%0A%0Aprint%28players_on_the_team%29%0Aprint%28party_guests%29%0A%0Aplayers_on_the_team.append%28%22Messi%22%29%0A%0A%23%20This%20should%20change%0Aprint%28players_on_the_team%29%0A%0A%23%20should%20this%20change%3F%0Aprint%28party_guests%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=7&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Now when we execute the second line of code, we create a brand new list, and store a brand new **reference**, a brand new arrow for it. We can modify the first list without worry about affecting the second. 


## Understanding how objects are made

The same approach we've had before applies for our custom objects. We will look into more examples in the next section, but for now, take a moment to focus on this key concept: How are objects made?

1. We will put aside some space in memory for our object.
2. We will initialize our variables - basically executing the code we wrote in __init__
3. We will return **a reference** to the object created.

Let's watch this in action:

<iframe width="1200" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=class%20Point%3A%0A%20%20%20%20def%20__init__%28self,%20x,%20y%29%3A%0A%20%20%20%20%20%20%20%20self.x%20%3D%20x%0A%20%20%20%20%20%20%20%20self.y%20%3D%20y%0A%20%20%20%20%20%20%20%20%0A%0A%0Anew_point%20%3D%20Point%286,%200%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

- After step 1, Python recognizes that we've defined a new class `Point`, and defined a method within it (`__init__`). Note that there are references being used here, but let's not focus on those for now.
- After step 2, we are trying to construct a new object. Our code moves to executing the `__init__` method. Note that `self` is a reference to a **Point Instance** - We've already put aside some memory for a Point.
- Steps 3-5 initialize our instance variables. Our point is getting its coordinates stored in memory.
- Step 6 we can now see that we have a `new_point` variable that is a **reference** to the Point object we've just seen created

### Equality

Take a look at the code below, and take a guess as to what it will output:
<iframe src="https://trinket.io/embed/python3/71bf995c54" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Bear in mind when it comes to objects: Having the same value, the same content, is not the same as **being the same object**

By default, when we use `==` to compare variables that **point** to objects, what we are comparing is the address they contain. In the example above, `basic_point == shared_reference` is `True` because they share the same address. `basic_point == same_coordinates` is `False` because they are different points, so the addresses are different. 

We will look into ways of customizing how equality is tested, but for now, let's keep learning about how objects are handled in memory

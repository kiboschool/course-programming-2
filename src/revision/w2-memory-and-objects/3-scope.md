# Frames and Scopes

Now, we are in Programming 2 now. We want to go a bit deeper with the content. The visualizations we saw in the previous section have some terms that we haven't defined yet. Let's explore them and what they mean. In particular, let's talk about what a **frame** is: Let's consider a very simple example:

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=x%20%3D%2010%0Aprint%28x%29%0A%0Adef%20my_function%28%29%3A%0A%20%20%20%20y%20%3D%205%0A%20%20%20%20print%28y%29%0A%20%20%20%20%0A%0Amy_function%28%29%0A%0Aprint%28y%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=8&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Let's click through our example step by step:

- Step 1: Shows that we store the variable `x` in *the global frame*.
- Step 2: Prints `x`, unsurprisingly we see 10 in our outpt
- Step 3: _Defines_ the function `my_function`. Note that this is also in **the global frame**, and that it's a reference.
- Step 4: We call our function, so our code jumps to where it is defined
- Step 5: Notice in our visualization that you can see `my_function` in blue under **the global frame**. As we execute a function, we create a new _frame_. These are called **Stack Frames**
- Step 6: We store a variable `y` in our function's stack frame. This is important info! Not all data is stored in the same place.
- Step 7: We want to print `y`, and we can find its value in our function's stack frame.
- Step 8: We **return** from the function, as its job is done. Notice that when you click to execute this step, the new stack frame we have created **will be deleted**
- Step 9: As we get into our final step, we want to print the value of `y` again, but take a look at our frames: `y` is nowhere to be found! As you click _Next_ here, we will get an error.

Let's look at a few different examples:

## Do names matter?

The way you name your variable matters for readability. Every variable is created with a purpose, and the name should reflect it. 

That being said, let's look at scenarios where two different variables have the same name: The following code is exactly the same as the previous example, except this time our function defines a variable called `x` instead of `y`:

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=x%20%3D%2010%0Aprint%28x%29%0A%0Adef%20my_function%28%29%3A%0A%20%20%20%20x%20%3D%205%0A%20%20%20%20print%28x%29%0A%20%20%20%20%0A%0Amy_function%28%29%0A%0Aprint%28x%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=8&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Our first few steps are the same: We have a global variable `x`, and a function. We ultimately call the function and it creates its own stack frame. 

What happens when we execute Step 6? Well we end up with a new variable, also called `x`, within the function's stack frame. This variable will only exist as long as we are still inside the function. So we can say the **scope** of this `x` is the function `my_function`

Once we finish executing the function, that `x`, with value 5, completely disappears!

So when we execute the final line of code, Python looks for `x` and finds a variable with that name in the **global frame**

As a rule of thumb, Python typically looks for a variable's name by:
- looking at the current frame.
- If not found, looking at the global frame.
- If not found, raising an error.

## Is the data gone forever?:

In the previous examples, we have looked at stack frames being created, variables being stored within that stack frame, then being deleted as the frame itself was deleted. Does that mean we can never get information out of a stack frame?

Well that would be the same as saying we can't get information out of a function, and we both know that's not the case. Let's look at the next example:

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20add_one%28some_number%29%3A%0A%20%20%20%20result%20%3D%20some_number%20%2B%201%0A%20%20%20%20return%20result%0A%20%20%20%20%0A%0Aglobal_var%20%3D%20add_one%284%29%0Aprint%28global_var%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=7&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Here we define a simple function: take a number as an input, compute that number + 1, then return the result. 

We call this function, then store its result in a global variable, before printing it. 

In particular let's focus on what happens when we execute Step 2: 
- Before we can create our variable in the global scope, we need to figure out what to put in it, so we need to execute and evaluate `add_one(4)`
- This means creating a frame for the `add_one` function. There is already a variable defined there: Our parameter! 
- As we execute Step 3 and 4 we are now ready to return. 
- When executing Step 5, notice that there is a new change to our Frame visualization: We put some memory aside for the return value specifically. 

Now that we know exactly what the function **returns** we can finish defining the `global_var` variable, which we can easily then print. 

If you had any lingering confusion about the difference between `print` and `return`, this should hopefully clarify it: 
- `print` lets you display some information to the terminal. This is meant for Human eyes!
- `return` immediately ends a function, and makes the value provided available to another frame. This is a tool to connect our code together

## Frames on frames on frames:

So far we have only seen examples where we had the **global frame** then one other one. In practice, we can have many frames active at the same time. This happens when you have functions that call other functions, so in other words it happens a lot!

Before walking through this code. Take a moment and think about two things:
- Firstly, what do you expect to see printed out?
- Secondly, what do you think will happen in terms of frames?

Give it a few minutes before running the code in the tool

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20add_one%28some_number%29%3A%0A%20%20%20%20result%20%3D%20some_number%20%2B%201%0A%20%20%20%20return%20result%0A%0Adef%20mult_two%28number%29%3A%0A%20%20%20%20result%20%3D%20number%20*%202%0A%20%20%20%20return%20result%0A%0Adef%20do_math%28number1,%20number2%29%3A%0A%20%20%20%20result%20%3D%20add_one%28number1%29%20%2B%20mult_two%28number2%29%0A%20%20%20%20return%20result%0A%20%20%20%20%0Aprint%28do_math%281,2%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=16&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

So what's going on here?

We define three functions, then make a call to `do_math(1, 2)`. We need to execute this function to figure out what to print. 

This immediately creates a new frame for that function. We will then try to create the `result` variable, but for that, we need to call two other functions. We start by calling the first one, `add_one`

This creates a new frame (Step 7). Within it, we create a variable called `result` that stores our calculation, then we return it, deleting the frame.

We are not ready to finish the `do_math` function yet though, we still need to call `mult_two`, so we create a new frame. Within it, we create a variable called `result` that stores our calculation, then we return it, deleting the frame.

Now we are finally able to figure out what `result` should be in the `do_math` frame. We're ready to return it to the global frame and print it. 

The key takeway here is that **none of those variables called result were related to each other, or ran the risk of messing with each other** They were each stored within their own frame, they each had their own scope.

## Definitions:
So let's formalize our takeaways from this: 

A **stack frame** is a section of memory put aside for a function. The variables needed to execute the function, as well as its parameters, are stored within the **stack frame**. These are then **deleted** when the function **returns**. 

The **scope** of a variable means the area of code where we can interact with the variable. The scope of a variable defined within a given stack frame is only that frame, so once the function is finished, we can no longer interact with the variable.

In Python, the **global frame** is available throughout the execution of our program. Anything defined within the global frame is therefore accessible throughout the program, and by all other frames. We say such variables have **global scope**

## Knowledge check:

[WIP]
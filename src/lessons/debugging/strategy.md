# Debugging Strategy

When you are debugging, that means something is not working the way that you expect it is. Your job as debugger is to investigate, and find out why your program is behaving the way it is.

_Fixing_ the bug is secondary. _Understanding_ what is going on comes first. Like a detective, your goal is to investigate and find the truth. When you know the truth, then you can achieve justice, or fix the bug.

## The Scientific Method

To some, science is about collecting tons of facts, or about Physics or Biology or Chemistry.

But at it's heart, Science is about _not fooling yourself_. It is very easy to come up with an idea about how something works ("the drug makes me sleepy because of its dormitive potency") but, unless you are careful, most of your ideas about how things work are **wrong**.

The scientific method is not about inventing something new. It's about _disproving hypotheses_, one by one.

Here are the steps in the cycle:
- Getting information
- Forming Hypotheses
- Testing your Hypotheses

Typically, you repeat these steps until you understand why the bug is happening.

## How to Debug

This [blog post from CS Professor John Regehr](https://blog.regehr.org/archives/199) lays out a scientific approach to debugging. It includes these steps:

1. Verify the Bug and Determine Correct Behavior
2. Stabilize, Isolate, and Minimize
3. Estimate a Probability Distribution for the Bug
4. Devise and Run an Experiment
5. Iterate Until the Bug is Found
6. Fix the Bug and Verify the Fix
7. Undo Changes
8. Create a Regression Test
9. Find the Bug’s Friends and Relatives

It's worth reading the post for more details on what each of these steps mean.

## Getting Information

If you are debugging, you probably already have some information. Something is going wrong!

There are tons of sources of information that could provide a clue about your bug. Here are some key sources:
- looking at the error
- checking your assumptions
- reading the code
- reading the documentation
- printing out information
- using an interactive debugger

**Look at the error** means actually reading the error message, if there is one. If not, it means looking at the output of your code, and comparing that closely to what you think it should be.

**Checking your assumptions** means checking basic hypotheses. Did the code run? Is the variable defined? Is the file loaded? Quite often, tricky bugs are due to basic assumptions.

**Reading documentation** can help if you are experiencing a bug with an API or a library. When it's someone else's code that you are interacting with, it's easy to misunderstand!

**Reading the code**. The code itself is usually where lots of information is! Rereading and explaining what you think is happening can help identify where the bug is, and sometimes, what the bug is. Reading the source code of a library can also be really helpful!

**Printing information** is one of the key tools in your toolbox. Print debugging can tell you what code is reached, and the values of your variables.

**Interactive debuggers** let you stop the program as it's running, inspect values, and execute statements. It's very powerful, but takes some practice to get used to.

## Forming Hypotheses

After you've gathered information, you need to make a guess about what is going wrong. Sometimes, it's easy to come up with lots of potential ideas. Other times, it's hard to come up with any guesses at all.

If you get stuck, it's worth checking your assumptions again and gathering more data, and seeing if that helps. If you're still stuck, it's often helpful to share your bug with a friend, or take a break and come back to the bug fresh.

## Testing your Hypothesis

Remember: Science is about **disproving** hypotheses. Not proving them! The key question is "What evidence would show that this idea is _false_?".

When you are debugging, you will find information about your program and how it runs. As you do, you'll come up with hypotheses for how it might be going wrong. When you do, you can't trust that you know for sure that you have correctly identified the error. You have to try to _disprove_ that it is the error.

Testing your hypothesis usually means _changing the code_ and _running it again_. It's really helpful to have a _minimal reproducible example_ when you do. If it's easy to repeat the bug, then you can quickly check the results of your change.

Tips for experiments:
- Test only one thing at a time
- Say out loud (or write down) what your hypothesis is, and why you think your change will help you tell if your hypothesis is wrong.
- Make experiments quick and repeatable

Often, beginners will try changing random things (or nothing at all) and rerun the code to see what happens. This is _not_ testing a hypothesis! Your changes should help you find out if your hypothesis about your code is correct.

<!--meta exposure: initial -->
<!--meta assessmentFormat: ProgrammingAssignment, GitHubClassroom -->
<!--meta submissionVia: GradeScope -->
<!--meta instructionType: specific -->
<!--meta submissionFormatFlexibility: no -->
<!--meta submissionTopicFlexibility: no -->
<!--meta rubricAvailable: yes -->
<!--meta rubricShared: yes -->
<!--meta groupWork: no -->
<!--meta automatedGrading: 80 -->
<!--meta studentInstructionsLink: https://github.com/kiboschool/programming2-w1-bank-accounts -->
<!--meta topics: classes -->

# Assignment 1: Banking Basics

In this assignment, we will create a **class** that models bank accounts. We will build a constructor, a custom way to display bank account information, as well as the basic operations one can do with an account: Deposit and withdraw money.

## Provided Code

Clone your repo using this link: [https://github.com/kiboschool/programming2-w1-bank-accounts](https://github.com/kiboschool/programming2-w1-bank-accounts)

`main.py` is where you will do the work. It has an incomplete `Account` class where you will have to create 4 methods.

`test.py` is used for testing. You will not need to read it or modify it. Use `python3 test.py` to run the tests. At the beginning they should all fail.

### Step 1: Initializing Accounts

in `main.py`, complete the `Account` class

Objects of this class **must** have the following two attributes:

- **owner**: This is a string that represents who owns the account. This should be a **parameter** to your constructor
- **balance**: This is a number that represents the amount of money in the account. This should always be **zero by default**

Create a constructor, i.e the `__init__` method, that would enable us to create objects that fit the above description.

```python
my_account = Account("Mehdi")
print(my_account.owner) # Shows Mehdi
print(my_account.balance) # Shows 0
```

Once you've convinced yourself that your code is correct. Run `python3 test.py`: You should pass 1/7 tests

### Step 2: Displaying Account Info

Let's make it easier to see what is going on in our account. Define an `__str__` method to display details of an account. 
We want to be able to do the following:

```python
print(my_account)
# Display "Mehdi's account balance is 0"
```

Recall that the `__str__` method needs to **return** a string, not print it!

Once you've convinced yourself that your code is correct. Run `python3 test.py`: You should pass 2/7 tests

### Step 3: Depositing to the account

At this point, we have stressed Mehdi enough with an empty bank account. Let's build a way to put some money in it. 

Define a `deposit` method that takes one parameter called amount, and **increases** the balance by that amount. 

We should be able to do the following in our code now:
```python
print(my_account)  # Display "Mehdi's account balance is 0"
my_account.deposit(100)
print(my_account)  # Display "Mehdi's account balance is 100"
```

There is a catch however! if the parameter is **Negative**, we should just ignore the operation altogether. our `deposit` method is meant to only put money in our account, it should never decrease our balance. The behaviour we want is:

```python
print(my_account)  # Display "Mehdi's account balance is 0"
my_account.deposit(-10)
print(my_account)  # Display "Mehdi's account balance is 0" 
# WE IGNORE NEGATIVE INPUTS
```

Once you've convinced yourself that your code is correct. Run `python3 test.py`: You should pass 4/7 tests

### Step 4: Withdrawing from the account

Unfortunately, everything that goes up must come down. Let's figure out how to withdraw money from the account. 

Define a `withdraw` method that takes one parameter called amount, and **decreases** the balance by that amount. As with `deposit` we want to ignore negative numbers.

There is something tricky about this method though: With `deposit`, we happily welcome any amount. Here though, we can not `withdraw` money we do not have.

Therefore a withdrawal may or may not work, it will depend on how much we have in our balance. Your method needs to be able to do the following:

- If we can withdraw the provided amount: change the balance, and **return True**
- If we can not withdraw the provided amount: do not change the balance and **return False**
- If the amount provided is negative: do not change the balance and **return False**

We should be able to do the following in our code now:

```python
print(my_account)  # Display "Mehdi's account balance is 0"
my_account.deposit(100)
print(my_account)  # Display "Mehdi's account balance is 100"

print(my_account.withdraw(20)) #Displays True
print(my_account)  # Display "Mehdi's account balance is 80"

# WE IGNORE NEGATIVE INPUTS
print(my_account.withdraw(-20)) #Displays False
print(my_account)  # Display "Mehdi's account balance is 80"

# We do not make withdrawals if they exceed the balance.
print(my_account.withdraw(200)) #Displays False
print(my_account)  # Display "Mehdi's account balance is 80"
```

Once you've convinced yourself that your code is correct. Run `python3 test.py`: You should pass 7/7 tests

### Optional challenge: Putting it all together

The final step to having a useful bank account is being able to transfer our balance to other people's accounts. 

Define a `transfer` method that takes two parameters: an amount, and another account that will serve as the recipient. If possible, we will _withdraw_ the amount from the initial account, and _deposit_ the same amount to the recipient. 

This is a bit tricky, as the withdrawal may or may not work. This is why we will want this method to also return a boolean for us: True if the transfer succeeded, and False otherwise:

- If we can withdraw the provided amount: change both account's balance, and **return True**
- If we can not withdraw the provided amount: do not change either account's balance and **return False**
- If the amount provided is negative: do not change either account's balance and **return False**

## Grading

| Criteria                            | Proficient                                        | Competent                                          | Developing                                       |
|-------------------------------------|---------------------------------------------------|----------------------------------------------------|--------------------------------------------------|
| **Coding Style (20%)**              |                                                   |                                                    |                                                  |
| 1. Indentation and Formatting       | Code is consistently well-indented and follows PEP 8 formatting guidelines. | Code is mostly well-indented and follows PEP 8 guidelines with minor deviations. | Code lacks consistent indentation and does not follow PEP 8 guidelines. |
| 2. Naming Conventions               | Meaningful and consistent variable/function/class names following PEP 8 conventions. | Mostly meaningful names, with occasional inconsistencies. | Variable/function/class names are unclear or inconsistent. |
| 3. Comments and Documentation       | Comprehensive comments and clear documentation for major functions and complex logic. | Adequate comments explaining major sections of code. | Lack of comments or insufficient documentation. |
| 4. Appropriate Use of Language Constructs | Demonstrates advanced understanding and appropriate use of Python language constructs (e.g., list comprehensions, generators). | Generally applies language constructs correctly, with occasional lapses. | Misuses or misunderstands key language constructs. |
| **Persistence (50%)**                    |                                                   |                                                    |                                                  |
| 5. Completeness                     | Evidence that all components of the assignment were attempted.  All functionality present. | Evidence that most elements of the assignment were attempted. Most functionality present. | Little evidence of completion of work.  Incomplete or major functionality missing.        |
| 6. Timeliness                       | Assignment started early (based on GitHub data).  GitHub commits show steady progress. Submitted on time. | Assignment is submitted late but GitHub data demonstrates an early or reasonable start date, with significant iteration on arrival to solution (i.e., multiple commits showing progress) | Submitted late. GitHub repository data shows late start and minimal iteration. |
| 7. Use of Resources                 | Assignment is fully complete and provides all functionality. If assignment is not fully complete, student attended office hours (or additional help sessions) and/or asked high quality and timely questions on Discord. | Assignment is not fully complete and there is minor evidence of effort to get assistance on assignment (e.g., office hours attendance or Discord discussions). | Assignment is incomplete and no evidence of seeking assistance. |
| **Correctness (30%)**               |                                                   |                                                    |                                                  |
| 8. Test Cases                       | Percentage of automated test cases that pass. |||

> **Evidence of Persistence:**
>
> In the event that you are unable to get your program fully functional, you will receive partial credit based on your evidence showing the amount
> of effort that went into learning the underlying concepts to complete the assignment or that you persistently sought appropriate assistance. Examples of persistence may
> include, but is not limited to, the following: Git commit history showing evolution of your program, attendance to office hours (Instructor or TA), asking
> thoughtful questions in the appropriate Discord forums, formation of study groups, completion of additional practice exercises, reading of third-party
> resources, etc.  
>
> To receive partial credit, you **must** create a file called `PERSISTENCE.md` in your GitHub repo alongside the `README.md` file, and include your evidence of
> persistence, for example, links to your Discord questions, narrative explaining dates and times of office hour sessions that you attended and what you learned, links to resources that you referenced,
> links to ChatGPT conversations that you initiated (focusing on concepts not just getting answers), etc. The better you can demonstrate your work on learning, the
> easier it will be to provide partial credit, so be thorough. Make sure that file is properly committed to your repo, and included in your Gradescope submission.

## Submitting Your Assignment

1. When you are done, `commit` and `push` your code to your remote repository.  (Note: In general, you should commit and push frequently, so that you have a backup of your work, so that there is evidence that you did your on work, and so that you can return to a previous state easily.)
2. Upload your submission in Gradescope via this link: [https://www.gradescope.com/courses/544003/assignments/2991606](https://www.gradescope.com/courses/544003/assignments/2991606)
3. Upload the zip archive of your assignment to Anchor below.

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
<!--meta studentInstructionsLink: https://github.com/kiboschool/programming2-w3-inheritance-acounts -->
<!--meta topics: inheritance -->

# Assignment 3: Banking Returns

In this assignment, we will expand on the work we did on Week 1, and see how we can model different types of Bank Accounts using Inheritance. 

## Provided Code

Clone your repo using this link: [https://github.com/kiboschool/programming2-w3-inheritance-acounts](https://github.com/kiboschool/programming2-w3-inheritance-acounts)

`main.py` is where you will do the work. You will be expected to define **three** different subclasses there. 

`test.py` is used for testing. You will not need to read it or modify it. Use `python3 test.py` to run the tests. At the beginning they should all fail. 

If all tests pass by the time you submit you will earn full marks. 

`account.py` contains a working implementation of the account class from Week 1. You are not expected to modify this file at all.

### The Account class

As a quick refresher, let's go over the class:

- An `Account` object has two attributes: an `owner` which is a string, and a `balance` which is the amount of money stored in the account. 
- we have an `__str__()` method, but it is not very helpful. You should ideally never see its output as you define the `__str__()` methods of our subclasses.
- we have a `deposit()` method which adds money to our balance.
- we have a `withdraw()` method which removes money from our balance **if possible**. This method returns **True** if the withdrawal was successful, and **False** otherwise.
- We have a `transfer()` method, which may be unfamiliar: This takes an amount and another account as a parameter - we call this account the recipient. We can then `withdraw` money from our account to `deposit` it in the recipient. This should only work if it's possible for us to `withdraw` the money in the first place. Make sure to study this method carefully, as you will need it later on. 

Similarly to `withdraw()`, `transfer()` returns **True** if the transfer was successful and **False** otherwise.

### Step 1: Checkings Account

Let's start with the simplest type of accounts, the checkings account. Create a subclass of `Account` called `CheckingAccount` and update it's `__str__` method so that our output would look like this:

```python
test_checking = CheckingAccount("Mehdi")
print(test_checking) # Display: Mehdi's Checking Account. Balance = 0
```

Convince yourself that `CheckingAccount` objects are able to handle the `deposit`, `withdraw` and `transfer` method.

Once you've convinced yourself that your code is correct. Run `python3 test.py`: You should pass 4/14 tests

### Step 2: Customizing Savings Account

Savings accounts are interesting because they accrue interest. The bank will multiply your balance by a small factor called the interest rate, and add it to your account every month, or every year, depending. 

Let's Create a savings account subclass of Account. It should have the following customizations:

- Its __init__ method should also include an interest rate parameter, and it should have a new attribute for the interest rate.
- Its __str__ method should clearly display that this is a savings account.
- It should have a new method, accrue_interest, which multiplies the balance by the interest value.

```python
test_saving = SavingsAccount("Mehdi", 1) #1% interest rate

print(test_saving) # Display: Mehdi's Savings Account. Balance = 0

test_saving.deposit(200)
test_saving.accrue_interest() # Should increase our balance by 1%, in other words 2 

print(test_saving) # Display: Mehdi's Savings Account. Balance = 202
```

Convince yourself that `SavingsAccount` objects are able to handle the `deposit`, `withdraw` and `transfer` method.

Once you've convinced yourself that your code is correct. Run `python3 test.py`: You should pass 7/14 tests

### Step 3: How do banks make money if they give you money?

If bans provide us interest, how do they make money? Well there are many strategies banks use, but one tricky one is that they charge users for making transfers. 

Now Checking Accounts usually get free transfers, but Savings Accounts do not, since the bank spends money on them for interest. Let's replicate this in our code.

Modify the `withdraw` method for the `SavingsAccount` class only. If we try to withdraw money from the account, or transfer it to someone else, the account's balance should be reduced by an additional **5**


```python
test_saving = SavingsAccount("Mehdi", 1) #1% interest rate

print(test_saving) # Display: Mehdi's Savings Account. Balance = 0

test_saving.deposit(100)
test_saving.withdraw(10) # This should really remove 15

print(test_saving) # Display: Mehdi's Savings Account. Balance = 85 

test_saving.transfer(20, test_checking)# This should really remove 25 from test_saving
```
Once you've convinced yourself that your code is correct. Run `python3 test.py`: You should pass 9/14 tests

### Step 4: LockedAccount

Another strategy banks use to make money is by holding your money for a long time. Some banks offer locked accounts: You can put money there, and it accrues interest like a savings account, but you are not allowed to take the money out for some amount of time. 

Let's create a `LockedAccount` class. It should have the following customizations:

- Its __init__ method should also include an interest rate parameter, and it should have a new attribute for the interest rate.
- Its __str__ method should clearly display that this is a savings account.
- It should be able to accrue_interest, which multiplies the balance by the interest value.
- Calling `withdraw()` or `transfer()` on an account like this should **always** return False, and should not 

Hint: What should the parent class of `LockedAccount` be? What saves you the most time?

```python
test_locked = LockedAccount("Mehdi", 5) #5% interest rate

print(test_locked) # Display: Mehdi's Locked Account. Balance = 0

test_locked.deposit(100)

print(test_locked.withdraw(10)) # Display False
print(test_locked.transfer(20, test_checking))# Display False

test_locked.accrue(interest)

print(test_locked) # Display: Mehdi's Locked Account. Balance = 105 

```

Once you've convinced yourself that your code is correct. Run `python3 test.py`: You should pass 14/14 tests at this point!

## Grading

| Criteria                            | Proficient                                        | Competent                                          | Developing                                       |
|-------------------------------------|---------------------------------------------------|----------------------------------------------------|--------------------------------------------------|
| **Coding Style (20%)**   ||||
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

## Submitting Your Work

Your work must be submitted Anchor for degree credit and to Gradescope for grading.

**For coding tasks involving Github Classroom:**

1. Ensure that you `commit` and `push` your local code changes to your remote repository.  (Note: In general, you should commit and push frequently, so that you have a backup of your work, so that there is evidence that you did your own work, and so that you can return to a previous state easily.)
2. Upload your submission to [Gradescope](https://www.gradescope.com) via the appropriate submission link by selecting the correct GitHub repository from the drop-down list.
3. Export a zip archive of your GitHub repository by visiting your repo on [GitHub](https://www.github.com), clicking on the green `Code` button, and selecting "Download Zip".
4. Upload the zip file of your repository to Anchor using the form below.

**For cases where you answer questions on Gradescope:**

1. Complete the work in [Gradescope](https://www.gradescope.com) by navigating tot he appropriate link.
2. Export it as a pdf using th Google Chrome plugin: [https://gofullpage.com/](https://gofullpage.com/).  This plugin will do multiple screen captures while scrolling through your document, and then stitch them into a pdf that you can download.
3. Upload the generated pdf to Anchor using the form below.

**For any work completed outside of GitHub or Gradescope:**

1. Take either screen captures of your work or export a pdf showing your complete work.
2. Submit the materials to [Gradescope](https://www.gradescope.com) via the appropriate submission link for the course.
3. Upload the screen captures or pdf files to Anchor using the form below.

> **Note:** Anchor submissions can occur at any time during the term, but it is **critical** that you upload all of your work to
> Anchor before the last day of the term.  Gradescope submissions must be submitted before the deadline (or the late deadline, if applicable).

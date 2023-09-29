# Exercises

---

> 💡 This is your chance to put what you’ve learned into action.
>
# Banking Returns!

In this assignment, we will expand on the work we did on Week 1, and see how we can model different types of Bank Accounts using Inheritance. 

### Provided code:
`main.py` is where you will do the work. You will be expected to define **three** different subclasses there. 

`test.py` is used for testing. You will not need to read it or modify it. Use `python3 test.py` to run the tests. At the beginning they should all fail. 

If all tests pass by the time you submit you will earn full marks. 

`account.py` contains a working implementation of the account class from Week 1. You are not expected to modify this file at all.

### The account class
As a quick refresher, let's go over the class:

- An `Account` object has two attributes: an `owner` which is a string, and a `balance` which is the amount of money stored in the account. 
- we have an `__str__()` method, but it is not very helpful. You should ideally never see its output as you define the `__str__()` methods of our subclasses.
- we have a `deposit()` method which adds money to our balance.
- we have a `withdraw()` method which removes money from our balance **if possible**. This method returns **True** if the withdrawal was successful, and **False** otherwise.
- We have a `transfer()` method, which may be unfamiliar: This takes an amount and another account as a parameter - we call this account the recipient. We can then `withdraw` money from our account to `deposit` it in the recipient. This should only work if it's possible for us to `withdraw` the money in the first place. Make sure to study this method carefully, as you will need it later on. 

Similarly to `withdraw()`, `transfer()` returns **True** if the transfer was successful and **False** otherwise.

### Step 1: Checkings Account (1 point)
Let's start with the simplest type of accounts, the checkings account. Create a subclass of `Account` called `CheckingAccount` and update it's `__str__` method so that our output would look like this:

```python
test_checking = CheckingAccount("Mehdi")
print(test_checking) # Display: Mehdi's Checking Account. Balance = 0
```

Convince yourself that `CheckingAccount` objects are able to handle the `deposit`, `withdraw` and `transfer` method.

Once you've convinced yourself that your code is correct. Run `python3 test.py`: You should pass 4/14 tests

### Step 2: Customizing Savings Account (2 points)

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

### Step 3: How do banks make money if they give you money? (2 points)
If bans provide us interest, how do they make money? Well there are many strategies banks use, but one tricky one is that they charge users for making transfers. 

Now Checking Accounts usually get free tansfers, but Savings Accounts do not, since the bank spends money on them for interest. Let's replicate this in our code.

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

### Step 4: LockedAccount (3 points)
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

## Submitting an assignment

When you are done, `commit` and `push` your code. Submit a link to your work on
Github using this form: **[Programming Exercise log](https://forms.gle/UbWLpo86JsWxrpNe9)**.

Be sure that the link you submit will take the instructor directly to your code.

<aside>

**If you get stuck**
1. Read the instructions again.
2. Remember **G**o **C**limb **K**ibo - first Google, then ask the Community on Discord, then reach out to Kibo instructional team.

</aside>

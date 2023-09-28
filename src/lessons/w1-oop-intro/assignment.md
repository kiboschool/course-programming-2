# Exercises

---

> 💡 This is your chance to put what you’ve learned into action.
>

# Banking Basics

In this assignment, we will create a **class** that models bank accounts. We will build a constuctor, a custom way to display bank account information, as well as the basic operations one can do with an account: Deposit and withdraw money.

### Provided code:
`main.py` is where you will do the work. It has an incomplete `Account` class where you will have to create 4 methods.

`test.py` is used for testing. You will not need to read it or modify it. Use `python3 test.py` to run the tests. At the beginning they should all fail. 

If all tests pass by the time you submit you will earn full marks. 

### Step 1: Initializing Accounts (2 points)

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

### Step 2: Displaying Account Info (1 point)
Let's make it easier to see what is going on in our account. Define an `__str__` method to display details of an account. 
We want to be able to do the following:

```python
print(my_account)
# Display "Mehdi's account balance is 0"
```

Recall that the `__str__` method needs to **return** a string, not print it!

Once you've convinced yourself that your code is correct. Run `python3 test.py`: You should pass 2/7 tests

### Step 3: Depositing to the account (2 points)
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

### Step 4: Withdrawing from the account (3 points)
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

## Submitting an assignment

When you are done, `commit` and `push` your code. Submit a link to your work on
Github using this form: **[Programming Exercise log](https://forms.gle/UbWLpo86JsWxrpNe9)**.

Be sure that the link you submit will take the instructor directly to your code.

<aside>

**If you get stuck**
1. Read the instructions again.
2. Remember **G**o **C**limb **K**ibo - first Google, then ask the Community on Discord, then reach out to Kibo instructional team.

</aside>

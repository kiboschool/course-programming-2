# Testing



<!--

------------------------------- in progress -------------------------------



    • Outline
        ◦ Introduce testing
        ◦ Show testing examples
        ◦ Introduce refactoring (incorporating thoughts on readability from week 6)
            ▪ New theme - higher level of thinking about coding, not just what, but why. Rob: Decomposition, Objects, what is ‘good’, why certain strategies / tips help to avoid kinds of problems
            ▪ Refactoring to reuse code. We’ve seen lots of places in the CourseManager project that show a list, edit, remove. Could create one ListManager, that would be more complicated, but would also eliminate lots of code. Note that more branches = more possible bugs, where as passing in plain data is often safer.
        ◦ Discuss how testing can help with refactoring (pinning)
        ◦ Writing test cases on the boundaries to catch the most bugs
        ◦ Writing test cases where the branches are to catch the most bugs (follow each branch, ‘coverage’)
        ◦ Writing test cases whenever a bug has been identified, that indicates it’s a weak part
        ◦ Discuss assert (for checking data) and how it makes code less fragile
        ◦ Convert from position parameters to named parameters - named params can be less fragile
    • Code Examples (some provided by us, some left to be written by students)
        ◦ We provide a buggy “microprocessor” implementation. Write tests to identify that bugs, and fix them
    • COURSE PROJECT: OBJECT-ORIENTED CLOTHING STORE
        ◦ Similar skills as the CourseManager final project from programming-1.
        ◦ We can make this simple - it’s just an end-of-week project.
        ◦ Flow: Run console app. See options View Shirts, View Hats, View Shoes, View Cart, Buy Items in Cart, View Previous Purchases
            ▪ When Viewing, can Add To Cart
            ▪ Pick a Quantity and parseInt on it
            ▪ Totalling the cart cost does demo a nice polymorphism property of just calling .getPrice() on everything
            ▪ When completing purchase
                • Persist simple object with Price, DatePurchased, Quantity, Item Description
                • Can save to json
                • Can also save by inserting rows to a db to sqlite
            ▪ No need for more features: no need to persist anything else, no read from inventory json, no need for counting stock/inventory, compute prices, sales/10% off coupon
    • We’ll provide many tests, student must write a couple of their own (which we can meta-test if we enforce the test looks a certain way) 


-->

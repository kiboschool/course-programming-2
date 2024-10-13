<!--meta exposure: repeated -->
<!--meta assessmentFormat: ProgrammingAssignment, GitHubClassroom -->
<!--meta submissionVia: GradeScope -->
<!--meta instructionType: specific -->
<!--meta submissionFormatFlexibility: no -->
<!--meta submissionTopicFlexibility: no -->
<!--meta rubricAvailable: yes -->
<!--meta rubricShared: yes -->
<!--meta groupWork: no -->
<!--meta automatedGrading: 80 -->
<!--meta studentInstructionsLink: https://github.com/kiboschool/programming2-w7-store-order-processor -->
<!--meta topics: unit testing -->

# Assignment 6: Testing

Clone your repo using this link: [https://github.com/kiboschool/programming2-w7-store-order-processor](https://github.com/kiboschool/programming2-w7-store-order-processor)

In this project, you will write tests that check if a program is working correctly.

There are two parts of the project. First, you will explore the code for the Order Processor. Then, you will write a set of tests that check that the implementation is working correctly.

## Provided Code

### Part One: Understanding the Order Processor

Part of managing an online store is handling inventory. The store receives orders, and some code has to update the inventory. For this online store, there is already an `OrderProcessor` class that can update the inventory based on the orders that come in.

This store has 3 types of merchandise: `jacket`, `slacks`, and `pair_of_shoes`.

There are 3 brands the store sells, `fruche`, `onalaja` and `kente`.

The store starts with a quantity of 20 of each of the different items for each brand. So, in the beginning, there will be

- 20 Fruche jackets
- 20 Onalaja jackets
- 20 Kente jackets
- 20 Fruche slacks
- 20 Onalaja slacks
- 20 Fruche pair\_of\_shoes
- 20 Onalaja pair\_of\_shoes
- 20 Kente pair\_of\_shoes

For simplicity, this project won't connect to a database or persist the results to a file - it will just print the results.

The other parts of the program send the `OrderProcessor` a json file with an order, and the order processor interprets it and deducts from the inventory.

An order is a JSON list of objects with a `type`, `brand`, and `quantity`.

An example order looks like this:

```json
[
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "1"}
]
```

In processing this order, the inventory would deduct 2 from the Fruche jackets, and deduct 1 from the Kente slacks.

The program should print this as a result:

```
Remaining inventory:
jacket fruche 18
jacket onalaja 20
jacket kente 20
slacks fruche 20
slacks onalaja 20
slacks kente 19
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 20
```

#### Explore the program

For Part 1, you don't need to write any code. Complete the following steps to understand what the program is doing:

* Run `main.py` and see the results.
* The sample orders are stored in json files named `example1.json`,  `example2.json`, and  `example3.json`. Edit `main.py` so that runs `example2.json`, and run `main.py` to see the results. Also try `example3.json`.
* Read through `implementations/store_order_processor.py` and trace through how it processes an order.
  * Find the part of code that raises an exception if the brand for an order is not one of the 3 supported brands.
  * Understand what the `search_in_list` method does.

In summary, here are the features that exist in `implementations/store_order_processor.py`:

* Ordering an item subtracts it from the inventory.
* An order that uses more than the available inventory is not valid.
* If input is not valid, raise an `StoreOrderProcessorException`.
* The inventory is displayed after each order.

### Part Two: Writing Tests

The next part of the assignment is to write tests that check that the `StoreOrderProcessor` implementation works correctly.

Edit `test_store_order_processor.py`. See the `TODO` comments in the file. For each `TODO` comment, write a test. The existing tests in the file show examples of how to set up and test the order processor.

Run the tests with `python test_store_order_processor.py`. All the tests should pass.

The next step is fun. Notice all of the files like `implementations/with_bugs_01.py`. These are different Store Order Processors that have realistic bugs. If the tests are working correctly, they will detect the bugs. In other words - if you pass a buggy implementation to your tests, you would expect one or more of the tests to fail! You can try this. Read the buggy implementations - a comment at the top of the file describes the problem.

We have provided a file `test_tests.py` - a Python program that tests the tests. It loops through every `with_bugs` file, runs the tests on it, and confirms that the tests have a failure. If the tests did not have a failure, they are allowing a buggy program to pass, which isn't right.

Test the tests you've written by running `test_tests.py`. If it runs with no errors, your tests are catching the right bugs. The `test_tests.py` tests are how the project will be autograded.

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

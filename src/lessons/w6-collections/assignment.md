
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
<!--meta studentInstructionsLink: https://github.com/kiboschool/programming2-w6-preference-analysis -->
<!--meta topics: collections -->

# Assignment 5: Picky Eaters

## Provided Code

Clone your repo using this link: [https://github.com/kiboschool/programming2-w6-preference-analysis](https://github.com/kiboschool/programming2-w6-preference-analysis)

For this week's assignment, we will manipulate collections to answer some questions about the food tastes of a group of people. We asked them what their preferred meals were, and stored all that information in a dictionary.

The `preferences` dictionary maps a `string` representing a person's name, to a `set` of strings, representing the three meals they like the most.

```python
preferences = {
  "Mehdi": {"Lasagna", "Tagine", "Steak"},
  "Tolu": {"Pepper Soup", "Noodles", "Lasagna"},
  "Stephen": {"Butter Chicken", "Salad", "Noodles"}
}
```

We are curious to know who amongst all our users has the most "unique" taste. Let's think about how to define that:

- For each meal, we will compute how many times that meal shows up in our dictionary
- For each user, we will then attribute a "score" based on how often each of their meals showed up across 
- We will then look for the user(s) with the **lowest** score, meaning their meals showed up the least often throughout our dataset

In order to achieve this we will build three functions using our knowledge of collections and data structures

## Step 1: Meal Counting

There is already a nice hint in the title of this step! Let's think about using a `Counter` object.

Recall that a `Counter` object is a special kind of dictionary, which works very well for counting objects. Counters can take all kinds of inputs:

- Strings, so the counter will count the characters in the string.
- Lists, so the counter will count the elements in the list.
- Sets, so the counter will count the elements in the set.

For example:

```python
from collections import Counter

letters = Counter('Africa')
print(letters) 
# {'a': 2, 'f': 1, 'r': 1, 'i': 1, 'c': 1}

letters.update({'a', 's', 'i'})
print(letters)
# {'a': 3, 'f': 1, 'r': 1, 'i': 2, 'c': 1, 's': 1}
# Note how the counter changed: 's' became a new entry, while 'a' and 'i' were incremented.
```

Armed with this knowledge, and using the `update` method above, complete the `create_meal_frequencies` method. Looping through all the preferences in the provided dictionary, create and return a counter that counts how often each meal appears.

For example, given

```python
preferences = {
	"Mehdi": {"Lasagna", "Tagine", "Steak"},
	"Tolu": {"Pepper Soup", "Noodles", "Lasagna"},
	"Stephen": {"Butter Chicken", "Salad", "Noodles"}
}
```

We want to see:

```python
print(create_meal_frequencies(preferences))

>> {'Lasagna': 2, 'Noodles': 2, 'Tagine': 1, 'Steal': 1, 'Pepper Soup': 1, 'Butter Chicken': 1, 'Salad': 1}
```

Once completed, run test.py: `test_meal_frequencies` should pass.

## Step 2: Creating User Scores

We want to be able to score each of our participants based on the frequencies. For example, Mehdi's score should be 4, because "Lasagna" has a frequency of 2, "Tagine" has a frequency of 1, and "Steak" has a frequency of 1. Their sum adds up to 4.

We can compute the score for Mehdi easily by looping through all the meals in his set of preferences, looking up each meal in our frequency dictionary

You need to repeat this process for all the users!

```python
preferences = {
	"Mehdi": {"Lasagna", "Tagine", "Steak"},
	"Tolu": {"Pepper Soup", "Noodles", "Lasagna"},
	"Stephen": {"Butter Chicken", "Salad", "Noodles"}
}

frequencies = create_meal_frequencies(preferences)

user_scores = create_user_scores(preferences, frequencies)

print(user_scores)
>> {"Mehdi": 4, "Tolu": 5, "Stephen": 4}
```

Once completed, run test.py: `test_score_users` should now be passing.

## Step 3: Finding the Most Unique Preferences

We are getting close to wrapping this up! We now have a dictionary with scores, so all we want is to extract the users that have the lowest scores. We can do this in two steps.

First, how do we find the lowest score? Well the `min()` method of the `Math` library gives us the smallest element of a collection. The collection we care about here is the _list of all values from the users_score dictionary_ For example,

```python
print(user_scores)
>> {"Mehdi": 4, "Tolu": 5, "Stephen": 4}

print(min(user_scores))
>> 4
```

Now that we know the smallest number, let's find all the users that have that number as their value! You should be able to do this with a loop and a condition, or with list comprehensions.

```python
find_users_with_lowest_score(user_score)
>> ["Mehdi", "Stephen"]
```

Note that order doesn't matter here, but you need to make sure to return all the users that share the lowest score.

Once completed, run `test.py`: all tests should now be passing, translating into full marks!

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

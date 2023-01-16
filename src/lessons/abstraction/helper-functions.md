# Helper Functions



<!--

------------------------------- in progress -------------------------------



    • Outline
        ◦ (We can also use this week as a buffer depending on progress of previous classes)
        ◦ (Go back to the “ways OOP helps us write code” list above)
        ◦ Helper functions (easier to discuss by showing examples)
            ▪ Writing to a text file takes a few lines of code, what if you use that a lot?
            ▪ Reading weather from a certain city takes a few lines of code, make a helper
                • And abstract it again to use another helper that reads json from any api and parses the json
            ▪ Only fix the bug in one place. Only add the new feature in one place. DRY if possible.
            ▪ Trade-off, you get less flexibility. But gain simplicity.
        ◦ Interfaces
            ▪ Important concept that we’ll use for this week’s project and final project
            ▪ Like helper functions, they hide the details
            ▪ You can even switch between them though, calling code does not change
        ◦ Why do people use json?
            ▪ Let’s consider a world where everything was a one-off text format
            ▪ We’re trying to persist a simplified soccer player goals example.
            ▪ What if there are bugs in the data coming in? Or it’s from another version of the program? Don’t want bad data structure coming in or your program will malfunction
            ▪ Light discussion of regex as to how to parse the input, say tab-delimited and # of goals is an integer
                • regexone.com
            ▪ That would be quicker than parsing into vars and checking if int, # of fields, etc
            ▪ But still needs a custom regex.
            ▪ JSON though is a great way to not need to write the regex
        ◦ Examples
            ▪ persist() and load() can be abstract methods– different implementations
                • We’re persisting some data but we were beginning programmers and wrote it to a text file format
                • We then realized we can use JSON (easier parsing)
                • We then realized we can use sql (better enforces structure)
                • Because persist() and load() were abstract methods, the calling code didn’t need to change as we made these changes
            ▪ One way we abstract on writing to db is an ‘orm’
            ▪ render() can be an abstract method 
                • Render to console
                • Render using PIL to save a png to disk
        ◦ Abstraction/interfaces are a key part of code quality
        ◦ Rob’s thoughts on code quality:
            ▪ Heuristic measures of ‘good’ code…
                • How easy is it to change?
                • How easy is it for someone else to understand?
                • Linter warnings
                • Lines of code
            ▪ How fast is your code? Objective measures of ‘good’ code…
                • Runtime / benchmarking speed
                • Memory / benchmarking RAM
                • Kinds of operations / slowness
            ▪ How correct is your code?
                • Does it pass the tests?
                • Do the tests check all the possible ways your program could be used?
                • Are there other ways your program could be correct or incorrect?
            ▪ How good is your application?
                • Does it have all the good features?
                • What features does it have that it should not?
    • COURSE PROJECT: REFACTORED PHONE BOOK (guided, autogradable, student barely writes new code)
        ◦ GUIDED PHONE BOOK REFACTORING, Repo already exists
            ▪ Make it into OOP
            ▪ Abstraction comes into play – we changed the implementation and calling code+tests do not change!
            ▪ We added a feature for inverse lookup
            ▪ Tests still pass
            ▪ Student writes a new test, say for the new inverse lookup feature
            ▪ (one testing principle is not to have too many implementation assumptions, test the public interface if possible)


-->

# Testing continued

## Important concepts in unit testing
### Test Driven Development
Some developers strongly believe in the value of unit testing to the extent that a new way of coding has emerged a few years ago: Test Driven Development. The idea behind TDD is to write the tests **first**, then the actual code. 

You should set yourself up with a series of failed tests, then aim to make them all pass. While this technique is often debated and polarizing (Some devs swear by it, others really dislike it), it's a good approach to adopt early in your career as it pushes you to think about your logic very early on as you set up the tests.

### Test Coverage
Many unit testing frameworks track a metric called test coverage: This is the percentage of lines of code in your program that were executed by your tests. You will likely encounter projects and individuals that boast of 90% or 95% test coverage, meaning they have very thorough testing. 

While higher coverage values are better than lower ones, recall that the presence of tests does not imply the absence of bugs: Because our functions could receive such a wide range of possible inputs, having tested a line of code once with one sample input is not enough to **guarantee** that there is no bug there. As projects grow bigger and more complex it's impossible to fully trust your tests. 

It is however stil worth tracking code coverage, as projects with low coverage - or god forbid none at all! - should be treated very carefully, and with a deliberate focus on testing the parts of the code that are untested.

This is often seen as the _bare minimum_ for your work to be included in a serious professional and/or open source project: If you do not show a high test coverage, other developers will not trust your contribution. 

### Mocking

As we've seen in the previous video, unit tests focus on isolating small portions of the code to focus on. All the examples we've seen so far have involved simple, self contained functions, but every now and then our code will interact with another system. This can be an api call or a connection to a database to name a few examples. How can we then test such a function?

Well one approach is to run it as it is, but this runs the risk of our unit tests failing because the system has a problem, not because our own code is incorrect. 

Another approach is to use **mocking**. This is a technique to "swap out" an object or a class for a fake version we can use for testing. This is a fairly complex topic, and you will not be assessed on it in this course, but we will rely on it in future courses. You can check out the video below for a hands on demo on how to use mocking with the unit test framework. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/6tNS--WetLI?si=0UpDBxWB3kxUagZF&amp;start=1715" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

_Note that the video starts on the mocking focused part of the tutorial, but it is overall a good resource for using unittest_

## Other kinds of testing:
While unit tests are extremely common, they are not the only types of tests we write. Two other tests are notable and you should be aware of them, though we won't write them until future classes.

### Integration tests:
While unit tests want to mock other systems to focus on simple, isolated logic, it's important for us to trust that the whole system works well together. It's great that our code works well if we mock a call to an external API, but what would happen if the API actually broke?

What would happen if the developers responsible for the API changed the format of it? 

Integration tests aim to test the system altogether, with all its parts talking to each other. They tend to be more complex to write and think about, but are arguably even better than unit tests in telling you if your program does the righ thing.

### Performance tests:
In some scenarios, we really care about the **performance** of our code, not only its **correctness**

Perhaps we are working on a very time sensitive scenario, and our code **must** execute faster than some target time. 

Maybe we are dealing with extrelemy large amounts of data, and our code **must** run fine even if we throw Gigabytes at it. 

In situations like this, it is important to have tests that assert that after making some changes, our code **remains as fast**, or even gets faster! Similarly, we care about our code **handling memory** well enough even after changes in scenarios where we are dealing with huge data.

## Testing as a professional focus:

While some amount of testing is expected of any professional developer, it is a focus area for many companies who hire dedicated developers focusing on testing and QA. If you enjoy the process of breaking down the logic of a function and testing it thoroughly, then this path could be one to explore. Check out this video for more context on this kind of work. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/ChhYCujkMZ0?si=1taZCiH-yEaOkw-0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# What's next:

Next week will be our final week of new content! we will carry on where we left off with a focus on professional concepts and methods to apply in your coding moving forward.

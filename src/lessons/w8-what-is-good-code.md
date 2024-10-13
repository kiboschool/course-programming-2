# What is Good Code?

We are heading towards the final portion of this course, and we will take a
shift in our approach. So far, throughout programming 1 and programming 2, you
have mostly worked on very small programs consisting of a few functions. As you
spent time practicing exercises and working on assignments, you thought hard
about these functions for many minutes, perhaps a few hours...Then you submitted
your work and moved on to other concerns.

You have so far spent little time with the code you have written, and that is
expected at this stage.

However, in the context of professional software development, the reality is
quite different. Take a moment and watch this video - you can fast forward it.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sySIzGu88WA?si=6iun7pdumYpl1TW-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This animation shows all the changes happening to a git repository. In
particular, this is the git repository for VLC, a popular video player you may
be familiar with. Each circle is a specific file. Files are grouped close to
each other if they are in the same folder. The little images you see appear and
disappear represent contributors, and you can see briefly a line between
contributors and files whenever someone edits the project.

Let's add some numbers to the equation:

- The video showcases changes from 1999 to 2011. That's 12 years of working on
  the same codebase!
- 5 different programming languages.
- 96000+ commits over the history of the project.
- 580+ different contributors.

How can anyone keep track of so much complexity? well there are a few things to
note:

1. You don't really have to keep track of ALL of it. By the time projects grow
   this big, many individuals specialize in a specific part of it.
2. We write, and push each other to write, very good code.

What do we mean by good code here? Well good code should be correct, it should
do the right thing we agreed upon. We've been practicing that, and with our new
knowledge of testing, we can make sure it stays correct.

Good code is also performant: It works quickly, does not use more memory than
necessary, and won't occasionally crash the machine running it. We will learn a
lot more about how to assess the performance of our code in our Algorithms
course.

The aspect of "good code" we want to focus on this week, and for the rest of our
time as growing developers, is that good code should be easy to work with. We
should strive to make it as easy to read and understand as possible, and as easy
to adapt to future challenges as possible. This is how we get to build projects
that hundreds can collaborate on. Put yourself in the position of a new team
member at VLC. Where would you even start? well written code gives you a good
logical start, and guides you step by step.

Many concepts come together to make code easy to work with, and we will spend
this week introducing a few, as we head towards your final project for the
course where you will spend weeks 9 and 10 working on the same codebase!

## Preview:

Here is what we will be exploring this week:

- What makes code good? how can we make our code better?
- How can we make our code resilient and flexible?
- How can we think about good abstractions reliably?

## Why does this matter?

We should build up our intuition for what makes good code. This will serve you
well in future courses and in the professional world where you will be working
on the same codebase for months at a time. As we head towards our first long
term assignment, you will soon have the opportunity to apply these design
principles for yourself
---
title: code-review
summary: how to conduct a code review
authors: ["ivan k"]
tags: ["interview", "code-review"]
date: 24-Oct-2022
source:
- https://www.youtube.com/watch?v=XKu_SEDAykw
published: true
---

# Code Review

If I see something wrong?

- Mostly ask questions

## Steps

- [ ] Read a description of a code under review, description of a pull request
  + [ ] Clarify requirements
  + [ ]**Question**: Let's clarify requirements. What the code suppose to be doing?
  + [ ]**Question**: What are the business requirements?
  + [ ]**Question**: What are potential inputs, nulls expected, single threaded or multi threaded environment?
- [ ] Walk trough fist time, after that second time
    - [ ] Are there enough/sufficient amount of comments in the code or not?
    - [ ] Methods have docs or not?
    - [ ] Understand where formatter was used or not
    - [ ] Any high level syntax and [style](https://google.github.io/styleguide/) issues
    - [ ] Walked through the code and wrote comments as I attempted to understand the algo. Checked correctness of the algo
    - [ ] Checked if boundary conditions were handled correctly
- [ ] Review unit tests. We will get back to them
  * [ ] Understand where its possible to test or not
- [ ] Look for Flags
  * [ ] Lack of comments
  * [ ] The code follows good [style](https://google.github.io/styleguide/)
  * [ ] Naming consistent across the code, naming conventions
  * [ ] Syntax errors, unidiomatic use of the language (is it Python or Python written in Java)
  * [ ] Library routines
  * [ ] Are there any logs/debug in the code
  * [ ] Is a code easy to follow (**Question**: can you explain an interaction)
  * [ ] If its multithreading, identify use of singletons and shared values
  * [ ] Complicated code review
    + I can't really follow it too well. Maybe changes are not going to do what they say are going to do.
    * Pull down changes
    + Manually test changes
    + Set breakpoints
- [ ] Language features
    - [ ] Language features used appropriately
    - [ ] Is this a Python or Python in Java way
- [ ] Best practices
  * [ ] Class names
  * [ ] Variables names
    * [ ] Suggested better naming of variables
  * [ ] Function names
    + [ ] Looked for any method or variable declarations to fix but didn't find any issues
  * [ ] Do not redefine built ins
- [ ] Efficiency and Underlying issues of performance in code
  * [ ] Can processing be saved e.g. cached or not
  * [ ] Correct data structures in use
    + [ ] Fixed some minor errors and suggested better data structures to store data (nothing fancy here, a Set instead of a List)
  * [ ] Wrote down time and space complexity
    + [ ] Understand a [code complexity](https://blog.codacy.com/an-in-depth-explanation-of-code-complexity/) TODO
    + [ ] Understand a [Big O notation](https://developerinsider.co/big-o-notation-explained-with-examples/) TODO
  * [ ] Algorithms (TODO)
    + [ ] Finally suggested a algo with better time complexity. Didn't have to implement it though.
    > TODO different algorithms to suggest

- [ ] Review unit tests again
  * [ ] Unit tests are correct
  * [ ] Is class under tests is being mocked(should not be)

- [ ] At the end -> Compliment Good Code
  * [ ] Provide suggestions
  * [ ] Leave comments
  * [ ] Decide outcome of a code review(Approve or provide suggestions)
  * [ ] Not feel comfortable right now to approve. If someone else approve it, Ill not hold back a CR.

## When you're solving coding problems or doing a code review, the interviewer will usually assess

- Do you think like an engineer? How do you think logically to accomplish a programming task? We're looking for evidence of your past as a strong coder.
- Do you make good choices around which data structures to use for different problems?
- Can you identify underlying problems and issues of performance in code?
- Can you identify good style, idiomacy, efficiency, and correctness in code?
- Do you have basic knowledge of core language libraries?
- Things we are lenient on: syntax errors, unidiomatic use of the language, library routines, if it takes you more time to get started with solving a problem.
- What if we had, as we do above, multiple if conditions and each one was quite complex?
- What if we had multiple if conditions and the code in the body of each one were quite complex?
- Would the code be easier or harder to understand?
- By reducing software complexity, we can develop with greater predictability. What I mean by that is we’re better able to say—with confidence—how long a section of code takes to complete.
- To prepare, practice coding exercises similar to Hackerrank and Pramp. 

## Hints

- When the risk of potential defects is reduced, there are fewer defects to find—and remove. As a result, the maintenance cost also reduces.
- Given that, by reducing code complexity, you reduce the risk of introducing defects; whether they’re small or large, slightly embarrassing or bankruptcy-inducing.

## Videos

- [example coding interview](https://www.youtube.com/watch?v=XKu_SEDAykw)

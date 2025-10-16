Module 06 - Functions and Modularity Basics
Weeks Covered: Week 6

Session 1 (1.5 hrs)
- Define functions with parameters and return values to promote reuse.
- Trace function calls with flow diagrams and emphasize proper naming.
- Convert Week 3 loop solutions into reusable functions.

Session 2 (1.5 hrs)
- Compose functions with loops and conditional logic (factorial, prime tests).
- Discuss local versus global variables and scope pitfalls.
- Practice modular design by splitting a problem into helper functions.

Homework and Practice
- Write at least five functions including `is_prime(n)`, `count_vowels(text)`, and `max_of_three(a, b, c)`.
- Refactor earlier homework into function-based solutions.
- Document each function with a brief comment or docstring describing its purpose.

Sample Question
- Prompt: Write a function `square(n)` that returns the square of a number, and demonstrate it by squaring 12.
- Solution:
```python
def square(n):
    return n * n

print(square(12))  # 144
```

Practice Challenge
- Prompt: Implement a function `greet(name)` that returns `Hello, <name>!`, then read a name from the user and print the returned string.
- Solution:
```python
def greet(name):
    return "Hello, " + name + "!"

user_name = input("Enter your name: ")
print(greet(user_name))
```

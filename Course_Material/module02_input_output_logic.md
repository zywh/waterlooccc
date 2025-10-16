Module 02 - Input, Output, and Basic Logic
Weeks Covered: Week 2

Session 1 (1.5 hrs)
- Review `input()` for user interaction and discuss prompt messaging.
- Convert between strings and numbers using `int()`, `float()`, and `str()`.
- Practice formatted printing with f-strings and `.format()`.

Session 2 (1.5 hrs)
- Build conditional logic with `if`, `elif`, and `else`.
- Compare values using `==`, `!=`, `<`, `>`, `<=`, `>=`.
- Explore boolean operators `and`, `or`, `not` in decision problems.

Homework and Practice
- Implement five small programs requiring user input and decisions (e.g., movie rating checker, password validator).
- Read through CCC Junior sample problems focusing on input and simple branching.
- Reflect on how to test each branch within a program.

Sample Question
- Prompt: Ask the user for a test score (0-100). Print `Pass` if the score is 50 or higher and `Retake` otherwise.
- Solution:
```python
score = int(input("Enter your score: "))
if score >= 50:
    print("Pass")
else:
    print("Retake")
```

Practice Challenge
- Prompt: Create a program that asks for an age. If the age is under 13, print `Child`; if it is between 13 and 18 inclusive, print `Teen`; otherwise print `Adult`.
- Solution:
```python
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age <= 18:
    print("Teen")
else:
    print("Adult")
```

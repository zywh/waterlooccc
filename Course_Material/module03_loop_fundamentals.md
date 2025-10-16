Module 03 - Loop Fundamentals
Weeks Covered: Week 3

Session 1 (1.5 hrs)
- Introduce `while` loops with clear start, stop, and step conditions.
- Demonstrate common pitfalls such as infinite loops and off-by-one errors.
- Counting exercises: tallying numbers, decrementing counters.

Session 2 (1.5 hrs)
- Present `for` loops with `range(start, stop, step)`.
- Compute sums, averages, and factorial-like products.
- Use loops to generate basic text patterns and sequences.

Homework and Practice
- Write programs that sum the first `N` integers, compute average temperatures, and print right-angled triangles of asterisks.
- Attempt a past CCC Junior counting problem (e.g., 2010 J1) and reflect on test cases.
- Journal one debugging tip discovered while working with loops.

Sample Question
- Prompt: Print the numbers 1 through 5 on separate lines using a loop.
- Solution:
```python
for i in range(1, 6):
    print(i)
```

Practice Challenge
- Prompt: Ask the user for a positive integer `N` and print the sum of the integers from 1 to `N`.
- Solution:
```python
N = int(input("Enter a positive integer: "))
total = 0
for i in range(1, N + 1):
    total += i
print("Sum from 1 to", N, "is", total)
```

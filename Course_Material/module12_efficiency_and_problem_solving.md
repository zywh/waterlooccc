Module 12 - Efficiency and Full Problem-Solving Practice
Weeks Covered: Weeks 15-16

Session 1 (1.5 hrs)
- Discuss time limits in the CCC and how nested loops affect runtime.
- Introduce Big-O notation informally to compare algorithm efficiency.
- Examine slow sample solutions and brainstorm optimizations.

Session 2 (1.5 hrs)
- Walk through a full CCC Junior set together, focusing on strategy and pacing.
- Encourage independent work on a different year's J1-J2 with facilitator support.
- Debrief common solution patterns and pitfalls.

Homework and Practice
- Profile a solution that uses nested loops and refactor it to run faster (e.g., using precomputed counts).
- Attempt two problems under a 1-hour time window to simulate contest pressure.
- Submit at least one solution to the CCC online grader and analyze the feedback.

Sample Question
- Prompt: Given a list of `N` integers (with `N` up to 10,000), determine whether any value appears more than once. The naive approach compares every pair. Improve the solution to run in `O(N log N)` or better.
- Solution:
```python
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
seen = set()
duplicate_found = False
for value in numbers:
    if value in seen:
        duplicate_found = True
        break
    seen.add(value)
if duplicate_found:
    print("Duplicate detected")
else:
    print("All values are unique")
```

Practice Challenge
- Prompt: Time how long it takes to sum the integers from 1 to `1_000_000` using a loop, then compute the same result using the formula `n * (n + 1) // 2`. Report the difference and explain which approach is better for large `n`.
- Solution:
```python
import time

n = 1_000_000

start = time.time()
total_loop = 0
for i in range(1, n + 1):
    total_loop += i
loop_time = time.time() - start

start = time.time()
total_formula = n * (n + 1) // 2
formula_time = time.time() - start

print("Loop total:", total_loop, "time:", loop_time)
print("Formula total:", total_formula, "time:", formula_time)
print("Formula is faster because it runs in constant time regardless of n.")
```

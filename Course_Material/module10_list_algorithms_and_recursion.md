Module 10 - List Algorithms and Introductory Recursion
Weeks Covered: Weeks 11-12

Session 1 (1.5 hrs)
- Explain the idea behind sorting and step through Bubble Sort manually.
- Compare linear search and binary search on sorted lists.
- Discuss slicing, sublists, and merging techniques with hands-on examples.

Session 2 (1.5 hrs)
- Introduce recursion with factorial, Fibonacci, and countdown examples.
- Relate recursive thinking to divide-and-conquer and bottom-up strategies.
- Emphasize base cases and stack depth to avoid infinite recursion.

Homework and Practice
- Implement Bubble Sort and track the list after each pass.
- Write both iterative and recursive versions of factorial and compare them.
- Attempt a CCC Junior list-processing problem (e.g., 2020 J2) using helper functions.

Sample Question
- Prompt: Sort the list `[5, 1, 4, 2]` using Bubble Sort and print the sorted result.
- Solution:
```python
numbers = [5, 1, 4, 2]
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)  # [1, 2, 4, 5]
```

Practice Challenge
- Prompt: Write a recursive function `countdown(n)` that prints numbers from `n` down to `0`, then prints `"Blast off!"`.
- Solution:
```python
def countdown(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
```

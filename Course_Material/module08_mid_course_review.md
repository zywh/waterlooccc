Module 08 - Mid-Course Review and Simple Algorithms
Weeks Covered: Week 8

Session 1 (1.5 hrs)
- Review major concepts from Weeks 1 through 7 with a recap quiz.
- Introduce brute-force search by checking every possibility in a small range.
- Discuss debugging strategies: print statements, tracing tables, and test cases.

Session 2 (1.5 hrs)
- Tackle counting problems that require frequency tallies in lists or strings.
- Explain basic time complexity intuition (what makes a solution fast enough for `N ≤ 100`).
- Work through a mixed set of CCC Junior practice problems collaboratively.

Homework and Practice
- Attempt a complete pair of CCC Junior problems (e.g., 2015 J1 and J2) under relaxed timing.
- Summarize personal strengths and weaknesses discovered during the review.
- Revisit one earlier assignment and improve its structure or readability.

Sample Question
- Prompt: Count how many times the letter `a` appears in the word `canada`.
- Solution:
```python
word = "canada"
count = 0
for letter in word:
    if letter == "a":
        count += 1
print(count)  # 3
```

Practice Challenge
- Prompt: Write a program that reads `N` integers (with `N ≤ 100`) and reports how many of them are greater than or equal to 50.
- Solution:
```python
N = int(input("How many numbers? "))
count = 0
for _ in range(N):
    value = int(input())
    if value >= 50:
        count += 1
print(count)
```

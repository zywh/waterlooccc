Module 05 - Lists and Dictionaries
Weeks Covered: Week 5

Session 1 (1.5 hrs)
- Create and manipulate lists with indexing, slicing, `append()`, `insert()`, and `remove()`.
- Practice traversing lists to compute totals, minima, maxima, and search outcomes.
- Introduce list comprehensions as a preview for advanced learners.

Session 2 (1.5 hrs)
- Understand dictionary key-value storage and common methods (`get`, `keys`, `values`).
- Build frequency counters and simple lookup tables.
- Demonstrate `sorted()` for producing ordered views of lists and dictionary keys.

Homework and Practice
- Manage a list of grades: add entries, compute averages, and detect duplicates.
- Build a dictionary that tracks inventory counts for a small store scenario.
- Implement a CCC-style data processing problem that reads a list of integers and reports statistics.

Sample Question
- Prompt: Given a list of integers `[4, 1, 3, 4, 2]`, count how many times the value `4` appears.
- Solution:
```python
numbers = [4, 1, 3, 4, 2]
count = 0
for value in numbers:
    if value == 4:
        count += 1
print(count)  # 2
```

Practice Challenge
- Prompt: Read five names from the user and store how many times each name appears using a dictionary. Display the counts.
- Solution:
```python
name_counts = {}
for _ in range(5):
    name = input("Enter a name: ")
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1
for name, count in name_counts.items():
    print(name, "appears", count, "time(s)")
```

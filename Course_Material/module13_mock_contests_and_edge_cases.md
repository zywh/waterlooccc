Module 13 - Mock Contests and Edge Cases
Weeks Covered: Weeks 17-19

Session 1 (1.5 hrs)
- Run a simulated 3-question contest (J1-J3 difficulty) under timed conditions.
- Analyze contest strategies: reading all problems first, budgeting time, partial scoring.
- Debrief common mistakes and discuss improvement plans.

Session 2 (1.5 hrs)
- Study advanced recursion patterns (tree exploration, subset generation).
- Investigate edge cases such as empty input, maximum constraints, and file reading basics.
- Conclude with a second mock challenge or targeted practice on tougher J4/J5 problems.

Homework and Practice
- Complete any unfinished mock contest problems and submit refined solutions.
- Solve one harder CCC problem (e.g., 2019 J5) focusing on recursion or graph traversal.
- Build a personal checklist for contest day (input parsing, testing, time management).

Sample Question
- Prompt: Using recursion, generate all subsets of a given list of three names and print them one per line.
- Solution:
```python
def generate_subsets(items, index, current):
    if index == len(items):
        print(current)
        return
    generate_subsets(items, index + 1, current)
    generate_subsets(items, index + 1, current + [items[index]])

names = ["Alex", "Bo", "Chen"]
generate_subsets(names, 0, [])
```

Practice Challenge
- Prompt: Read integers from a text file named `scores.txt`, where each line holds one score. Print the highest score and the number of entries processed. Provide a solution that gracefully handles an empty file.
- Solution:
```python
def analyze_scores(filename):
    try:
        with open(filename, "r") as handle:
            values = [int(line.strip()) for line in handle if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    if not values:
        print("No scores available.")
        return
    print("Highest score:", max(values))
    print("Number of scores:", len(values))

analyze_scores("scores.txt")
```

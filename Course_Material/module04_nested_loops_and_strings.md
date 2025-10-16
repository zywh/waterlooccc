Module 04 - Nested Loops and String Basics
Weeks Covered: Week 4

Session 1 (1.5 hrs)
- Review how nested loops iterate over grids and coordinate pairs.
- Build pattern generators such as multiplication tables and checkerboards.
- Trace nested loops with hand-drawn tables to reinforce understanding.

Session 2 (1.5 hrs)
- Explore string indexing, slicing, and the `len()` function.
- Practice common string methods: `upper()`, `lower()`, `find()`, `replace()`.
- Reverse strings and inspect palindromes using loops.

Homework and Practice
- Create nested loop programs that draw rectangles, stairs, and hollow boxes.
- Write three string-processing scripts such as counting vowels or replacing characters.
- Work through a CCC J3 or J4 simulation problem that involves distance tables or grid traversal.

Sample Question
- Prompt: Print a 3 by 3 grid of `#` symbols using nested loops.
- Solution:
```python
for row in range(3):
    line = ""
    for col in range(3):
        line += "#"
    print(line)
```

Practice Challenge
- Prompt: Ask the user for a word and report whether it is a palindrome.
- Solution:
```python
word = input("Enter a word: ")
reversed_word = ""
for index in range(len(word) - 1, -1, -1):
    reversed_word += word[index]
if word == reversed_word:
    print("Palindrome")
else:
    print("Not a palindrome")
```

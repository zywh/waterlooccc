Module 09 - Advanced Conditionals and String Algorithms
Weeks Covered: Weeks 9-10

Session 1 (1.5 hrs)
- Refine complex `if-elif-else` trees and nested conditions.
- Demonstrate `break` and `continue` for early loop exits and skipping iterations.
- Build interactive loops such as number guessing games with feedback.

Session 2 (1.5 hrs)
- Explore string parsing with `split()`, `join()`, and slice-based manipulation.
- Introduce simple substitution ciphers and decoding tasks.
- Peek at regular expressions for pattern detection (optional extension).

Homework and Practice
- Create a menu-driven program that lets a user choose repeated actions until they exit.
- Solve a string-heavy CCC Junior problem (e.g., 2018 J3) and annotate test cases.
- Experiment with at least one additional practice task involving message parsing.

Sample Question
- Prompt: Implement a loop that asks the user to guess a secret number `42`. Provide hints ("Too high"/"Too low") until the correct number is guessed.
- Solution:
```python
SECRET = 42
while True:
    guess = int(input("Guess the number: "))
    if guess == SECRET:
        print("Correct!")
        break
    elif guess < SECRET:
        print("Too low")
    else:
        print("Too high")
```

Practice Challenge
- Prompt: Read a message and shift every letter forward by one in the alphabet (wrapping `z` to `a`). Leave spaces unchanged. Provide the encoded message.
- Solution:
```python
message = input("Enter a message: ")
encoded = ""
for char in message:
    if "a" <= char <= "z":
        offset = ord(char) - ord("a")
        encoded += chr((offset + 1) % 26 + ord("a"))
    elif "A" <= char <= "Z":
        offset = ord(char) - ord("A")
        encoded += chr((offset + 1) % 26 + ord("A"))
    else:
        encoded += char
print(encoded)
```

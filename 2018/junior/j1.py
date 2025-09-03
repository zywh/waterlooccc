# Problem Statement — Telemarketer or not?

# You're given a 4-digit number (each digit provided on a separate line). A phone number is considered a telemarketer number if all the following conditions hold:

# The first of the four digits is either 8 or 9

# The last (fourth) digit is either 8 or 9

# The second and third digits are identical

# If all three conditions are met, output ignore; otherwise, output answer
# Read each of the four digits as strings
d1 = input().strip()
d2 = input().strip()
d3 = input().strip()
d4 = input().strip()

# Check the three conditions for a telemarketer number
is_telemarketer = (
    (d1 == '8' or d1 == '9') and  # first digit is 8 or 9
    (d4 == '8' or d4 == '9') and  # last digit is 8 or 9
    (d2 == d3)                    # second and third digits are the same
)

# Output result based on condition
print("ignore" if is_telemarketer else "answer")

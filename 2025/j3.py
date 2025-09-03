# CCC 2025 Junior J3: Product Codes

# Read input
N = int(input())

for _ in range(N):
    code = input().strip()
    
    uppercase_letters = ""
    current_number = ""
    total_sum = 0
    i = 0
    
    while i < len(code):
        char = code[i]
        
        if char.isupper():
            # If we were building a number, add it to sum first
            if current_number:
                total_sum += int(current_number)
                current_number = ""
            uppercase_letters += char
        elif char.islower():
            # If we were building a number, add it to sum first
            if current_number:
                total_sum += int(current_number)
                current_number = ""
            # Skip lowercase letters
        elif char.isdigit() or char == '-':
            # Start or continue building a number
            if char == '-':
                # If we were building a number, add it to sum first
                if current_number:
                    total_sum += int(current_number)
                current_number = "-"
            else:
                current_number += char
        
        i += 1
    
    # Don't forget to add the last number if there was one
    if current_number:
        total_sum += int(current_number)
    
    # Output the new code
    print(uppercase_letters + str(total_sum))

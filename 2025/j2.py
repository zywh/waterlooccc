# CCC 2025 Junior J2: Donut Shop

# Read input
D = int(input())  # Initial number of donuts
E = int(input())  # Number of events

# Start with the initial number of donuts
donuts = D

# Process each event
for _ in range(E):
    operation = input().strip()  # Either '+' or '-'
    quantity = int(input())      # Number of donuts
    
    if operation == '+':
        # Donuts baked (add to inventory)
        donuts += quantity
    elif operation == '-':
        # Donuts sold (subtract from inventory)
        donuts -= quantity

# Output the remaining donuts
print(donuts)

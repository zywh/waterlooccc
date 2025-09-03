# CCC 2025 Junior J1: Roller Coaster Ride

# Read input
N = int(input())  # Your position in line
C = int(input())  # Number of cars
P = int(input())  # Number of people per car

# Calculate total capacity of the train
total_capacity = C * P

# Check if you will be on the next train
# You will be on the train if your position (N) is <= total capacity
if N <= total_capacity:
    print("yes")
else:
    print("no")

# CCC 2025 Junior J4: Sunny Days

def max_consecutive_s(weather):
    """Find the maximum consecutive S's in the weather list"""
    max_count = 0
    current_count = 0
    
    for day in weather:
        if day == 'S':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    return max_count

# Read input
N = int(input())
weather = []
for _ in range(N):
    weather.append(input().strip())

max_possible = 0

# Try changing each day and see what gives maximum consecutive S's
for i in range(N):
    # Make a copy of the weather data
    modified_weather = weather.copy()
    
    # Change day i
    if modified_weather[i] == 'S':
        modified_weather[i] = 'P'
    else:
        modified_weather[i] = 'S'
    
    # Calculate max consecutive S's with this change
    consecutive = max_consecutive_s(modified_weather)
    max_possible = max(max_possible, consecutive)

print(max_possible)

# CCC 2023 Junior J2: Chili Peppers

pepper_heat = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000,
}

n = int(input())
total = 0
for _ in range(n):
    total += pepper_heat[input().strip()]

print(total)

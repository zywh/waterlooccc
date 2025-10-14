# CCC 2023 Junior J1: Deliv-e-droid

packages = int(input())
collisions = int(input())

score = 50 * packages - 10 * collisions
if packages > collisions:
    score += 500

print(score)

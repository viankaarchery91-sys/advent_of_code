# Read in the data
import sys
read = sys.stdin.read
f = open('day04.txt')

# Generate a matrix
rolls = [list(x) for x in f.read().split('\n')]

# Create a function that incorporates the Breath First Search (uses a tree diagram to check the value and add to a queue then does the next etc)
def count_neighbors(x, y):
    tot = 0

    # For x the direction can be -1, 0 or 1
    for dx in range(-1, 0, 1):
        # Neglect values at the end of the grid
        if x + dx < 0 or x + dx >= len(rolls):
            continue
    
    # For y the direction can be -1, 0, 1
    for dy in range(-1, 0, 1):
        # Neglect values at the edge of the grid
        if y + dy < 0 or y + dy >= len(rolls[x]):
            continue

        # If no shift then ignore
        if dx == dy == 0:
         continue

        # If there is @ then it is a roll
        if rolls[x + dx] [y +  dy] == '@':
            tot +=1
    return tot

# Count the rolls that can be retrieved
ans = 0

# Iterate over each cell in the grid
for i in range(len(rolls)):
    for j in range(len(rolls[i])):
        # Use count function from above and limit it to 4 rolls
        if rolls[i][j] == '@' and count_neighbors(i, j) < 4:
            ans += 1
print(ans)
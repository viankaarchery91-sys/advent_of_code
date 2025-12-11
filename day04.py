# Read in the data

with open('day04.txt', 'r') as f:
    lines = list[str] = f.readlines()
    rolls = [list(line.strip()) for line in lines]

# Create a function that incorporates the Breath First Search (uses a tree diagram to check the value and add to a queue then does the next etc)
def count_neighbors(x, y):
    tot = 0

    # For x the direction can be -1, 0 or 1
    for dx in range(-1, 0, 1):
        curr_x = x + dx
        # Neglect values at the end of the grid
        if curr_x < 0 or curr_x >= len(rolls):
            continue

    # For y the direction can be -1, 0, 1
        for dy in range(-1, 0, 1):
            curr_y = y + dy
        # Neglect values at the edge of the grid
            if curr_y < 0 or curr_y >= len(rolls[x]):
                continue
        # If no shift then ignore
            if dx == dy == 0:
                continue
        # If there is @ then it is a roll
            if rolls[curr_x] [curr_y] == '@':
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
# Open file
import sys
from bisect import bisect_left, bisect_right
read = sys.stdin.read
f = open('day05.txt')

# Read in the inputs. Separate it into two parts ad then parse it in as different parts
inp1, inp2 = f.read().split('\n\n')

# For inp1 make it into a list of ranges [x, y] by splitting by '\n' abd split by '-' to be x and y
fresh_raw = [list(map(int, rng.split ('-'))) for rng in inp1.split('\n')]

# Split again by '\n' and map to integers
available = list(map(int, inp2.split('\n')))

# Sort the two inputs and create empty lists
# Fresh range sort by x then y
fresh_raw.sort()

# Create a new list
fresh_processed = []

# Iterate through left and right and add new merge to new list
i = 0
while i < len(fresh_raw):
    # the right most range to be merged
    j = 1
    # High and low values 
    curr_min, curr_max = fresh_raw[i]

    # iterate over j while next range contains any value which intersects range
    while j + 1 < len(fresh_raw) and fresh_raw[j + 1][0] <= curr_max:
        j += 1

        # Update the high end of our merged range
        curr_max = max(curr_max, fresh_raw[j][1])

    # add the final merged range to the new array
    fresh_processed.append([curr_min, curr_max])

    # start again at the range 
    i = j + 1

# Use binary search to find a target value within an array
BIG_NUMBER = 10 * 18

# Variable to store ans
ans = 0

# Loop over and run the binary search
for ingredients in available:
    idx = bisect_left(fresh_processed, [ingredients, BIG_NUMBER]) -1
    if idx >= 0 and fresh_processed[idx][0] <= ingredients <= fresh_processed[idx][1]:
        ans += 1

print(ans)

# sum the size of the array
ans=0
for lo, hi in fresh_processed:
    ans += hi - lo + 1
print(ans)

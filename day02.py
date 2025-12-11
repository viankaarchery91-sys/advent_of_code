# read in the data
# import sys
# read = sys.stdin.read
f = open("day02_test.txt")
# split function looks at the text in the input file and breaks it up based on a comma
input_ids = f.read().split(',')
f.close()

# Now check if every number in the string is repeated (invalid)
def is_invalid(num):
    num_length = len(str(num))

    if num_length % 2 == 1:    # Check to see if the number length is odd. For an invalid id both numbers need to be even
        return False
    return str(num)[ :num_length // 2] == str(num)[num_length // 2:]

# Finally add the invalid  for each ID
ans = 0

for id in input_ids:
    lo, hi = id.split('-')
    lo = int(lo)
    hi = int(hi)

for num in range(lo, hi + 1):
    if is_invalid(num):
        ans += num

print(ans)
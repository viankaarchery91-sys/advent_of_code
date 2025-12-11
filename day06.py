import sys
read = sys.stdin.read
f = open('day06.txt')

# Split by any white spaces
ops = [x.split() for x in f.read().split('\n')]

# # N and M will be the rows and columns
N = len(ops)
M = len(ops[N-1])

# create a variable for ans
ans = 0 

# Iterate through each problem
for j in range(M):
    # Get numbers from each row exclude the last row
    nums = [ops[i][j] for i in range (N-1)]

    # Get operation from last row
    op = ops[N -1][j]

    # Concatenate nums using op
    # Eval for evaluating the resulting expression 
    # add final answer
    ans += eval(op.join(nums))
    
print(ans)
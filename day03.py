# Read in the data
# import sys
# read = sys.stdin.read
f = open('day03.txt')

# Each line becomes a sequence
sequences = f.read().split('\n')
f.close()

# Each string has is a battery supply and we need the two values that will give the highest joltage
# Create an array and use map to turn the values into integers
# Create a place to store the two largest values

digits = [list(map(int, list(sequence))) for sequence in sequences]


ans=0
for digs in digits:
    # Max value
    t_max = 0
    # Determine the lenght of the sequence as a number
    L = len(digs)
    # Loop through all the values in the first sequence
    for i in range(L):
        for j in range(i + 1, L):
            # Get new ma value
            t_max = max(t_max, 10 * digs[i] + digs[j])

    ans += t_max
print(ans)

# PART TWO
def solve(digits, J):
    # store the answer
    ans = 0
    for digs in digits:
        # length of the number string
        L = len(digs)
        # store the largest j digit number ending at or before positions i = 0 to L, for j = 0 to 12
        dp = [[0 for j in range(J + 1)] for i in range(L + 1)]
        # iterate over all positions in the number string
        for i in range(L):
            # iterate over all possible subsequence lengths
            for j in range(J + 1):
                # maximum of length j up to this position is at least as good as it was up to the previous position
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
                
                # create length j + 1 by using the candidate of length j up to the previous position, and the digit at position i+1 (i in 0-based) of the subsequence
                if j < J:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], 10 * dp[i][j] + digs[i])
        # the final answer for each string is the best possible subsequence of length J up to and including the final digit of the number string
        ans += dp[L][J]
    return ans
print(solve(digits, 12))
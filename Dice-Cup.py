'''
This python code is meant to show the most likely
outcome from the sum of two dice rolls
'''

import sys
try:
    # Get user input
    ab = input().split()
    n = int(ab[0])
    m = int(ab[1])

    # Initialize variables to 0
    most_likely = 0
    higher = 0
    lower = 0
    same = False

    # Verify user input does not have n less than 4
    # or m greater than 20
    if n < 4:
        sys.exit()
    if m > 20:
        sys.exit()

    # Check if numbers are the same, or else which one is higher
    # Set range for most likely sums
    if (n == m):
        most_likely = n + 1
        print(most_likely)
    else:
        higher = max(n,m) + 1
        lower = min(n,m) + 1
        # this is a loop to print range
        for most_likely in range(lower, higher+1):
            print(most_likely)
except:
    sys.exit()

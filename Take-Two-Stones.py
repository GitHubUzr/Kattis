'''
This python code is meant to take a user input variable 
and behave as if 2 is continuously subtracted until
the variable is less than 2, then determine if the
remainder is even or odd.
'''

nStonesEven = False
nStonesOdd = False

# Receive user input
nStones = int(input())

# Verify user has not entered > 10000000 or < 1
if nStones > 10000000 or nStones < 1:
    sys.exit()

# Determine if even or odd
# If even remainder, Bob wins the game
# If odd remainder, Alice wins the game
if nStones % 2 == 0:
    nStonesEven = True
    print("Bob")
else:
    nStonesOdd = True
    print("Alice")



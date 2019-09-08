'''
This python code is meant to find the original length
of a video that speeds up by a certain percent (p)
every time an event happens (n). The shortened video
length (k) is also used to determine the original length.
'''

try:
    import sys
    # receives input from first line
    # and splits into 3 different variables
    ab = input().split()
    n = int(ab[0])
    p = int(ab[1])/100
    k = int(ab[2])

    # receives input from second line
    # and creates an object to hold the values
    tsList = input().split()
    
    # converts list str values to int
    tsList = list(map(int, tsList))
    

    # Verify n is between 1 and 5000 (inclusive)
    # p is between 0 and 100 (inclusive)
    # and k is between n and 20000 (inclusive)
    if n < 1 or n > 5000:
        sys.exit()
    if p < 0 or p > 100:
        sys.exit()
    if k < n or k > 20000:
        sys.exit()

    total = 0

    # find difference between timestamps
    # multiply by percent
    # total is amount of time lost
    # last timestamp is compared to k
    for y in range(0,n):
        if(y == (n-1)):
            seconds = abs(tsList[y]-k)
            percent = p * (y + 1)
            total = total + (seconds * percent)
        else:
            seconds = abs(tsList[y]-tsList[y + 1])
            percent = p * (y + 1)
            total = total + (seconds * percent)

    # original time is time lost plus shortened video time(k)
    final = total+k

    # changes format to 3 decimal places
    print("{0:.3f}".format(final))
except:
    sys.exit()

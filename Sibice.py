import math
n, w, h = [int(number) for number in input().split()]
tri = math.hypot(w,h)
for x in range(n):
    y = int(input())
    if y <= w:
        print("DA")
    elif y <= h:
        print("DA")
    elif y <= tri:
        print("DA")
    else:
        print("NE")

'''This python program is meant to find the largest
area of a rectangle possible given four positive integers.
Each integer represents a line segment that is put down,
with a 90 degree turn after each segment. '''


# receives input as a list of numbers
n = [int(number) for number in input().split()]
# sorts the list (in ascending order)
n.sort()
# drawn order = [n[1],n[2],n[0],n[3]]
# find minimum value for opposite sides
length = min(n[1],n[0])
width = min(n[2],n[3])
# find area of rectangle
area = length * width
print(area)

'''The purpose of this python program is to find
   the total number of points on a square after n
   iterations when a square splits itself into 4
   smaller squares after every iteration.
'''

# this formula finds the new number of points across a side
def my_formula(val):
    my_sum = val+(val-1)
    return my_sum

# recives the input
n = int(input())

# the starting square has 2 points across a side
# (a point on each vertex)
points_across = 2

# repeat for number of iterations (n)
for x in range(n):
    # calls upon the function my_formula
    current = my_formula(points_across)
    # takes the answer from the formula to use in the next iteration
    points_across = current
# to find the total points within a square
# take the number of points_across and raise it to the power of 2
print((points_across)**2)

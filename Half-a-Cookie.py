import math
import sys
def d_between_2_points(xa,ya,xb,yb):
    distance_is = math.sqrt(((xa-xb)**2)+((ya-yb)**2))
    return distance_is
def solve_for_ceq(f1,f2):
    var_is = math.sqrt((f1**2) - (f2**2))
    return var_is
def quadratic(qa,qb,qc):
    qd = (qb**2) - (4*qa*qc)
    ans1 = (-qb-math.sqrt(qd))/(2*qa)
    ans2 = (-qb+math.sqrt(qd))/(2*qa)
    return ans1,ans2
for g in sys.stdin:
    r,x,y = [float(number) for number in g.split()]
    # check if point is inside circle
    check = d_between_2_points(0,0,x,y)
    if check > r:
        print("miss")
        continue
    # find slope of point-to-origin
    # find reverse slope
    if x == 0:
        reverse_slope = 0
    elif y == 0:
        reverse_slope = "undefined"
    else:
        my_slope = (y - 0) / (x - 0)
        reverse_slope = -(1/my_slope)
    # find intersections and distance between points
    if reverse_slope == "undefined":
        my_c = -((r**2) - (x**2))
        ys = quadratic(1,0,my_c)
        y1 = ys[0]
        y2 = ys[1]
        chord_length = d_between_2_points(x,y1,x,y2)
        x1 = x
        x2 = x
    elif reverse_slope == 0:
        my_c = -(r**2) - (y**2)
        xs = quadratic(1,0,my_c)
        x1 = xs[0]
        x2 = xs[1]
        chord_length = d_between_2_points(x1,y,x2,y)
        y1 = y
        y2 = y
    else:
        b = y - (reverse_slope * x)
        my_a = 1+reverse_slope**2
        my_b = (reverse_slope*b)+(reverse_slope*b)
        my_c = (b**2)-(r**2)
        xs = quadratic(my_a,my_b,my_c)
        x1 = xs[0]
        x2 = xs[1]
        y1 = (reverse_slope*x1)+b
        y2 = (reverse_slope*x2)+b
        chord_length = d_between_2_points(x1,y1,x2,y2)
        
    # find arc length
    angle = 2* math.asin(chord_length/(2*r))
    arc_length = r * angle
    # use proportions
    p = math.pi
    circle_area = p*(r**2)
    circle_length = 2*p*r
    arc_area = (arc_length * circle_area)/circle_length
    arc_area2 = 0.5*(angle*(r**2))
    #print(arc_area, arc_area2)
    # find area of chord to edge of circle
    # distance between 2 points formula modified
    s1 = d_between_2_points(0,0,x1,y1)
    s2 = d_between_2_points(0,0,x2,y2)
    s3 = chord_length
    h = (s1+s2+s3)/2
    triangle_area = math.sqrt(h*(h-s1)*(h-s1)*(h-s3))
    chord_area = arc_area - triangle_area
    cookie_half = circle_area - chord_area
    print(cookie_half, chord_area)

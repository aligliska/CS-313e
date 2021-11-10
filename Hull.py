#  File: Hull.py

#  Description: Given a list of points in a graph, this code finds the 
#  outer set of points to enclose all the points. The program also 
#  returns the area for the enclosing polygon. 

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Partner Name: Maxwell Kretschmer

#  Partner UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 6/25/2021

#  Date Last Modified: 6/27/2021


# output : individually printed tuples 

import sys
import math 


class Point(object):
    # constructor 
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    # prints point as a string 
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    # calculates the distance between two points  
    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    
    # overload equality tests of two points 
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))
    
    def __ne__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
        else:
            return (self.y < other.y)
        return (self.x < other.x)

    def __le__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
        else:
            return (self.y > other.y)
        return (self.x > other.x)
    
    def __ge__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
        else:
            return (self.y >= other.y)
        return (self.x >= other.x)


# determines the determinant for three points (p, q, r)
def determinant(p, q, r):
    p = Point(p[0], p[1])
    q = Point(q[0], q[1])
    r = Point(r[0], r[1])
    return (p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y* p.x)


# returns a list of outer points that form a convex 
def convex_hull(sorted_points):
    
    # adds first two points to upper_hull list 
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])

    # adds points to upper_hull, removing 2nd points if not right turn 
    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while (len(upper_hull) >= 3):
            if (determinant(upper_hull[-1], upper_hull[-2], upper_hull[-3]) <= 0):
                del upper_hull[-2]
            else:
                break 

    # adds last two points to lower_hull list 
    lower_hull = []
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])

    # adds points to lower_hull, removing 2nd points if not right turn 
    for j in range(len(sorted_points)-3, -1, -1):
        lower_hull.append(sorted_points[j])
        while (len(lower_hull) >= 3):
            if (determinant(lower_hull[-1], lower_hull[-2], lower_hull[-3]) <= 0):
                del lower_hull[-2]
            else:
                break

    # removes duplicate points from lower_hull that could be in upper_hull
    del lower_hull[0]
    del lower_hull[-1]

    # joins upper_hull and lower_hull 
    convex_hull_points = upper_hull + lower_hull

    return convex_hull_points


def area_enclosed(convex_points):
    # converts points to Point objects
    point_list = [Point(i[0], i[1]) for i in convex_points]

    det_area = 0
    
    # adds first half of the array to find determinant 
    for i in range(len(point_list)-1):
        det_area += point_list[i].x * point_list[i+1].y
    det_area += point_list[0].y * point_list[len(point_list)-1].x
    
    # subtracts second half of the array to find determinant
    for j in range(len(point_list)-1):
        det_area -= point_list[j].y * point_list[j+1].x
    det_area -= point_list[0].x * point_list[len(point_list)-1].y
    
    area = (1/2) * abs(det_area)
    return area


def main():
    # read in and format points from stdin
    unformatted_inList = sys.stdin.readlines()
    tempList = [entry.strip().strip("\n") for entry in unformatted_inList]
    
    num_points = int(tempList[0])
    del tempList[0]

    inList = [line.split("\t") for line in tempList]

    formatted_inList = [ [int(line[0]), int(line[1])] for line in inList]
    formatted_inList = sorted(formatted_inList)

    convex_hull_points = convex_hull(formatted_inList)
    
    # format and print hull points and area of the hull
    print("Convex Hull")

    for line in convex_hull_points:
        print(tuple(line))
    
    print()

    print(f"Area of Convex Hull =", area_enclosed(convex_hull_points))

if __name__ == "__main__":
  main()

#  File: Geometry.py

#  Description: This program inputs axis-values and side/radius/height values 
#  from a system input file, while stripping away comments. The program inputs 
#  each value as a float into each respective class. Within each class, the
#  program determines the specific attributes such as coincidence of objects
#  and inherent attributes like area and volume. The output prints out the
#  tested conditions. 

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 06/16/2021

#  Date Last Modified: 06/17/2021

import math
import sys


class Point (object):
  # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
    def __str__ (self):
        return "(" + str(float(self.x)) + ", " + str(float(self.y)) \
            + ", " + str(float(self.z)) + ")"

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
    def distance (self, other):
        return float(math.sqrt((self.x - other.x)**2 \
            + (self.y - other.y)**2 + (self.z - other.z)**2))

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
    def __eq__ (self, other):
        tol = 1.0e-6
        return ((abs(self.x - other.x) < tol) and \
            (abs(self.y - other.y) < tol) and \
            (abs(self.z - other.z) < tol)) 


class Sphere (object):
  # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.x = x
        self.y = y
        self.z = z
        self.center = Point(self.x, self.y, self.z)
        
        self.radius = radius

        #furthest points on the sphere from the center
        self.xmin = self.x - self.radius
        self.xmax = self.x + self.radius
        self.ymin = self.y - self.radius
        self.ymax = self.y + self.radius
        self.zmin = self.z - self.radius
        self.zmax = self.z + self.radius

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
    def __str__ (self):
        return "Center: (" + str(float(self.x)) + ", " \
            + str(float(self.y)) + ", " + str(float(self.z)) \
            + "), Radius: " + str(float(self.radius))

  # compute surface area of Sphere
  # returns a floating point number
    def area (self):
        return float(4*math.pi*(self.radius**2))

  # compute volume of a Sphere
  # returns a floating point number
    def volume (self):
        return float((4/3)*math.pi*(self.radius**3))

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
    def is_inside_point (self, p):
        return self.center.distance(p) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
    def is_inside_sphere (self, other):
        return (self.center.distance(other.center) + other.radius) \
            < self.radius
    
    # determines if the sphere is outside of the other shape  
    def is_outside_sphere(self, other):
        return self.center.distance(other.center) \
            > (self.radius + other.radius) 

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
    def is_inside_cube (self, a_cube):
        inside = True
        for corners in a_cube.cube_max_points:
            if self.center.distance(corners) < self.radius:
                inside = True
            else:
                inside = False
                break
        return inside
    
    # determines if the cube is outside of the sphere 
    def is_outside_cube(self, a_cube):
        outside = False
        if (self.xmax < a_cube.xmin) or (self.xmin > a_cube.xmax):
            outside = True
        elif (self.ymax < a_cube.ymin) or (self.ymin > a_cube.ymax):
            outside = True
        elif (self.zmax < a_cube.zmin) or (self.zmin > a_cube.zmax):
            outside = True
        return outside

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
    def is_inside_cyl (self, a_cyl):
        inside = True
        for point in a_cyl.cylinder_max_points:
            if self.center.distance(point) < self.radius:
                inside = True 
            else: 
                inside = False 
                break
        return inside 

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
    def does_intersect_sphere (self, other):
        return not self.is_inside_sphere(other) and \
            not self.is_outside_sphere(other)

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
    def does_intersect_cube (self, a_cube):
        return not self.is_inside_cube(a_cube) and \
            not self.is_outside_cube(a_cube)

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
    def circumscribe_cube (self):
        self.max_side = (self.radius*2) / math.sqrt(3)
        return Cube(self.x, self.y, self.z, self.max_side)


class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.x = x
        self.y = y
        self.z = z
        self.center = Point(self.x, self.y, self.z)

        self.side = side 
        self.length = self.side / 2

        # maximum distance of the edges from the center point
        self.xmin = self.x - self.length
        self.xmax = self.x + self.length
        self.ymin = self.y - self.length
        self.ymax = self.y + self.length
        self.zmin = self.z - self.length
        self.zmax = self.z + self.length

        # maximum distance of the corners of the cube from center 
        # location abbreviated (top, bottom, upper, lower, right, left)
        self.tur = Point(self.xmax, self.ymax, self.zmax)
        self.tul = Point(self.xmin, self.ymax, self.zmax)
        self.tbr = Point(self.xmax, self.ymax, self.zmin)
        self.tbl = Point(self.xmin, self.ymax, self.zmin)
        self.bur = Point(self.xmax, self.ymin, self.zmax)
        self.bul = Point(self.xmin, self.ymin, self.zmax)
        self.bbr = Point(self.xmax, self.ymin, self.zmin)
        self.bbl = Point(self.xmin, self.ymin, self.zmin)

        self.cube_max_points = [self.tur, self.tul, self.tbr, 
                                self.tbl, self.bur, self.bul, 
                                self.bbr, self.bbl]

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
    def __str__ (self):
        return "Center: (" + str(float(self.x)) + ", " \
            + str(float(self.y)) + ", " + str(float(self.z)) \
            + "), Side: " + str(float(self.side))

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self):
        return float(6*(self.side**2)) 

  # compute volume of a Cube
  # returns a floating point number
    def volume (self):
        return float(self.side**3)

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, p):
        return (self.xmin < p.x < self.xmax) and \
            (self.ymin < p.y < self.ymax) and \
            (self.zmin < p.z < self.zmax)

    # determine if a Sphere is strictly inside this Cube 
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        return (self.center.distance(a_sphere.center) \
            + a_sphere.radius) < self.side/2

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        return (self.xmin < other.xmin and self.xmax > other.xmax) \
            and (self.ymin < other.ymin and self.ymax > other.ymax) \
            and (self.zmin < other.zmin and self.zmax > other.zmax)
    
    # determines if cube is outside of cube
    def is_outside_cube(self, other):
        return (self.xmax < other.xmin or self.xmin > other.xmax) \
            or (self.ymax < other.ymin or self.ymin > other.ymax) \
            or (self.zmax < other.zmin or self.zmin > other.zmax) 

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        return (self.xmin < a_cyl.xmin and self.xmax > a_cyl.xmax) \
            and (self.ymin < a_cyl.ymin and self.ymax > a_cyl.ymax) \
            and (self.zmin < a_cyl.zmin and self.zmax > a_cyl.zmax)

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, other):
        return not self.is_inside_cube(other) and \
            not self.is_outside_cube(other)

    # determine the volume of intersection if this Cube 
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        # intersection will have 6 sides
        self.side_x1 = 0
        self.side_x2 = 0
        self.side_y1 = 0
        self.side_y2 = 0
        self.side_z1 = 0
        self.side_z2 = 0

        if self.does_intersect_cube(other):
            
            # finds the 2 x-faces of intersection 
            if self.xmin > other.xmin:
                self.side_x1 = self.xmin
            elif self.xmin < other.xmin: 
                self.side_x1 = other.xmin
            if self.xmax > other.xmax: 
                self.side_x2 = other.xmax
            elif self.xmax < other.xmax:
                self.side_x2 = self.xmax
            
            # finds the 2 y-faces of intersection 
            if self.ymin > other.ymin:
                self.side_y1 = self.ymin
            elif self.ymin < other.ymin: 
                self.side_y1 = other.ymin 
            if self.ymax < other.ymax:
                self.side_y2 = self.ymax
            elif self.ymax > other.ymax: 
                self.side_y2 = other.ymax 
            
            # finds the 2 z-faces of intersection 
            if self.zmin > other.zmin:
                self.side_z1 = self.zmin 
            elif self.zmin < other.zmin: 
                self.side_z1 = other.zmin 
            if self.zmax > other.zmax: 
                self.side_z2 = other.zmax
            elif self.zmax < other.zmax:
                self.side_z2 = self.zmax
        
        # determines the distance between faces to find volume 
        self.x_dimension = abs(self.side_x1 - self.side_x2)
        self.y_dimension = abs(self.side_y1 - self.side_y2)
        self.z_dimension = abs(self.side_z1 - self.side_z2)

        return float(self.x_dimension * self.y_dimension * self.z_dimension)

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):
        self.max_radius = self.side/2
        return Sphere(self.x, self.y, self.z, self.max_radius)


class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.x = x
        self.y = y
        self.z = z
        self.center = Point(self.x, self.y, self.z)

        self.radius = radius
        self.height = height

        # maximum points away from center of cylinder 
        self.xmin = self.x - self.radius 
        self.xmax = self.x + self.radius
        self.ymin = self.y - self.radius
        self.ymax = self.y + self.radius 
        self.zmin = self.z - (self.height/2)
        self.zmax = self.z + (self.height/2)

        self.tur = Point(self.xmax, self.ymax, self.zmax)
        self.tul = Point(self.xmin, self.ymax, self.zmax)
        self.tbr = Point(self.xmax, self.ymax, self.zmin)
        self.tbl = Point(self.xmin, self.ymax, self.zmin)
        self.bur = Point(self.xmax, self.ymin, self.zmax)
        self.bul = Point(self.xmin, self.ymin, self.zmax)
        self.bbr = Point(self.xmax, self.ymin, self.zmin)
        self.bbl = Point(self.xmin, self.ymin, self.zmin)

        self.cylinder_max_points = [self.tur, self.tul, self.tbr, 
                                    self.tbl, self.bur, self.bul, 
                                    self.bbr, self.bbl]

    # returns a string representation of a Cylinder of the form: 
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):
        return "Center: (" + str(float(self.x)) + ", " \
            + str(float(self.y)) + ", " + str(float(self.z)) \
            + "), Radius: " + str(float(self.radius)) + ", Height: " \
            + str(float(self.height))

    # compute surface area of Cylinder
    # returns a floating point number
    def area (self):
        return float((2*math.pi*(self.radius**2)) \
            + (2*math.pi*self.radius*self.height))

    # compute volume of a Cylinder
    # returns a floating point number
    def volume (self):
        return float((math.pi*(self.radius**2)* self.height)) 

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point (self, p):
        if (self.xmin < p.x < self.xmax) and \
            (self.ymin < p.y < self.ymax) and \
            (self.zmin < p.z < self.zmax):

            # creates a comparative point on the same z-plane 
            self.new_center = Point(self.x, self.y, p.z)
            if self.radius < (self.height/2):
                return self.new_center.distance(p) < self.radius
            elif self.radius > (self.height/2):
                return self.new_center.distance(p) < (self.height/2)

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        return (self.xmin < a_sphere.xmin < self.xmax) and \
        (self.xmin < a_sphere.xmax < self.xmax) and \
        (self.ymin < a_sphere.ymin < self.ymax) and \
        (self.ymin < a_sphere.ymax < self.ymax) and \
        (self.zmin < a_sphere.zmin < self.zmax) and \
        (self.zmin < a_sphere.zmax < self.zmax)

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        return (self.xmin < a_cube.xmin < self.xmax) and \
        (self.xmin < a_cube.xmax < self.xmax) and \
        (self.ymin < a_cube.ymin < self.ymax) and \
        (self.ymin < a_cube.ymax < self.ymax) and \
        (self.zmin < a_cube.zmin < self.zmax) and \
        (self.zmin < a_cube.zmax < self.zmax)

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, other):
        return (self.xmin < other.xmin < self.xmax) and \
            (self.xmin < other.xmax < self.xmax) and \
            (self.ymin < other.ymin < self.ymax) and \
            (self.ymin < other.ymax < self.ymax) and \
            (self.zmin < other.zmin < self.zmax) and \
            (self.zmin < other.zmax < self.zmax)
        
    # checks if other cylinder is outside of the cylinder 
    def is_outside_cylinder(self, other):   
        # checks if cylinder is completely out of bounds 
        return (self.xmax < other.xmin or self.xmin > other.xmax) \
            or (self.ymax < other.ymin or self.ymin > other.ymax) \
            or (self.zmax < other.zmin or self.zmin > other.zmax)

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder (self, other):
        return not self.is_inside_cylinder(other) and \
            not self.is_outside_cylinder(other)
            

def main():
    # read data from standard input
    unformatted_inList = sys.stdin.readlines()

    # formats data to a readable list, removing unnecessary characters
    temp_list = [entry.strip("\n").split("#", 1)[0].split("  ", 1)[0].split()
                for entry in unformatted_inList]
    
    inList = []

    # converts each numerical entry into a float
    for element in temp_list:
        converted = []
        for entry in element:
            converted.append(float(entry))
        inList.append(converted)

    # creates point objects p and q
    p = Point(inList[0][0], inList[0][1], inList[0][2])
    q = Point(inList[1][0], inList[1][1], inList[1][2])

    # creates sphere objects A and B
    sphereA = Sphere(inList[2][0], inList[2][1], inList[2][2], inList[2][3])
    sphereB = Sphere(inList[3][0], inList[3][1], inList[3][2], inList[3][3])

    # creates cube objects A and B
    cubeA = Cube(inList[4][0], inList[4][1], inList[4][2], inList[4][3])
    cubeB = Cube(inList[5][0], inList[5][1], inList[5][2], inList[5][3])

    # creates cylinder objects A and B
    cylA = Cylinder(inList[6][0], inList[6][1], inList[6][2], inList[6][3], 
    inList[6][4])
    cylB = Cylinder(inList[7][0], inList[7][1], inList[7][2], inList[7][3], 
    inList[7][4])

    '''
    Below are print statements to check the correctness of the above 
    algorithms.
    '''

    # print if the distance of p from the origin is greater 
    # than the distance of q from the origin
    origin = Point()
    if p.distance(origin) > q.distance(origin):
        print("Distance of Point p from the origin is greater than the", 
        "distance of Point q from the origin")
    else:
        print("Distance of Point p from the origin is not greater than", 
        "the distance of Point q from the origin")

    # print if Point p is inside sphereA
    if sphereA.is_inside_point(p):
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")

    # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB):
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")

    # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA):
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")

    # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA):
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")

    # print if sphereA intersects with sphereB
    if sphereB.does_intersect_sphere(sphereA):
        print("sphereA does intersect sphereB")
    else:
        print("sphereA does not intersect sphereB")

    # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB):
        print("cubeB does intersect sphereB")
    else:
        print("cubeB does not intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed 
    # by sphereA is greater than the volume of cylA
    if sphereA.circumscribe_cube().volume() > cylA.volume():
        print("Volume of the largest Cube that is circumscribed by sphereA", 
        "is greater than the volume of cylA")
    else:
        print("Volume of the largest Cube that is circumscribed by sphereA", 
        "is not greater than the volume of cylA")

    # print if Point p is inside cubeA
    if cubeA.is_inside_point(p):
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")

    # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA):
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")

    # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB):
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")

    # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA):
        print("cylA is inside cubeA")
    else:
        print("cylA is not inside cubeA")

    # print if cubeA intersects with cubeB
    if cubeA.does_intersect_cube(cubeB):
        print("cubeA does intersect cubeB")
    else:
        print("cubeA does not intersect cubeB")

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
        print("Intersection volume of cubeA and cubeB is greater than the", 
        "volume of sphereA")
    else:
        print("Intersection volume of cubeA and cubeB is not greater than", 
        "the volume of sphereA")

    # print if the surface area of the largest Sphere object inscribed 
    # by cubeA is greater than the surface area of cylA
    if cubeA.inscribe_sphere().area() > cylA.area():
        print("Surface area of the largest Sphere object inscribed by cubeA", 
        "is greater than the surface area of cylA")
    else:
        print("Surface area of the largest Sphere object inscribed by cubeA", 
        "is not greater than the surface area of cylA")

    # print if Point p is inside cylA
    if cylA.is_inside_point(p):
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")

    # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA):
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")

    # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA):
        print("cubeA is inside cylA")
    else:
        print("cubeA is not inside cylA")

    # print if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB):
        print("cylB is inside cylA")
    else:
        print("cylB is not inside cylA")

    # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB):
        print("cylB does intersect cylA")
    else:
        print("cylB does not intersect cylA")

if __name__ == "__main__":
  main()
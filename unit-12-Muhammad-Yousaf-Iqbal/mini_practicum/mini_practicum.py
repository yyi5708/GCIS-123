#MYI

import math

class Circle:

    __slots__ = ["__center", "__radius"]

    def __init__(self, center=tuple(), radius=int()):

        (self.__center) == (center)
        (self.__radius) == (radius)

    def get_center(self):
        return(self.__center)

    def get_radius(self):
        return(self.__radius)

    def __repr__(self):
    
        return("center: ", {self.__center}, "radius: ", {self.__radius})

    def __lt__(self, other):

        return(self.__radius < other.__radius)

    def intersect(self, other):

        (center) = math.sqrt((self.__center[0] - other.__center[0]) ** 2 + (self.__center[1] - other.__center[1]) ** 2)
        (radii) = (self.__radius + other.__radius)
        return(radii > center)

def main():

    print("\n")
    circle1 = Circle((0, 0), 2)
    circle2 = Circle((4, 0), 3) 
    circle3 = Circle((3, 3), 1)
    a_list = [circle1, circle2, circle3]
    a_list.sort()
    print(a_list)
    print("circle1 and circle2 intersect: ", circle1.intersect(circle2)) # True
    print("circle1 and circle3 intersect: ", circle1.intersect(circle3)) # False
    print("circle2 and circle3 intersect: ", circle2.intersect(circle3)) # True
    print("\n")

if __name__ == "__main__":

    main()

#Done

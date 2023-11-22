import math
def area(r):
    return math.pi*r*r
def perimeter(r):
    return 2*math.pi*r
r=int(input("enter the radius of circle:"))
print("area of a circle:",area(r))
print("area of a perimeter:",perimeter(r))

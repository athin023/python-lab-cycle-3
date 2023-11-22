import graphics.circle
import graphics.rectangle
import graphics.graphics3d.cuboid
import graphics.graphics3d.sphere
r=int(input("enter the radius of circle"))
r1=int(input("enter the radius of sphere"))
leng=int(input("enter the length of rectangle"))
bread=int(input("enter the breadth of rectangle"))
length=int(input("enter the length of cuboid"))
height=int(input("enter the height of cuboid"))
width=int(input("enter the width of cuboid"))
print("Area of circle is ",graphics.circle.area(r))
print("Perimeter of circle is ",graphics.circle.perimeter(r))
print("Area of rectangle is ",graphics.rectangle.area(leng,bread))
print("Perimeter of rectangle is ",graphics.rectangle.perimeter(leng,bread))
print("Area of cuboid is ",graphics.graphics3d.cuboid.area(length,width,height))
print("Perimeter of cuboid is ",graphics.graphics3d.cuboid.perimeter(length,width,height))
print("Area of sphere is ",graphics.graphics3d.sphere.area(r1))
print("Perimeter of sphere is ",graphics.graphics3d.sphere.perimeter(r1))

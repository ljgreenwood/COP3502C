'''
Program A will classify triangles based on their side lengths.
An equilateral triangle has 3 equal sides,
an isosceles triangle has 2 equal sides,
and a scalene triangle has no equal sides.

Input:
Side length 1:
Side length 2:
Side length 3:

Output (one of the following):
This is an equilateral triangle!
This is an isosceles triangle!
This is a scalene triangle!

You may assume:
The sides will form a valid triangle
All inputs will be positive numbers
'''

triangle_1 = float(input("Side length 1: "))
triangle_2 = float(input("Side length 2: "))
triangle_3 = float(input("Side length 3: "))

# checking that all sides are equal
if (triangle_1 == triangle_2) and (triangle_2 == triangle_3):
    print("This is an equilateral triangle!")
# checking that 1=2!=3, 2=3!=1,3=1!=2
elif (triangle_1 == triangle_2) and (triangle_2 != triangle_3) or (triangle_2 == triangle_3) and (triangle_3 != triangle_1) or (triangle_3 == triangle_1) and (triangle_1 != triangle_2):
    print("This is an isosceles triangle!")
else:
    # elif (triangle_1 != triangle_2) and (triangle_2 != triangle_3) and (triangle_1 != triangle_3):
    # if it is not equilateral or isosceles, it is scalene
    print("This is a scalene triangle!")
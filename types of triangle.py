#If the three sides of a triangle are entered through the keyboard write a program to check whether
#the triangle is isosceles , equilateral , scalene or right angled triangle
a=float(input("enter the first side"))
b=float(input("enter the second side "))
c=float(input("enter the third side "))
if a==b and b==c and c==a:
    print("triangle is equilateral triangle")
elif a==b or b==c or a==c:
    print("triangle is isosceles triangle ")
elif a*a==(b*b+c*c) or b*b==(a*a+c*c) or c*c==(b*b+a*a):
    print("the triangle is right angle triangle ")
elif a!=b and b!=c and c!=a:
    print("triangle is scalene triangle")
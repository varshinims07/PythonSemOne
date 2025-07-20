#Write a program to check whether a triangle is valid or not, when three angles of the triangle are entered through the keyboard
a=float(input("enter the first angle "))
b=float(input("enter the second angle "))
c=float(input("enter the third angle "))
if a+b+c==180:
    print("the triangle is valid")
else:
    print("triangle is not valid")
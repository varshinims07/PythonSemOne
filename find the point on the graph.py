#Given a point (x,y) write a program to find out if it lies on the x-axis, y-axis on the origin 
# or in one of the four quadrants
x=float(input("enter the point x "))
y=float(input("enter the point y  "))
if x==0 and y==0:
    print("the point is on the origin")
elif x==0 and y!=0:
    print("the point is on the y axis ")
elif y==0 and x!=0:
    print("the point is on the x axis")        
elif x>0 and y>0:
    print("the point is on the 1st quadrant")    
elif x<0 and y>0:
    print("the point is on the 2nd quadrant")
elif x<0 and y<0:
    print("the point is on the 3rd quadrant")
elif  x>0 and y<0:
    print("the point is on the 4th quadrant")
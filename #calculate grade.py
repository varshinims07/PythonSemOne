#calculate grade 
a=int(input("enter your attendence "))
b=int(input("enter your test percentage"))
if b>=90 and a>=95:
    print("grade A+")
elif b>=80 and  b<89 and a>=90:
    print("grade A")
elif b>=70 and b<79 and a>=85:
    print("grade B")
elif b>=60 and  b<69 and a>=75 and  a<84:
    print("grade C")
else:
    print("grade F")
    
#loan eligibility
a=int(input("enter your age"))
b=int(input("enter your income "))
c=int(input("enter your credit score "))
if a<18 :
    print("not eligible for loan ")
if a>18 or a<60:
    if b>50000 and c>750:
        print("eligible for premium loan")
    elif b>30000 or b<50000 and c>650 or c<750:
        print("eligible for standard loan")
    else:
        print("loan under review")
if a>60:
    print("special senior citizen loan options available ")
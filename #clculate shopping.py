#clculate shopping 
premium_coust=1
regular_coust=0
a=int(input("enter the  shopping payment"))
b=int(input("enter the type of coustomer "))
if a>10000:
    if b==1:
        print("20 percent discount")
        a=a-20/100*a
        print(a)
        if b==0:
            print("10 percent discount ")
            a=a-10/100*a
            print(a)
elif a>5000 and a<=10000:
    if b==1:
        print("15 percent discount")
        a=a-15/100*a
        print(a)
        if b==0:
            print("5 percent discount ")
        a=a-5/100*a
        print(a)
elif a<5000:
    print("no discount available ")
else:
    print("the final amount is ",a)

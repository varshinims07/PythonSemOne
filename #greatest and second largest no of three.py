#greatest and second largest no of three nos 
a=int(input("enter the first no"))
b=int(input("enter the second no"))
c=int(input("enter the third no"))
if a>b and a>c:
    print("a=",a,"is largest")
    if b>c :
        print("b is second largest ")
    else:
            print("c is second largest ")
elif b>a and b>c:
    print("b=",b,"is largest ")
    if a>c:
        print("a is second largest")
    else:
        print("c is second largest")
elif c>a and c>b:
    print("c is largest")        
    if b>a:
        print("b is second largest")
    else:
        print("print a is second largest")
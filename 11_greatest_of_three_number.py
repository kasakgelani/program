a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
if(a>b):
    if(a>c):
        print("the greatest no is:",a)
    else:
        print("the greatest no is:",c)
else:
    if(b>c):
        print("the greatest no is:",b)
    else:
        print("the greatest no is:",c)
        

num = int(input("enter a number :"))
factorial = 1
if num < 0:
    print("factorial does not exist for a negative numbers")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*1
    print(f'the factorial of {num} is {factorial}')

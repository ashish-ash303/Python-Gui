from math import *
try:
    a = int(input("Enter First No. :- "))
except Exception:
    print("Please enter a correct input")
    a = int(input("Enter First No. :- "))
b = int(input("Enter Second No. :- "))
c = int(input("Select numeric option for operation  1.ADD, 2. SUBS,  3. MULTY 4. DIV :- "))

if c == 1:
    result = a+b
    print("Addition of {} and {} is {}").format(a, b, result)
elif c == 2:
    result = a - b
    if result < 0:
        print("Substraction of {} and {} is {}").format(a, b, -1*result)
    else:
        print("Substraction of {} and {} is {}").format(a, b, result)
elif c == 3:
    result = a * b
    print("multiplication of {} and {} is {}").format(a, b, result)
elif c == 4:
    try:
        result = (a / b)
        print("Division of {} and {} is {}").format(a, b, result)
    except ZeroDivisionError:
        print("Number can not be divided by Zero")

else:
    print("Please enter the correct option")

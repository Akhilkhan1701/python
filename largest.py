a,b,c=int(input("Enter the first number: ")), int(input("Enter the second number: ")), int(input("Enter the third number: "))


if (a>b)and (a>c):
    print("The largest number is", a)
elif (b>a) and (b>c):
    print("The largest number is", b)
else:
    print("The largest number is", c)
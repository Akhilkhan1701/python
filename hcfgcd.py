num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

def hcf(num1,num2):
    if num1>num2:
        smaller=num2
    else:
        smaller=num1
    for i in range(1,smaller+1):
        if((num1%i==0) and (num2%i==0)):
            hcf=i
    return hcf
    

print(hcf(num1,num2))
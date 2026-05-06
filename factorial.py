num=int(input("Enter a number: "))

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

c=factorial(num)
print(f"The factorial of {num} is: {c}")
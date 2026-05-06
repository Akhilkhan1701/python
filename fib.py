num=int(input("Enter a number: "))

def fib(n):
    if n<0:
        return "not possible"
    if n==0:
        return 1
    if n==1:
        return 1
    if n>1:
        return fib(n-1)+fib(n-2)
    

c=fib(num)
print(f"The {num}th Fibonacci number is: {c}")


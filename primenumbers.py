start=int(input("Enter a starting number: "))
num=int(input("Enter a number: "))



for i in range(start,num+1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)

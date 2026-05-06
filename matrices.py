a=[[1,5,8],
   [2,3,6],
   [2,4,8]]
b=[[11,5,8],
   [2,3,6],
   [2,5,6]]
c=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]

for d in c:
    print(d)
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[0,0,0],[0,0,0],[0,0,0]]


for i in range(len(a)):
    for j in range(len(a)):
        b[i][j]=a[j][i]

for k in b:
    print(k)
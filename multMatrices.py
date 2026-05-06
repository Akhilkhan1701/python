a=[[2,3,4],[1,0,2],[3,1,5]]
b=[[1,2,0],[3,1,4],[2,0,1]]
c=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]

for l in c:
    print(l)
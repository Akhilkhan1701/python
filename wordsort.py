a="Harry potter and the prisoner of azkaban"

w=a.split()

print(w)

for i in range(len(w)):

    w[i]=w[i].lower()
    # for j in range(i+1,len(w)):
    #    if w[i]>w[j]:
    #       w[i],w[j]=w[j],w[i]

w.sort()   
print(w)
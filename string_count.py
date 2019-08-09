n=str(input("Enter the string"))
le=len(n)
count=0
for i in range(le-1):
    for j in range(le):
        if n[j]==n[i]:
            count=count+1
        else:
            continue    
    print("%s count is :%d"%(n[i],count))
    count=0

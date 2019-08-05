tup=tuple(input("Enter the tuple").split(","))
st=str(input("Enter the value"))
le=len(tup)
ls=[]
for i in range(le):
    if i==le-1:
        ls +=st
        continue
    else:
        ls +=list(tup[i])
print(tuple(ls))        
        
        
        

tup=tuple(input("Enter the tuple").split())
le=len(tup)
st=""
for i in range(le):
    if int(tup.count(tup[i])) >=2:
        st +=tup[i]
    else:
        continue
le1=len(st)
s=round(le1/2)
for i in range(s):
    print(st[i],end="")
            
        
    

    
    
            

n=list(input("Enter the value").split())
le=len(n)
li=[]
for i in range(le):
    if n[i].isdigit():
        li.append(n[i])
    else:
        continue
print(li)    
        

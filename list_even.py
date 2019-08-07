n=int(input("Enter the numbers"))
li=[]
for i in range(n+1):
    if i==0:
        li.append(i)
    elif i%2==0:
        li.append(i)
    else:
        continue
le=len(li)
for i in range(le):
    print(li[i],end=",")
        

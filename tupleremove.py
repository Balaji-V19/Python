st=tuple(input("Enter the tuple").split(","))
le=len(st)
tup=""
s=int(input("enter the index"))
for i in range(le):
    if i==s:
        continue
    else:
        tup +=st[i] +","
    
tp=tuple(tup.split(","))
print(tp)

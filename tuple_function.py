n=(1,2,3,4,5,6,7,8,9,10)
le=len(n)
fst=round(le/2)
print("first half")
for i in range(fst):
    print(n[i],end="")
print("\nSecond half")    
for j in range(fst,le-1):
    print(n[j],end="")

n=str(input("Enter the string"))
n2=str(input("Enter the substring"))
co=0
"""
le=len(n)-1
le2=len(n2)        
for i in range(le,0,-1):
    for j in range(le2):
        if n[i] == n2[j]:
            co+=1
        else:
            continue
print(co)        """
print(n.find(n2))  

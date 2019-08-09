n=list(map(int,input("Enter the 1st list").split(",")))
n2=list(map(int,input("Enter the 2nd list").split(",")))
le=len(n)
le2=len(n2)
if le >= le2:
    for i in range(le):
        for j in range(le2):
            if n[i]==n2[j]:
                print(n[i])
            else:
                continue
else:
    for i in range(le2):
        for j in range(le):
            if n2[i]==n[j]:
                print(n[j])
            else:
                continue
            

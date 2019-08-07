n=list(map(int,input("Enter the string").split(",")))
le=len(n)
val=0
for i in range(le):
    if n[i]%2!=0:
        val=n[i]**2
        print(val)
        
        

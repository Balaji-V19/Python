n=int(input("Enter the limit"))
val=0
for i in range(n+1):
    if i >0:
        val += i/(i+1)
    else:
        continue
print(val)    
    
        

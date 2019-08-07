n=str(input("Enter the string"))
le=len(n)
dig=0
alp=0
for i in range(le):
    if n[i].isdigit():
        dig=dig+1
    elif n[i].isalpha():
        alp=alp+1
    else:
        continue
print("Letters count is : %d"%alp)
print("Digits count is : %d"%dig)
    
        

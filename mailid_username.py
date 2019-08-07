n=str(input("Enter the mail id"))
le=len(n)
st=""
for i in range(le):
    if n[i]=='@':
        break
    else:
        st+=n[i]
print(st)        
        

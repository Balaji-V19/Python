n=int(input("Enter the no of rows"))
n1=int(input("Enter the no of col"))
li=[]
for i in range(n):
    mat=[]
    for j in range(n1):
        mat.append(int(input()))
    li.append(mat)
n2=int(input("Enter the 2nd matrix row"))
n3=int(input("Enter the 2rd matrix col"))
ma=[]
for i in range(n2):
    l=[]
    for j in range(n3):
        l.append(int(input()))
    ma.append(l)
an=[]    
for i in range(n):
    ans=[]
    for j in range(n1):
        ans.append(ma[i][j]+li[i][j])
    an.append(ans)    
        
    
for i in range(n):
    for j in range(n1):
        print(an[i][j],end="")
    print()    
        

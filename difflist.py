def funs(ln):
    l=len(ln)
    b=True
    for i in range(0,l):
        for j in range(i+1,l):
            if ln[i] == ln[j]:
                b=False
                break
    if b:
        print("Different")
    else:
        print("Not Different")
        
             
        
    
ls=list(input("Enter the value").split(","))
funs(ls)

ls=list(input("Enter the list").split(","))
l=len(ls)
if l<3:
    print("Enter more than elements")
else:
    while l>3:
        print("Removed value %s"%ls[2])
        ls.remove(ls[2])
        l=l-1
        
        

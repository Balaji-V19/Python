n=list(map(int,input("Enter the list").split(",")))
le=max(n)
while max(n)==le:
    n.remove(max(n))
print(max(n))    

n=int(input("From number"))
n1=int(input("To number"))
for i in range(n,n1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

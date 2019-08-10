def fibonaci(n):
    if n<=0:
        return "Invalid Value"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)

n=int(input("Enter the value"))
for i in range(1,n+1):
    print(fibonaci(i),end=",")

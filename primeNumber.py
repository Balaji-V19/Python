n=int(input("Enter the number"))
for i in range(2,n):
    if n%i ==0:
        print("Not Prime number")
        break
else:
    print("Prime Number")

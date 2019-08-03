ls=str(input("Enter the list"))
l1=list(ls.split(","))
n=input("Enter the string to search")
if n in l1:
    print("True")
else:
    print("False")

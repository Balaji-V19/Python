st=str(input("Enter the list "))
li=list(st.split(","))
print("1.find the count \n 2.append to the particular index")
ch=int(input("Enter the option"))
if ch==1:
    n2=str(input("Enter the number to count"))
    ct=li.count(n2)
    print("Count of the list %d"%ct)
else:
    n3=int(input("Enter the number to append"))
    n4=int(input("Enter the index"))
    li.insert(n4,n3)
    print("Inserted successfully")

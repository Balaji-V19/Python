import array as arr
n=int(input("Enter the number"))
n2=int(input("Enter the number"))
a=arr.array('i',[])
b=arr.array('i',[])
for i in range(n):
    a.append(int(input("Enter the numbers")))
for j in range(n2):
    b.append(int(input("Enter the numbersss")))
ls=str(list(a))
ls2=str(list(b))
print(ls)
print(ls2)
if ls.find(ls2)!=-1:
    print("No")
else:
    print("Yes")

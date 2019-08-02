st=str(input("Enter the string"))
l=len(st)
i=l-1
s1=""
while i>=0:
    s1+=st[i]
    i=i-1
if st==s1:
    print("Palindrome")
else:
    print("Not palindrome")

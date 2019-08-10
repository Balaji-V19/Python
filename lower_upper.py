n=str(input("Enter the string"))
le=len(n)
for i in range(le):
    if n[i].isupper():
        print(n[i].lower(),end="")
    else:
        print(n[i].capitalize(),end="")

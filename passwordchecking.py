import re
n=list(input("Enter the password here").split(","))
le=len(n)
for i in range(le):
    if len(n[i]) >6:
        if re.search("[a-z]",n[i]):
            if re.search("[A-Z]",n[i]):
                if re.search("[@#$%&^*]",n[i]):
                    if re.search("[0-9]",n[i]):
                        print("valid pswd is:",n[i])
    else:
        print("InValid")

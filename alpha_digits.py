n=input("Enter the string")
fst=0
snd=0
trd=0
fth=0
fith=0
le=len(n)
for i in range(le):
    if n[i].isalnum():
        fst=1
    if n[i].isalpha():
        snd=1
    if n[i].isdigit():
        trd=1
    if n[i].islower():
        fth=1
    if n[i].isupper():
        fith=1
if fst==1:
    print("True")
else:
    print("False")
if snd==1:
    print("True")
else:
    print("False")    
if trd==1:
    print("True")
else:
    print("False")    
if fth==1:
    print("True")
else:
    print("False")    
if fith==1:
    print("True")
else:
    print("False")    
        
    
    

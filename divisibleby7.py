s=2000
e=3200
for i in range(s,e+1):
    if i%7!=0 and i%5==0:
        continue
    else:
        print(i)

dic=dict(d=0,w=0)
#print(dic)
while True:
    val=list(input("Enter the cmd").split())
    le=len(val)
    if le==0:
        break
    if le >2:
        print("Enter valid cmd")
    else:
        if str(val[0])=='d':
            dic['d']+=int(val[1])
        elif val[0]=='w':
            dic['w']+=int(val[1])
        else:
            break
res=int(dic['d']) - int(dic['w'])
print(res)
        
    

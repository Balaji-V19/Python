"""n={"name":345,"no":123,"add":3456}
j=0
for i in n.values():
    #print(i)
    j += int(i)
    
print(j)    """

n={"name":"balaji","no":345,"address":"dfg"}
j=""
for i in n.values():
    j += str(i)
print(j)    

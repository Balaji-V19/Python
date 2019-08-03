

n=str(input("enter the from date:(YYYY,MM,DD) -- "))
li1=list(n.split(","))
n1=str(input("Enter the to date:(YYYY,MM,DD)-- "))
li2=list(n1.split(","))
if li2[0] != li1[0]:
    li2[0]=str(int(li2[0]) - int(li1[0]))
    print("%s years"%li2[0])
    if li2[1] !=li1[1]:
        if li2[1] >= li1[1]:
            li2[1]=str(int(li2[1]) - int(li1[1]))
            print("%s months"%li2[1])
            if li2[2] != li1[2]:
                if li2[2] >= li1[2]:
                    li2[2]=str(int(li2[2]) - int(li1[2]))
                    print("%s Days"%li2[2])
                elif li2[2] < li1[2]:
                    li2[2]=str(int(li1[2])-int(li2[2]))
                    print("%s Days" %li2[2])
                else:
                    print("%s Days"%li2[2])
        elif li2[1] < li1[1]:
            li2[1]=str(int(li1[1])-int(li2[1]))
            print("%s months"%li1[2])
            if li2[2] != li1[2]:
                if li2[2] >= li1[2]:
                    li2[2]=str(int(li2[2]) - int(li1[2]))
                    print("%s Days"%li2[2])
                elif li2[2] < li1[2]:
                    li2[2]=str(int(li1[2])-int(li2[2]))
                    print("%s Days" %li2[2])
                else:
                    print("%s Days"%li2[2])
        else:
            print("%s months" %li2[1])
            if li2[2] != li1[2]:
                if li2[2] >= li1[2]:
                    li2[2]=str(int(li2[2]) - int(li1[2]))
                    print("%s Days"%li2[2])
                elif li2[2] < li1[2]:
                    li2[2]=str(int(li1[2])-int(li2[2]))
                    print("%s Days" %li2[2])
                else:
                    print("%s Days"%li2[2])
                   
                   
else:
    print("Finished Successfully") 

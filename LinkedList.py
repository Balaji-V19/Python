class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

        """ Linked list manipulation in starting position"""
    def addAtBeggin(self,d):
        new=Node(d)
        new.next=self.head
        self.head=new
    def delatbeggin(self):
        temp=self.head
        self.head=self.head.next
        temp.next=None
        """ print the linked list"""
    def printnode(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"==>",end=" ")
            temp=temp.next
        print("None")

        """ linked list manipulation in middle"""
    def DeleteAtMiddle(self,pos):
        temp=self.head
        while temp.next.data !=pos:
            temp=temp.next
        if temp.next.data==pos:
            temp.next=temp.next.next
            pos=None
    def InsertAtMiddle(self,data,pos):
        temp=self.head
        while temp.data!=pos:
            temp=temp.next
        if temp.data==pos:
            new=Node(data)
            new.next=temp.next
            temp.next=new

            """ Linked list manipulation in end"""
    def InsertAtEnd(self,data):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        if temp.next==None:
            new=Node(data)
            temp.next=new
    def DeleteAtEnd(self):
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        if temp.next.next==None:
            temp.next=None
            
            
            
ob1=LinkedList()
ch=0
while ch<8:
    print("\n 1.add at beggining \n 2.delete at beggining\n 3.print the list \n 4.InsertatMiddle \n 5.Delete At Middle \n 6.Add at end \n 7.delete at end \n 8.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        dt=input("Enter the value to add")
        ob1.addAtBeggin(dt)
        ob1.printnode()
    elif ch==2:
        ob1.delatbeggin()
        ob1.printnode()
    elif ch==3:
        ob1.printnode()
    elif ch==4:
        dt=input("Enter the value to Insert")
        po=input("Enter the position")
        ob1.InsertAtMiddle(dt,po)
        ob1.printnode()
    elif ch==5:
        po=input("Enter the position")
        ob1.DeleteAtMiddle(po)
        ob1.printnode()
    elif ch==6:
        po=input("Enter the value to insert")
        ob1.InsertAtEnd(po)
        ob1.printnode()
    elif ch==7:
        ob1.DeleteAtEnd()
        ob1.printnode()
    else:
        break
        

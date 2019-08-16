class Stack:
    def __init__(self):
        self.Stack=[]
    def Push(self,data):
        if data not in self.Stack:
            self.Stack.append(data)
            return True
        else:
            return False
    def Pop(self):
        if len(self.Stack)<=0:
            return ("No element")
        else:
            return self.Stack.pop()
s=Stack()
ch='Y'
while ch=='Y':
    inp=input("Enter the value")
    s.Push(inp)
    ch=input("Do you want to continue (Y/N)")
print(s.Pop())

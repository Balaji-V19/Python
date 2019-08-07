def funct():
    print("function working")
    try:
        x=5/0
    except (ZeroDivisionError,NameError):
        print("Error Handled")
    else:
        print("Execute")
funct()        

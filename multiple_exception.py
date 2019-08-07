try:
    print(x)
    print(2/0)
except (ZeroDivisionError , NameError):
    print("Error Handler")
else:
    print("Not contain error")

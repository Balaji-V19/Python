n=int(input("Enter the year"))
if n%4==0:
    print("Leap year")
    if n%100==0:
        print("Not Leap Year")
        if n%400==0:
            print("Leap year")
else:
    print("Not Leap year")

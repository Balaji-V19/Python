from itertools import permutations
n=list(map(int,input("Enter the no's").split(",")))
per = permutations(n)
for i in list(per):
    print(i)

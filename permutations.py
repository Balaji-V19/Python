from itertools import permutations
n=list(input("Enter the list to purmutate").split(","))
per=permutations(n)
for i in list(per):
    print(i)

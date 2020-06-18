from itertools import permutations

l=list(input("Enter any list\n"))
k=int(input("Enter the sublist length\n"))
for i in range(0,len(l),k):
    i=list(permutations(l[i:i+k]))
    print(i)
    
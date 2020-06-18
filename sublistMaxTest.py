l1=list(input("Enter the list"))
k=int(input('Enter the subarray length'))
l2=[]
for i in range(0,len(l1)-k+1):
    l3=list(l1[i:i+k])
    l2.append(max(l3))
print(l2)
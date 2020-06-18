s=input('Enter a sentence\n')
l=s.split(' ')
lis=[]
for i in l:
    if i not in lis:
        lis.append(i)
print(str(lis))
    
    
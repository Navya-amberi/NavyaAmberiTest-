s=input('Enter any plaindrome')
flag=0
for i in range(int(len(s)/2)):
    if s[i]!=s[len(s)-i-1]:
        flag=1
if flag==1:
    print('Not a palindrome')
else:
        print('palindrome')
def isPrime(num):
    for i in range(2,num):
        if (num%i)==0:
            return False
    return True
n=int(input('Enter any number\n'))
for i in range(2,n):
    if(isPrime(i) and isPrime(n-i)):
        print(i,n-i)
    

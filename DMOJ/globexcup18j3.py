def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2==0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1 , 2):
        if n%i==0:
            return False    

    return True

def sumDigits(n):
    a = sum(int(j) for j in list(str(n)))
    return a

size = int(input())
count = 0
for i in range(size):
    num = int(input())
    if isPrime(num) and isPrime(sumDigits(num)):
        count += 1
print(count)
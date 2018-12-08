num = int(input())
notPrime = True

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i*i < n:
        if n % i == 0:
            return False
        i += 1
    return True

while notPrime:
    if isPrime(num):
        print(num)
        break
    num += 1
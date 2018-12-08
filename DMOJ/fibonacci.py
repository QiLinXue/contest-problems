import math
a = (1+math.sqrt(5))/2
b = (1-math.sqrt(5))/2

def fib(n):
    return (a**n-b**n)/math.sqrt(5)

print(round(fib(int(input())) % 1000000007))
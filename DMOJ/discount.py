import sys
raw_input = sys.stdin.readline
a = raw_input().split(" ")
size = int(a[0])
budget = int(a[1])

counter = 0
for i in range(size):
    a = raw_input().split(" ")
    if int(a[0])*(100-int(a[1]))/100 <= budget:
        counter += 1

print(counter)
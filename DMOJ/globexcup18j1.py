size = int(input())
count = 0
for j in range(size):
    i = input()
    if int(float(i)) == (float(i))-0.5:
        count += 1
    elif round(float(i)) == int(float(i))+1:
        count += 1
print(count)
print(size-count)
import sys
raw_input = sys.stdin.readline
size = int(raw_input())
nums = []

for i in range(size):
    nums.append(int(raw_input()))

import collections
counts = sorted(list(collections.Counter(nums).items()),key=lambda x: x[1],reverse=True)

maxCount = counts[0][1]
maxCount2 = -1
numMax = 0
numMax2 = 0

maxArr = []
maxArr2 = []

for i in counts:
    if i[1] == maxCount:
        numMax += 1
        maxArr.append(i[0])
    elif maxCount2 == -1:
        maxCount2 = i[1]
        numMax2 += 1
        maxArr2.append(i[0])

    elif i[1] == maxCount2:
        numMax2 += 1
        maxArr2.append(i[0])
    
    else:
        break

if numMax > 1:
    print(max(maxArr)-min(maxArr))

else:
    highest = counts[0][0]
    a = abs(highest-max(maxArr2))
    b = abs(highest-min(maxArr2))
    print(max(a,b))


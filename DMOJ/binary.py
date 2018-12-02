size = int(input())
nums = []
for i in range(size):
    a = int(input())
    nums.append(a)
for num in nums:
    binRep = bin(num)[2:]

    if len(binRep) % 4 == 1:
        binRep = ('000' + binRep)
    if len(binRep) % 4 == 2:
        binRep = ('00' + binRep) 
    if len(binRep) % 4 == 3:
        binRep = ('0' + binRep) 
    binRep = [binRep[i:i+4] for i in (range(0, len(binRep), 4))]
    print(' '.join(binRep))

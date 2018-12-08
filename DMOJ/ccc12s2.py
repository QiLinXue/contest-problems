arom = input()

keys = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}
sum = 0
for i in range(0,len(arom)-1,2):
    c = int(arom[i])
    v = keys[arom[i+1]]
    sign = 1
    if i < len(arom)-2 and keys[arom[i+3]] > v:
        sign = -1
    sum += sign * c * v
print(sum)
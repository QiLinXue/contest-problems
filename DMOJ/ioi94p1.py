size = int(input())
tri = []
for i in range(size):
    tri.append([int(a) for a in input().split()])

newTri = tri.copy()

for y in range(0,len(tri)-1):
    for x in range(len(tri[y])):
        if(tri[y][x] + tri[y+1][x] > newTri[y+1][x]):
            if(x == 0): newTri[y+1][x] += tri[y][x]
            else: newTri[y+1][x] += max(tri[y][x] , tri[y][x-1])
    newTri[y+1][x+1] += tri[y][x]

print(max(tri[len(tri)-1]))

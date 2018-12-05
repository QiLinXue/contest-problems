import statistics
num = int(input())
coor = [[int(i[0]),int(i[1])] for i in [input().split() for j in range(num)]]
minX, minY = statistics.median([i[0] for i in coor]), statistics.median([i[1] for i in coor])
print(int(sum((abs(i[0]-minX)+abs(i[1]-minY)) for i in coor)))

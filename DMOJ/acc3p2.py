# Too slow, timeout error

# (1) Get Input
num = int(input())
coor = []
for i in range(num):
    coor.append(input().split())

# (2) Create grid that can fit the kings and that starts at 0
lowestX = min(int(i[0]) for i in coor)
highestX = max(int(i[0]) for i in coor)
lowestY = min(int(i[1]) for i in coor)
highestY = max(int(i[1]) for i in coor)

xRange = highestX-lowestX+1
yRange = highestY-lowestY+1

megaBoard = [[0] * xRange] * yRange

# (3) Reassign the coordinates so smallest is at (0,0)
xDiff = xRange-highestX-1
yDiff = yRange-highestY-1

updatedCoor = []
for row in coor:
    updatedCoor.append([int(row[0])+xDiff,int(row[1]) + yDiff])

# (4) A King Class
class King:
    def __init__(self,x,y,board):
        self.x = x
        self.y = y
        self.board = board.copy()
        self.moveBoard = []
        self.createBoard()

    def createBoard(self):
        for j in range(0,len(self.board)):
            oneDirection = []
            for i in range(0,len(self.board[0])):
                oneDirection.append(max(abs(i-self.x),abs(j-self.y)))
            self.moveBoard.append(oneDirection)

    def display(self):
        print(self.moveBoard)

# Create a list of all the kings
kingList = []
for king in updatedCoor:
    kingList.append(King(king[0],king[1],megaBoard))

# Sum up the value of all the king's "min moves to each square"
mBoard = []
for i in range(0,len(megaBoard)):
    tempSum2 = []
    for j in range(0,len(megaBoard[i])):
        tempSum = 0
        for king in kingList:
            tempSum += king.moveBoard[i][j]
        tempSum2.append(tempSum)
    mBoard.append(tempSum2)

# Find the Minimum
minimum = -1
for row in mBoard:
    if minimum == -1 or minimum > min(row):
        minimum = min(row)
print(minimum)
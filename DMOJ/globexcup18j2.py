import statistics
num = int(input())
marks = [int(i) for i in input().split()]
s = statistics.mean(marks)
if sum(1 for j in marks if j > s) > num/2:
    print("Winnie should take the risk")
else:
    print("That's too risky")
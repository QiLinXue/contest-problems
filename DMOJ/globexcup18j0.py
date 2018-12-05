numSell = int(input().split(" ")[1])
print(sum(sorted([int(i) for i in input().split(" ")])[numSell:]))
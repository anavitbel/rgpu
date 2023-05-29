a = []
for _ in range(4):
    a.append([int(x) for x in input().split()])
row, col = [int(x) for x in input().split()]
if row == 0:
    if col == 0:
        s = a[row - 1][col] + a[row + 1][col] + a[row][col - 1] + a[row][col + 1]
print(s)
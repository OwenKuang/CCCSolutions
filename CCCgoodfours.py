x = int(input())
count = 0
for i in range(x//5, -1, -1):
    j = (x - 5 * i) // 4
    if 5 * i + 4 * j == x:
        count += 1
print(count)

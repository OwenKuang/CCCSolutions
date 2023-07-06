c, r = map(int, input().split())
x, y = 0, 0
a = 1
b = 1
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break 
    if x + a > c:
        x =c
    elif x + a < 0: 
        x = 0
    else:
        x += a
    if y + b > r:
        y  = r
    elif y + b < 0:
        y = 0
    else:
        y += b
    print(x, y)
    
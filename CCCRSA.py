x = int(input())
y = int(input())
rsa = 0 
for i in range(x, y + 1):
    count = 0 
    for j in range(1, i + 1 ):
        if i % j == 0:
            count += 1
    if count == 4:
        rsa += 1

print("The number of RSA numbers between" , x , "and" , y , "is" , rsa)
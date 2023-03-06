import math
obser = int(input())
speed = 0 
fastest = 0 
y = []
t = []
d = [] 

for i in range(obser):
   x = input()
   x = x.split()
   y.append(x)

y = sorted(y, key=lambda x: int(x[0]))
for i in y:
    t.append(i[0])
    d.append(i[1]) 
   
for i in range (len(t) - 1):
    time = abs(int(t[i]) - int(t[i+1]))
    distance = abs(int(d[i]) - int(d[i+1]))
    speed = distance / time 
    if speed >= fastest:
        fastest = speed
    else:
        continue 
print(fastest)
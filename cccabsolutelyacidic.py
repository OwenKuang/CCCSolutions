x = int(input())
freqs = [0 for _ in range(1001)]

for i in range(x):
    read = int(input())
    freqs[read] += 1

highest = max(freqs)
values = []

if freqs.count(highest) >= 2:
    for i in range(len(freqs)):
        if freqs[i] == highest: 
            values.append(i)
    print((abs(min(values) - max(values))))
else:
    for i in range(len(freqs)):
        if int(freqs[i]) == highest:
            highestval = i
            freqs[i] = 0
    
    for i in range(len(freqs)):
        if freqs[i] == max(freqs):
            values.append(i)
    print(max(abs( highestval - min(values)), abs(highestval - max(values))))
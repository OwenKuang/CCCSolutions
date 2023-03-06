p = int(input())
g = int(input())
r = int(input())
o = int(input())
total = int(input())
cnt = 0
min_tickets = total
for i in range(total//p + 1):
    for j in range(total//g + 1):
        for k in range(total//r + 1):
            for l in range(total//o + 1):
                s = i*p + j*g + k*r + l*o
                if s == total:
                    print("# of PINK is", i, "# of GREEN is", j, "# of RED is", k, "# of ORANGE is", l)
                    cnt += 1
                    min_tickets = min(min_tickets, i+j+k+l)
print("Total combinations is", cnt, end="",)
print(".")
print("Minimum number of tickets to print is", min_tickets, end="")
print(".")

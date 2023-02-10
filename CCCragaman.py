from string import ascii_lowercase
fatal = 0
margin = 0 
firstlist = []
secondlist = []
first = input()
second = input()
howmanyerror = second.count("*")

for i in ascii_lowercase:
    a = first.count(i)
    firstlist.append(a)
    b = second.count(i)
    secondlist.append(b)

for i in range(len(firstlist)):
    if firstlist[i] < secondlist[i]:
        fatal += 1
    elif firstlist[i] != secondlist[i]:
        margin += 1


if fatal != 0:
    print("N")
elif margin <= howmanyerror:
    print("A")
else:
    print("N")
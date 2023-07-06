"""x = int(input())
y = []
number = 0
count = 0
for i in range(x):
    y.append([])
z = 1
next1 = 100
limit = 0
emptylist = []
counter = 0
while number != z :
    val = int(input())
    if next1 == 100:
        limit = val

    elif next1 == 1:
        count += 1
        limit = val
    
    next1 = 0 

    if val == 1 and count + 1 < x :
        next1 = 1
    
    if count + 1 == x:
        if val not in y[count]:
            counter += 1
        
    if counter == limit:
        number = z
    y[count].append(val)
    if counter == limit:
        number = z

print(y)
for i in range(len(y)):
    indexnumber = 1
    lakelist = []
    branchlist = []
    for j in range(len(y[i])):

        branchlist.append(y[i][len(y[i]) - j  - 1])
        
        if y[i][len(y[i]) - j  - 1] == indexnumber:
            lakelist.append(y[i][len(y[i]) - j  - 1] )
        if len(branchlist) > 0 and branchlist[len(branchlist) - 1] == indexnumber:
            lakelist.append(branchlist[len(branchlist) - 1])
            branchlist.remove(branchlist[len(branchlist) - 1])
        if len(branchlist) > 0  and  len(lakelist) > 0 and branchlist[len(branchlist) - 1] == lakelist[len(lakelist) - 1]:
            lakelist.append(branchlist[len(branchlist) - 1])
            branchlist.remove( branchlist[len(branchlist) - 1])
        if len(branchlist) > 0  and  len(lakelist) > 0 and branchlist[len(branchlist) - 1] == lakelist[len(lakelist) - 1] + 1:
            lakelist.append(branchlist[len(branchlist) - 1])
            branchlist.remove( branchlist[len(branchlist) - 1])
    print(y[i])
    print(lakelist)
    print(branchlist)
    if branchlist == []:
        print("Y")
    else:
        print("N")

for i in range(len(y)):
    indexnumber = 1
    lakelist = []
    branchlist = []
    ordered = z.sort()
    for j in range(len(y[i])): 
        
        lastindex = len(y[i]) - 1
        branchlist.append(y[i][lastindex])
        lastbindex = len(branchlist) - 1
        y[i].remove(y[i][lastindex])
        if y[i] != [] and y[i][lastindex - 1] == indexnumber - 1:
            y[i].remove(y[i][lastindex -  1])
        elif branchlist[lastbindex] == indexnumber :
            branchlist.remove(branchlist[lastbindex])
            indexnumber += 1
   
    if y[i] == [] and branchlist == []:
        print("Y")
    else:
        print("N")
"""
"""
for i in range(len(y)):
    indexnumber = 1
    branchlist = []
    for j in range(len(y[i]) - 1): 

        lastindex = len(y[i]) - 1
        
        if y[i][lastindex] == indexnumber:
            y[i].pop(lastindex)
            indexnumber += 1
        elif branchlist != [] and branchlist[len(branchlist) - 1] == indexnumber:
            z = branchlist.remove(branchlist[len(branchlist) - 1])

            indexnumber += 1
        elif y[i][lastindex] != indexnumber:
            branchlist.append(y[i][lastindex])
            z = y[i].pop(lastindex)
        else:
            break
        print(branchlist)
        print(y[i])
    if branchlist == [] and y[i] == []:
        print("Y")
    else:
        print("N")
        
"""
x = int(input())
for i in range(x):
    mt = []
    finished = 0
    indexnumber = 1
    branchlist = []
    lennums = int(input())
    for j in range(lennums):
        ing = int(input())
        mt.append(ing)

    while finished == 0:
        lastindex = len(mt) - 1
        if len(mt) != 0 and mt[lastindex] == indexnumber:
            mt.pop()
            indexnumber += 1
        
        elif len(branchlist) != 0 and branchlist[len(branchlist) - 1] == indexnumber:
            branchlist.pop()
            
            indexnumber += 1
        elif len(mt) != 0 and mt[lastindex] != indexnumber:
           
            branchlist.append(mt[lastindex])
            mt.pop()
        else:
            break
        if len(mt) == 0 and len(branchlist) == 0:
            finished = 1
    if len(branchlist) == 0 and len(mt) == 0:
        print("Y")
    else:
        print("N")
    
        
        


import os


# Bracking file to smaller ones 
with open("inputfile.txt") as fileinput:
    numfiles = 0
    for (i, line) in enumerate(fileinput):
        with open(f"file{numfiles}.txt", "a") as fileout:
            fileout.write(line)
            if os.path.getsize(f"file{numfiles}.txt") > 200_000_000:
                numfiles += 1


# Sorting each file 
elem = [0 for i in range(0, numfiles + 1)]
for num in range(0, numfiles + 1):
    values = dict()
    with open(f"file{num}.txt", "r") as file:
        for line in file:
            line = line.strip(' \n')
            lst = list(line.split(" "))
            for i in lst:
                if int(i) in values.keys():
                    values[int(i)] += 1
                    elem[num] += 1
                else:
                    values[int(i)] = 1
                    elem[num] += 1
    with open(f"file{num}.txt", "w") as file:
        item, number =0, 0
        while item < elem[num]:
            if number in values.keys():
                for j in range(0, values[number]):
                    file.write(f"{str(number)}\n")
                    item += 1
            number += 1


# Merging files together
lst = [None for i in range(0, numfiles + 1)]
curindex = [0 for i in range(0, numfiles + 1)]
for num in range(0, numfiles + 1):
    with open(f"file{num}.txt", "r") as f:
        lst[num] = int(f.readline().strip(" \n"))
with open("outfile.txt","w") as file:
    while True:
        i = lst.index(min(lst))
        file.write(f"{lst[i]}\n")
        curindex[i] += 1
        if curindex[i] >= elem[i]:
            lst[i] = 10000001                        # biggest element in file
        
        else:
            with open(f"file{i}.txt","r") as ff:
                a = ff.read().split('\n')
                lst[i] = int(a[curindex[i]])
        if  [10000001] * len(lst) == lst:
            break


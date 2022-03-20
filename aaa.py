from sort import numfiles
lst=[None for i in range(0,numfiles+1)]
for num in range(0,numfiles+1):
    with open(f"file{num}.txt", "r") as f:
        lst[num]=f.readline().strip(" \n")




pass

#########################
# Bracking file to smaller ones 
#########################

with open("inputfile.txt")as fileinput:
    chunk_size = 125
    for (i, line) in enumerate(fileinput):
        numfiles=int(i/chunk_size)
        with open(f"file{int(i/chunk_size)}.txt", "a") as fileout:
            fileout.write(line)
        lastline_no=i+1


#########################
# Sorting each file 
#########################

for num in range(0,numfiles+1):
    dct=dict()
    with open(f"file{num}.txt", "r") as file:
        for line in file:
            line = line.strip(' \n')
            lst = list(line.split(" "))
            for i in lst:
                try: dct[int(i)] += 1
                except: dct[int(i)] = 1
    with open(f"file{num}.txt", "w") as file:
        item,number =0,0
        k=4000;                                       # fileum gtnvox 
        if num==numfiles: k=lastline_no%125*32        # elementneri qanak
        while item<k:
            if number in dct.keys():
                for j in range(0, dct[number]):
                    file.write(f"{str(number)} ")
                    item+=1
                    if item%32==0:
                        file.write("\n")
            number+=1


#########################
# Merging files together 
#########################
#########################
# Bracking file to smaller ones 
#########################


with open("inputfile.txt")as fileinput:
    chunk_size = 125
    for (i, line) in enumerate(fileinput):
        numfiles=int(i/chunk_size)
        with open(f"file{int(i/chunk_size)}.txt", "a") as fileout:
            fileout.write(line)


#########################
# Sorting each file 
#########################

for num in range(0,numfiles+1):
    values=dict()
    elem=0
    with open(f"file{num}.txt", "r") as file:
        for line in file:
            line = line.strip(' \n')
            lst = list(line.split(" "))
            for i in lst:
                if int(i) in values.keys():
                    values[int(i)] += 1
                    elem+=1
                else:
                    values[int(i)] = 1
                    elem+=1
    with open(f"file{num}.txt", "w") as file:
        item,number =0,0
        while item<elem:
            if number in values.keys():
                for j in range(0, values[number]):
                    file.write(f"{str(number)}\n")
                    item+=1
            number+=1


#########################
# Merging files together 
#########################

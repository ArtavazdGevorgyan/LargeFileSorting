#from sort import numfiles
numfiles,n=1,0
for num in range(0,numfiles):
    n+=1
    with open (f"file{num}.txt","r") as file1, open(f"file{num+1}.txt","r") as file2:
        with open(f"f{n}.txt","w") as file:
            for line in file1:
                item1 = int(line.strip(' \n'))
                for line2 in file2:
                    item2 = int(line2.strip(' \n'))
                    if item1>item2:
                        file.write(f"{str(item2)}\n")
                    else:
                        file.write(f"{str(item1)}\n")
                        break

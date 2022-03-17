import random
#import os

with open("inputfile.txt", "w") as file:
    for line in range(0, 2585):
        for i in range(0, 32):
            file.write(str(random.randint(0, 9999)) + " ")
        file.write("\n")

#print(os.path.getsize("input.txt"))

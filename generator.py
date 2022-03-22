import random
import os

with open("inputfile.txt", "w") as file:
    while os.path.getsize("inputfile.txt")<4_000_000_000:
        for i in range(0, 32):
            file.write(f"{str(random.randint(0, 9_999_999))} ")
        file.write("\n")

#print(os.path.getsize("input.txt"))

import os
os.listdir("testFolder")

file = "A.txt"
file.endswith(".txt")

for file in os.listdir("testFolder"):
    if file.endswith(".txt"):
        print(file)



import os
import shutil

os.mkdir("mvFolder")

for file in os.listdir("testFolder"):
    if file.endswith(".txt"):
        path = "testFolder" + "/" + file
        shutil.move(path,"mvFolder")
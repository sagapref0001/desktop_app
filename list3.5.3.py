import os

try:
    os.mkdir("newfolder")
except(FileExistsError):
    print("error")
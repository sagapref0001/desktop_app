import os
try:
    os.mkdir("test.txt")
except(FileExistsError):
    print("エラー！！")
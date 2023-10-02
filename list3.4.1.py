import shutil
import os

# ファイルの読み込み
with open("test.txt", "r") as file:
    v = file.read()

# 条件分岐によるファイルの移動
if len(v) != 0:
    os.mkdir("txtfolder")
    shutil.move("test.txt","txtfolder")
else:
    os.remove("test.txt")
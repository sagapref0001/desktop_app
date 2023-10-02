import os

#フォルダの作成
try:
    os.mkdir("newfolder"/"subfolder")
except:
    print("error")

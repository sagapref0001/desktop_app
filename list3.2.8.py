import os
import shutil

# テキストファイルの削除
os.remove("newfolder/test.txt")
# フォルダの削除
shutil.rmtree("newfolder")

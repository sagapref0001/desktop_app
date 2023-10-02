import os
# 条件分岐によるファイル作成
if os.path.exists("newfolder"):
    print("既にフォルダが存在します。")
else:
    os.mkdir("newfolder")
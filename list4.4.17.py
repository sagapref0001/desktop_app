import tkinter as tk
from tkinter import filedialog

# ウインドウの作成
root = tk.Tk()

# フォルダの選択
def browse_func():
    # グローバル変数の宣言
    global dir_path
    # ステータスの更新
    statusbar["text"] = "Here we go!!"
    # 整理するフォルダのパス
    dir_path = filedialog.askdirectory()
    for file in os.listdir(dir_path):
        path = dir_path + "/" + file
        shutil.move(path,save_path)

def run_func():
    try:
        # ファイルを移動するフォルダのパス
        Save_path = filedialog.askdirectory()
        for file in os.listdir(dir_path):
            path = dir_path + "/" + file
            shutil.move(path,save_path)
        # ステータス更新
        statusbar["text"] = "Done!!"
    except:
        statusbar["text"] = "Error!!"

# フォルダパスの出力
print(dir_path)

# ウインドウ状態の維持
root.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import shutil

# 関数
# Browse...
def browse_func():
    # グローバル変数の宣言
    global dir_path
    # ステータスの更新
    statusbar["text"] = "Here We go!!"
    # 整理するフォルダのパス
    dir_path = filedialog.askdirectory()

# RUN
def run_func():
    try:
        # ファイルを移動するフォルダのパス
        save_path = filedialog.askdirectory()
        # 拡張子の判別とファイルの移動
        for file in os.listdir(dir_path):
            if file.endswith(cb.get()):
                path = dir_path + "/" + file
                shutil.move(path,save_path)
        # ステータスの更新
        statusbar["text"] = "Done!!"
    except:
        # ステータスの更新
        statusbar["text"] = "Error!!"

# GUI
# ウインドウの作成
root = tk.Tk()
# ステータスバー設置
statusbar = tk.Label(root,text = "Here we go!!",bd=1,relief=tk.SUNKEN,anchor=tk.W)
statusbar.pack(side=tk.BOTTOM,fill=tk.X)
# 実行ボタン
run_button = tk.Button(root,text="RUN",command=run_func)
run_button.pack(padx=10,ipadx=20,side=tk.BOTTOM)
# ラベルフレーム
frame = ttk.LabelFrame(root,text="Select Extension",padding=10)
frame.pack(padx=20,pady=5,side=tk.BOTTOM)
# コンボボックス
extensions = [".docx",".py",".txt",".xlsx",".zip"]
cb = ttk.Combobox(frame,values=extensions)
cb.pack(side=tk.LEFT)
# 参照ボタン
browse_button = tk.Button(frame,text="Browse...",command=browse_func)
browse_button.pack(padx=10,side=tk.LEFT)
# ウインドウ状態の維持
root.mainloop()


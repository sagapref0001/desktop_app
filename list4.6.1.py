import tkinter as tk
from tkinter import ttk

# GUI
# ウインドウの作成
root = tk.Tk()

# フレーム
frame = ttk.Frame(root,padding=5)
frame.pack(padx=5,pady=5)

# テキストボックス
txtbox = tk.Text(frame,width=60,height=20)

# スクロールバー作成
yscroll = tk.Scrollbar(frame,orient=tk.VERTICAL,command=txtbox.yview)
txtbox["yscrollcommand"] = yscroll.set
yscroll.pack(side=tk.RIGHT,fill=tk.Y)

# テキストボックスの配置
txtbox.pack()

root.mainloop()
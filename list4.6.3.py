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

# メニューバーの作成
menubar = tk.Menu(root)
root.configure(menu=menubar)
# Fileメニュー
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label = "File",menu=filemenu)
# Fileメニューの内容
filemenu.add_command(label= "Open...")
filemenu.add_command(label = "Save as...")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=lambda :root.destroy())

# Helpメニュー
helpmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)

# >Manual
helpmenu.add_command(label="Manual")

# 定型文のボタン設置
fp_button = tk.Button(root,text="Fixed Phrase")
fp_button.pack(padx=10,pady=10,ipady=5,fill=tk.X)

root.mainloop()
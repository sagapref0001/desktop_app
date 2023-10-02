import tkinter as tk
from tkinter import ttk

# ウインドウの作成
root = tk.Tk()

# ラベルフレーム
frame = ttk.LabelFrame(root,text= "Launcher",padding=10)
frame.grid(row= 0, column= 0, padx= 15, pady= 15)

# ボタン
run_button1 = tk.Button(frame, text= "RUN1")
run_button1.grid(row= 0, column= 0, padx= 5)

run_button2 = tk.Button(frame, text= "RUN2")
run_button2.grid(row= 0, column= 1, padx= 5)

# メニューバーの作成
menubar = tk.Menu(root)
root.configure(menu = menubar)

# Fileメニュー
filemenu = tk.Menu(menubar, tearoff= 0)
menubar.add_cascade(label = "File", menu = filemenu)

# >Setting
filemenu.add_command(label = "Setting")

# セパレータ
filemenu.add_separator()
# >Exit
filemenu.add_command(label = "Exit")

# HELPメニュー
helpmenu = tk.Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "Help", menu= helpmenu)

# ウインドウ状態の維持
root.mainloop()


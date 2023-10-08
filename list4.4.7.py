import tkinter as tk
from tkinter import ttk
# ウインドウの作成
root = tk.Tk()

# ステータスバーの設置
statusbar = tk.Label(root,text= "He we go!!",bd=1,relief=tk.SUNKEN,anchor=tk.W)
statusbar.pack(side = tk.BOTTOM,fill = tk.X)

# 実行ボタン
run_button = tk.Button(root,text = "RUN")
run_button.pack(pady=10,ipadx=20,side=tk.BOTTOM)

# ラベルフレーム
frame = ttk.Labelframe(root,text="Select Extension",padding=10)
frame.pack(padx=20,pady=5,side=tk.BOTTOM)

# コンボボックス
extensions = [".docx",".py",".txt",".xlsx",".zip"]
cb = ttk.Combobox(frame,values=extensions,state="readonly")
cb.pack(side=tk.LEFT)
cb.current(0)

# 参照ボタン
browse_button = tk.Button(frame,text="Browse...")
browse_button.pack(padx=10,side=tk.LEFT)

# ウインドウ状態の維持
root.mainloop()

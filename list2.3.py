import tkinter as tk

#ウインドウの作成
root = tk.Tk()

# ウインドウサイズの指定
root.geometry("250x100")

# Runボタン
run_button = tk.Button(root,text = "Run")
run_button.place(x=110,y=30)

# ウインドウ状態の維持
root.mainloop()

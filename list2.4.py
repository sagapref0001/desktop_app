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

# ###関数###
# #関数の定義
# def run_func():
#     print("Hello!!")
#     print("OK")
#
# ###GUI###
# #ウインドウのサイズ指定
# root.geometry("250x100")
# #Runのボタン
# run_button = tk.Button(root,text = "Run",command = run_func)
# run_button.place(x=100,y=30)
# root.mainloop()


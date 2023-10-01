import tkinter as tk

###関数###
#関数の定義
def run_func():
    print("Hello!!")
    print("OK")

###GUI###
# ウインドウの作成
root = tk.Tk()

#ウインドウのサイズ指定
root.geometry("250x100")
#Runのボタン
run_button = tk.Button(root,text = "Run",command = run_func)
run_button.place(x=100,y=30)
root.mainloop()


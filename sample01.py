import tkinter as tk

#ウインドウの作成
root = tk.Tk()
#ウインドウのサイズ指定
root.geometry("250x100")
#Runのボタン
run_button = tk.Button(root,text="Run")
run_button.place(x=100,y=30)
root.mainloop()

def run_func():
    print("Hello!!")


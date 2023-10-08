import tkinter as tk

# 関数
def sub_window():
    # サブウインドウの作成
    mini_window =tk.Toplevel(root)
    # ボタン２
    button2 = tk.Button(mini_window,text="Push2")
    button2.pack(padx=50,pady=25)

#GUI
#ウインドウの作成
root = tk.Tk()
# ボタン１
button1= tk.Button(root,text="Push1",command=sub_window)
button1.pack(padx=100,pady=50)

root.mainloop()





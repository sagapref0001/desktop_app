import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# ラジオボタンの値
radio_value = tk.IntVar()
# ラジオボタン１
radio_1 = ttk.Radiobutton(root,text="Test1",variable=radio_value,value=1)
radio_1.grid(row=0,column=0)
# ラジオボタン２
radio_2 = ttk.Radiobutton(root,text="Test2",variable=radio_value,value=2)
radio_2.grid(row=1,column=0)

# チェックボタン
button = tk.Button(root,text="Check",command= lambda :print(radio_value.get()))
button.grid(row=2,column=0)

root.mainloop()


import tkinter as tk
from tkinter import ttk
import configparser

# 設定ファイル用のインスタンス
config = configparser.ConfigParser()
# 読込むiniファイルを指定
config.read("settings.ini")

def sub_window():
    # サブウインドウの作成
    fp_window = tk.Toplevel(root)
    # ラベルフレーム1
    frame1 = ttk.Labelframe(fp_window,text="Registration",padding=10)
    frame1.pack(padx=20,pady=10)
    # ラベル
    reg_label = tk.Label(frame1,text="Fixed Phrase:")
    reg_label.pack(side=tk.LEFT,anchor=tk.W)
    # 定型文入力欄
    reg_box = tk.Entry(frame1,width=50)
    reg_box.pack(side=tk.LEFT)
    # 保存ボタン
    save_button = tk.Button(frame1,text="Save")
    save_button.pack(padx=10,side=tk.LEFT)
    # ラベルフレーム２
    frame2 = ttk.Labelframe(fp_window,text="Save Slot",padding=10)
    frame2.pack(padx=20,pady=5,fill=tk.X)
    # ラジオボタン
    radio_value=tk.IntVar()
    read_base = config["Fixed Phrase"]
    radio_1 = ttk.Radiobutton(frame2,text=read_base.get("Phrase1"),variable=radio_value,value=1)
    radio_1.grid(row=0,column=0,sticky=tk.W)
    radio_2 = ttk.Radiobutton(frame2,text=read_base.get("Phrase2"),variable=radio_value,value=2)
    radio_2.grid(row=1,column=0,sticky=tk.W)
    radio_3 = ttk.Radiobutton(frame2,text=read_base.get("Phrase3"),variable=radio_value,value=3)
    radio_3.grid(row=2,column=0,sticky=tk.W)
    radio_4 = ttk.Radiobutton(frame2,text=read_base.get("Phrase4"),variable=radio_value,value=4)
    radio_4.grid(row=3,column=0,sticky=tk.W)
    radio_5 = ttk.Radiobutton(frame2,text=read_base.get("Phrase5"),variable=radio_value,value=5)
    radio_5.grid(row=4,column=0,sticky=tk.W)

    set_button = tk.Button(fp_window,text="Set")
    set_button.pack(padx=20,pady=10,ipady=5,fill=tk.X)

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
fp_button = tk.Button(root,text="Fixed Phrase",command=sub_window)
fp_button.pack(padx=10,pady=10,ipady=5,fill=tk.X)

root.mainloop()
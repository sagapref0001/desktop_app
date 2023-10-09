import tkinter as tk


def sub_window():
    # サブウインドウの作成
    fp_window = tkinter.Toplevel(root)
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
    radio.value=tk.IntVar()
    read_base = config["Fixed Phrase"]
    radio_1 = ttk.Radiobutton(frame2,text="Phrase1",variable=radio_value,value=1)
    radio_1.grid(row=o,column=0,sticky=tk.W)
    radio_2 = ttk.Radiobutton(frame2,text="Phrase2",variable=radio_value,value=2)
    radio_2.grid(row=1,column=0,sticky=tk.W)
    radio_3 = ttk.Radiobutton(frame2,text="Phrase3",variable=radio_value,value=3)
    radio_3.grid(row=2,column=0,sticky=tk.W)
    radio_4 = ttk.Radiobutton(frame2,text="Phrase4",variable=radio_value,value=4)
    radio_4.grid(row=3,column=0,sticky=tk.W)
    radio_5 = ttk.Radiobutton(frame2,text="Phrase5",variable=radio_value,value=5)
    radio_5.grid(row=4,column=0,sticky=tk.W)

# 定型文ボタン
fp_button = tk.Button(root,text="Fixed Phrase",command=sub.window)
fp_button.pack(padx=10,pady=10,ipady=5,fill=tk.X)




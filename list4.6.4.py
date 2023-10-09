import tkinter


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

# 定型文ボタン
fp_button = tk.Button(root,text="Fixed Phrase",command=sub.window)
fp_button.pack(padx=10,pady=10,ipady=5,fill=tk.X)




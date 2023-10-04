import tkinter as tk
from tkinter import ttk
import subprocess
import configparser

# configparserのインスタンス化
config = configparser.ConfigParser()

#関数
# RUN1
def run1_func():
    # 読込む設定ファイルを指定
    config.read("config.ini")
    # 設定ファイルから値の取得
    read_base = config["Run1"]
    app1 = read_base.get("app1")
    app2 = read_base.get("app2")
    # プログラムリストの作成
    programs = [app1,app2]
    # プログラムの起動
    for v in programs:
        subprocess.Popen(v)

def run2_func():
    # 読込む設定ファイルを指定
    config.read("config.ini")
    # 設定ファイルから値の取得
    read_base = config["Run2"]
    app1 = read_base.get("app1")
    app2 = read_base.get("app2")
    app3 = read_base.get("app3")
    # プログラムリストの作成
    programs = [app1,app2,app3]
    # プログラムの起動
    for v in programs:
        subprocess.Popen(v)

# setting
def set_func():
    # テキストエディタのディレクトリ
    notepad =r"C:\Windows\System32\notepad.exe"
    # 設定ファイルを開く
    subprocess.run([notepad,"config.ini"])

# Manual
def man_func():
    # マニュアルを開く
    subprocess.run(["start","manual.txt"],shell=True)

# GUI
# ウインドウの作成
root = tk.Tk()
# ラベルフレーム
frame = ttk.LabelFrame(root, text = "Lancher",padding=10)
frame.grid(row = 0, column = 0, padx = 15, pady = 15)
# ボタン
run_button1 = tk.Button(frame, text="RUN1",command = run1_func)
run_button1.grid(row=0,column=0,padx=5)

run_button2 = tk.Button(frame,text="RUN2",command=run2_func)
run_button2.grid(row=0,column=1,padx=5)

# メニューバーの作成

# Fileメニュー
filemenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "File",menu=filemenu)

# Setting
filemenu.add_command(label ="Setting",command = set_func)

# セパレータ
filemenu.add_separator()

# Exit
filemenu.add_command(label="Exit",command=lambda:root.destroy())

# Helpメニュー
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Help",menu=helpmenu)

# Manual
helpmenu.add_command(label="Manual",command=man_func)

root.mainloop()
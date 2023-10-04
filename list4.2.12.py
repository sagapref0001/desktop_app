import subprocess

def set_func():
    # テキストエディタのディレクトリ
    notepad = r"C:\Windows\System32\notepad.exe"
    # 設定ファイルを開く
    subprocess.run([notepad, "config.ini"])

def man_func():
    subprocess.run(["start","manual.txt"],shell=true)

def exit_func():
    root.destroy()

#サブプロセスのインポート
import subprocess

#メモ帳のパス
notepad = r"C:\Windows\System32\notepad.exe"
#Webブラウザのパス
ie = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

programs = [notepad,ie]

for v in programs:
    subprocess.Popen(v)
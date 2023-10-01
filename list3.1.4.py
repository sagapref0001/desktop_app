#サブプロセスのインポート
import subprocess

#メモ帳のパス
notepad = r"C:\Windows\System32\notepad.exe"
#Webブラウザのパス
ie = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
#メモ帳の起動
subprocess.Popen(notepad)
#Webブラウザの起動
subprocess.Popen(ie)

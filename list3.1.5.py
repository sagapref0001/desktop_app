#サブプロセスのインポート
import subprocess

#メモ帳のパス
notepad = r"C:\Windows\System32\notepad.exe"
#Webブラウザのパス
ie = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
# プログラムのリスト作成
programs = [notepad,ie]
# プログラムの起動
for p in programs:
    subprocess.Popen(p)
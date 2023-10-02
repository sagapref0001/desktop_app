import configparser

# インスタンス化
config = configparser.ConfigParser()
# 設定ファイルの内容
config["Run1"] = {
    "app1": r"C:\Windows\System32\notepad.exe",
    "app2": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
}
config["Run2"] = {
    "app1": r"C:\Windows\System32\notepad.exe",
    "app2": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "app3": r"C:\Program Files\WindowsApps\Microsoft.Paint_11.2304.33.0_x64__8wekyb3d8bbwe\PaintApp\mspaint.exe"
}

# 設定ファイルへの書込み
with open("config.ini","w+") as file:
    config.write(file)

# 読み込む設定ファイルを指定
config.read("config.ini")
# 設定ファイルから値の取得
read_base = config["Run1"]
print(read_base.get("app1"))


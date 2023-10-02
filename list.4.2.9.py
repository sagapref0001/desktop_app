import subprocess
import configparser

# configparserのインスタンス化
config = configparser.ConfigParser()

def run1_func():
    config.read("config.ini")
    read_base = config["Run1"]
    app1 = read_base.get("app1")
    app2 = read_base.get("app2")

    programs = [app1,app2]
    for v in programs:
        subprocess.Popen(v)




#coding:utf-8
import subprocess
import yaml
import datetime
import os 

# 出力先フォルダ
save_dir = "gerende_status/"

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

# 設定ファイル読み込み 
f        = open("gerendes.yml", "r+")
gerendes = yaml.load(f)
f.close()

# ヘッドレスChromeの設定
browser_bin     = "google-chrome"
browser_options = ["--headless",
                   "--disable-gpu",
                   #"--window-size=1024,768",
                   "--hide-scrollbars",
                   "--dump-dom"]

# 実行コマンド
cmd_base = [browser_bin]
for opt in browser_options:
    cmd_base.append(opt)
print("\nexecuting.. \n" + str(cmd_base))

# バージョンチェック
#subprocess.check_call([browser_bin ,"--headless", "--version"], shell=False)

# 日付文字列取得
now = datetime.datetime.now().strftime('%Y%m%d_%H%M')

for gere in gerendes:
    g_name = gere['name']
    g_type = gere['type']
    g_url  = gere['url']

    # 無効な設定をスキップ
    if not "http" in g_url : continue

    # 保存先ファイルパス
    save_to = save_dir + g_name + "_" + g_type + "_" + now + ".html"

    try:
        print(g_url)

        f = open(save_to, mode="w") # 出力先のオープン

        cmd = cmd_base + [g_url]

        proc = subprocess.Popen(
                cmd,
                env=os.environ,
                shell  = False,                            #シェル経由($ sh -c "command")で実行。
                #stdin  = subprocess.PIPE,                 #1
                #stdout = subprocess.PIPE)                 #2
                stdout = f)
                #stderr = subprocess.PIPE)                 #3
        proc.communicate() #処理実行を待つ
        f.close()

    except Exception as e:
        print(str(e))
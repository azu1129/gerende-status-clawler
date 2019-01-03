# gerende-status-clawler
スキー場の リフト運行・積雪状況 などを収集するために書いたスクリプトです。過去気象データと組み合わせて機械学習の教師データにしたいという目論見です（いつやるのか）

# more detail
単にyamlファイルに書かれたWebページを順次 ダウンロードするだけです。他の用途にも使えます。
ここからさらにseleniumでスクレイピングする予定だったんですが、ゲレンデごとにDOMターゲットを設定するのが大変なので、とりあえずデータソースを収集するところまで…（本当にやるのか）

# installation

* chrome (--headless 可能なバージョン CentOSならCentOS6以上必須)
* chromedriver
* pip install pyYAML

# usage

$ crontab -e
```
08 10,13,15 * 11-12,1-5 * ~/gerende-status-clawler/kick_clawler.sh
```


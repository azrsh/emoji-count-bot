# Emoji Count Bot
このDiscord Botはサーバ内でそれぞれの絵文字が使われた回数を集計します.

# 使用方法
## コマンドから呼び出せるようにする
`bottoken.py`内の`BOT_TOKEN`をあなたのボットトークンに置き換えてください.  
ボットサーバーを起動し,  ボットが招待されたサーバのチャンネルで`/count-emoji`と入力すれば利用できます.
## Github Actionsで定期実行する
このリポジトリをフォークし, Settings内のSectretsに `BOT_TOKEN`, `GUILD_ID`, `CHANNEL_ID`を設定してください.  
定期実行の周期や時刻はworkflowファイルを編集すれば変更できます.

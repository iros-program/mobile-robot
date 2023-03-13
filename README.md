# 移動ロボット
DIYプロジェクトで教育や研究や商品開発のために簡単にプログラミングできるロボットです。
対象は学生・エンジニア・研究者など
https://i-ros.com/mobile-robot

## インストール
・まず、python3環境を作る必要です。  
・次、下記のコメントでソースコードや必要なライブラリーインストールをしてください。
```
git clone https://github.com/iros-program/mobile-robot.git
cd mobile-robot
pip3 install -r requirements.txt
```
## Ubuntuの場合
/dev/ttyUSB0のパーミッションなどロボットに接続ができないとき、下のコマンドで実行ユーザをdialoutグループに追加します。
sudo adduser $USER dialout

## サンプル実行
```
python3 forward.py
```
## デモ動画
Switchコントローラーを使ってswitch_controller.pyサンプルでロボットを動かした動画をyoutubeへアップしました。   
[Youtube動画](https://www.youtube.com/watch?v=yShiS1NlSEk)

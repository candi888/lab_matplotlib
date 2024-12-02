# 図面作成の効率化(Matplotlib)
- plot.py内の「基本設定」の部分だけ適切にいじれば，以下のような図面が作れる
- Adobe Illustratorで編集する際にはsvgを使う
- （簡単な使い方）
  -  適当なフォルダを作って，plot.pyを配置する
  -  その後，同じ階層に"plot_original_data"という名前のフォルダを作り，その直下に使用する素データのdatファイルなどを全て入れる
  -  plot.py内の「基本設定1」「基本設定2」の中の数値などを適切にいじったのち，以下コマンドをターミナル上で実行
    -  python <実行するplot.pyのパス>
    -  //例（カレントディレクトリ直下にplot.pyがある場合）
    -  python plot.py
  -  "plot_result"というフォルダが自動で作られ，その中に画像ファイル等が出力される

![sample2_res](https://github.com/user-attachments/assets/2f8e1266-6591-48e9-a0d4-c35e5abb42dd)
![sample3_res](https://github.com/user-attachments/assets/5f6ceaa7-0a3b-4110-a487-6962e822c4cc)

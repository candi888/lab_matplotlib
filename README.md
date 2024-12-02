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
![sample1_res](https://github.com/user-attachments/assets/f027bc17-8276-4903-8b0d-8fdd14f64601)
![sample2_res](https://github.com/user-attachments/assets/bd22881b-4e59-4c29-9611-b884a5160061)
![sample3_res](https://github.com/user-attachments/assets/bdb00110-0414-4c76-8fd1-4637a8a87ad8)

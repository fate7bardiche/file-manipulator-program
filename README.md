# file-manipulator-program

## 概要
本リポジトリは、コマンドと引数を渡すことでファイルを操作する、コマンドラインインターフェースを提供します。

## 使用方法
各コマンドの説明に、実行方法の例を記載しています。

この後説明する各コマンドより右側のコマンドライン引数を引数と呼ぶことにします。  
以下の後に各コマンドおよび引数を渡してください。
```
$ python3 file_manipulator.py 
```

### reverseコマンド
入力ファイル内の内容を反転し、出力ファイルに上書き保存します。

- 第一引数: 入力ファイル名
- 第二引数: 出力ファイル名

実行例
```
$ python3 file_manipulator.py reverse example/reverse/input_file.txt example/reverse/output_file.txt
```

### copyコマンド
入力ファイルの内容を、出力ファイルにコピーします。  
すでに出力ファイルが存在する場合は、上書き保存されます。

- 第一引数: 入力ファイル名
- 第二引数: 出力ファイル名

実行例
```
$ python3 file_manipulator.py copy example/copy/input_file.txt example/copy/output_file.txt
```

### duplicate_contentsコマンド
入力ファイルの内容を指定した回数分入力ファイルに複製します。

- 第一引数: 入力ファイル名
- 第二引数: 複製回数

実行例
```
$ python3 file_manipulator.py duplicate-contents example/duplicate_contents/input_file.txt 4
```

### replace_stringコマンド
入力ファイルから任意の文字Aを検索します。  
その後、検索した任意の文字Aを任意の文字Bに変換します。

- 第一引数: 入力ファイル名
- 第二引数: 入力ファイル内から探し出したい文字列
- 第三引数: 置換文字列(検索で見つかった文字列をこれに変換する)

実行例
```
$ python3 file_manipulator.py replace-string example/replace_string/input_file.txt string integer
```

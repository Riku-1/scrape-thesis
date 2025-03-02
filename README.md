## scrape-thesis
論文のデータをスクレイピングで取得するスクリプト

### :warning: 注意 :warning:
このスクリプトを外部から機械的に連続で実行するのはやめてください。  
（法に触れる恐れがあります）

### 使い方
1. pipenvをインストール  
    pipenvをインストールします。多分
    ```shell script
    pip install pipenv
    ```
    とかですが環境によります。
    
    その後以下で必要なライブラリを取得します。
    
1. 依存ライブラリをインストール  
    pipenvを使って依存ライブラリをインストールします
    ```shell script
    pipenv install
    ```
1. .envファイルの作成
    .env.exampleをコピーし、.envという名前にリネームしてください。  
    その後、DEEPL_API_KEYにDeepLのAPIキーを入力してください。  
    (APIキーは一般チャンネルのWikiにあります。)
    
1. input.txtにデータを取得したい論文のurlを書きます  
    このフォルダにinput.txtというファイルを作成してください。  
    中身は論文のurlを一行ずつ書いてください。
    ```
    // 例
    https://www.nature.com/articles/s41467-020-19293-9
    https://www.nature.com/articles/s41467-020-18077-5
    ```

1. その後main.pyを叩けばデータ取得が実行されます
    ```shell script
    python main.py
    ```
    データはoutputフォルダに出力されます。

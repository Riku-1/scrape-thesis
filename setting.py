from dotenv import load_dotenv
import os

# 各種数値
SLEEP_TIME_SEC = 3  # スクレイピング時の待機秒数

# 環境変数
load_dotenv()
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')

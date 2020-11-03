import logger
import sys
import time

from usecase.scrape.scrape_usecase_factory import get_scrape_usecase
from domain.thesis import Thesis
from input_urls import get_urls
from setting import SLEEP_TIME_SEC

# logger設定
sys.excepthook = logger.uncaught_exception

# input.txtからurlを取得
urls = get_urls()

if not len(urls):
    msg = "urlがありません。プログラムを終了します。"
    logger.warning(msg)
    print(msg)
    raise SystemExit(1)

# 論文情報取得
scrape_usecases = []
for index, url in enumerate(urls):
    if index != 0:  # 初回はスリープしない
        time.sleep(SLEEP_TIME_SEC)

    try:
        scrape_usecase = get_scrape_usecase(url)
    except Exception as err:
        msg = f"html取得エラー: {url}のデータが取得できませんでした。"
        logger.warning(msg, err)
        print(msg)
        continue

    scrape_usecases.append(scrape_usecase)

# 論文整形
thesis_list: [Thesis] = []
for usecase in scrape_usecases:
    try:
        thesis = usecase.get_thesis()
    except RuntimeError as err:
        msg = f"parseエラー: {usecase.url}のデータ処理に失敗しました。"
        logger.warning(msg, err)
        print(msg)
        continue

    thesis_list.append(thesis)

# 出力
for thesis in thesis_list:
    print("title")
    print(thesis.title)

    print("abstract")
    print(thesis.abstract)

    print("introduction")
    print(thesis.introduction)

    print("results")
    print(thesis.results)

    print("discussion")
    print(thesis.discussion)

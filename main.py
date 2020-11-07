import logger
import sys
import time

from usecase.scrape.scrape_usecase_factory import get_scrape_usecase
from domain.thesis import Thesis
from formatting import delete_brackets
from infrastructure.file.input_urls import get_urls
from infrastructure.file.output_thesis import output_csv
from setting import SLEEP_TIME_SEC

# logger設定
sys.excepthook = logger.uncaught_exception

# input.txtからurlを取得
urls = get_urls()

if not len(urls):
    msg = "urlがありません。プログラムを終了します。"
    logger.warning(msg)
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
        continue

    scrape_usecases.append(scrape_usecase)

# 論文整形
thesis_list: [Thesis] = []
for usecase in scrape_usecases:
    try:
        logger.info(f"{usecase.url}の情報を整形します...")
        title = usecase.get_title()
        abstract = usecase.get_abstract()
        introduction = usecase.get_introduction()
        results = usecase.get_results()
        discussion = usecase.get_discussion()

        thesis = Thesis(
            usecase.url,
            title,
            delete_brackets(abstract),
            delete_brackets(introduction),
            delete_brackets(results),
            delete_brackets(discussion)
        )
    except RuntimeError as err:
        msg = f"parseエラー: {usecase.url}のデータ処理に失敗しました。"
        logger.warning(msg, err)
        continue

    thesis_list.append(thesis)

# 出力
output_num = 0
for thesis in thesis_list:
    result = output_csv(thesis)
    if result:
        output_num += 1

logger.info(f"{len(urls)}URL中{output_num}個のデータを出力しました")

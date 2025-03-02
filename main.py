import logger
import sys
import time

from domain.thesis import Thesis
from formatting import delete_brackets
from infrastructure.file.input_urls import get_urls
from infrastructure.file.output_thesis import output_csv
from usecase.scrape.scrape_usecase_factory import get_scrape_usecase
from usecase.translate_usecase import translate_thesis
from setting import SLEEP_TIME_SEC

# logger設定
sys.excepthook = logger.uncaught_exception

# input.txtからurlを取得
urls = get_urls()

if not len(urls):
    logger.warning("urlがありません。プログラムを終了します。")
    raise SystemExit(1)

# 論文情報取得
scrape_usecases = []
for index, url in enumerate(urls):
    if index != 0:  # 初回はスリープしない
        time.sleep(SLEEP_TIME_SEC)

    try:
        scrape_usecase = get_scrape_usecase(url)
    except Exception as err:
        logger.warning(f"html取得エラー: {url}のデータが取得できませんでした。", err)
        continue

    scrape_usecases.append(scrape_usecase)

# 論文整形
thesis_list: [Thesis] = []
for usecase in scrape_usecases:
    logger.info(f"{usecase.url}の情報を整形します...")
    try:
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
        logger.warning(f"parseエラー: {usecase.url}のデータ処理に失敗しました。", err)
        continue

    thesis_list.append(thesis)

# 論文翻訳
translated_thesis_list = []
for thesis in thesis_list:
    logger.info(f"{thesis.url}を翻訳します...")
    translated_thesis = translate_thesis(thesis)
    translated_thesis_list.append(translated_thesis)

# 出力
output_num = 0
for thesis in translated_thesis_list:
    result = output_csv(thesis)
    if result:
        output_num += 1

logger.info(f"{len(urls)}URL中{output_num}個のデータを出力しました")

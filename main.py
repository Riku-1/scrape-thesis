import logger
import sys

from usecase.scrape.scrape_usecase_factory import get_scrape_usecase
from domain.thesis import Thesis

# logger設定
sys.excepthook = logger.uncaught_exception

# TODO: インプットの方式を考える
urls = [
    "https://www.nature.com/articles/s41467-020-19293-9",
    "https://www.nature.com/articles/s41467-020-18077-5"
]

# 論文情報取得
thesis_list: [Thesis] = []
for url in urls:
    try:
        scrape_usecase = get_scrape_usecase(url)
        page = scrape_usecase.get_page()
        thesis = scrape_usecase.get_thesis(page)
    except RuntimeError as err:
        logger.warning(err)
        print(err)
        continue

    thesis_list.append(thesis)

# 出力
for thesis in thesis_list:

    print("abstract")
    print(thesis.abstract)

    print("introduction")
    print(thesis.introduction)

    print("results")
    print(thesis.results)

    print("discussion")
    print(thesis.discussion)

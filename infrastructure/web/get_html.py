from bs4 import BeautifulSoup
import urllib3

import logger


def get_soup(url: str) -> BeautifulSoup:
    """
    beautiful soupを使ってページを取得する
    :return:
    """
    logger.info(f"{url}の情報を取得します...")

    # header偽装
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }

    http = urllib3.PoolManager()
    r: urllib3.HTTPResponse = http.request("GET", url, headers=headers)
    soup = BeautifulSoup(r.data, "html.parser")

    # 上付き文字を消去
    for sup in soup("sup"):
        sup.decompose()

    return soup

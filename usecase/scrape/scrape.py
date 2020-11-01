import urllib3
from bs4 import BeautifulSoup

from domain import Thesis
import formatting


def get_thesis(url: str) -> Thesis.Thesis:
    """
    論文を取得する
    :param url:
    :return:
    """
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

    abstract: str = soup.select_one("#Abs1-content > p").get_text()
    introductions = soup.select("#Sec1-content > p")
    _introductions = ""
    for intro in introductions:
        _introductions += intro.get_text()

    return Thesis.Thesis(
        formatting.delete_brackets(abstract),
        formatting.delete_brackets(_introductions)
    )



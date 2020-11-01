import urllib3
from bs4 import BeautifulSoup

import formatting


def get_thesis(url: str):
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
    # TODO: nth-childの分だけforを回す
    introduction: str = soup.select_one("#Sec1-content > p:nth-child(2)").get_text()

    _abstract = formatting.delete_brackets(abstract)
    _introduction = formatting.delete_brackets(introduction)

    return _abstract


import re

import urllib3
from bs4 import BeautifulSoup

import string

url = "https://www.nature.com/articles/s41467-020-18002-w"
# header偽装
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
}

http = urllib3.PoolManager()
r: urllib3.HTTPResponse = http.request("GET", url, headers=headers)

soup = BeautifulSoup(r.data, "html.parser")
abstract: str = soup.select_one("#Abs1-content > p").get_text()
# TODO: nth-childの分だけforを回す
introduction: str = soup.select_one("#Sec1-content > p:nth-child(2)").get_text()

_abstract = string.delete_brackets(abstract)
_introduction = string.delete_brackets(introduction)

print(_abstract)

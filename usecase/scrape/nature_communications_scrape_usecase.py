from bs4 import BeautifulSoup
from lxml import html

from usecase.scrape.scrape_usecase import ScrapeUseCase


def _get_section(soup: BeautifulSoup, section_name: str) -> str:
    """
    NatureCommunicationの各セクション（AbstractやIntroduction）の内容を取得する
    NOTE: NCのセクションのidは各論文ごとにバラバラなので（Resultsがセクション4だったりセクション7だったりする）
    見出しを検索して各セクションが何番目かを取得し、取得したセクションのidから内容を取得する
    :param soup:
    :param section_name:
    :return:
    """
    dom: html.HtmlElement = html.fromstring(str(soup))
    # textがセクション名（AbstractやIntroduction）の名前のh2要素を取得する（見出し）
    title_id = dom.xpath(f"//h2[text()='{section_name}']")[0].get("id")
    # 見出しのidに-contentを加えたものが各セクションの内容のidになるので、これを取得する
    section_id = title_id + "-content"

    contents = soup.select(f"#{section_id} > p")
    _content = ""
    for content in contents:
        _content += content.get_text()

    return _content


class NatureCommunicationsScrapeUseCase(ScrapeUseCase):
    def _get_abstract(self, soup: BeautifulSoup) -> str:
        return soup.select_one("#Abs1-content > p").get_text()

    def _get_introduction(self, soup: BeautifulSoup) -> str:
        introductions = soup.select("#Sec1-content > p")
        _introductions = ""
        for intro in introductions:
            _introductions += intro.get_text()

        return _introductions

from bs4 import BeautifulSoup
from lxml import html

import logger
from usecase.scrape.scrape_usecase import ScrapeUseCase


class NatureCommunicationsScrapeUseCase(ScrapeUseCase):
    def _get_title(self, soup: BeautifulSoup) -> str:
        elm = soup.select_one(".c-article-title")

        if not elm:
            logger.warning(f"{self.url}のタイトルが取得できませんでした。")
            return ""

        return elm.get_text()

    def _get_abstract(self, soup: BeautifulSoup) -> str:
        return self.__get_section(soup, "Abstract")

    def _get_introduction(self, soup: BeautifulSoup) -> str:
        return self.__get_section(soup, "Introduction")

    def _get_results(self, soup: BeautifulSoup) -> str:
        return self.__get_section(soup, "Results")

    def _get_discussion(self, soup: BeautifulSoup) -> str:
        return self.__get_section(soup, "Discussion")

    def __get_section(self, soup: BeautifulSoup, section_name: str) -> str:
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
        section_name_dom = dom.xpath(f"//h2[text()='{section_name}']")
        if not section_name_dom:
            logger.warning(f"{self.url}の{section_name}が取得できませんでした。")
            return ""

        # 見出しのidに-contentを加えたものが各セクションの内容のidになるので、これを取得する
        title_id = section_name_dom[0].get("id")
        section_id = title_id + "-content"

        contents = soup.select(f"#{section_id} > p")
        _content = ""
        for content in contents:
            _content += content.get_text()

        return _content

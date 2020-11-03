from abc import ABC, abstractmethod

from bs4 import BeautifulSoup
import urllib3

from domain.thesis import Thesis
from formatting import delete_brackets
import logger


class ScrapeUseCase(ABC):
    """"
    論文スクレイピングユースケースの基底クラス
    """
    def __init__(self, url: str) -> None:
        self.url = url
        self.page: BeautifulSoup = self.__get_page()

    def __get_page(self) -> BeautifulSoup:
        """
        beautiful soupを使ってページを取得する
        :return:
        """
        logger.info(f"{self.url}の情報を取得します...")

        # header偽装
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

        http = urllib3.PoolManager()
        r: urllib3.HTTPResponse = http.request("GET", self.url, headers=headers)
        soup = BeautifulSoup(r.data, "html.parser")

        # 上付き文字を消去
        for sup in soup("sup"):
            sup.decompose()

        return soup

    def get_thesis(self) -> Thesis:
        """
        論文のドメインクラスを取得する
        :return:
        """
        logger.info(f"{self.url}の情報を整形します...")

        title = self._get_title(self.page)
        abstract = self._get_abstract(self.page)
        introduction = self._get_introduction(self.page)
        results = self._get_results(self.page)
        discussion = self._get_discussion(self.page)

        return Thesis(
            self.url,
            title,
            delete_brackets(abstract),
            delete_brackets(introduction),
            delete_brackets(results),
            delete_brackets(discussion)
        )

    @abstractmethod
    def _get_title(self, soup: BeautifulSoup) -> str:
        """
        タイトルを取得する
        :param soup:
        :return:
        """
        pass

    @abstractmethod
    def _get_abstract(self, soup: BeautifulSoup) -> str:
        """
        アブストラクトを取得する
        :param soup:
        :return:
        """
        pass

    @abstractmethod
    def _get_introduction(self, soup: BeautifulSoup) -> str:
        """
        イントロダクションを取得する
        :param soup:
        :return:
        """
        pass

    @abstractmethod
    def _get_results(self, soup: BeautifulSoup) -> str:
        """
        リザルトを取得する
        :param soup:
        :return:
        """
        pass

    @abstractmethod
    def _get_discussion(self, soup: BeautifulSoup) -> str:
        """
        ディスカッションを取得する
        :param soup:
        :return:
        """
        pass

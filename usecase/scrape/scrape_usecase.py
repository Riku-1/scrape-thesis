from abc import ABC, abstractmethod
from dataclasses import dataclass

from bs4 import BeautifulSoup
import urllib3

from domain.thesis import Thesis
from formatting import delete_brackets


@dataclass
class ScrapeUseCase(ABC):
    """"
    論文スクレイピングユースケースの基底クラスを作成
    """
    url: str

    def get_thesis(self) -> Thesis:
        """
        論文のドメインクラスを取得する
        :return:
        """
        soup = self.get_soup()
        abstract = self.get_abstract(soup)
        introduction = self.get_introduction(soup)
        return Thesis(
            self.url,
            delete_brackets(abstract),
            delete_brackets(introduction)
        )

    def get_soup(self) -> BeautifulSoup:
        """
        beautiful soupを使ってページを取得する
        :return:
        """
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

    @abstractmethod
    def get_abstract(self, soup: BeautifulSoup) -> str:
        """
        アブストラクトを取得する
        :param soup:
        :return:
        """
        pass

    @abstractmethod
    def get_introduction(self, soup: BeautifulSoup) -> str:
        """
        イントロダクションを取得する
        :param soup:
        :return:
        """
        pass

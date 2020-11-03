from abc import ABC, abstractmethod
from dataclasses import dataclass
from setting import SLEEP_TIME_SEC
import time

from bs4 import BeautifulSoup
import urllib3

from domain.thesis import Thesis
from formatting import delete_brackets
import logger


@dataclass
class ScrapeUseCase(ABC):
    """"
    論文スクレイピングユースケースの基底クラス
    """
    url: str

    def get_thesis(self) -> Thesis:
        """
        論文のドメインクラスを取得する
        :return:
        """
        message = f"{self.url}の情報を取得します..."
        logger.info(message)
        print(message)
        time.sleep(SLEEP_TIME_SEC)  # WARNING: 業務妨害対策

        soup = self.__get_soup()
        abstract = self._get_abstract(soup)
        introduction = self._get_introduction(soup)
        results = self._get_results(soup)
        discussion = self._get_discussion(soup)

        return Thesis(
            self.url,
            delete_brackets(abstract),
            delete_brackets(introduction),
            delete_brackets(results),
            delete_brackets(discussion)
        )

    def __get_soup(self) -> BeautifulSoup:
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

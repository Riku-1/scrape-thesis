from abc import ABC, abstractmethod
from dataclasses import dataclass

from bs4 import BeautifulSoup

from domain.thesis import Thesis


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
        return Thesis(
            self.url,
            self.get_abstract(soup),
            self.get_introduction(soup)
        )

    def get_soup(self) -> BeautifulSoup:
        # TODO: 書く
        pass

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

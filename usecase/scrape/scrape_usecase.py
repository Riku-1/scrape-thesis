from abc import ABC, abstractmethod

from bs4 import BeautifulSoup

from domain.thesis import Thesis
from formatting import delete_brackets
from infrastructure.web.get_html import get_soup
import logger


class ScrapeUseCase(ABC):
    """"
    論文スクレイピングユースケースの基底クラス
    """
    def __init__(self, url: str) -> None:
        self.url = url
        self.page = get_soup(url)

    def get_thesis(self) -> Thesis:
        """
        論文のドメインクラスを取得する
        :return:
        """
        logger.info(f"{self.url}の情報を整形します...")

        title = self._get_title()
        abstract = self._get_abstract()
        introduction = self._get_introduction()
        results = self._get_results()
        discussion = self._get_discussion()

        return Thesis(
            self.url,
            title,
            delete_brackets(abstract),
            delete_brackets(introduction),
            delete_brackets(results),
            delete_brackets(discussion)
        )

    @abstractmethod
    def _get_title(self) -> str:
        """
        タイトルを取得する
        :return:
        """
        pass

    @abstractmethod
    def _get_abstract(self) -> str:
        """
        アブストラクトを取得する
        :return:
        """
        pass

    @abstractmethod
    def _get_introduction(self) -> str:
        """
        イントロダクションを取得する
        :return:
        """
        pass

    @abstractmethod
    def _get_results(self) -> str:
        """
        リザルトを取得する
        :return:
        """
        pass

    @abstractmethod
    def _get_discussion(self) -> str:
        """
        ディスカッションを取得する
        :return:
        """
        pass

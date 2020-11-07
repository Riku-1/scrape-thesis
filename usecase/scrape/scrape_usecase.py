from abc import ABC, abstractmethod

from infrastructure.web.get_html import get_soup


class ScrapeUseCase(ABC):
    """"
    論文スクレイピングユースケースの基底クラス
    """
    def __init__(self, url: str) -> None:
        self.url = url
        self.page = get_soup(url)

    @abstractmethod
    def get_title(self) -> str:
        """
        タイトルを取得する
        :return:
        """
        pass

    @abstractmethod
    def get_abstract(self) -> str:
        """
        アブストラクトを取得する
        :return:
        """
        pass

    @abstractmethod
    def get_introduction(self) -> str:
        """
        イントロダクションを取得する
        :return:
        """
        pass

    @abstractmethod
    def get_results(self) -> str:
        """
        リザルトを取得する
        :return:
        """
        pass

    @abstractmethod
    def get_discussion(self) -> str:
        """
        ディスカッションを取得する
        :return:
        """
        pass

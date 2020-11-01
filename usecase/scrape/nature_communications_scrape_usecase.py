from bs4 import BeautifulSoup

from usecase.scrape.scrape_usecase import ScrapeUseCase


class NatureCommunicationsScrapeUseCase(ScrapeUseCase):
    def _get_abstract(self, soup: BeautifulSoup) -> str:
        return soup.select_one("#Abs1-content > p").get_text()

    def _get_introduction(self, soup: BeautifulSoup) -> str:
        introductions = soup.select("#Sec1-content > p")
        _introductions = ""
        for intro in introductions:
            _introductions += intro.get_text()

        return _introductions

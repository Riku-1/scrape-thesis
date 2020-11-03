from usecase.scrape.nature_communications_scrape_usecase import NatureCommunicationsScrapeUseCase
from usecase.scrape.scrape_usecase import ScrapeUseCase


def get_scrape_usecase(url: str) -> ScrapeUseCase:
    if url.startswith("https://www.nature.com/"):
        return NatureCommunicationsScrapeUseCase(url)

    raise RuntimeError(f"{url}は対応していないサイトです。")

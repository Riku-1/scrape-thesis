from usecase.scrape.scrape_usecase_factory import get_scrape_usecase


# TODO: インプットの方式を考える
url = "https://www.nature.com/articles/s41467-020-19293-9"

scrape_usecase = get_scrape_usecase(url)
thesis = scrape_usecase.get_thesis()
print(thesis)

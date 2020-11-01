from usecase.scrape import scrape

# TODO: インプットの方式を考える
url = "https://www.nature.com/articles/s41467-020-18002-w"
thesis = scrape.get_thesis(url)
print(thesis)

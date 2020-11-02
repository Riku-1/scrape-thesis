from usecase.scrape.scrape_usecase_factory import get_scrape_usecase


# TODO: インプットの方式を考える
url = "https://www.nature.com/articles/s41467-020-19293-9"

try:
    scrape_usecase = get_scrape_usecase(url)
except RuntimeError as err:
    print(err)

thesis = scrape_usecase.get_thesis()

print("abstract")
print(thesis.abstract)

print("introduction")
print(thesis.introduction)

print("results")
print(thesis.results)

print("discussion")
print(thesis.discussion)

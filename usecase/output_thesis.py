import csv

from domain.thesis import Thesis
from formatting import space_to_underscore
import logger


def output_csv(thesis: Thesis):
    print(f"{thesis.url}の情報を出力します...")
    if thesis.title == "":
        msg = f"{thesis.url}のタイトルが空のためファイルを出力できません。プログラムを終了します。"
        logger.error(msg)
        print(msg)
        raise SystemExit(1)

    filename = space_to_underscore(f"output/{thesis.title}")
    with open(filename, "w") as f:
        # NOTE: writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL) とすると""なしで出力できるが、出力が必要な場合エラーになる
        writer = csv.writer(f)

        writer.writerow(["url"])
        writer.writerow([thesis.url])
        writer.writerow([])

        writer.writerow(["title"])
        writer.writerow([thesis.title])
        writer.writerow([])

        writer.writerow(["abstract"])
        writer.writerow([thesis.abstract])
        writer.writerow([])

        writer.writerow(["introduction"])
        writer.writerow([thesis.introduction])
        writer.writerow([])

        writer.writerow(["results"])
        writer.writerow([thesis.results])
        writer.writerow([])

        writer.writerow(["discussion"])
        writer.writerow([thesis.discussion])

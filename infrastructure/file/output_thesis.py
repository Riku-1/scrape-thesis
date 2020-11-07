import csv

from domain.thesis import Thesis
from formatting import space_to_underscore
import logger


def output_csv(thesis: Thesis) -> bool:
    """
    論文情報をcsvに出力する
    :param thesis:
    :return: 出力に成功したかどうか
    """
    logger.info(f"{thesis.url}の情報を出力します...")

    if thesis.title == "":
        logger.warning(f"{thesis.url}のタイトルが空のためファイルを出力できません。出力をスキップします。")
        return False

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

        return True
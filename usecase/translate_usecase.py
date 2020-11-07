from domain.thesis import Thesis
from infrastructure.web.translate import translate
import logger


def translate_thesis(thesis: Thesis) -> Thesis:
    """
    論文を翻訳する
    :param thesis:
    :return: 翻訳情報が入力された論文クラス
    """
    try:
        translated_list = translate([
            thesis.title,
            thesis.abstract,
            thesis.introduction,
            thesis.results,
            thesis.discussion
        ])

        thesis.title_translated = translated_list[0]
        thesis.abstract_translated = translated_list[1]
        thesis.introduction_translated = translated_list[2]
        thesis.results_translated = translated_list[3]
        thesis.discussion_translated = translated_list[4]
    except Exception as err:
        logger.warning(f"{thesis.url}の翻訳に失敗しました。", err)
        # 翻訳に失敗した場合、その時点での論文情報を返す
        return thesis

    return thesis

import re

"""
文字列操作に関するモジュール
"""


def delete_brackets(sentence: str) -> str:
    """
    括弧を削除する。ただし、(Fig...)は残す
    なお、(Fig...)に一致する正規表現は \(Fig.+?\)
    (Fig...)以外の括弧に一致する正規表現は \((?!Fig).+?\)
    すべての括弧を削除する場合は \(.+?\)
    :param sentence: 文字列
    :return: 括弧削除後の文字列
    """
    return re.sub(r"\((?!Fig).+?\)", "", sentence)


def space_to_underscore(sentence: str) -> str:
    """
    スペースをアンダースコア（_）に変換する
    :param sentence:
    :return:
    """
    return sentence.replace(" ", "_")

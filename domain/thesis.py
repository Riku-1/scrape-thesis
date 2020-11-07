from dataclasses import dataclass


@dataclass
class Thesis:
    """
    論文クラス
    """
    url: str
    title: str
    abstract: str
    introduction: str
    results: str
    discussion: str
    title_translated: str = ""
    abstract_translated: str = ""
    introduction_translated: str = ""
    results_translated: str = ""
    discussion_translated: str = ""

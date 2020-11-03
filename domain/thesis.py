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

from dataclasses import dataclass


@dataclass
class Thesis:
    """
    論文クラス
    """
    url: str
    abstract: str
    introduction: str

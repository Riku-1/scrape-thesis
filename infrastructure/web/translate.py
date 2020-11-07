import requests

import logger
import setting

DEEPL_TRANSLATE_URL = "https://api.deepl.com/v2/translate"


def translate(text_list: [str]) -> [str]:
    """
    文章を翻訳する
    :param text_list:
    :return: 翻訳された文章のリスト
    NOTE: 返り値もtext_listの順番どおりになる
    > The parameter may be specified multiple times and translations
        are returned in the same order as they are requested.
    from https://www.deepl.com/docs-api/translating-text/
    """
    params = {
        "auth_key": setting.DEEPL_API_KEY,
        "text": text_list,
        "target_lang": "JA",
    }

    res = requests.post(DEEPL_TRANSLATE_URL, params)

    if res.status_code == 403:
        msg = "DeepLの認証に失敗しました"
        logger.warning(msg)
        raise Exception(msg)
    if res.status_code == 413:
        msg = "テキストのサイズが多すぎます。"
        logger.warning(msg)
        raise Exception(msg)
    if res.status_code == 429:
        msg = "DeepL APIがビジー状態です。しばらく待ってから再度実行してください。"
        logger.warning(msg)
        raise Exception(msg)
    if res.status_code == 456:
        msg = "DeepLの翻訳上限に達しました。"
        logger.warning(msg)
        raise Exception(msg)

    translated_list = []
    for elm in res.json()["translations"]:
        translated_list.append(elm["text"])

    return translated_list

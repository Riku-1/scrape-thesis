import requests

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

    res = requests.get(DEEPL_TRANSLATE_URL, params)

    if res.status_code == 403:
        raise Exception("DeepLの認証に失敗しました。")
    if res.status_code == 413:
        raise Exception("テキストのサイズが多すぎます。")
    if res.status_code == 429:
        raise Exception("DeepL APIがビジー状態です。しばらく待ってから再度実行してください。")
    if res.status_code == 456:
        raise Exception("DeepLの翻訳上限に達しました。")
    print(res.json())

    translated_list = []
    for elm in res.json()["translations"]:
        translated_list.append(elm["text"])

    return translated_list

import logger


def get_urls() -> [str]:
    """
    input.txtからurlをlistで取得する
    :return:
    """
    try:
        f = open("input.txt", "r")
    except FileNotFoundError as err:
        logger.error("input.txtが存在しません。input.txtを配置してからもう一度実行してください。")
        raise SystemExit(1)

    data = f.read()
    f.close()

    return data.splitlines()

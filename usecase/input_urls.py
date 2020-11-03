import logger


def get_urls() -> [str]:
    """
    input.txtからurlをlistで取得する
    :return:
    """
    try:
        f = open("input.txt", "r")
    except FileNotFoundError as err:
        msg = "input.txtが存在しません。プログラムを終了します。"
        logger.error(msg)
        print(msg)
        raise SystemExit(1)

    data = f.read()
    f.close()

    return data.splitlines()

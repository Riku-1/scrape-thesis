import logging
from typing import Any, Optional

FORMATTER = logging.Formatter('%(levelname)s : %(name)s : %(asctime)s : %(message)s')
LOG_FILE_PATH = "log/python.log"


# TODO: なんか動いてないので直す
def uncaught_exception(err_type, err_value, traceback) -> None:
    """
    補足されていない場合の例外処理
    :param err_type:
    :param err_value:
    :param traceback:
    :return:
    """
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(LOG_FILE_PATH)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(FORMATTER)
    logger.setLevel(logging.WARNING)
    logger.addHandler(handler)

    sys_logger = logging.getLogger("system")
    sys_logger.error("Uncaught exception", exc_info=(err_type, err_value, traceback))


def critical(err: Exception, msg: str = "") -> None:
    __out("critical", msg, err)


def error(msg: Any, err: Optional[Exception] = None) -> None:
    __out("error", msg, err)


def warning(msg: Any, err: Optional[Exception] = None) -> None:
    __out("warning", msg, err)


def info(msg: Any, err: Optional[Exception] = None) -> None:
    __out("info", msg, err)


def debug(msg: Any, err: Optional[Exception] = None) -> None:
    __out("debug", msg, err)


def __out(method_name: str, msg: Any, err: Optional[Exception] = None) -> None:
    """
    log出力メソッドを抽象化したもの。method_nameのログを出力する
    :param method_name:
    :param msg:
    :param err:
    :return:
    """
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(LOG_FILE_PATH)
    handler.setLevel(logging.INFO)
    handler.setFormatter(FORMATTER)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    method = getattr(logger, method_name)

    if not err:
        method(msg)
        return

    method(msg, exc_info=(type(err), err, err.__traceback__))

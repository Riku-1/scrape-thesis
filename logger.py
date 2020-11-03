import logging

formatter = '%(levelname)s : %(asctime)s : %(message)s'

logging.basicConfig(filename="log/python.log", level=logging.DEBUG, format=formatter)
logger = logging.getLogger(__name__)


def uncaught_exception(err_type, err_value, traceback):
    """
    補足されていない場合の例外処理
    :param err_type:
    :param err_value:
    :param traceback:
    :return:
    """
    logger.error("Uncaught exception", exc_info=(err_type, err_value, traceback))


def critical(err: Exception, msg: str = ""):
    logger.critical(msg, exc_info=(type(err), err, err.__traceback__))


def error(err: Exception, msg: str = ""):
    logger.error(msg, exc_info=(type(err), err, err.__traceback__))


def warning(err: Exception, msg: str = ""):
    logger.warning(msg, exc_info=(type(err), err, err.__traceback__))


def info(err: Exception, msg: str = ""):
    logger.info(msg, exc_info=(type(err), err, err.__traceback__))


def debug(err: Exception, msg: str = ""):
    logger.debug(msg, exc_info=(type(err), err, err.__traceback__))

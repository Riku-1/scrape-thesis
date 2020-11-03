import logging

formatter = '%(levelname)s : %(asctime)s : %(message)s'

logging.basicConfig(filename="log/python.log", level=logging.DEBUG, format=formatter)


def uncaught_exception(err_type, err_value, traceback):
    """
    補足されていない場合の例外処理
    :param err_type:
    :param err_value:
    :param traceback:
    :return:
    """
    logger = logging.getLogger(__name__)
    logger.error("Uncaught exception", exc_info=(err_type, err_value, traceback))
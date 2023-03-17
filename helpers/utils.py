import logging


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler = logging.FileHandler("./logs/execution.log")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

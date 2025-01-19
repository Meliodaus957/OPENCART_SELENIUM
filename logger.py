import logging


def setup_logger():
    logger = logging.getLogger("OpenCartTests")
    logger.setLevel(logging.INFO)

    # Обработчик вывода логов в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Форматирование сообщений
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger

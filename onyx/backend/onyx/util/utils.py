import logging


def decode_log_level(level: str):
    level = level.lower()

    if level.__contains__('debug'):
        return logging.DEBUG

    if level.__contains__('info'):
        return logging.INFO

    if level.__contains__('fatal'):
        return logging.FATAL

    if level.__contains__('critical'):
        return logging.CRITICAL

    if level.__contains__('error'):
        return logging.ERROR

    return logging.WARNING


def decode_mime_type(value: str):
    if value.__contains__('image'):
        return 'image'

    return 'text'

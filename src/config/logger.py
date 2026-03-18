import logging
import os
from pathlib import Path
from datetime import datetime

LOG_ROOT = Path(__file__).parent.parent.parent / 'logs'
os.makedirs(LOG_ROOT, exist_ok=True)

DEFAULT_LOG_FORMAT = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)-8s - %(filename)s:%(lineno)4d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def get_logger(
        name: str = 'agent',
        level: int = logging.INFO,
        file_level: int = logging.DEBUG,
        log_file: str = None,
) -> logging.Logger:
    _logger = logging.getLogger(name)
    _logger.setLevel(logging.DEBUG)

    # 避免重复添加handler
    if _logger.handlers:
        return _logger

    # 控制台的handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(DEFAULT_LOG_FORMAT)

    _logger.addHandler(console_handler)

    # 文件handler
    if not log_file:
        log_file = os.path.join(LOG_ROOT, f'{name}_{datetime.now().strftime('%Y%m%d')}.log')
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(file_level)
    file_handler.setFormatter(DEFAULT_LOG_FORMAT)

    _logger.addHandler(file_handler)

    return _logger

# 快捷logger
logger = get_logger()

if __name__ == '__main__':
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
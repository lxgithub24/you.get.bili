# -*- coding:utf-8 -*-
import logging

logger = logging.getLogger('lxlog')
logger.setLevel(logging.DEBUG)

handerler1 = logging.StreamHandler()
handerler1.setLevel(logging.INFO)

handerler2 = logging.FileHandler(filename='lx.conf')
handerler2.setLevel(logging.WARN)

formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

handerler1.setFormatter(formatter)
handerler2.setFormatter(formatter)

logger.addHandler(handerler1)
logger.addHandler(handerler2)

logger.info('info message')
logger.debug('debug message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
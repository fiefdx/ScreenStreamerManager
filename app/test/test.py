# -*- coding: utf-8 -*-
'''
Created on 2017-03-04
@summary: test
@author: YangHaitao
'''

import os
import sys
import logging
import time

cwd = os.path.split(os.path.realpath(__file__))[0]
sys.path.insert(0, os.path.split(cwd)[0])

from config import CONFIG
import logger
from utils.run_cmd import run_rtmp

LOG = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.config_logging(file_name = "test.log",
                          log_level = CONFIG["log_level"],
                          dir_name = "logs",
                          day_rotate = False,
                          when = "D",
                          interval = 1,
                          max_size = 20,
                          backup_count = 5,
                          console = True)
    LOG.info("Test Start")
    t = time.time()
    p = run_rtmp(full_screen = False)
    time.sleep(10)
    p.kill()
    p.terminate()
    tt = time.time()
    LOG.info("Use Time: %ss", tt - t)
    LOG.info("Test Exit!")

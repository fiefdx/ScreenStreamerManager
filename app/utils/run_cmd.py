# -*- coding: utf-8 -*-
'''
Created on 2017-03-04
@summary: run cmd
@author: YangHaitao
'''

import logging
from subprocess import Popen, PIPE

from config import CONFIG

LOG = logging.getLogger(__name__)


def run_get_active_window():
    v = -1
    try:
        p = Popen(CONFIG["get_active_window"], shell = True, stdout = PIPE)
        vs = p.stdout.read()
        v = int(vs)
    except Exception, e:
        LOG.exception(e)
    return v

def run_rtmp(full_screen = True, window_id = -1):
    p = None
    try:
        args = []
        args.append("-config=%s" % CONFIG["rtmp_config_path"])
        if full_screen:
            args.append("-full_screen=true")
        else:
            args.append("-full_screen=false")
        if window_id != -1:
            args.append("-wid=%s" % window_id)
        LOG.debug("cmd: %s, args: %s", CONFIG["rtmp"], args)
        p = Popen(args, executable = CONFIG["rtmp"], shell = False)
    except Exception, e:
        LOG.exception(e)
    return p

def run_mjpeg():
    p = None
    try:
        args = ["-config=%s" % CONFIG["mjpeg_config_path"]]
        LOG.debug("cmd: %s, args: %s", CONFIG["mjpeg"], args)
        p = Popen(args, executable = CONFIG["mjpeg"], shell = False)
    except Exception, e:
        LOG.exception(e)
    return p

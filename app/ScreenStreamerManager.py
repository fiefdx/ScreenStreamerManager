#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017-03-04
@summary: ScreenStreamer Manager
@author: YangHaitao
'''

import logging

import wx

from config import CONFIG
from views.main import MainFrame
import logger


LOG = logging.getLogger(__name__)

class MainApp(wx.App):
    def OnInit(self):
        w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
        h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
        frame = MainFrame("ScreenStreamerManager", (w / 2 - 200, h / 2 - 265), (300, 290))
        self.SetTopWindow(frame)
        frame.Show()
        return True

if __name__ == "__main__":
    logger.config_logging(file_name = "ScreenStreamerManager.log", 
                          log_level = CONFIG['log_level'], 
                          dir_name = "logs", 
                          day_rotate = False, 
                          when = "D", 
                          interval = 1, 
                          max_size = 20, 
                          backup_count = 5, 
                          console = True)
    
    LOG.info("ScreenStreamerManager Start!")
    try:
        app = MainApp()
        app.MainLoop()
    except Exception, e:
        LOG.exception(e)
    LOG.info("ScreenStreamerManager Exit!")
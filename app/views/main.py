# -*- coding: utf-8 -*-
'''
Created on 2017-03-04
@summary: main window
@author: YangHaitao
'''

import time
import logging

import wx

from config import CONFIG
from utils.run_cmd import run_rtmp, run_mjpeg, run_get_active_window

LOG = logging.getLogger(__name__)


class MainFrame(wx.Frame):
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size, style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.p = None
        self.timer = None

        self.SetTextCtrl()
        self.SetChoice()
        self.SetCheckbox()
        self.SetButton()
        self.SetStatusBar()

        self.SetSizer(self.sizer)
        self.Layout()
        self.Fit()
        self.SetSizeWH(size[0], size[1])

    def SetStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusStyles([wx.SB_RAISED])
        self.statusbar.SetMinHeight(28)

    def SetTextCtrl(self):
        self.textctrl_id = wx.TextCtrl(self, -1, size = (320, -1))
        sizer = wx.FlexGridSizer(cols = 2, hgap = 6, vgap = 6)
        sizer.Add(wx.StaticText(self, label = "Window ID"), 0, wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.textctrl_id, 1, wx.EXPAND)
        self.sizer.Add(sizer, flag = wx.EXPAND | wx.ALL, border = 10)

    def SetButton(self):
        self.select_button = wx.Button(self, -1, label = "Select")
        self.run_button = wx.Button(self, -1, label = "Run")
        self.stop_button = wx.Button(self, -1, label = "Stop")
        self.Bind(wx.EVT_BUTTON, self.OnSelect, self.select_button)
        self.Bind(wx.EVT_BUTTON, self.OnRun, self.run_button)
        self.Bind(wx.EVT_BUTTON, self.OnStop, self.stop_button)
        self.stop_button.Disable()
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.select_button, 0, wx.RIGHT | wx.BOTTOM)
        sizer.Add(self.run_button, 0, wx.RIGHT | wx.BOTTOM)
        sizer.Add(self.stop_button, 0, wx.RIGHT | wx.BOTTOM)
        self.sizer.Add(sizer, 0, wx.ALIGN_CENTER)

    def SetChoice(self):
        self.execute = wx.Choice(self, -1, (85, 18), choices = ["rtmp", "mjpeg"])
        self.execute.SetStringSelection("rtmp")
        box = self.MakeStaticBoxSizer("Execute", [self.execute])
        self.sizer.Add(box, 0, wx.ALL, 10)

    def SetCheckbox(self):
        self.full_screen = wx.CheckBox(self, -1, "Full Screen", (35, 40), (145, 20))
        self.full_screen.SetValue(False)
        box = self.MakeStaticBoxSizer("Options", [self.full_screen])
        self.sizer.Add(box, 0, wx.ALL, 10)

    def MakeStaticBoxSizer(self, boxlabel, items):
        box = wx.StaticBox(self, -1, boxlabel)
        sizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        for item in items:
            sizer.Add(item, 0, wx.ALL, 2)
        return sizer

    def OnSelect(self, event):
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnSelectTimer, self.timer)
        self.select_start_at = time.time()
        self.current_window_id = run_get_active_window()
        self.select_button.Disable()
        self.select_time = 5000
        self.statusbar.SetStatusText("Time: %.2fs" % (self.select_time / 1000.0))
        self.timer.Start(100)

    def OnSelectTimer(self, event):
        self.select_time -= 100
        self.statusbar.SetStatusText("Time: %.2fs" % (self.select_time / 1000.0))
        window_id = run_get_active_window()
        if window_id != self.current_window_id or time.time() - self.select_start_at >= 5:
            self.timer.Stop()
            self.select_button.Enable()
            self.statusbar.SetStatusText("")
        self.textctrl_id.SetValue("%s" % window_id)

    def OnRun(self, event):
        if ["rtmp", "mjpeg"][self.execute.GetCurrentSelection()] == "rtmp":
            full_screen = self.full_screen.GetValue()
            window_id = int(self.textctrl_id.GetValue())
            self.p = run_rtmp(full_screen = full_screen, window_id = window_id)
        else:
            self.p = run_mjpeg()
        self.select_button.Disable()
        self.run_button.Disable()
        self.stop_button.Enable()
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnRunTimer, self.timer)
        self.statusbar.SetStatusText("Running ...")
        self.timer.Start(100)

    def OnRunTimer(self, event):
        if self.p:
            flag = self.p.poll()
            if flag != None:
                self.timer.Stop()
                self.statusbar.SetStatusText("Stopped")
                self.select_button.Enable()
                self.run_button.Enable()
                self.stop_button.Disable()

    def OnStop(self, event):
        if self.p:
            self.p.kill()

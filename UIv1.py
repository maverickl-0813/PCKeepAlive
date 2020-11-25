# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################


class MainFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent,
                          id=wx.ID_ANY,
                          title=u"PCKeepAlive",
                          pos=wx.DefaultPosition,
                          size=wx.Size(350, 120),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
## Class MainPanel
###########################################################################

class MainPanel (wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(350, 120), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        H_Sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.freq_label = wx.StaticText(self, wx.ID_ANY, u"Keystroke Frequency", wx.DefaultPosition, wx.DefaultSize, 0)
        self.freq_label.Wrap(-1)

        H_Sizer.Add(self.freq_label, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.freq_ctrl = wx.TextCtrl(self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        self.freq_ctrl.SetMaxLength(3)
        H_Sizer.Add(self.freq_ctrl, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.SwitchButton = wx.Button(self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0)
        H_Sizer.Add(self.SwitchButton, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        MainSizer.Add(H_Sizer, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        H_Sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.checkbox_wait_thread = wx.CheckBox(self, wx.ID_ANY, u"Waiting for background thread to stop", wx.DefaultPosition, wx.DefaultSize, 0)
        H_Sizer2.Add(self.checkbox_wait_thread, 0, wx.ALL, 5)

        MainSizer.Add(H_Sizer2, 0, 0, 5)

        self.SetSizer(MainSizer)
        self.Layout()

    def __del__(self):
        pass



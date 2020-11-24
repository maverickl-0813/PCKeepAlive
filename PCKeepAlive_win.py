import wx
import pyautogui
import time
from threading import Thread


class KeepAliveTask:
    def __init__(self, sleep_time=10):
        self._running = False
        self.sleep_time = sleep_time
        #print("Task initialized with sleep time %s seconds." % self.sleep_time)

    def terminate(self):
        self._running = False

    def run(self):
        self._running = True
        while self._running:
            pyautogui.press('up')
            time.sleep(self.sleep_time)


class MainWindow(wx.Frame):
    def __init__(self, parent, style, title, size):
        # Threading task preparation
        self.keep_alive = KeepAliveTask()
        self.thr_keep_alive = None
        # Initialize UI
        wx.Frame.__init__(self, parent, style=style, title=title, size=size)
        self.MainPanel = wx.Panel(self)
        self.h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.outer_sizer = wx.BoxSizer(wx.VERTICAL)
        # Switch button
        self.SwitchButton = wx.Button(self.MainPanel, label="Start", size=(100, 50))
        self.h_sizer.Add(self.SwitchButton, 1, wx.CENTER)
        self.Bind(wx.EVT_BUTTON, self.onClickStart, self.SwitchButton)
        # Status bar
        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusText("Ready")
        # Finalize UI
        self.outer_sizer.Add(self.h_sizer, 1, wx.CENTER)
        self.MainPanel.SetAutoLayout(True)
        self.MainPanel.SetSizer(self.outer_sizer)
        self.MainPanel.Layout()
        self.Show(True)

    def onClickStart(self, event):
        # Init/Start task and thread
        self.thr_keep_alive = Thread(target=self.keep_alive.run, daemon=True)
        self.thr_keep_alive.start()
        #print("Start keep alive!")

        self.SwitchButton.SetLabel("Stop")
        self.Bind(wx.EVT_BUTTON, self.onClickStop, self.SwitchButton)
        if self.thr_keep_alive.is_alive():
            self.statusbar.SetStatusText("Running keep alive!")

    def onClickStop(self, event):
        # Stop and finalize thread
        self.SwitchButton.Disable()
        self.SwitchButton.SetLabel("Stopping...")
        if self.thr_keep_alive.is_alive():
            self.keep_alive.terminate()
        while self.thr_keep_alive.is_alive():
            self.statusbar.SetStatusText("Wait for background thread to stop...")
            time.sleep(1)
        self.SwitchButton.Enable()
        self.SwitchButton.SetLabel("Start")
        self.Bind(wx.EVT_BUTTON, self.onClickStart, self.SwitchButton)
        self.statusbar.SetStatusText("Ready")
        self.thr_keep_alive = None


if __name__ == '__main__':
    app = wx.App(False)
    mystyles = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION | wx.MINIMIZE_BOX
    frame = MainWindow(None, style=mystyles, title="Keep Your PC Alive!", size=(300, 150))
    app.MainLoop()

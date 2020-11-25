import wx
import pyautogui
import time
from threading import Thread
from UIv1 import MainFrame
from UIv1 import MainPanel


class KeepAliveTask:
    def __init__(self, sleep_time=10):
        self._running = False
        self.sleep_time = sleep_time
        #print("Task initialized with sleep time %s seconds." % self.sleep_time)
    
    def set_sleep(self, sleep):
        self.sleep_time = sleep
        #print("Sleep time set to %s seconds." % self.sleep_time)
        
    def terminate(self):
        self._running = False

    def run(self):
        self._running = True
        while self._running:
            pyautogui.press('up')
            time.sleep(self.sleep_time)


class keepalive_UI(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, parent)
        self.MainFrame = MainFrame
        self.MainPanel = MainPanel(self)
        self.MainPanel.SwitchButton.Bind(wx.EVT_BUTTON, self.onClickStart)
        self.statusBar.SetStatusText("Ready")
        
        # Init Keepalive task instance
        self.sleep_time = self.__get_freq_ctrl_value()
        self.keep_alive = KeepAliveTask(self.sleep_time)
        self.thr_keep_alive = None
        self.wait_thread_end = False
        
        self.Show(True)
    
    def onClickStart(self, event):
        # Determine if we need to wait for thread stop.
        self.wait_thread_end = self.MainPanel.checkbox_wait_thread.GetValue()
        self.MainPanel.checkbox_wait_thread.Disable()
        
        # Init/Start Thread
        self.sleep_time = self.__get_freq_ctrl_value()
        self.keep_alive.set_sleep(self.sleep_time)
        self.thr_keep_alive = Thread(target=self.keep_alive.run, daemon=True)
        self.thr_keep_alive.start()

        # UI transitions
        self.MainPanel.SwitchButton.SetLabel("Stop")
        self.MainPanel.SwitchButton.Bind(wx.EVT_BUTTON, self.onClickStop)
        self.MainPanel.freq_ctrl.Disable()
        if self.thr_keep_alive.is_alive():
            self.statusBar.SetStatusText("Running keep alive!")
    
    def onClickStop(self, event):
        # Stop and finalize thread
        if self.wait_thread_end:
            self.MainPanel.SwitchButton.Disable()
            self.MainPanel.SwitchButton.SetLabel("Stopping...")
        if self.thr_keep_alive.is_alive():
            self.keep_alive.terminate()
        if self.wait_thread_end:
            while self.thr_keep_alive.is_alive():
                self.statusBar.SetStatusText("Wait for background thread to stop...")
                time.sleep(1)
            self.MainPanel.SwitchButton.Enable()
        self.MainPanel.SwitchButton.SetLabel("Start")
        self.MainPanel.SwitchButton.Bind(wx.EVT_BUTTON, self.onClickStart)
        self.statusBar.SetStatusText("Ready")
        self.MainPanel.freq_ctrl.Enable()
        self.MainPanel.checkbox_wait_thread.Enable()
        self.thr_keep_alive = None

    def __get_freq_ctrl_value(self):
        return int(self.MainPanel.freq_ctrl.GetValue())
        

if __name__ == '__main__':
    app = wx.App(False)
    mainUI = keepalive_UI(None)
    app.MainLoop()

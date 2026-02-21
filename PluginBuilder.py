import wx
import sys

from app import PluginBuilder
from app.plugin_builder import RedirectText

def main():
    app = wx.App()
    frame = PluginBuilder(None)

    sys.stdout = RedirectText(frame.m_textCtrl1)

    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()

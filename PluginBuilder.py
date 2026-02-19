import wx
import sys

from app import PluginBuilder
from app.plugin_builder import RedirectText

# current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.chdir(current_dir)
# sys.path.insert(0, os.path.join(current_dir, "ci"))



app = wx.App()
frame = PluginBuilder(None)
sys.stdout = RedirectText(frame.m_textCtrl1)
frame.Show()
app.MainLoop()

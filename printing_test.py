import wx
import sys

class RedirectText:
    def __init__(self, text_ctrl):
        self.out = text_ctrl

    def write(self, string):
        self.out.AppendText(string)

    def flush(self):
        pass  # Needed for compatibility


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Print to Text Area", size=(500, 400))

        panel = wx.Panel(self)

        # Create multiline text area
        self.log = wx.TextCtrl(
            panel,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2
        )

        # Button to test printing
        btn = wx.Button(panel, label="Print Something")
        btn.Bind(wx.EVT_BUTTON, self.on_print)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.log, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        panel.SetSizer(sizer)

        # Redirect stdout
        redir = RedirectText(self.log)
        sys.stdout = redir
        sys.stderr = redir  # optional: capture errors too

    def on_print(self, event):
        print("Hello from wxPython!")
        print("This goes inside the text area.")


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


app = MyApp()
app.MainLoop()
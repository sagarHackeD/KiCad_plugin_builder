from .plugin_builder_gui_base import MainFrame


import wx
import sys

class RedirectText:
    def __init__(self, text_ctrl):
        self.out = text_ctrl

    def write(self, string):
        self.out.AppendText(string)

    def flush(self):
        pass  # Needed for compatibility



class PluginBuilder(MainFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

    def on_validate( self, event ):
        
        m_filePicker1 = self.m_filePicker1.GetPath()
        if not m_filePicker1:
            print("No file selected.")
            return
    
        print(f"Selected file: {m_filePicker1}")
        print("Validating the JSON file...")
        from .util import validate_json
        validate_json(m_filePicker1)



    
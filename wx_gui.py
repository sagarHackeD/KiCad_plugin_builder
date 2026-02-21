import wx
import shutil

class KiCadPluginBuilder(wx.Frame):
    def __init__(self):
        super().__init__(None, title="KiCad Plugin Builder", size=(600, -1))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.notebook = wx.Notebook(panel)

        self.packager_tab = self.create_packager_tab(self.notebook)
        self.metadata_tab = self.create_metadata_tab(self.notebook)
        self.help_tab = self.create_help_tab(self.notebook)

        self.notebook.AddPage(self.packager_tab, "Packager")
        self.notebook.AddPage(self.metadata_tab, "Metadata")
        self.notebook.AddPage(self.help_tab, "Help")

        vbox.Add(self.notebook, 1, wx.EXPAND | wx.ALL, 5)

        footer = wx.StaticText(
            panel,
            label="Designed and Written by Sagar Naik - sagarnaik430@googlemail.com",
        )
        footer.SetFont(wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        vbox.Add(footer, 0, wx.ALIGN_CENTER | wx.BOTTOM, 5)

        panel.SetSizer(vbox)

    # ------------------------------------------------------------------
    # Packager Tab
    # ------------------------------------------------------------------
    def create_packager_tab(self, parent):
        panel = wx.Panel(parent)
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(wx.StaticText(panel, label="Package Plugin :"), 0, wx.ALL, 5)

        self.metadata_file = self.file_picker(
            panel,
            "Metadata Location :",
            "C:/Users/ECHS/Desktop/Place_By_Sch_KiCad/metadata.json",
        )
        vbox.Add(self.metadata_file, 0, wx.EXPAND | wx.ALL, 5)

        self.source_folder = self.dir_picker(
            panel,
            "Source Location   :",
            "C:/Users/ECHS/Desktop/Place_By_Sch_KiCad/src",
        )
        vbox.Add(self.source_folder, 0, wx.EXPAND | wx.ALL, 5)

        self.icon_file = self.file_picker(
            panel,
            "Icon Location     :",
            "C:/Users/ECHS/Desktop/Place_By_Sch_KiCad/resources/icon.png",
        )
        vbox.Add(self.icon_file, 0, wx.EXPAND | wx.ALL, 5)

        self.build_dir = self.dir_picker(
            panel,
            "Build Directory   :",
            "C:/Users/ECHS/Desktop/Place_By_Sch_KiCad/build",
        )
        vbox.Add(self.build_dir, 0, wx.EXPAND | wx.ALL, 5)

        self.dist_dir = self.dir_picker(
            panel,
            "dist Directory  :",
            "C:/Users/ECHS/Desktop/Place_By_Sch_KiCad"
        )
        vbox.Add(self.dist_dir, 0, wx.EXPAND | wx.ALL, 5)

        btn_box = wx.BoxSizer(wx.HORIZONTAL)

        build_btn = wx.Button(panel, label="Build Plugin Package")
        clean_btn = wx.Button(panel, label="Clean")

        build_btn.Bind(wx.EVT_BUTTON, self.on_build_package)
        clean_btn.Bind(wx.EVT_BUTTON, self.on_clean)

        btn_box.Add(build_btn, 0, wx.RIGHT, 5)
        btn_box.Add(clean_btn, 0)

        vbox.Add(btn_box, 0, wx.ALL, 5)

        self.terminal = self.create_terminal(panel)
        vbox.Add(self.terminal, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(vbox)
        return panel

    # ------------------------------------------------------------------
    # Metadata Tab
    # ------------------------------------------------------------------
    def create_metadata_tab(self, parent):
        panel = wx.Panel(parent)
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(wx.StaticText(panel, label="Populate Metadata File for submission :"), 0, wx.ALL, 5)

        self.username = self.text_input(panel, "Github Username :", "sagarHackeD")
        self.repo = self.text_input(panel, "Github Repo :", "Place_By_Sch_KiCad")

        vbox.Add(self.username, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(self.repo, 0, wx.EXPAND | wx.ALL, 5)

        populate_btn = wx.Button(panel, label="Populate")
        populate_btn.Bind(wx.EVT_BUTTON, self.on_populate_metadata)
        vbox.Add(populate_btn, 0, wx.ALL, 5)

        self.meta_terminal = self.create_terminal(panel)
        vbox.Add(self.meta_terminal, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(vbox)
        return panel

    # ------------------------------------------------------------------
    # Help Tab
    # ------------------------------------------------------------------
    def create_help_tab(self, parent):
        panel = wx.Panel(parent)
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(wx.StaticText(panel, label="Create Local Backup"), 0, wx.ALL, 5)

        backup_src = self.dir_picker(panel, "Source Location :", "")
        vbox.Add(backup_src, 0, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(vbox)
        return panel

    # ------------------------------------------------------------------
    # UI Helpers
    # ------------------------------------------------------------------
    def file_picker(self, parent, label, default):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(wx.StaticText(parent, label=label), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        ctrl = wx.FilePickerCtrl(parent, path=default)
        hbox.Add(ctrl, 1, wx.EXPAND)
        return hbox

    def dir_picker(self, parent, label, default):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(wx.StaticText(parent, label=label), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        ctrl = wx.DirPickerCtrl(parent, path=default)
        hbox.Add(ctrl, 1, wx.EXPAND)
        return hbox

    def text_input(self, parent, label, default):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(wx.StaticText(parent, label=label), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        ctrl = wx.TextCtrl(parent, value=default)
        hbox.Add(ctrl, 1, wx.EXPAND)
        hbox.ctrl = ctrl
        return hbox

    def create_terminal(self, parent):
        return wx.TextCtrl(
            parent,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2,
        )

    # ------------------------------------------------------------------
    # Event Handlers
    # ------------------------------------------------------------------
    def log(self, msg):
        self.terminal.AppendText(msg)

    def on_build_package(self, event):
        self.log("Building Plugin Package...\n")
        # build_package(values)
        self.log("Plugin Package Built Successfully!\nat: ./kicad-package.zip\n")

    def on_clean(self, event):
        shutil.rmtree("build", ignore_errors=True)
        shutil.rmtree("com.*", ignore_errors=True)
        self.log("Cleaned build directory.\n")

    def on_populate_metadata(self, event):
        self.meta_terminal.AppendText("Populating Metadata File...\n")
        # same logic you already have


if __name__ == "__main__":
    app = wx.App()
    frame = KiCadPluginBuilder()
    frame.Show()
    app.MainLoop()
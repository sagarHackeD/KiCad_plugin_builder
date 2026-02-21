import os

from .PackageBuilderBase import MainFrame

import json


class RedirectText:
    def __init__(self, text_ctrl):
        self.out = text_ctrl

    def write(self, string):
        self.out.AppendText(string)

    def flush(self):
        pass  # Needed for compatibility


class PluginBuilder(MainFrame):
    input_data = {"metadata_file": "", "src_folder": "", "icon_file": ""}

    def __init__(self, parent=None):
        super().__init__(parent)
        self.json_file = "data.json"
        self.populate_inputs(self.json_file)

        self.m_filePicker1.SetPath(self.input_data.get("metadata_file", ""))
        self.m_dirPicker1.SetPath(self.input_data.get("src_folder", ""))
        self.m_filePicker12.SetPath(self.input_data.get("icon_file", ""))

    def populate_inputs(self, json_file):
        try:
            with open(json_file, "r") as f:
                self.input_data = json.load(f)
        except FileNotFoundError:
            print(f"{json_file} not found.")

    def save_inputs(self, event, json_file=None):
        if json_file is None:
            json_file = self.json_file
        with open(json_file, "w") as f:
            json.dump(self.input_data, f, indent=4)

    def on_validate(self, event):
        m_filePicker1 = self.m_filePicker1.GetPath()
        if not m_filePicker1:
            print("No file selected.")
            return

        print(f"Selected file: {m_filePicker1}")
        print("Validating the JSON file...")
        from .util import validate_json

        validate_json(m_filePicker1)

    def e_button_build(self, event):
        print("Building the plugin...")
        from packager import (
            MetadataGenerator,
            PackagerClass,
            get_release_urls_github,
            get_owner_repo,
        )

        medata = MetadataGenerator()
        package_dir = medata.create_package_dir()
        packager_ = PackagerClass(package_dir)
        packager_.package()
        owner, repo = get_owner_repo("metadata.json")
        print(f"Fetching release information for {owner}/{repo}...")
        releses = get_release_urls_github(owner, repo)
        medata.create(releses, package_dir)
        print("Plugin build process completed.")

    def e_metadata_file_select(self, event):
        m_filePicker1 = self.m_filePicker1.GetPath()
        if not m_filePicker1:
            print("No file selected.")
            return
        print(f"Selected file: {m_filePicker1}")
        self.input_data["metadata_file"] = m_filePicker1
        self.save_inputs(event)

    def e_src_folder_select(self, event):
        src_folder = self.m_dirPicker1.GetPath()
        if not src_folder:
            print("No folder selected.")
            return
        print(f"Selected folder: {src_folder}")
        self.input_data["src_folder"] = src_folder
        self.save_inputs(event)

    def e_icon_file_select(self, event):
        icon_file = self.m_filePicker12.GetPath()
        if not icon_file:
            print("No file selected.")
            return
        print(f"Selected file: {icon_file}")
        self.input_data["icon_file"] = icon_file
        self.save_inputs(event)

    def e_button_clean(self, event):
        print("Cleaning up the build environment...")
        from .util import clean_build_environment

        clean_build_environment()
        print("Cleanup completed.")

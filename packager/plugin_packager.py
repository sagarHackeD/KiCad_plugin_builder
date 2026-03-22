import glob
import json
import os
import shutil

from PIL import Image

class PackagerClass:
    """Class to build KiCad plugin package."""

    def __init__(
        self,
        build_dir="build",
        metadata_file="metadata.json",
        src_folder="src",
        icon_file="resources/icon.png",
        dist_dir="dist",
    ):
        self.build_dir = build_dir
        self.metadata_file = metadata_file
        self.src_folder = src_folder
        self.icon_file = icon_file
        self.dist_dir = dist_dir

    def __create_build_dir(self):
        for directory in [self.dist_dir,self.build_dir + "/resources",self.build_dir + "/plugins"]:
            os.makedirs(directory, exist_ok=True)
            print(f"""Creating directory {directory}""")


    def resize_image(self, input_path, size, dist_path):
        img = Image.open(input_path)
        img_resized = img.resize(size, Image.Resampling.LANCZOS)
        img_resized.save(dist_path)
        print(f"""Resizing {input_path} to {size} at {dist_path}""")

    def __copy_icons_to_build_dir(self):
        self.resize_image(self.icon_file, (64, 64), self.build_dir + "/resources/icon.png")
        self.resize_image(self.icon_file, (24, 24), self.build_dir + "/plugins/icon.png")

    def __copy_files_to_build_dir(self):
        files_to_copy = glob.glob(self.src_folder + "/*.py")
        for file in files_to_copy:
            shutil.copy(file, self.build_dir + "/plugins")
            print(f"Copying {file} to {self.build_dir}/plugins")

        with open(self.metadata_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)
            metadata.pop("Repository",None)

        with open(self.build_dir+"/metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)

        # shutil.copy(self.metadata_file, self.build_dir)
        print(f"Copying {self.metadata_file} to {self.build_dir}")

    def __build_plugin_zip(self, zip_filename):
        shutil.make_archive(zip_filename.replace(".zip", ""), "zip", self.build_dir)
        print(f"Creating {zip_filename} from {self.build_dir}")

    def __remove_build_dir(self):
        shutil.rmtree(self.build_dir, ignore_errors=True)
        print(f"Removing build directory {self.build_dir}")

    def package(self):
        """Build the plugin package."""
        self.__remove_build_dir()
        self.__create_build_dir()
        self.__copy_icons_to_build_dir()
        self.__copy_files_to_build_dir()
        self.__build_plugin_zip(self.dist_dir + "/kicad-package.zip")
        self.__remove_build_dir()


if __name__ == "__main__":
    packager = PackagerClass(
        build_dir="build",
        metadata_file="metadata.json",
        src_folder="src",
        icon_file="resources/icon.png",
        dist_dir="dist",
    )

    packager.package()  # build the package

import glob
import os
import shutil

from PIL import Image

class Packager:
    """Class to build KiCad plugin package."""

    def __init__(
        self,
        build_dir="build",
        metadata_file="metadata.json",
        src_folder="src",
        icon_file="resources/icon.png",
        output_dir="output",
    ):
        self.build_dir = build_dir
        self.metadata_file = metadata_file
        self.src_folder = src_folder
        self.icon_file = icon_file
        self.output_dir = output_dir

    def __create_build_dir(self):
        os.makedirs(self.output_dir, exist_ok=True)
        os.mkdir(self.build_dir)
        os.mkdir(self.build_dir + "/resources")
        os.mkdir(self.build_dir + "/plugins")

    def resize_image(self, input_path, size, output_path):
        img = Image.open(input_path)
        img_resized = img.resize(size, Image.Resampling.LANCZOS)
        img_resized.save(output_path)

    def __copy_icons_to_build_dir(self):
        self.resize_image(
            self.icon_file, (64, 64), self.build_dir + "/resources/icon.png"
        )
        self.resize_image(
            self.icon_file, (24, 24), self.build_dir + "/plugins/icon.png"
        )

    def __copy_files_to_build_dir(self):
        files_to_copy = glob.glob(self.src_folder + "/*.py")
        for file in files_to_copy:
            shutil.copy(file, self.build_dir + "/plugins")
        shutil.copy(self.metadata_file, self.build_dir)

    def __build_plugin_zip(self, zip_filename):
        # print(os.path.abspath(self.build_dir))
        shutil.make_archive(zip_filename.replace(".zip", ""), "zip", self.build_dir)
        print(f"Created {zip_filename}")

    def __remove_build_dir(self):
        shutil.rmtree(self.build_dir, ignore_errors=True)

    def package(self):
        """Build the plugin package."""
        self.__remove_build_dir()
        self.__create_build_dir()
        self.__copy_icons_to_build_dir()
        self.__copy_files_to_build_dir()
        self.__build_plugin_zip(self.output_dir + "/KiCad_plugin.zip")
        self.__remove_build_dir()


if __name__ == "__main__":
    packager = Packager(
        build_dir="build",
        metadata_file="metadata.json",
        src_folder="src",
        icon_file="resources/icon.png",
        output_dir="output",
    )

    packager.package()  # build the package

import glob
import os
import shutil

from PIL import Image


class Packager:
    """Class to build KiCad plugin package."""

    def __init__(self,build_dir="build",metadata_file="metadata.json",src_folder = 'src',icon_file="resources/icon.png"):
        self.build_dir = build_dir
        self.metadata_file = metadata_file
        self.src_folder = src_folder
        self.icon_file = icon_file
        pass

    def __create_build_dir(self):
        os.mkdir(self.build_dir)
        os.mkdir(self.build_dir+"/resources")
        os.mkdir(self.build_dir+"/plugins")

    def __resize_image(self, input_path, size, output_path):
        img = Image.open(input_path)
        img_resized = img.resize(size, Image.Resampling.LANCZOS)
        img_resized.save(output_path)

    def __copy_icons_to_build_dir(self):
        self.__resize_image(self.icon_file, (64, 64), self.build_dir+"/resources/icon.png")
        self.__resize_image(self.icon_file, (24, 24), self.build_dir+"/plugins/icon.png")

    def __copy_files_to_build_dir(self):
        files_to_copy = glob.glob(self.src_folder+"/*.py")
        for file in files_to_copy:
            shutil.copy(file, self.build_dir+"/plugins")
        shutil.copy(self.metadata_file, self.build_dir)

    def __build_plugin_zip(self, zip_filename):
        shutil.make_archive(zip_filename.replace(".zip", ""), "zip", self.build_dir)
        print(f"Created {zip_filename}")

    def __remove_build_dir(self):
        shutil.rmtree(self.build_dir, ignore_errors=True)

    def package(self):
        self.__remove_build_dir()
        self.__create_build_dir()
        self.__copy_icons_to_build_dir()
        self.__copy_files_to_build_dir()
        self.__build_plugin_zip("KiCad_plugin.zip")
        # self.__remove_build_dir()


packager = Packager("build","metadata.json",'src',"resources/icon.png")


if __name__ == "__main__":
    # make sure your metadata file is filled with necessory information before running this script

    packager.package()

    # after packaging check the zip file with Packaging Toolkit https://gitlab.com/kicad/addons/metadata#packaging-toolkit

    # after verifying you have to create a relesease on github and upload the zip file or any other publically accessible location

    # then run the metadata generator to create icon and a metadata file with sha256, download link and size information for submitting to the KiCad plugin manager
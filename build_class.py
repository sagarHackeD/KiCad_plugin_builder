import glob
import hashlib
import json
import os
import shutil
import zipfile

from PIL import Image


class Packager:
    """Class to build KiCad plugin package."""

    READ_SIZE = 65536

    def __init__(self):
        pass

    def __create_build_dir(self):
        os.mkdir("build")
        os.mkdir("build/resources")
        os.mkdir("build/plugins")

    def __resize_image(self, input_path, size, output_path):
        img = Image.open(input_path)
        img_resized = img.resize(size, Image.Resampling.LANCZOS)
        img_resized.save(output_path)

    def __copy_icons_to_build_dir(self):
        self.__resize_image("resources/icon.png", (64, 64), "build/resources/icon.png")
        self.__resize_image("resources/icon.png", (24, 24), "build/plugins/icon.png")

    def __copy_files_to_build_dir(self):
        files_to_copy = glob.glob("src/*.py")
        for file in files_to_copy:
            shutil.copy(file, "build/plugins")
        shutil.copy("metadata.json", "build")

    def __build_plugin_zip(self, zip_filename):
        shutil.make_archive(zip_filename.replace(".zip", ""), "zip", "build")
        print(f"Created {zip_filename}")

    def __remove_build_dir(self):
        shutil.rmtree("build", ignore_errors=True)

    def package(self):
        self.__remove_build_dir()
        self.__create_build_dir()
        self.__copy_icons_to_build_dir()
        self.__copy_files_to_build_dir()
        self.__build_plugin_zip("KiCad_plugin.zip")







class MetadataGenerator:

    def __sha256sum(self, filename):
        h = hashlib.sha256()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    def __file_size_bytes(self, filename):
        return os.path.getsize(filename)

    def __install_size_bytes(self, zip_filename):
        total = 0
        with zipfile.ZipFile(zip_filename, "r") as zipf:
            for info in zipf.infolist():
                # Only files, not directories
                if not info.is_dir():
                    total += info.file_size
        return total

    def __getsha256(self, filename) -> str:
        sha256 = hashlib.sha256()
        with open(filename, "rb") as f:
            while data := f.read(self.READ_SIZE):
                sha256.update(data)
        return sha256.hexdigest()

    def __get_package_metadata(self, filename):
        z = zipfile.ZipFile(filename, "r")
        install_size = sum(
            entry.file_size for entry in z.infolist() if not entry.is_dir()
        )
        return {
            "download_sha256": self.__getsha256(filename),
            "download_size": os.path.getsize(filename),
            "install_size": install_size,
        }

    def __generate_metadata(self, output_metadata_file, zip_filename):
        with open("build/metadata.json", "r", encoding="utf-8") as f:
            metadata = json.load(f)
            version = metadata["versions"][0]
            package_metadata = self.__get_package_metadata(zip_filename)
            version.update(package_metadata)

        with open(output_metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)
            f.write("\n")
        print(f"Generated {output_metadata_file} with updated metadata.")

    def __create_package_Metadata(self):
        pass



packager = Packager()

if __name__ == "__main__":
    packager.package()
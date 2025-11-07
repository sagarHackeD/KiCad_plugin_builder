import hashlib
import json
import os
import zipfile


class MetadataGenerator:
    """Class to generate metadata for KiCad plugin package."""

    READ_SIZE = 65536

    def __init__(self, download_url: str):
        self.download_url = download_url
        self.download_dir = "build"
        self.download_path = os.path.join(self.download_dir, "kicad-package.zip")

    def download_zip(self):
        import requests

        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir, exist_ok=True)

        response = requests.get(self.download_url, stream=True, timeout=30)
        response.raise_for_status()
        with open(self.download_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

    def extract_metadata_from_zip(self):
        with zipfile.ZipFile(self.download_path, "r") as zip_ref:
            zip_ref.extract("metadata.json", self.download_dir)

    def generate_metadata(self):
        with open(self.download_dir + "/metadata.json", "r", encoding="utf-8") as f:
            metadata = json.load(f)
            version = metadata["versions"][0]
            package_metadata = self.__get_package_stats(self.download_path)
            version.update(package_metadata)

        output_metadata_file = os.path.join(self.download_dir, "metadata.json")
        os.makedirs(self.download_dir, exist_ok=True)
        with open(output_metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)
            f.write("\n")
        print(f"Generated {output_metadata_file} with updated metadata.")

    # def __sha256sum(self, filename):
    #     h = hashlib.sha256()
    #     with open(filename, "rb") as f:
    #         for chunk in iter(lambda: f.read(8192), b""):
    #             h.update(chunk)
    #     return h.hexdigest()

    # def __file_size_bytes(self, filename):
    #     return os.path.getsize(filename)

    # def __install_size_bytes(self, zip_filename):
    #     total = 0
    #     with zipfile.ZipFile(zip_filename, "r") as zipf:
    #         for info in zipf.infolist():
    #             # Only files, not directories
    #             if not info.is_dir():
    #                 total += info.file_size
    #     return total

    def __getsha256(self, filename) -> str:
        sha256 = hashlib.sha256()
        with open(filename, "rb") as f:
            while data := f.read(self.READ_SIZE):
                sha256.update(data)
        return sha256.hexdigest()

    def __get_package_stats(self, filename):
        z = zipfile.ZipFile(filename, "r")
        install_size = sum(
            entry.file_size for entry in z.infolist() if not entry.is_dir()
        )
        return {
            "download_sha256": self.__getsha256(filename),
            "download_size": os.path.getsize(filename),
            "install_size": install_size,
            "download_url": self.download_url,
        }


medata = MetadataGenerator(
    "https://github.com/sagarHackeD/Snap_To_Grid_KiCAD/releases/download/v1.0.1/kicad-package.zip"
)

if __name__ == "__main__":
    medata.download_zip()
    medata.extract_metadata_from_zip()
    medata.generate_metadata()

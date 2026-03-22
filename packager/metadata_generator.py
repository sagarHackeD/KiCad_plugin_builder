import hashlib
import json
import os
import zipfile
import requests


class MetadataGenerator:
    """Class to generate metadata for KiCad plugin package."""

    READ_SIZE = 65536

    version_data = []

    def __init__(self, in_metadata):
        self.build_dir = "build"
        self.version_data = []
        self.dist_dir = "dist"
        self.in_metadata = in_metadata
        # self.download_path = os.path.join(self.download_dir, "kicad-package.zip")

    def download_zip(self, release, download_dir: str = "build"):
        """Download the zip file from the release and save it to the specified directory."""
        self.download_url = release["browser_download_url"]
        self.version = release["tag_name"]
        self.version_path = os.path.join(download_dir, self.version)

        if not os.path.exists(self.version_path):
            os.makedirs(self.version_path, exist_ok=True)

        self.build_dir = self.version_path
        self.download_path = os.path.join(self.version_path, "kicad-package.zip")

        response = requests.get(self.download_url, stream=True, timeout=30)
        response.raise_for_status()
        with open(self.download_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return self.download_path, self.version

    def extract_metadata_from_zip(self, metadata, download_path: str, version: str):
        with zipfile.ZipFile(download_path, "r") as zip_ref:
            zip_ref.extract(metadata, os.path.dirname(download_path))

    def generate_metadata(self, input_metadata_file, version_data, package_dir):

        os.makedirs(package_dir, exist_ok=True)

        with open(input_metadata_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)
            metadata["versions"] = version_data
            metadata.pop("Repository",None)

        dist_metadata_file = os.path.join(package_dir, "metadata.json")
        with open(dist_metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)
            f.write("\n")
        print(f"Generated {dist_metadata_file} with updated metadata.")

    def __getsha256(self, filename) -> str:
        sha256 = hashlib.sha256()
        with open(filename, "rb") as f:
            while data := f.read(self.READ_SIZE):
                sha256.update(data)
        return sha256.hexdigest()

    def __get_package_stats(self, filename):
        with zipfile.ZipFile(filename, "r") as z:
            install_size = sum(
                entry.file_size for entry in z.infolist() if not entry.is_dir()
            )
        return {
            "download_sha256": self.__getsha256(filename),
            "download_size": os.path.getsize(filename),
            "install_size": install_size,
            "download_url": self.download_url,
        }

    def extract_version_from_zip(self, metadata, download_path: str) -> str:
        data = self.__get_package_stats(download_path)
        with zipfile.ZipFile(download_path, "r") as zip_ref:
            with zip_ref.open(metadata) as f:
                metadata = json.load(f)
                metadata["versions"] = {**metadata["versions"][0], **data}

                return metadata["versions"]

    def create_package_dir(self):
        with open(self.in_metadata, "r", encoding="utf-8") as f:
            metadata = json.load(f)
            identifier = metadata["identifier"]

            if not os.path.exists(os.path.join(self.dist_dir, identifier)):
                os.makedirs(os.path.join(self.dist_dir, identifier), exist_ok=True)

        return os.path.join(self.dist_dir, identifier)

    def create(self, releases, package_dir):
        for release in releases:
            print(f"Processing release: {release['tag_name']} - {release['name']}")

            download_path, version = self.download_zip(release, download_dir="build")
            self.extract_metadata_from_zip("metadata.json",download_path, version)
            self.version_data.append(self.extract_version_from_zip("metadata.json",download_path))

        self.generate_metadata(self.in_metadata, self.version_data, package_dir)

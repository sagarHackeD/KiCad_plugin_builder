import json
import os
from packager_class import Packager
from metadata_generator_class import MetadataGenerator


packager = Packager("build","metadata.json",'src',"resources/icon.png")

medata = MetadataGenerator(
    "https://github.com/sagarHackeD/Snap_To_Grid_KiCAD/releases/download/v1.0.1/kicad-package.zip"
)

if __name__ == "__main__":
    # make sure your metadata file is filled with necessory information before running this script

    packager.package()

    # after packaging check the zip file with Packaging Toolkit https://gitlab.com/kicad/addons/metadata#packaging-toolkit

    # after verifying you have to create a relesease on github and upload the zip file or any other publically accessible location

    # then run the metadata generator to create icon and a metadata file with sha256, download link and size information for submitting to the KiCad plugin manager

    # create a package

    with open("metadata.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
        identifier = metadata["identifier"]

        if not os.path.exists(identifier):
            os.makedirs(identifier, exist_ok=True)

        print(os.path.join(identifier, "metadata.json"))



    medata.download_zip()
    medata.extract_metadata_from_zip()
    medata.generate_metadata(os.path.join(identifier, "metadata.json"))
    packager.resize_image("resources/icon.png", (64, 64), os.path.join(identifier, "icon.png"))

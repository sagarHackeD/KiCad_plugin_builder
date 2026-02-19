import json
import os

from packager import MetadataGenerator, PackagerClass


if __name__ == "__main__":
    #Step 1 : generate a zip file for your plugin using the packager 
    packager_ = PackagerClass(
        build_dir="build",
        metadata_file="metadata.json",
        src_folder="src",
        icon_file="resources/icon.png",
        output_dir="output",
    )
    
    packager_.package()

    ## Step 2 : create a release on github and upload the zip file or any other publically accessible location

    ## Step 3 : run the metadata generator to create icon and a metadata file with sha256, download link and size information for submitting to the KiCad plugin manager

    medata = MetadataGenerator("https://github.com/sagarHackeD/Place_By_Sch_KiCad/releases/download/v2.1.0/kicad-package.zip")

    # make sure your metadata file is filled with necessory information before running this script

    # after packaging check the zip file with Packaging Toolkit https://gitlab.com/kicad/addons/metadata#packaging-toolkit

    # after verifying you have to create a relesease on github and upload the zip file or any other publically accessible location

    # then run the metadata generator to create icon and a metadata file with sha256, download link and size information for submitting to the KiCad plugin manager

    # create a package

    output_dir = "output"

    with open("metadata.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
        identifier = metadata["identifier"]

        if not os.path.exists(os.path.join(output_dir, identifier)):
            os.makedirs(os.path.join(output_dir, identifier), exist_ok=True)

        print(os.path.join(output_dir, identifier, "metadata.json"))

    medata.download_zip()
    medata.extract_metadata_from_zip()
    medata.generate_metadata(os.path.join(output_dir, identifier, "metadata.json"))
    packager_.resize_image("resources/icon.png", (64, 64), os.path.join(output_dir, identifier, "icon.png"))

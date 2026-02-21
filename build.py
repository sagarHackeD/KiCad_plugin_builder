import os

from packager import MetadataGenerator, PackagerClass, get_release_urls_github, get_owner_repo


if __name__ == "__main__":
    medata = MetadataGenerator()
    package_dir = medata.create_package_dir()
    ## Step 1 : generate a zip file for your plugin using the packager
    packager_ = PackagerClass(
        build_dir=medata.build_dir,
        metadata_file="metadata.json",
        src_folder="src",
        icon_file="resources/icon.png",
        dist_dir=medata.dist_dir,
    )

    packager_.package()

    ## Step 2 : create a release on github and upload the zip file or any other publically accessible location

    ## Step 3 : run the metadata generator to create a metadata file with sha256, download link and size information for submitting to the KiCad plugin manager

    owner, repo = get_owner_repo("metadata.json")

    print(f"Fetching release information for {owner}/{repo}...")

    releses = get_release_urls_github(owner, repo)
    # releses = get_release_urls_github("sagarHackeD", "Snap_To_Grid_KiCAD")

    medata.create(releses, package_dir)

    # make sure your metadata file is filled with necessory information before running this script

    # after packaging check the zip file with Packaging Toolkit https://gitlab.com/kicad/addons/metadata#packaging-toolkit

    # after verifying you have to create a relesease on github and upload the zip file or any other publically accessible location

    # then run the metadata generator to create icon and a metadata file with sha256, download link and size information for submitting to the KiCad plugin manager

    # create a package

    # medata.download_zip()
    # medata.extract_metadata_from_zip()
    # medata.generate_metadata(os.path.join(dist_dir, identifier, "metadata.json"))
    packager_.resize_image("resources/icon.png", (64, 64), os.path.join(package_dir, "icon.png"))




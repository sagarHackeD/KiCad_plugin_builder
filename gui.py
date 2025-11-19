import os
import shutil
import PySimpleGUI as sg
from packager_class import Packager
from metadata_generator_class import MetadataGenerator

from github import get_release_urls


sg.set_options(font=("Courier", 12))
sg.set_options(icon="icon.ico")
sg.theme("BlueMono")


def build_package(values):
    packager = Packager(
        "build",
        values["metadata_file"],
        values["source_folder"],
        values["icon_file"],
    )

    packager.package()  # build the package


def output_terminal(key: str):
    return [
        sg.Output(
            size=(60, 10),
            k=key,
            expand_x=True,
            expand_y=True,
            echo_stdout_stderr=True,
        )
    ]


Packager_layout = [
    [sg.Text("Package Plugin : ")],
    [
        sg.Text("Metadata Location : "),
        sg.Input(
            "C:/Users/ECHS/Desktop/Place_By_Sch_KiCad/metadata.json", k="metadata_file"
        ),
        sg.FileBrowse(),
        sg.Button("Ok", k="metadata_gen_Key"),
    ],
    [
        sg.Text("Source Location   : "),
        sg.Input("C:/Users/ECHS/Desktop/Place_By_Sch_KiCad/src", k="source_folder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Icon Location     : "),
        sg.Input(
            "C:/Users/ECHS/Desktop/Place_By_Sch_KiCad/resources/icon.png", k="icon_file"
        ),
        sg.FileBrowse(),
    ],
    [
        sg.Button("Build Plugin Package", k="Build Plugin Package"),
        sg.Button("Clean", k="cleanKey"),
    ],
    output_terminal("terminal_packager"),
]

Metadata = [
    [sg.Text("Populate Metadata File for submission : ")],
    [sg.Text("Github Username : "), sg.Input("sagarHackeD", k="usernameKey")],
    [sg.Text("Github Repo : "), sg.Input("Place_By_Sch_KiCad", k="repoKey")],
    [
        sg.Button("Populate", k="metadata_populate_Key"),
        # sg.Button("Clean", k="cleanKey"),
    ],
    output_terminal("terminal_packager"),
]

help_layout = [
    [sg.Text("Create Local Backup")],
    [
        sg.Text("Source Location : "),
        sg.Input("", k="source_folder"),
        sg.FolderBrowse(),
    ],
]


layout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab("Packager", Packager_layout, key="PackagerTab"),
                    sg.Tab("Metadata", Metadata, key="MetadataTab"),
                    sg.Tab("Help", help_layout, key="HelpTab"),
                ]
            ],
            key="-TAB GROUP-",
            expand_x=True,
            expand_y=True,
        ),
    ],
    [
        sg.Text(
            "Designed and Written by Sagar Naik - sagarnaik430@googlemail.com",
            font=("Courier", 8),
        )
    ],
]

window = sg.Window("KiCad Plugin Builder", layout, resizable=True, finalize=True)

while True:
    event, values = window.read()  # type: ignore
    if event in (sg.WIN_CLOSED, "Exit", "cancel"):
        window.close()
        break
    if event:
        match event:
            case "metadata_gen_Key":
                print("Metadata")
            case "Build Plugin Package":
                print("Building Plugin Package...\n")
                build_package(values)
                print("Plugin Package Built Successfully!\nat: ./KiCad_plugin.zip\n")
            case "cleanKey":
                shutil.rmtree("build", ignore_errors=True)
                shutil.rmtree("com.*", ignore_errors=True)
                print("Cleaned build directory.\n")

            case "metadata_populate_Key":
                print("Populating Metadata File...\n")

                for urls in get_release_urls(values["usernameKey"], values["repoKey"]):
                    print(f"Found URL: {urls}\n")
                    metadata_generator = MetadataGenerator(urls)
                    metadata_generator.download_zip()
                    metadata_generator.extract_metadata_from_zip()
                    metadata_generator.generate_metadata("metadata.json")
                    print("Metadata File Populated Successfully!\n")
                    break

    
            case _:
                # for v in values:
                #     pass
                # print(f"{v:<25} =  {values[v]}\n")
                print(f"Event: {event}\n")

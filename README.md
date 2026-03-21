# KiCad Plugin Builder

A comprehensive plugin packager and builder tool for KiCad plugins shared on PCM (Plugin Manager).

## Overview

KiCad Plugin Builder is a Python-based tool that streamlines the process of packaging, building, and preparing KiCad plugins for distribution through the KiCad Plugin Manager. It provides both a graphical user interface (GUI) and command-line utilities to automate the packaging workflow.

## Features

- **Plugin Packaging**: Automatically package KiCad plugins into distributable ZIP files
- **Metadata Generation**: Create and manage plugin metadata files with SHA256 checksums, download links, and size information
- **GUI Interface**: User-friendly wxPython interface for easy plugin management
- **GitHub Integration**: Automatic release URL fetching from GitHub repositories
- **Icon Processing**: Automatic resizing of plugin icons to standard dimensions (64x64)
- **Build Automation**: Streamlined build process with configurable directories and source paths

## Project Structure

```
KiCad_plugin_builder/
├── PluginBuilder.py      # Main entry point for the GUI application
├── build.py              # Build script for automated packaging
├── wx_gui.py             # wxPython GUI implementation
├── app/                  # Application core modules
├── packager/             # Packaging utilities and metadata generation
├── resources/            # Icons and other resources
├── LICENSE               # MIT License
└── README.md             # This file
```

## Installation

### Requirements

- Python 3.7 or higher
- wxPython
- Additional dependencies as specified in the project

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sagarHackeD/KiCad_plugin_builder.git
   cd KiCad_plugin_builder
   ```

2. Install dependencies:
   ```bash
   pip install wxPython
   ```

## Usage

### GUI Application

Run the graphical interface:
```bash
python PluginBuilder.py
```

The GUI provides three main tabs:

#### 1. **Packager Tab**
- Configure metadata, source, and icon file locations
- Set build and distribution directories
- Build plugin packages
- Clean build artifacts

#### 2. **Metadata Tab**
- Generate and manage plugin metadata files
- Configure plugin information for PCM submission

#### 3. **Help Tab**
- Access documentation and usage instructions

### Command-Line Build

For automated or scripted builds:
```bash
python build.py
```

The build script performs the following steps:

1. **Packaging Phase**: Creates a distributable ZIP file
   - Input: Plugin source files and metadata
   - Output: Packaged plugin ZIP file

2. **Release Phase**: Creates GitHub releases
   - Upload the packaged ZIP file to a GitHub release

3. **Metadata Generation**: Creates metadata for PCM submission
   - Generates SHA256 checksums
   - Includes download links
   - Captures file size information

## Configuration

### Metadata File Format

Create a `metadata.json` file with your plugin information:

```json
{
  "plugin_name": "Your Plugin Name",
  "version": "1.0.0",
  "repository": "owner/repo",
  "author": "Your Name",
  "description": "Plugin description"
}
```

### Required Resources

- `metadata.json`: Plugin metadata configuration
- `src/`: Source directory containing your plugin code
- `resources/icon.png`: Plugin icon (will be resized to 64x64)

## Workflow

### Step 1: Prepare Your Plugin
- Organize plugin files in the `src/` directory
- Create `metadata.json` with plugin information
- Prepare a high-resolution icon file

### Step 2: Package the Plugin
```bash
python build.py
```

### Step 3: Create GitHub Release
- Create a release on GitHub
- Upload the generated ZIP file from the `dist/` directory

### Step 4: Verify and Submit
- Use the [KiCad Packaging Toolkit](https://gitlab.com/kicad/addons/metadata#packaging-toolkit) to verify your package
- Submit the generated metadata file to the KiCad Plugin Manager

## API Functions

### Key Classes and Functions

- **MetadataGenerator**: Handles metadata file creation and management
- **PackagerClass**: Core packaging functionality
- **get_release_urls_github()**: Fetches release URLs from GitHub
- **get_owner_repo()**: Extracts owner and repository information from metadata

## KiCad Plugin Manager Submission

After packaging and verification:

1. Ensure all metadata is complete in the generated metadata file
2. Verify the package using the [KiCad Packaging Toolkit](https://gitlab.com/kicad/addons/metadata#packaging-toolkit)
3. Create a GitHub release with your packaged ZIP file
4. Submit the metadata file to the KiCad Plugin Manager for inclusion

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Designed and written by **Sagar Naik**
- Email: sagarnaik430@googlemail.com

## Support

For issues, feature requests, or contributions, please visit the [GitHub repository](https://github.com/sagarHackeD/KiCad_plugin_builder).
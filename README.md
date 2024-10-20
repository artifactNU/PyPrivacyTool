# PyPrivacyTool

PyPrivacyTool is a comprehensive suite of privacy-enhancing tools designed to help users protect their digital privacy and security. Built with Python, this toolset includes functionalities such as metadata removal from files, secure file deletion, data anonymization, and more. PyPrivacyTool aims to provide an accessible and easy-to-use interface for individuals and organizations concerned about data privacy.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [General Usage](#general-usage)
  - [Remove Metadata](#remove-metadata)
  - [Secure Delete](#secure-delete)
- [Supported File Formats](#supported-file-formats)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Features

- **Metadata Removal**: Remove metadata from images, PDFs, and audio files to protect personal information.
- **Secure File Deletion**: Permanently delete files and directories by overwriting them multiple times.
- **Data Anonymization**: *(Planned)* Anonymize sensitive data in datasets while preserving data utility.
- **Privacy Audit**: *(Planned)* Analyze systems for potential privacy leaks and provide recommendations.
- **User-Friendly Interface**: Command-line interface with comprehensive help and options.

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Steps

1. **Clone the Repository**

       git clone git@github.com:artifactNU/PyPrivacyTool.git
       cd PyPrivacyTool

2. **Install the Package**

   Install PyPrivacyTool in editable mode to reflect any code changes immediately:

       pip install -e .

3. **Install Dependencies**

   PyPrivacyTool's dependencies should be installed automatically during the package installation. If not, you can install them manually:

       pip install -r requirements.txt

## Usage

PyPrivacyTool provides a unified command-line interface with multiple subcommands for different tools. You can access the main help menu or specific tool help menus.

### General Usage

    pyprivacytool [tool] [options]

To display the main help message with a list of available tools:

    pyprivacytool --help

### Remove Metadata

Remove metadata from files to protect personal information embedded within them.

**Usage:**

    pyprivacytool remove-metadata --file FILE_PATH [--output OUTPUT_PATH] [--list-formats]

**Options:**

- `--file, -f` **(required)**: Path to the file from which to remove metadata.
- `--output, -o`: Path to save the file without metadata. If not specified, the original file will be overwritten.
- `--list-formats`: List all supported file formats for metadata removal.

### Secure Delete

Securely delete files or directories by overwriting them with random data multiple times.

**Usage:**

    pyprivacytool secure-delete (--file FILE_PATH | --dir DIR_PATH) [--passes PASSES] [--verbose]

**Options:**

- `--file, -f`: Path to the file to securely delete.
- `--dir, -d`: Path to the directory to securely delete.
- `--passes, -p`: Number of overwrite passes (default: 3).
- `--verbose, -v`: Enable verbose output.

## Supported File Formats

The `remove-metadata` tool supports the following file formats:

- **Images**: `.jpg`, `.jpeg`, `.png`
- **PDFs**: `.pdf`
- **Audio**: `.mp3`, `.flac`, `.wav`

## Examples

### Remove Metadata from an Image

    pyprivacytool remove-metadata --file image.jpg --output image_clean.jpg

### Remove Metadata from a PDF

    pyprivacytool remove-metadata --file document.pdf --output document_clean.pdf

### Securely Delete a File

    pyprivacytool secure-delete --file sensitive.txt --passes 5 --verbose

### Securely Delete a Directory

    pyprivacytool secure-delete --dir /path/to/directory --passes 3

## Project Structure

    PyPrivacyTool/
    ├── src/
    │   └── pyprivacytool/
    │       ├── __init__.py
    │       ├── main.py
    │       ├── remove_metadata.py
    │       ├── secure_delete.py
    │       ├── data_anonymizer.py (WIP)
    │       ├── privacy_audit.py (WIP)
    │       └── # ... other modules
    ├── tests/
    │   ├── __init__.py
    │   ├── test_remove_metadata.py
    │   ├── test_secure_delete.py
    │   └── # ... other tests
    ├── setup.py
    ├── requirements.txt
    └── README.md

- **`src/pyprivacytool/`**: Contains the source code modules.
- **`tests/`**: Contains unit tests for the modules.
- **`setup.py`**: Build script for setuptools.
- **`requirements.txt`**: Lists project dependencies.

## Contributing

Contributions are welcome! Please read CONTRIBUTING.md for details on how to contribute to this project.

6. **Create a Pull Request**

   Go to your fork on GitHub and click "New Pull Request."

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Contributors**: Thank you to all the contributors who have helped improve this project.
- **Libraries Used**:
  - [Pillow](https://python-pillow.org/): For image processing.
  - [PyPDF2](https://github.com/py-pdf/PyPDF2): For PDF manipulation.
  - [Mutagen](https://mutagen.readthedocs.io/): For audio metadata handling.

## Contact

For any inquiries or support, please open an issue on the GitHub repository or contact [simon@artifact.nu](mailto:simon@artifact.nu).

**GitHub Repository**: [https://github.com/artifactNU/PyPrivacyTool](https://github.com/yourusername/PyPrivacyTool)

---


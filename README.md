
---

# LeanDesk Cleaning Module

The LeanDesk Cleaning Module is a Python tool designed to help you organize and clean your directories by clustering files into specific folders based on their types. This module is especially useful for maintaining a tidy Downloads folder.

## Features

- **PDF Files:** Move PDF files to the 'PDF files' directory.
- **Document Files:** Move .docx and .doc files to the 'Documents files' directory.
- **Audio Files:** Move .mp3 and .mp4 files to the 'MP3 files' directory.
- **Excel Files:** Move .xlsx and .xls files to the 'Excel files' directory.
- **Zip Files:** Move .zip files to the 'Zip files' directory.
- **Executable Files:** Move .exe files to the 'Exe files' directory.
- **Text Files:** Move .txt files to the 'Text files' directory.
- **Image Files:** Move .png, .jpeg, and .jpg files to the respective directories.
- **CSV Files:** Move .csv files to the 'CSV files' directory.
- **GIF Files:** Move .gif files to the 'GIF files' directory.
- **HTML Files:** Move .html files to the 'HTML files' directory.
- **Notebook Files:** Move .ipynb files to the 'Notebook files' directory.
- **Presentation Files:** Move .pptx and .ppt files to the 'PPT files' directory.
- **SVG Files:** Move .svg files to the 'SVG files' directory.
- **MOV Files:** Move .mov files to the 'MOV files' directory.
- **JSON Files:** Move .json files to the 'JSON files' directory.
- **WebP Files:** Move .webp files to the 'WebP files' directory.

## Installation

1. Clone the repository or download the source code.
2. Navigate to the module's root directory in the command line.
3. Run `pip install .` to install the module.

## Usage

### Command-Line Interface (CLI)

Run the following command in the terminal to clean a directory:

```bash
clean /path/to/directory
```

Replace `/path/to/directory` with the path to the directory you want to clean.

Example:

```bash
clean C:\Users\YourUserName\Downloads
```

## Permissions

Ensure that you have the necessary permissions to perform cleaning operations in the specified directory. The module may move, create, and organize files, so proper permissions are essential.

---

Feel free to add more sections or details to the README based on your preferences or any additional information users might find helpful.
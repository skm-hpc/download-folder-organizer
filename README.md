# 📂 Download Organizer — Python Mini Project

A lightweight Python utility that automatically organizes files in the current user's **Downloads** folder into categorized directories based on file type.

The project requires **no external Python packages** and provides clean, color-coded terminal output with real-time progress, individual file sizes, category statistics, and a final storage summary.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)
![Dependencies](https://img.shields.io/badge/Dependencies-None-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- Automatically detects the current user's `Downloads` folder
- No need to manually enter the Downloads path
- Organizes files by extension
- Automatically creates category folders
- Supports:
  - 🖼️ Images
  - 📄 Documents
  - 🎬 Videos
  - 🎵 Audio
  - 📦 Archives
  - 📁 Others
- Shows individual file sizes
- Shows total Downloads size before processing
- Displays an inline progress bar for every file
- Shows percentage and file counter
- Prevents overwriting existing files
- Reports skipped files separately
- Reports errors separately
- Provides category-wise file counts and storage usage
- Displays total files and total data processed
- Shows processing time
- Uses ANSI colors for a modern terminal interface
- Works on Linux, macOS, and Windows terminals
- Uses only Python standard-library modules

---

## 📸 Project Overview

The application scans the user's Downloads folder and automatically moves files into appropriate folders:

```text
Downloads/
│
├── Images/
├── Documents/
├── Videos/
├── Audio/
├── Archives/
└── Others/
```

---

## 🚀 Getting Started

### Requirements

- Python 3.8 or newer
- A standard terminal
- No external Python packages

Check your Python version:

```bash
python3 --version
```

Example:

```text
Python 3.12.3
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-download-organizer.git
```

Enter the project directory:

```bash
cd python-download-organizer
```

---

## ▶️ Run the Script

### Linux / macOS

```bash
python3 organize_download.py
```

### Windows

```bash
python organize_download.py
```

The script automatically detects the current user's Downloads folder.

Examples:

```text
Linux:
/home/username/Downloads

macOS:
/Users/username/Downloads

Windows:
C:\Users\username\Downloads
```

No path needs to be entered manually.

---

## 🗂️ File Categories

### 🖼️ Images

Supported extensions:

```text
.jpg
.jpeg
.png
.gif
.webp
.bmp
.svg
.ico
.tiff
.tif
```

Destination:

```text
Downloads/Images/
```

### 📄 Documents

Supported extensions:

```text
.pdf
.doc
.docx
.txt
.rtf
.odt
.xls
.xlsx
.ppt
.pptx
.csv
```

Destination:

```text
Downloads/Documents/
```

### 🎬 Videos

Supported extensions:

```text
.mp4
.mkv
.avi
.mov
.wmv
.flv
.webm
.m4v
```

Destination:

```text
Downloads/Videos/
```

### 🎵 Audio

Supported extensions:

```text
.mp3
.wav
.m4a
.aac
.flac
.ogg
.wma
```

Destination:

```text
Downloads/Audio/
```

### 📦 Archives

Supported extensions:

```text
.zip
.rar
.7z
.tar
.gz
.bz2
.xz
.iso
```

Destination:

```text
Downloads/Archives/
```

### 📁 Others

Any unsupported extension is placed into:

```text
Downloads/Others/
```

For example:

```text
.exe
.deb
.AppImage
.xyz
```

---

## 🖥️ Sample Terminal Output

> **Note:** The output below is a hypothetical example for documentation purposes. It does not represent an actual run or any user's files.

```text
========================================================================
                       DOWNLOAD ORGANIZER
                  Automatic File Organization
========================================================================

Downloads folder
  /home/user/Downloads

Files detected: 12
Total size: 184.32 MB

Starting organization...

[##------------------]   8%  1/12 [OK  ] holiday_photo.jpg        2.14 MB -> Images/
[###-----------------]  16%  2/12 [OK  ] project_report.pdf       1.82 MB -> Documents/
[#####---------------]  25%  3/12 [OK  ] presentation.pptx        5.36 MB -> Documents/
[######--------------]  33%  4/12 [OK  ] movie_clip.mp4           48.75 MB -> Videos/
[########------------]  41%  5/12 [OK  ] song.mp3                  8.21 MB -> Audio/
[##########----------]  50%  6/12 [OK  ] archive.zip               12.64 MB -> Archives/
[###########---------]  58%  7/12 [OK  ] screenshot.png              1.03 MB -> Images/
[############--------]  66%  8/12 [SKIP] data.csv                     0 B -> Documents/
[###############-----]  75%  9/12 [OK  ] notes.txt                   23.45 KB -> Documents/
[################----]  83% 10/12 [OK  ] setup.exe                   15.26 MB -> Others/
[##################--]  91% 11/12 [OK  ] document.docx                3.17 MB -> Documents/
[####################] 100% 12/12 [OK  ] wallpaper.webp               1.48 MB -> Images/

------------------------------------------------------------------------
                       ORGANIZATION SUMMARY
------------------------------------------------------------------------

  Images       :    3 file(s)        4.65 MB
  Documents    :    5 file(s)       10.82 MB
  Videos       :    1 file(s)       48.75 MB
  Audio        :    1 file(s)        8.21 MB
  Archives     :    1 file(s)       12.64 MB
  Others       :    1 file(s)       15.26 MB

------------------------------------------------------------------------

  [OK] Successfully moved : 11     184.32 MB
  [--] Skipped             : 1       0 B
  [!!] Errors              : 0       0 B

  [##] Total files scanned : 12
  [MB] Total data scanned  : 184.32 MB
  [TIME] Processing time   : 0.03 seconds

[SUCCESS] Download organization completed.
```

---

## 📊 File Size Reporting

The application automatically converts file sizes into readable units.

Examples:

```text
512 B
18.12 KB
4.82 MB
1.27 GB
2.41 TB
```

It reports:

### Individual file size

```text
report.pdf    4.82 MB
```

### Category size

```text
Documents : 12 files    28.64 MB
```

### Total size

```text
Total data scanned : 184.32 MB
```

### Successfully moved size

```text
Successfully moved : 11    184.32 MB
```

---

## 🛡️ Existing File Protection

The script does **not overwrite an existing destination file**.

If:

```text
Downloads/Documents/report.pdf
```

already exists and another `report.pdf` is found in the Downloads folder, the new file is skipped.

The terminal reports:

```text
[SKIP] report.pdf -> already exists
```

Skipped files are included in the final statistics.

---

## 📈 Final Statistics

The summary provides:

| Statistic | Description |
|---|---|
| Successfully moved | Number and size of files moved |
| Skipped | Files that were not moved because the destination already existed |
| Errors | Files that could not be moved |
| Files scanned | Total files found in Downloads |
| Total data scanned | Combined size of all detected files |
| Processing time | Time taken to organize the files |

Category-level statistics are also displayed.

---

## 🔧 Customizing Categories

The categories can be modified inside:

```python
CATEGORIES = {
    "Images": (...),
    "Documents": (...),
    "Archives": (...),
    "Videos": (...),
    "Audio": (...),
}
```

For example, to add a Design category:

```python
"Design": (
    ".psd",
    ".ai",
    ".eps",
)
```

The category can then be added to the category color and summary configuration.

---

## 🖥️ Cross-Platform Support

The script uses:

```python
Path.home()
```

to determine the current user's home directory.

Therefore it automatically resolves the Downloads folder for:

### Linux

```text
/home/username/Downloads
```

### macOS

```text
/Users/username/Downloads
```

### Windows

```text
C:\Users\username\Downloads
```

No hard-coded username or machine-specific path is required.

---

## 🧩 Technologies Used

The project uses only Python's standard library:

```python
from pathlib import Path
import shutil
import time
import sys
```

### `pathlib`

Used for filesystem paths and detecting the user's Downloads directory.

### `shutil`

Used to move files between directories.

### `time`

Used to calculate processing time.

### `sys`

Used to detect terminal capabilities and control ANSI color output.

---

## 📁 Repository Structure

Recommended repository layout:

```text
python-download-organizer/
│
├── organize_download.py
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚠️ Important Notes

The program **moves files**, rather than copying them.

Before using it on an important Downloads folder, make sure you understand the category rules and destination behavior.

Files with unsupported extensions are placed in:

```text
Others/
```

Existing destination files are skipped rather than overwritten.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Test the script.
5. Commit your changes:

```bash
git add .
git commit -m "Add new feature"
```

6. Push the branch:

```bash
git push origin feature/new-feature
```

7. Open a Pull Request.

---

## 📄 License

This project is released under the **MIT License**.

See the `LICENSE` file for details.

---

## ⭐ Project Summary

**Download Organizer** is a simple Python automation project designed to keep the user's Downloads directory clean and organized.

It automatically detects the current user's Downloads folder, identifies files by extension, creates the required category directories, moves files safely, reports individual and aggregate file sizes, displays real-time progress, and provides a detailed completion summary.

```text
Downloads
    │
    ├── Images
    ├── Documents
    ├── Videos
    ├── Audio
    ├── Archives
    └── Others
```

**Simple. Automatic. Cross-platform. No external dependencies.**

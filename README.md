# SAM Reader

**SAM Reader** is a powerful Python application designed to read and extract data from the Windows Registry, specifically from the `HKEY_LOCAL_MACHINE\SAM` key. This tool can be useful for system administrators, security researchers, or anyone interested in inspecting the SAM (Security Account Manager) database on Windows.

---

## Features

- Reads data from `HKEY_LOCAL_MACHINE\SAM`
- Parses and displays relevant security account information
- Simple CLI interface for easy use
- Packaged as a standalone `.exe` for Windows (no Python installation required)
- Written entirely in Python using the `winreg` module

---

## Installation

If you want to run the Python script directly:

```bash
git clone https://github.com/ManjaroLover153/SAM-Reader.git
cd sam-reader
python main.py
```

Or simply download the installer from releases section.

---

# Usage
Run the application via command line:
```bash
python main.py
```
or, if you have the executable:
```bash
dist/main.exe
```
Follow the prompts to extract SAM data.

---
# Requirements
- Windows OS (due to the usage of the Windows Registry and winreg module)
- Python 3.x (if running the .py script)
- Administrator privileges may be required to access certain registry keys (or use ExecTI if using `.exe`)

# Security Warning
Accessing the SAM database involves sensitive system data. Use responsibly and only on machines where you have permission.

---

# Contributing
Contributions, bug reports, and feature requests are welcome! Feel free to open issues or submit pull requests.

---
# License
MIT License — see `LICENSE` file for details.

# Contact
Created by ManjaroLover153 — https://github.com/ManjaroLover153

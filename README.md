# EuroMillions Number Picker (Ubuntu Edition)

A modern, dark-themed Python application for generating EuroMillions lottery numbers. This version uses **CustomTkinter** for a sleek, high-DPI "Dark Mode" aesthetic native to Linux desktops.

## 🚀 Features

* **Modern GUI**: Powered by `customtkinter` (a modern wrapper for Tkinter).
* **EuroMillions Logic**: Generates 5 unique main numbers (1–50) and 2 unique lucky stars (1–12).
* **Auto-Sorting**: Numbers are displayed in ascending order for easy entry.
* **Linux Optimized**: Centered window launching with custom gold and blue accents.

## 🛠 Prerequisites (Ubuntu/Debian)

Before running the application, you must install the Python UI and environment modules globally on your Ubuntu system:

```bash
sudo apt update
sudo apt install python3-tk python3-venv python3-pip -y

```

## 📦 Installation & Setup (Step-by-Step)

### 1. Open Your Terminal

You can use either:

* **The Main Ubuntu Terminal**: Press `Ctrl`+`Alt`+`T`.
* **VS Code Terminal**: Go to `Terminal` > `New Terminal`.
* **CD to the lotto number picker folder** Or just right click the folder and open in terminal.

### 2. Create the Virtual Environment

This creates a "sandbox" folder named `.venv` inside your project directory to keep your system clean.

```bash
python3 -m venv .venv

```

### 3. Activate the Environment

This tells your terminal to use the "sandbox" you just created.

```bash
source .venv/bin/activate

```

**How to tell it worked:** Your terminal prompt will now show `(.venv)` at the very beginning of the line, something like this:

> `(.venv) user@ubuntu:~/lotto number picker$`

### 4. Install CustomTkinter (**Crucial Step**)

**Important:** You must see that `(.venv)` prefix before running this. This ensures the library is installed *inside* your project and not globally on your computer.

```bash
pip install customtkinter

```

### 5. Launch the Picker

While the `(.venv)` is still active, run:

```bash
python3 lotto_picker.py

```

### 6. Finished?

When you are done, you can exit the "sandbox" by typing:

```bash
deactivate

```

## ⚙️ Configuration

The script is designed to be modified. Open `lotto_picker.py` in your editor (Gedit, VS Code, etc.) to tweak:

* **`EUROMILLIONS_CONFIG`**: Change the number ranges or count.
* **`STYLE_CONFIG`**: Adjust HEX color codes and window dimensions.

---

## ⚠️ Disclaimer

This project is provided "as-is" without warranty. I am not responsible for any issues, data loss, or "explosions" (code-related or otherwise) that may occur. **Use at your own risk.**

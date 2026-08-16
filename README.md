# EuroMillions Number Picker

A modern, dark-themed Python application for generating EuroMillions lottery numbers. It uses **CustomTkinter** for a sleek, high-DPI "Dark Mode" aesthetic, and runs on **macOS, Windows, and Linux**.

## 🚀 Features

* **Modern GUI**: Powered by `customtkinter` (a modern wrapper for Tkinter).
* **EuroMillions Logic**: Generates 5 unique main numbers (1–50) and 2 unique lucky stars (1–12).
* **Auto-Sorting**: Numbers are displayed in ascending order for easy entry.
* **Cross-Platform**: Centered window launching with custom gold and blue accents.

## 🛠 Prerequisites

* **uv** – the fast Python package and environment manager.
  * macOS (Homebrew): `brew install uv`
  * Windows (PowerShell): `pip install uv`
  * Linux/macOS (curl installer): `curl -LsSf https://astral.sh/uv/install.sh | sh`
  * Or installation from the docs: https://docs.astral.sh/uv/getting-started/installation/
* **Python 3.14+** – if you don't have it installed, uv will download a compatible version automatically when you first run the project.

> [!TIP]
> On some Linux distributions, Tk needs to be installed as a system package. If you get a `_tkinter` import error, run `sudo apt install python3-tk` (Debian/Ubuntu).

## 📦 Installation & Setup

Open a terminal (Terminal on macOS/Linux, PowerShell on Windows) and navigate to the project folder:

```bash
cd lotto-number-picker
```

### 1. Sync the Environment

This creates a `.venv` "sandbox" folder in your project and installs all dependencies (from `pyproject.toml` / `uv.lock`) into it — keeping your system clean.

```bash
uv sync
```

> [!NOTE]
> **How to tell it worked:** You'll see a line like `Installed 3 packages` and a `.venv` folder will appear in the project directory.

### 2. Launch the Picker

```bash
uv run lotto_picker.py
```

> [!NOTE]
> `uv run` automatically checks that the environment is up to date first, so a fresh clone needs nothing more than this single command.

### Screenshot of App

![Lotto number picker Screenshot](./image/Screenshot.png)

### 3. Adding New Dependencies

If you want to add a package later, use uv instead of pip:

```bash
uv add package-name
```

No `deactivate` needed — uv manages the virtual environment for you, so there's nothing to activate or deactivate.

## 🧑‍💻 Development

* Lint and format checks are handled by **ruff** (installed as a dev dependency):
  ```bash
  uv run ruff check .
  uv run ruff format .
  ```

## ⚙️ Configuration

The script is designed to be modified. Open `lotto_picker.py` in your editor (VS Code, PyCharm, etc.) to tweak:

* **`EUROMILLIONS_CONFIG`**: Change the number ranges or count.
* **`STYLE_CONFIG`**: Adjust HEX color codes and window dimensions.

---

## ⚠️ Disclaimer

> [!CAUTION]
> This project is provided "as-is" without warranty. I am not responsible for any issues, data loss, or "explosions" (code-related or otherwise) that may occur. **Use at your own risk.**
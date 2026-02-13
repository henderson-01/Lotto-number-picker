# EuroMillions Number Picker

A Python desktop application that generates random numbers for the EuroMillions lottery using a modern, dark-themed Graphical User Interface (GUI).

## Description

This tool helps users pick lottery numbers by generating a random set of "Main Numbers" and "Lucky Stars" based on configurable rules. It ensures all generated numbers are unique within their sets and displays them in an easy-to-read, sorted format.

## Features

- **GUI Interface**: Built with `tkinter`, featuring a custom dark theme with gold and blue accents.
- **Random Generation**: Generates 5 unique main numbers and 2 unique lucky stars per click.
- **Sorted Results**: Numbers are automatically sorted for convenience.
- **Responsive Design**: The window centers automatically on your screen upon launch.

## Prerequisites

- **Python 3.x**
- **Tkinter**: This is included with most standard Python installations.
  - *Linux users*: You might need to install it explicitly (e.g., `sudo apt-get install python3-tk`).

## Installation & Usage

1.  **Download** the `lotto_picker.py` file to your local machine.
2.  **Open a terminal** or command prompt.
3.  **Navigate** to the directory containing the file.
4.  **Run** the application:

    ```bash
    python lotto_picker.py
    ```

5.  Click the **"Generate Numbers"** button to get a new set of lottery numbers.

## Configuration

The application is designed to be easily configurable. You can modify the constants at the top of `lotto_picker.py` to adjust the rules or styling:

- `EUROMILLIONS_CONFIG`: Change the count, minimum, and maximum values for numbers.
- `STYLE_CONFIG`: Customize colors, fonts, and window dimensions.

## Project Structure

- `lotto_picker.py`: The main application script containing logic and UI code. 
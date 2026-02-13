import random
import tkinter as tk

# --- Configuration ---

# EuroMillions Rules
EUROMILLIONS_CONFIG = {
    "main_numbers": {"count": 5, "min": 1, "max": 50},
    "lucky_stars": {"count": 2, "min": 1, "max": 13},
}

# UI Styling
STYLE_CONFIG = {
    "window_bg": "#2e2e2e",
    "frame_bg": "#3e3e3e",
    "text_color": "white",
    "button_bg": "#4a4a4a",
    "button_active_bg": "#5a5a5a",
    "numbers_color": "#003366",  # Dark blue
    "stars_color": "#FFD700",    # Gold
    "stars_text_color": "black",
    "title_font": ("Helvetica", 20, "bold"),
    "label_font": ("Helvetica", 14, "bold"),
    "number_font": ("Helvetica", 16, "bold"),
    "button_font": ("Helvetica", 12, "bold"),
}


class LottoApp:
    """
    A tkinter application for picking lottery numbers.
    """

    def __init__(self, window, lottery_config, style_config):
        """
        Initializes the lottery number picker application.
        """
        self.window = window
        self.lottery_config = lottery_config
        self.style = style_config

        self.number_labels = []
        self.star_labels = []

        self._setup_window()
        self._create_widgets()

    def _setup_window(self):
        """Configures the main application window."""
        self.window.title("EuroMillions Number Picker")
        self.window.geometry("480x480")
        self.window.configure(bg=self.style["window_bg"])
        self.window.resizable(False, False)

        # Center the window on the screen
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def _create_widgets(self):
        """Creates and places all the UI widgets in the window."""
        title_label = tk.Label(
            self.window,
            text="EuroMillions Number Picker",
            bg=self.style["window_bg"],
            fg=self.style["text_color"],
            font=self.style["title_font"]
        )
        title_label.pack(pady=(20, 10))

        results_frame = tk.Frame(
            self.window,
            bg=self.style["frame_bg"],
            relief="sunken",
            borderwidth=2
        )
        results_frame.pack(pady=20, padx=20, fill="x")

        # Display for the main numbers
        self.number_labels = self._create_number_display(
            results_frame, "Your Numbers",
            self.lottery_config["main_numbers"]["count"],
            self.style["numbers_color"]
        )

        # Display for the lucky stars
        self.star_labels = self._create_number_display(
            results_frame, "Lucky Stars",
            self.lottery_config["lucky_stars"]["count"],
            self.style["stars_color"],
            text_color=self.style["stars_text_color"]
        )

        # Action Button
        pick_button = tk.Button(
            self.window,
            text="Generate Numbers",
            command=self.generate_and_display_numbers,
            bg=self.style["button_bg"],
            fg=self.style["text_color"],
            font=self.style["button_font"],
            relief='raised',
            borderwidth=2,
            activebackground=self.style["button_active_bg"],
            activeforeground=self.style["text_color"]
        )
        pick_button.pack(padx=20, pady=20, ipady=15, fill="x")

    def _create_number_display(self, parent, label_text, count, color, text_color=None):
        """Creates a framed display for a set of numbers."""
        if text_color is None:
            text_color = self.style["text_color"]

        frame = tk.Frame(parent, bg=self.style["frame_bg"])
        frame.pack(pady=10)

        label = tk.Label(
            frame,
            text=label_text,
            bg=self.style["frame_bg"],
            fg=self.style["text_color"],
            font=self.style["label_font"]
        )
        label.pack(pady=5)

        number_frame = tk.Frame(frame, bg=self.style["frame_bg"])
        number_frame.pack()

        labels = []
        for _ in range(count):
            num_label = tk.Label(
                number_frame,
                text="",
                bg=color,
                fg=text_color,
                font=self.style["number_font"],
                width=3, height=1, relief="solid", borderwidth=2
            )
            num_label.pack(side="left", padx=5, pady=5)
            labels.append(num_label)
        return labels

    def _pick_numbers(self, count, min_val, max_val):
        """Picks a sorted list of unique numbers within a given range."""
        return sorted(random.sample(range(min_val, max_val + 1), count))

    def generate_and_display_numbers(self):
        """Generates and displays the new lottery numbers."""
        # Generate main numbers
        main_cfg = self.lottery_config["main_numbers"]
        numbers = self._pick_numbers(
            main_cfg["count"], main_cfg["min"], main_cfg["max"])

        # Generate lucky stars
        star_cfg = self.lottery_config["lucky_stars"]
        stars = self._pick_numbers(
            star_cfg["count"], star_cfg["min"], star_cfg["max"])

        # Update labels
        for label, num in zip(self.number_labels, numbers):
            label.config(text=str(num))

        for label, star in zip(self.star_labels, stars):
            label.config(text=str(star))

    def run(self):
        """Starts the tkinter main loop."""
        self.window.mainloop()


def main():
    """Sets up and runs the lottery application."""
    root = tk.Tk()
    app = LottoApp(root, EUROMILLIONS_CONFIG, STYLE_CONFIG)
    app.run()


if __name__ == "__main__":
    main()

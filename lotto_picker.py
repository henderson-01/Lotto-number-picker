import random
import customtkinter as ctk

# --- Configuration ---

# EuroMillions Rules
EUROMILLIONS_CONFIG = {
    "main_numbers": {"count": 5, "min": 1, "max": 50},
    "lucky_stars": {"count": 2, "min": 1, "max": 12},
}

# UI Styling Constants
STYLE_CONFIG = {
    "numbers_color": "#1f538d",  # Custom blue for main numbers
    "stars_color": "#cc9900",  # Gold for lucky stars
    "title_font": ("Helvetica", 24, "bold"),
    "label_font": ("Helvetica", 14, "bold"),
    "number_font": ("Helvetica", 18, "bold"),
}


class LottoApp:
    """
    A CustomTkinter application for picking EuroMillions numbers.
    """

    def __init__(self, window, lottery_config, style_config):
        self.window = window
        self.lottery_config = lottery_config
        self.style = style_config

        self.number_labels = []
        self.star_labels = []

        self._setup_window()
        self._create_widgets()

    def _setup_window(self):
        """Configures the main application window."""
        self.window.title("EuroMillions Picker")
        self.window.geometry("480x520")
        self.window.resizable(False, False)

        # CTk specific theme settings
        # Modes: "System" (standard), "Dark", "Light"
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

    def _create_widgets(self):
        """Creates and places all the UI widgets using CTk components."""

        # Title
        title_label = ctk.CTkLabel(
            self.window,
            text="EuroMillions Number Picker",
            font=self.style["title_font"],
        )
        title_label.pack(pady=(30, 10))

        # Main Results Container
        results_frame = ctk.CTkFrame(self.window)
        results_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Display for the main numbers
        self.number_labels = self._create_number_display(
            results_frame,
            "Your Numbers",
            self.lottery_config["main_numbers"]["count"],
            self.style["numbers_color"],
        )

        # Display for the lucky stars
        self.star_labels = self._create_number_display(
            results_frame,
            "Lucky Stars",
            self.lottery_config["lucky_stars"]["count"],
            self.style["stars_color"],
        )

        # Action Button
        pick_button = ctk.CTkButton(
            self.window,
            text="Generate Numbers",
            command=self.generate_and_display_numbers,
            font=self.style["label_font"],
            height=50,
        )
        pick_button.pack(padx=20, pady=(10, 30), fill="x")

    def _create_number_display(self, parent, label_text, count, color):
        """Creates a framed display for a set of numbers using CTkLabel."""

        # Section Label
        section_label = ctk.CTkLabel(
            parent, text=label_text, font=self.style["label_font"]
        )
        section_label.pack(pady=(15, 5))

        # Container for the circles/boxes
        number_container = ctk.CTkFrame(parent, fg_color="transparent")
        number_container.pack(pady=5)

        labels = []
        for _ in range(count):
            num_label = ctk.CTkLabel(
                number_container,
                text="-",
                width=50,
                height=50,
                fg_color=color,
                text_color="white",
                corner_radius=8,
                font=self.style["number_font"],
            )
            num_label.pack(side="left", padx=5)
            labels.append(num_label)
        return labels

    def _pick_numbers(self, count, min_val, max_val):
        """Picks a sorted list of unique numbers."""
        return sorted(random.sample(range(min_val, max_val + 1), count))

    def generate_and_display_numbers(self):
        """Generates numbers and updates the CTk labels."""
        main_cfg = self.lottery_config["main_numbers"]
        numbers = self._pick_numbers(
            main_cfg["count"], main_cfg["min"], main_cfg["max"]
        )

        star_cfg = self.lottery_config["lucky_stars"]
        stars = self._pick_numbers(star_cfg["count"], star_cfg["min"], star_cfg["max"])

        # Update Main Numbers
        for label, num in zip(self.number_labels, numbers):
            label.configure(text=str(num))

        # Update Stars
        for label, star in zip(self.star_labels, stars):
            label.configure(text=str(star))


def main():
    root = ctk.CTk()
    LottoApp(root, EUROMILLIONS_CONFIG, STYLE_CONFIG)
    root.mainloop()


if __name__ == "__main__":
    main()

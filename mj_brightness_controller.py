import tkinter as tk
from tkinter import messagebox
import os
import subprocess


class BrightnessControllerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MJ Brightness Controller")
        self.root.geometry("300x150")
        self.root.resizable(False, False)

        # App Header
        header = tk.Label(root, text="MJ Brightness Controller", font=("Arial", 14, "bold"))
        header.pack(pady=10)

        # Brightness Scale
        self.scale = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Brightness (%)")
        self.scale.set(self.get_brightness())
        self.scale.pack(pady=10)

        # Apply Button
        apply_button = tk.Button(root, text="Apply", command=self.set_brightness)
        apply_button.pack(pady=5)

        # About Button
        about_button = tk.Button(root, text="About", command=self.show_about)
        about_button.pack(pady=5)

    def get_brightness(self):
        """Fetch current brightness using ddcutil."""
        try:
            result = subprocess.check_output(["ddcutil", "getvcp", "10"], stderr=subprocess.DEVNULL)
            brightness = int(result.decode().split("current value = ")[1].split(",")[0].strip())
            return brightness
        except Exception:
            return 50  # Default value if ddcutil is not working

    def set_brightness(self):
        """Set brightness using ddcutil."""
        brightness = self.scale.get()
        try:
            os.system(f"ddcutil setvcp 10 {brightness}")
            messagebox.showinfo("Success", f"Brightness set to {brightness}%.")
        except Exception:
            messagebox.showerror("Error", "Failed to set brightness. Ensure DDC/CI is enabled on your monitor.")

    def show_about(self):
        """Show about dialog."""
        messagebox.showinfo(
            "About MJ Brightness Controller",
            "MJ Brightness Controller v1.0\n"
            "Developed by [Your Name]\n"
            "For controlling external monitor brightness on Linux."
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = BrightnessControllerApp(root)
    root.mainloop()

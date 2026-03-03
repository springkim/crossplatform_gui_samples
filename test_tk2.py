
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle



class App:
    def __init__(self, root):
        self.root = root
        style = ThemedStyle(root)
        #style.set_theme("equilux")  # dark theme
        #style.set_theme("arc")
        #style.set_theme("plastik")
        style.set_theme("clearlooks")

        self.root.title("Tkinter Widget Example")
        self.root.geometry("400x500")

        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill="both", expand=True)

        # ----- Button -----
        ttk.Label(main_frame, text="버튼:").grid(row=0, column=0, sticky="w", pady=5)
        self.button = ttk.Button(main_frame, text="Click Button", command=self.on_button_clicked)
        self.button.grid(row=0, column=1, sticky="ew", pady=5)

        # ----- Checkbox -----
        ttk.Label(main_frame, text="Checkbox:").grid(row=1, column=0, sticky="w", pady=5)
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(
            main_frame,
            text="Check me",
            variable=self.checkbox_var,
            command=self.on_checkbox_changed
        )
        self.checkbox.grid(row=1, column=1, sticky="w", pady=5)

        # ----- Dropdown -----
        ttk.Label(main_frame, text="Dropdown:").grid(row=2, column=0, sticky="w", pady=5)
        self.selected_option = tk.StringVar(value="Option 1")
        self.dropdown = ttk.OptionMenu(
            main_frame,
            self.selected_option,
            "Option 1",
            "Option 1",
            "Option 2",
            "Option 3",
            command=self.on_dropdown_changed
        )
        self.dropdown.grid(row=2, column=1, sticky="ew", pady=5)

        # ----- Text Edit -----
        ttk.Label(main_frame, text="TextEdit:").grid(row=3, column=0, sticky="nw", pady=5)
        self.text_edit = tk.Text(main_frame, height=5)
        self.text_edit.grid(row=3, column=1, sticky="ew", pady=5)

        # ----- Slider -----
        ttk.Label(main_frame, text="Slider:").grid(row=4, column=0, sticky="w", pady=5)
        self.slider = ttk.Scale(
            main_frame,
            from_=0,
            to=100,
            orient="horizontal",
            command=self.on_slider_changed
        )
        self.slider.set(50)
        self.slider.grid(row=4, column=1, sticky="ew", pady=5)

        # ----- Listbox -----
        ttk.Label(main_frame, text="ListView:").grid(row=5, column=0, sticky="nw", pady=5)
        self.listbox = tk.Listbox(main_frame, height=5)
        self.listbox.insert("end", "Item A")
        self.listbox.insert("end", "Item B")
        self.listbox.insert("end", "Item C")
        self.listbox.grid(row=5, column=1, sticky="ew", pady=5)

        # ----- Status Label -----
        self.status_label = ttk.Label(main_frame, text="Status display area")
        self.status_label.grid(row=6, column=0, columnspan=2, pady=15)

        main_frame.columnconfigure(1, weight=1)

    # Event handlers
    def on_button_clicked(self):
        self.status_label.config(text="Button was clicked.")

    def on_checkbox_changed(self):
        state = "Checked" if self.checkbox_var.get() else "Unchecked"
        self.status_label.config(text=f"Checkbox state: {state}")

    def on_dropdown_changed(self, value):
        self.status_label.config(text=f"Selected option: {value}")

    def on_slider_changed(self, value):
        self.status_label.config(text=f"Slider value: {int(float(value))}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
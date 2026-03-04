import customtkinter as ctk

# Appearance settings
ctk.set_appearance_mode("System")  # "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter Widget Example")
        self.geometry("480x640")

        # Main frame
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # ----- Button -----
        ctk.CTkLabel(main_frame, text="Button:").grid(row=0, column=0, sticky="w", pady=8)

        self.button = ctk.CTkButton(
            main_frame,
            text="Click Button",
            command=self.on_button_clicked
        )
        self.button.grid(row=0, column=1, sticky="ew", pady=8)

        # ----- Checkbox -----
        ctk.CTkLabel(main_frame, text="Checkbox:").grid(row=1, column=0, sticky="w", pady=8)

        self.checkbox_var = ctk.BooleanVar()
        self.checkbox = ctk.CTkCheckBox(
            main_frame,
            text="Check me",
            variable=self.checkbox_var,
            command=self.on_checkbox_changed
        )
        self.checkbox.grid(row=1, column=1, sticky="w", pady=8)

        # ----- Dropdown -----
        ctk.CTkLabel(main_frame, text="Dropdown:").grid(row=2, column=0, sticky="w", pady=8)

        self.dropdown = ctk.CTkOptionMenu(
            main_frame,
            values=["Option 1", "Option 2", "Option 3"],
            command=self.on_dropdown_changed
        )
        self.dropdown.set("Option 1")
        self.dropdown.grid(row=2, column=1, sticky="ew", pady=8)

        # ----- Text Edit -----
        ctk.CTkLabel(main_frame, text="TextEdit:").grid(row=3, column=0, sticky="nw", pady=8)

        self.text_edit = ctk.CTkTextbox(main_frame, height=100)
        self.text_edit.grid(row=3, column=1, sticky="ew", pady=8)
        self.text_edit.insert(ctk.END, "English\n한국어\n日本語")
        # ----- Slider -----
        ctk.CTkLabel(main_frame, text="Slider:").grid(row=4, column=0, sticky="w", pady=8)

        self.slider = ctk.CTkSlider(
            main_frame,
            from_=0,
            to=100,
            command=self.on_slider_changed
        )
        self.slider.set(50)
        self.slider.grid(row=4, column=1, sticky="ew", pady=8)

        # ----- ListView (Scrollable Frame) -----
        ctk.CTkLabel(main_frame, text="ListView:").grid(row=5, column=0, sticky="nw", pady=8)

        self.list_frame = ctk.CTkScrollableFrame(main_frame, height=120)
        self.list_frame.grid(row=5, column=1, sticky="ew", pady=8)

        for item in ["Item A", "Item B", "Item C"]:
            btn = ctk.CTkButton(
                self.list_frame,
                text=item,
                height=30,
                command=lambda i=item: self.on_list_item_clicked(i)
            )
            btn.pack(fill="x", pady=2)

        # ----- Status Label -----
        self.status_label = ctk.CTkLabel(
            main_frame,
            text="Status display area"
        )
        self.status_label.grid(row=6, column=0, columnspan=2, pady=20)

        main_frame.columnconfigure(1, weight=1)

    # Event handlers
    def on_button_clicked(self):
        self.status_label.configure(text="Button was clicked.")

    def on_checkbox_changed(self):
        state = "Checked" if self.checkbox_var.get() else "Unchecked"
        self.status_label.configure(text=f"Checkbox state: {state}")

    def on_dropdown_changed(self, value):
        self.status_label.configure(text=f"Selected option: {value}")

    def on_slider_changed(self, value):
        self.status_label.configure(text=f"Slider value: {int(value)}")

    def on_list_item_clicked(self, item):
        self.status_label.configure(text=f"Selected list item: {item}")


if __name__ == "__main__":
    app = App()
    app.mainloop()

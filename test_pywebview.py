import webview


class Api:
    def __init__(self):
        self.checkbox_state = False
        self.selected_option = "Option 1"
        self.slider_value = 50

    def on_button_clicked(self):
        return "Button was clicked."

    def on_checkbox_changed(self, checked):
        self.checkbox_state = checked
        state = "Checked" if checked else "Unchecked"
        return f"Checkbox state: {state}"

    def on_dropdown_changed(self, value):
        self.selected_option = value
        return f"Selected option: {value}"

    def on_slider_changed(self, value):
        self.slider_value = int(float(value))
        return f"Slider value: {self.slider_value}"

    def get_text_content(self, text):
        return f"Text content: {text}"


if __name__ == "__main__":
    api = Api()
    window = webview.create_window(
        "Pywebview Widget Example",
        "index.html",
        width=480,
        height=640,
        js_api=api
    )
    webview.start()

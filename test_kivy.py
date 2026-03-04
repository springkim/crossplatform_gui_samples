from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '640')
import platform
from kivy.core.text import LabelBase

if platform.system() == 'Windows':
    LabelBase.register('Roboto', 'C:/Windows/Fonts/malgun.ttf')
elif platform.system() == 'Darwin':
    LabelBase.register('Roboto', '/System/Library/Fonts/AppleSDGothicNeo.ttc')
else:
    LabelBase.register('Roboto', '/usr/share/fonts/truetype/noto/NotoSansKR-Regular.ttf')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.metrics import dp


class SimpleListView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [
            {"text": "Item A"},
            {"text": "Item B"},
            {"text": "Item C"},
        ]
        self.viewclass = "Label"

        self.layout_manager = RecycleBoxLayout(
            default_size=(None, dp(30)),
            default_size_hint=(1, None),
            size_hint=(1, None),
            orientation="vertical",
        )
        self.layout_manager.bind(
            minimum_height=self.layout_manager.setter("height")
        )
        self.add_widget(self.layout_manager)


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(

            orientation="vertical", spacing=10, padding=20, **kwargs
        )

        self.status_label = Label(
            text="Status display area",
            size_hint_y=None,
            height=40,
        )

        # 1. Button
        button_layout = BoxLayout(size_hint_y=None, height=40)
        button_layout.add_widget(Label(text="Button:", size_hint_x=0.3))
        button = Button(text="Click button")
        button.bind(on_press=self.on_button_clicked)
        button_layout.add_widget(button)
        self.add_widget(button_layout)

        # 2. Checkbox
        checkbox_layout = BoxLayout(size_hint_y=None, height=40)
        checkbox_layout.add_widget(Label(text="Checkbox:", size_hint_x=0.3))
        self.checkbox = CheckBox()
        self.checkbox.bind(active=self.on_checkbox_changed)
        checkbox_layout.add_widget(self.checkbox)
        self.add_widget(checkbox_layout)

        # 3. Dropdown (Spinner)
        dropdown_layout = BoxLayout(size_hint_y=None, height=40)
        dropdown_layout.add_widget(Label(text="Dropdown:", size_hint_x=0.3))
        self.spinner = Spinner(
            text="Select option",
            values=("Option 1", "Option 2", "Option 3"),
        )
        self.spinner.bind(text=self.on_dropdown_changed)
        dropdown_layout.add_widget(self.spinner)
        self.add_widget(dropdown_layout)

        # 4. Text Edit
        text_layout = BoxLayout(size_hint_y=None, height=120)
        text_layout.add_widget(Label(text="TextEdit:", size_hint_x=0.3))
        self.text_input = TextInput(multiline=True)
        self.text_input.text = "English\n한국어\n日本語"
        text_layout.add_widget(self.text_input)
        self.add_widget(text_layout)

        # 5. Slider
        slider_layout = BoxLayout(size_hint_y=None, height=40)
        slider_layout.add_widget(Label(text="Slider:", size_hint_x=0.3))
        self.slider = Slider(min=0, max=100, value=50)
        self.slider.bind(value=self.on_slider_changed)
        slider_layout.add_widget(self.slider)
        self.add_widget(slider_layout)

        # 6. ListView (RecycleView)
        list_layout = BoxLayout(size_hint_y=None, height=120)
        list_layout.add_widget(Label(text="ListView:", size_hint_x=0.3))
        self.list_view = SimpleListView()
        list_layout.add_widget(self.list_view)
        self.add_widget(list_layout)

        self.add_widget(self.status_label)

    # Event handlers
    def on_button_clicked(self, instance):
        self.status_label.text = "Button was clicked."

    def on_checkbox_changed(self, instance, value):
        checked = "Checked" if value else "Unchecked"
        self.status_label.text = f"Checkbox state: {checked}"

    def on_dropdown_changed(self, spinner, text):
        self.status_label.text = f"Selected option: {text}"

    def on_slider_changed(self, instance, value):
        self.status_label.text = f"Slider value: {int(value)}"


class TestApp(App):
    title = "Kivy Widget Example"

    def build(self):
        return MainLayout()


if __name__ == "__main__":
    TestApp().run()

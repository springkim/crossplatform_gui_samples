from nicegui import ui


# Button
def on_button_clicked():
    status.set_text("Button was clicked.")


# Checkbox
def on_checkbox_changed(e):
    state = "Checked" if e.value else "Unchecked"
    status.set_text(f"Checkbox state: {state}")


# Dropdown
def on_dropdown_changed(e):
    status.set_text(f"Selected option: {e.value}")


# Slider
def on_slider_changed(e):
    status.set_text(f"Slider value: {int(e.value)}")


with ui.column().classes('w-96 mx-auto p-5 gap-4'):
    with ui.row().classes('w-full items-center'):
        ui.label('버튼:').classes('w-24')
        ui.button('Click Button', on_click=on_button_clicked).classes('flex-1')

    with ui.row().classes('w-full items-center'):
        ui.label('Checkbox:').classes('w-24')
        ui.checkbox('Check me', on_change=on_checkbox_changed)

    with ui.row().classes('w-full items-center'):
        ui.label('Dropdown:').classes('w-24')
        ui.select(['Option 1', 'Option 2', 'Option 3'], value='Option 1',
                  on_change=on_dropdown_changed).classes('flex-1')

    with ui.row().classes('w-full items-center'):
        ui.label('Slider:').classes('w-24')
        ui.slider(min=0, max=100, value=50, on_change=on_slider_changed).classes('flex-1')

    with ui.row().classes('w-full items-center'):
        ui.label('TextEdit:').classes('w-24')
        ui.textarea(value="English\n한국어\n日本語").classes('flex-1')


    status = ui.label('Status display area').classes('w-full text-center text-gray-500 mt-4')

ui.run(native=True, window_size=(480, 640), title='NiceGUI Widget Example')

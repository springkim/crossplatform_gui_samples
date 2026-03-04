import flet as ft


def main(page: ft.Page):
    page.title = "Flet 위젯 예제"
    page.window.width = 480
    page.window.height = 640

    status_label = ft.Text("상태 표시 영역")

    # 1. 버튼
    def on_button_click(e):
        status_label.value = "버튼이 클릭되었습니다."

    button = ft.Button(
        content=ft.Text("버튼 클릭"),
        on_click=on_button_click
    )

    # 2. 체크박스
    def on_checkbox_change(e):
        checked = "체크됨" if e.control.value else "해제됨"
        status_label.value = f"체크박스 상태: {checked}"

    checkbox = ft.Checkbox(
        label="체크하세요",
        on_change=on_checkbox_change
    )

    # 3. 드롭다운 (⚠ 변경됨)
    def on_dropdown_select(e):
        status_label.value = f"선택된 옵션: {e.data}"

    dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("옵션 1"),
            ft.dropdown.Option("옵션 2"),
            ft.dropdown.Option("옵션 3"),
        ],
        on_select=on_dropdown_select,

    )

    # 4. 텍스트 에디트
    text_edit = ft.TextField(
        hint_text="여기에 텍스트 입력...",
        multiline=True,
        min_lines=3,
        max_lines=5,
    )
    text_edit.value = "English\n한국어\n日本語"

    # 5. 슬라이더
    def on_slider_change(e):
        status_label.value = f"슬라이더 값: {int(e.control.value)}"

    slider = ft.Slider(
        min=0,
        max=100,
        value=50,
        divisions=100,
        on_change=on_slider_change,
    )

    # 6. 리스트뷰
    list_view = ft.ListView(
        controls=[
            ft.Text("항목 A"),
            ft.Text("항목 B"),
            ft.Text("항목 C"),
        ],
        height=100,
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row([ft.Text("버튼:"), button]),
                ft.Row([ft.Text("체크박스:"), checkbox]),
                ft.Row([ft.Text("드롭다운:"), dropdown]),
                ft.Row([ft.Text("텍스트Edit:"), text_edit]),
                ft.Row([ft.Text("슬라이더:"), slider]),
                ft.Row([ft.Text("리스트뷰:"), list_view]),
                status_label,
            ],
            spacing=15,
        )
    )


if __name__ == "__main__":
    ft.run(main)

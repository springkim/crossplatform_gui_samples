import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="wxPython 위젯 예제", size=(400, 500))

        panel = wx.Panel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        form_sizer = wx.FlexGridSizer(rows=6, cols=2, hgap=10, vgap=10)
        form_sizer.AddGrowableCol(1, 1)  # 오른쪽 컬럼 확장

        # 1. 버튼
        form_sizer.Add(wx.StaticText(panel, label="버튼:"), 0, wx.ALIGN_CENTER_VERTICAL)
        self.button = wx.Button(panel, label="버튼 클릭")
        self.button.Bind(wx.EVT_BUTTON, self.on_button_clicked)
        form_sizer.Add(self.button, 1, wx.EXPAND)

        # 2. 체크박스
        form_sizer.Add(wx.StaticText(panel, label="체크박스:"), 0, wx.ALIGN_CENTER_VERTICAL)
        self.checkbox = wx.CheckBox(panel, label="체크하세요")
        self.checkbox.Bind(wx.EVT_CHECKBOX, self.on_checkbox_changed)
        form_sizer.Add(self.checkbox, 1, wx.EXPAND)

        # 3. 드롭다운
        form_sizer.Add(wx.StaticText(panel, label="드롭다운:"), 0, wx.ALIGN_CENTER_VERTICAL)
        self.combobox = wx.ComboBox(
            panel,
            choices=["옵션 1", "옵션 2", "옵션 3"],
            style=wx.CB_READONLY
        )
        self.combobox.Bind(wx.EVT_COMBOBOX, self.on_combobox_changed)
        form_sizer.Add(self.combobox, 1, wx.EXPAND)

        # 4. 텍스트 에디트 (멀티라인)
        form_sizer.Add(wx.StaticText(panel, label="텍스트Edit:"), 0, wx.ALIGN_CENTER_VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        form_sizer.Add(self.text_ctrl, 1, wx.EXPAND)

        # 5. 슬라이더
        form_sizer.Add(wx.StaticText(panel, label="슬라이더:"), 0, wx.ALIGN_CENTER_VERTICAL)
        self.slider = wx.Slider(panel, minValue=0, maxValue=100, value=50)
        self.slider.Bind(wx.EVT_SLIDER, self.on_slider_changed)
        form_sizer.Add(self.slider, 1, wx.EXPAND)

        # 6. 리스트뷰 (ListBox 사용)
        form_sizer.Add(wx.StaticText(panel, label="리스트뷰:"), 0, wx.ALIGN_TOP)
        self.listbox = wx.ListBox(panel, choices=["항목 A", "항목 B", "항목 C"])
        form_sizer.Add(self.listbox, 1, wx.EXPAND)

        # 상태 출력 라벨
        self.status_label = wx.StaticText(panel, label="상태 표시 영역")

        main_sizer.Add(form_sizer, 1, wx.ALL | wx.EXPAND, 20)
        main_sizer.Add(self.status_label, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)

        panel.SetSizer(main_sizer)
        self.Centre()
        self.Show()

    # 이벤트 핸들러
    def on_button_clicked(self, event):
        self.status_label.SetLabel("버튼이 클릭되었습니다.")

    def on_checkbox_changed(self, event):
        checked = "체크됨" if self.checkbox.GetValue() else "해제됨"
        self.status_label.SetLabel(f"체크박스 상태: {checked}")

    def on_combobox_changed(self, event):
        value = self.combobox.GetValue()
        self.status_label.SetLabel(f"선택된 옵션: {value}")

    def on_slider_changed(self, event):
        value = self.slider.GetValue()
        self.status_label.SetLabel(f"슬라이더 값: {value}")


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
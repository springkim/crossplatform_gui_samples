import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QCheckBox, QComboBox,
    QTextEdit, QSlider, QListView, QVBoxLayout, QFormLayout, QLabel
)
from PySide6.QtCore import Qt, QStringListModel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 위젯 예제")
        self.resize(480, 640)

        # 전체 레이아웃
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()

        # 1. 버튼
        self.button = QPushButton("버튼 클릭")
        self.button.clicked.connect(self.on_button_clicked)
        form_layout.addRow("버튼:", self.button)

        # 2. 체크박스
        self.checkbox = QCheckBox("체크하세요")
        self.checkbox.stateChanged.connect(self.on_checkbox_changed)
        form_layout.addRow("체크박스:", self.checkbox)

        # 3. 드롭다운 (콤보박스)
        self.combobox = QComboBox()
        self.combobox.addItems(["옵션 1", "옵션 2", "옵션 3"])
        self.combobox.currentIndexChanged.connect(self.on_combobox_changed)
        form_layout.addRow("드롭다운:", self.combobox)

        # 4. 텍스트 에디트
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("여기에 텍스트 입력...")
        self.text_edit.setPlainText("English\n한국어\n日本語")
        form_layout.addRow("텍스트Edit:", self.text_edit)

        # 5. 슬라이더
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.on_slider_changed)
        form_layout.addRow("슬라이더:", self.slider)

        # 6. 리스트뷰
        self.list_view = QListView()
        self.list_model = QStringListModel()
        self.list_model.setStringList(["항목 A", "항목 B", "항목 C"])
        self.list_view.setModel(self.list_model)
        form_layout.addRow("리스트뷰:", self.list_view)

        # 상태 출력 라벨
        self.status_label = QLabel("상태 표시 영역")
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.status_label)

        self.setLayout(main_layout)

    # 슬롯 정의
    def on_button_clicked(self):
        self.status_label.setText("버튼이 클릭되었습니다.")

    def on_checkbox_changed(self, state):
        checked = "체크됨" if state == Qt.Checked else "해제됨"
        self.status_label.setText(f"체크박스 상태: {checked}")

    def on_combobox_changed(self, index):
        value = self.combobox.itemText(index)
        self.status_label.setText(f"선택된 옵션: {value}")

    def on_slider_changed(self, value):
        self.status_label.setText(f"슬라이더 값: {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

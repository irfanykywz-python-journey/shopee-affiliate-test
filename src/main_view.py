from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QHBoxLayout, QSplitter, QLabel, QComboBox

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        splitter = QSplitter()
        splitter.addWidget(self.left_widget())
        splitter.addWidget(self.righ_widget())
        splitter.setSizes([150, 300])

        layout.addWidget(splitter)

    def left_widget(self):
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)

        self.cookies_label = QLabel('Cookies')
        layout.addWidget(self.cookies_label)

        self.cookies_input = QTextEdit()
        layout.addWidget(self.cookies_input)

        self.script_label = QLabel('Script')
        self.script_input = QComboBox()
        self.script_input.setPlaceholderText('Select Script')
        layout.addWidget(self.script_input)

        self.open_button = QPushButton("Open")
        self.open_button.setCheckable(True)
        layout.addWidget(self.open_button)

        return widget

    def righ_widget(self):
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)

        self.log_input = QTextEdit()
        self.log_input.setReadOnly(True)
        layout.addWidget(self.log_input)

        return widget
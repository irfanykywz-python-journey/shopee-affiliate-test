import os
from pathlib import Path

from src.main_thread import MainThread
from src.main_view import MainView
from src.utils import get_setting, get_script


class MainViewModel(MainView):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shopee Affiliate Test")
        self.resize(800, 600)

        self.setting = get_setting()

        self.init_ui()

    def init_ui(self):
        self.setup_ui()

        # signal
        self.open_button.clicked.connect(self.open)

        # fill script from file on dir
        self.script_input.addItems(get_script())

        # fill
        self.cookies_input.setText(self.setting.value("cookies"))
        self.script_input.setCurrentText(self.setting.value("script_selected"))


    def open(self):
        def process(val):
            self.log_input.append(val)

        script = self.script_input.currentText()
        self.setting.setValue("script_selected", script)

        cookies = self.cookies_input.toPlainText()
        self.setting.setValue("cookies", cookies)

        if self.open_button.isChecked():
            self.thread = MainThread(self, {
                'script': os.path.join('scripts', script),
                'cookies': cookies
            })
            self.thread.process.connect(process)
            self.thread.start()
        else:
            self.thread.terminate()
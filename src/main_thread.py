from PySide6.QtCore import QThread, Signal

from src.utils import get_class

class MainThread(QThread):

    process = Signal(tuple)

    def __init__(self, parent, payload):
        super().__init__(parent)
        self.payload = payload

    def run(self):
        Classes = get_class(self.payload['script'])
        self.script = Classes(parent=self)
        self.script.run()

    def terminate(self):
        self.script.stop()

import sys
from PySide6.QtWidgets import QApplication

from src.main_viewmodels import MainViewModel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainViewModel()
    window.show()
    sys.exit(app.exec())

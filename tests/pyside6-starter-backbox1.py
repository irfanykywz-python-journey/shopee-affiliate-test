import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QFrame, QSizePolicy, QSpacerItem
)
from PySide6.QtGui import QFont, QPalette, QColor, Qt

class Header(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("header")
        layout = QHBoxLayout()
        layout.setContentsMargins(32, 16, 32, 16)
        layout.setSpacing(20)

        self.logo = QLabel("MyLibrary")
        font = QFont("Segoe UI", 20, QFont.Bold)
        self.logo.setFont(font)
        self.logo.setStyleSheet("color: black;")
        layout.addWidget(self.logo, alignment=Qt.AlignLeft)

        layout.addStretch()

        # Navigation buttons/items
        self.nav_btns = []
        for name in ["Docs", "Components", "Showcase", "GitHub"]:
            btn = QPushButton(name)
            btn.setObjectName("navButton")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFlat(True)
            self.nav_btns.append(btn)
            layout.addWidget(btn, alignment=Qt.AlignRight)

        self.setLayout(layout)

class HeroSection(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(32, 64, 32, 64)
        layout.setSpacing(24)

        self.headline = QLabel("Build your Component Library")
        font = QFont("Segoe UI", 48, QFont.DemiBold)
        self.headline.setFont(font)
        self.headline.setStyleSheet("color: black;")
        self.headline.setWordWrap(True)
        layout.addWidget(self.headline)

        self.subtext = QLabel("A clean, modern UI library with elegant components for your next project.")
        font_sub = QFont("Segoe UI", 18)
        self.subtext.setFont(font_sub)
        self.subtext.setStyleSheet("color: #6b7280;")
        self.subtext.setWordWrap(True)
        layout.addWidget(self.subtext)

        self.cta_button = QPushButton("Get Started")
        self.cta_button.setObjectName("ctaButton")
        self.cta_button.setCursor(Qt.PointingHandCursor)
        self.cta_button.setFixedSize(160, 48)
        layout.addWidget(self.cta_button, alignment=Qt.AlignLeft)

        self.setLayout(layout)

class FeatureCard(QFrame):
    def __init__(self, title, description):
        super().__init__()
        self.title = title
        self.description = description
        self.init_ui()

    def init_ui(self):
        self.setObjectName("featureCard")
        self.setMinimumWidth(260)
        self.setMaximumWidth(320)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title_lbl = QLabel(self.title)
        font_title = QFont("Segoe UI", 20, QFont.Bold)
        title_lbl.setFont(font_title)
        title_lbl.setStyleSheet("color: black;")
        layout.addWidget(title_lbl)

        desc_lbl = QLabel(self.description)
        font_desc = QFont("Segoe UI", 14)
        desc_lbl.setFont(font_desc)
        desc_lbl.setStyleSheet("color: #6b7280;")
        desc_lbl.setWordWrap(True)
        layout.addWidget(desc_lbl)

        self.setLayout(layout)

class FeaturesSection(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(32)

        features = [
            ("Modern Typography", "Use elegant, bold fonts with perfect hierarchy to create clarity."),
            ("Clean Layout", "Generous whitespace with flexible grids for responsive design."),
            ("Interactive Elements", "Smooth transitions, hover states and modern controls.")
        ]

        for title, desc in features:
            card = FeatureCard(title, desc)
            layout.addWidget(card)

        self.setLayout(layout)

class Container(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        self.header = Header()
        self.hero = HeroSection()
        self.features = FeaturesSection()

        main_layout.addWidget(self.header)
        main_layout.addWidget(self.hero)
        main_layout.addWidget(self.features)
        main_layout.addStretch()

        self.setLayout(main_layout)
        # Set max width and center
        self.setMaximumWidth(1200)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Component Library Starter")
        self.setMinimumSize(900, 700)
        self.init_ui()

    def init_ui(self):
        self.container = Container()
        scroll_widget = QWidget()
        scroll_layout = QHBoxLayout()
        scroll_layout.addStretch()
        scroll_layout.addWidget(self.container)
        scroll_layout.addStretch()
        scroll_widget.setLayout(scroll_layout)

        self.setCentralWidget(scroll_widget)

        # Set up stylesheet for modern styling
        self.setStyleSheet("""
        /* General background and font */
        QWidget {
            background-color: #ffffff;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Header Styling */
        #header {
            background: #ffffff;
            border-bottom: 1px solid #e5e7eb;
            position: sticky;
            top: 0;
        }

        /* Navigation buttons */
        #navButton {
            color: #374151;
            font-size: 16px;
            background: transparent;
            border: none;
            padding: 8px 12px;
            border-radius: 6px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        #navButton:hover {
            background-color: #f3f4f6;
            color: #111827;
        }

        /* Hero Section */
        QLabel {
            selection-background-color: #2563eb;
        }

        /* CTA Button */
        #ctaButton {
            background-color: #111827;
            color: white;
            font-weight: 700;
            font-size: 18px;
            border: none;
            border-radius: 12px;
            transition: background-color 0.3s ease;
        }
        #ctaButton:hover {
            background-color: #1e40af;
        }
        #ctaButton:pressed {
            background-color: #374151;
        }

        /* Feature Cards */
        #featureCard {
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }

        /* Scroll area adjustments if needed */
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


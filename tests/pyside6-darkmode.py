import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,
    QFrame, QLineEdit, QTabWidget, QStackedWidget, QFormLayout, QSizePolicy, QSpacerItem,
    QMessageBox
)
from PySide6.QtGui import QFont, QIcon, QAction
from PySide6.QtCore import Qt

class Header(QWidget):
    def __init__(self, theme_toggle_callback):
        super().__init__()
        self.theme_toggle_callback = theme_toggle_callback
        self.dark_mode = False
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
        for name in ["Docs", "Components", "Showcase", "GitHub"]:
            btn = QPushButton(name)
            btn.setObjectName("navButton")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFlat(True)
            layout.addWidget(btn, alignment=Qt.AlignRight)

        # Theme toggle button
        self.theme_btn = QPushButton("Light Mode")
        self.theme_btn.setObjectName("themeToggle")
        self.theme_btn.setCursor(Qt.PointingHandCursor)
        self.theme_btn.setFixedSize(120, 32)
        self.theme_btn.clicked.connect(self.toggle_theme)
        layout.addWidget(self.theme_btn, alignment=Qt.AlignRight)

        self.setLayout(layout)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.theme_btn.setText("Dark Mode")
        else:
            self.theme_btn.setText("Light Mode")
        self.theme_toggle_callback(self.dark_mode)

class InfoCard(QFrame):
    def __init__(self, icon_text, title, value):
        super().__init__()
        self.icon_text = icon_text
        self.title = title
        self.value = value
        self.init_ui()

    def init_ui(self):
        self.setObjectName("infoCard")
        self.setMinimumWidth(220)
        self.setMaximumWidth(280)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(24, 16, 24, 16)
        layout.setSpacing(16)

        icon_label = QLabel(self.icon_text)
        icon_label.setObjectName("iconLabel")
        icon_label.setFixedSize(40, 40)
        font_icon = QFont("Segoe UI Symbol", 20)
        icon_label.setFont(font_icon)
        icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon_label)

        text_layout = QVBoxLayout()
        text_layout.setSpacing(4)

        title_lbl = QLabel(self.title)
        font_title = QFont("Segoe UI", 14, QFont.DemiBold)
        title_lbl.setFont(font_title)
        title_lbl.setStyleSheet("")
        text_layout.addWidget(title_lbl)

        value_lbl = QLabel(self.value)
        font_value = QFont("Segoe UI", 24, QFont.Bold)
        value_lbl.setFont(font_value)
        value_lbl.setStyleSheet("color: #111827;")
        text_layout.addWidget(value_lbl)

        layout.addLayout(text_layout)
        self.setLayout(layout)

class SettingsForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(20)

        self.name_input = QLineEdit()
        self.email_input = QLineEdit()

        self.name_input.setPlaceholderText("John Doe")
        self.email_input.setPlaceholderText("john@example.com")

        layout.addRow("Name:", self.name_input)
        layout.addRow("Email:", self.email_input)

        self.subscribe_btn = QPushButton("Subscribe")
        self.subscribe_btn.setObjectName("ctaButton")
        self.subscribe_btn.setFixedSize(160, 40)
        self.subscribe_btn.setCursor(Qt.PointingHandCursor)
        self.subscribe_btn.clicked.connect(self.on_subscribe)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.subscribe_btn)
        btn_layout.addStretch()

        outer_layout = QVBoxLayout()
        outer_layout.addLayout(layout)
        outer_layout.addLayout(btn_layout)
        outer_layout.addStretch()

        self.setLayout(outer_layout)

    def on_subscribe(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        if not name or not email:
            QMessageBox.warning(self, "Invalid Input", "Please enter both name and email.")
            return
        QMessageBox.information(self, "Subscribed", f"Thank you for subscribing, {name}!")
        self.name_input.clear()
        self.email_input.clear()

class TabsSection(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(32, 0, 32, 32)
        layout.setSpacing(24)

        self.tabs = QTabWidget()
        self.tabs.setObjectName("mainTabs")

        # Overview tab - info cards
        overview_tab = QWidget()
        overview_layout = QHBoxLayout()
        overview_layout.setContentsMargins(16, 16, 16, 16)
        overview_layout.setSpacing(24)
        cards_data = [
            ("⚙️", "Components", "42"),
            ("📦", "Packages", "8"),
            ("🌐", "Languages", "5"),
        ]
        for icon, title, val in cards_data:
            card = InfoCard(icon, title, val)
            overview_layout.addWidget(card)
        overview_layout.addStretch()
        overview_tab.setLayout(overview_layout)
        self.tabs.addTab(overview_tab, "Overview")

        # Settings tab - form
        settings_tab = SettingsForm()
        self.tabs.addTab(settings_tab, "Settings")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

class Container(QWidget):
    def __init__(self, theme_toggle_callback):
        super().__init__()
        self.theme_toggle_callback = theme_toggle_callback
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        self.header = Header(self.theme_toggle_callback)
        main_layout.addWidget(self.header)

        # Hero section with headline, subtitle, and CTA
        hero = QWidget()
        hero_layout = QVBoxLayout()
        hero_layout.setContentsMargins(32, 48, 32, 48)
        hero_layout.setSpacing(20)

        headline = QLabel("Build your Component Library")
        headline_font = QFont("Segoe UI", 44, QFont.DemiBold)
        headline.setFont(headline_font)
        headline.setWordWrap(True)
        headline.setStyleSheet("color: #111827;")
        hero_layout.addWidget(headline)

        subtext = QLabel("A clean, modern UI toolkit crafted for developers who value clarity and design.")
        subtext_font = QFont("Segoe UI", 18)
        subtext.setFont(subtext_font)
        subtext.setStyleSheet("color: #6b7280;")
        subtext.setWordWrap(True)
        hero_layout.addWidget(subtext)

        cta_btn = QPushButton("Get Started")
        cta_btn.setObjectName("ctaButton")
        cta_btn.setCursor(Qt.PointingHandCursor)
        cta_btn.setFixedSize(160, 48)
        hero_layout.addWidget(cta_btn, alignment=Qt.AlignLeft)

        hero.setLayout(hero_layout)
        main_layout.addWidget(hero)

        # Tabs section with overview and settings form
        tabs_section = TabsSection()
        main_layout.addWidget(tabs_section)

        main_layout.addStretch()
        self.setLayout(main_layout)
        self.setMaximumWidth(1200)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.setWindowTitle("PySide6 Component Library Extended Demo")
        self.setMinimumSize(900, 700)
        self.init_ui()

    def init_ui(self):
        self.container = Container(self.toggle_theme)
        scroll_widget = QWidget()
        scroll_layout = QHBoxLayout()
        scroll_layout.addStretch()
        scroll_layout.addWidget(self.container)
        scroll_layout.addStretch()
        scroll_widget.setLayout(scroll_layout)
        self.setCentralWidget(scroll_widget)
        self.apply_light_theme()

    def toggle_theme(self, is_dark):
        if is_dark:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()

    def apply_light_theme(self):
        self.dark_mode = False
        self.setStyleSheet("""
        QWidget {
            background-color: #ffffff;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            color: #111827;
        }
        #header {
            background: #ffffff;
            border-bottom: 1px solid #e5e7eb;
        }
        #navButton, #themeToggle {
            color: #374151;
            font-size: 16px;
            background: transparent;
            border: none;
            padding: 8px 12px;
            border-radius: 6px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        #navButton:hover, #themeToggle:hover {
            background-color: #f3f4f6;
            color: #111827;
        }
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
        #infoCard, #infoCard:hover {
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            transition: box-shadow 0.3s ease;
        }
        #infoCard:hover {
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        #iconLabel {
            color: #2563eb;
        }
        QTabWidget::pane {
            border: none;
        }
        QTabBar::tab {
            padding: 12px 24px;
            font-size: 16px;
            font-weight: 600;
            color: #6b7280;
            border-bottom: 3px solid transparent;
            margin-right: 16px;
        }
        QTabBar::tab:selected {
            color: #111827;
            border-bottom-color: #2563eb;
        }
        QLineEdit {
            border: 1px solid #d1d5db;
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 16px;
        }
        QLineEdit:focus {
            border-color: #2563eb;
            outline: none;
        }
        """)

    def apply_dark_theme(self):
        self.dark_mode = True
        self.setStyleSheet("""
        QWidget {
            background-color: #121212;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            color: #e0e0e0;
        }
        #header {
            background: #1f1f1f;
            border-bottom: 1px solid #333333;
        }
        #navButton, #themeToggle {
            color: #9ca3af;
            font-size: 16px;
            background: transparent;
            border: none;
            padding: 8px 12px;
            border-radius: 6px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        #navButton:hover, #themeToggle:hover {
            background-color: #2c2c2c;
            color: #ffffff;
        }
        #ctaButton {
            background-color: #bb86fc;
            color: #121212;
            font-weight: 700;
            font-size: 18px;
            border: none;
            border-radius: 12px;
            transition: background-color 0.3s ease;
        }
        #ctaButton:hover {
            background-color: #9e6fff;
        }
        #ctaButton:pressed {
            background-color: #7a52cc;
        }
        #infoCard, #infoCard:hover {
            background: #1f1f1f;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(255,255,255,0.05);
            transition: box-shadow 0.3s ease;
        }
        #infoCard:hover {
            box-shadow: 0 8px 20px rgba(255,255,255,0.1);
        }
        #iconLabel {
            color: #bb86fc;
        }
        QTabWidget::pane {
            border: none;
        }
        QTabBar::tab {
            padding: 12px 24px;
            font-size: 16px;
            font-weight: 600;
            color: #9ca3af;
            border-bottom: 3px solid transparent;
            margin-right: 16px;
        }
        QTabBar::tab:selected {
            color: #ffffff;
            border-bottom-color: #bb86fc;
        }
        QLineEdit {
            border: 1px solid #333333;
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 16px;
            background: #121212;
            color: #e0e0e0;
        }
        QLineEdit:focus {
            border-color: #bb86fc;
            outline: none;
        }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

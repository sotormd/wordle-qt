#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication

from modules import ui, themes

if __name__ == "__main__":
    current_style = themes.get_current_style() 
    app = QApplication(sys.argv)
    app.setStyleSheet(ui.get_stylesheet(current_style))
    window = ui.WordleUI(app, current_style)
    window.show()
    sys.exit(app.exec())

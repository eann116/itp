import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
)
# Import the Terminal Widget
from PyQtTerminal import TerminalWidget 

# Your custom function (for example, to clear the terminal)
def clear_terminal(terminal):
    """Clears the terminal widget."""
    terminal.clear()

class TerminalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQtTerminal Example")
        
        # --- GUI Setup ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 1. Create the Terminal Widget
        self.terminal = TerminalWidget()
        layout.addWidget(self.terminal)

        # 2. Add a Button to run a function
        self.button = QPushButton("Clear Terminal")
        layout.addWidget(self.button)

        # 3. Connect the Button to the function (using a lambda to pass the widget)
        # We pass the terminal object as an argument to our custom function
        self.button.clicked.connect(lambda: clear_terminal(self.terminal))
        
        # --- Start the terminal process ---
        # The TerminalWidget handles the QProcess internally,
        # usually running /bin/bash or /bin/sh by default.
        self.terminal.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TerminalWindow()
    window.show()
    sys.exit(app.exec())
from PyQt6.QtWidgets import QLabel, QPushButton, QWidget


def create_buttons(parent, result):
    button_plus = QPushButton("+", parent)
    button_minus = QPushButton("-", parent)
    button_reset = QPushButton("reset", parent)

    button_width = parent.width() - 26
    button_height = 54
    button_plus.setGeometry(13, parent.height() - 295, button_width, button_height)
    button_minus.setGeometry(13, parent.height() - 230, button_width, button_height)
    button_reset.setGeometry(13, parent.height() - 165, button_width, button_height)

    for button in (button_plus, button_minus, button_reset):
        button.setStyleSheet(
            "QPushButton { color: white; background-color: gray; border: 1px solid black; border-radius: 0px; font-size: 14px; }"
        )

    def plus_clicked():
        result.setText(str(int(result.text()) + 1))

    def minus_clicked():
        result.setText(str(int(result.text()) - 1))

    def reset_clicked():
        result.setText("0")

    button_plus.clicked.connect(plus_clicked)
    button_minus.clicked.connect(minus_clicked)
    button_reset.clicked.connect(reset_clicked)

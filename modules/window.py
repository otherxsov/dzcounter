from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QFrame,QHBoxLayout,QLabel,QMainWindow,QScrollArea,QWidget)

from .app import app
from .buttons import create_buttons


WIDTH_WINDOW = 1024
HEIGHT_WINDOW = 800

screen_geometry = app.primaryScreen()
HEIGHT_WINDOW = screen_size.height()
WIDTH_WINDOW = screen_size.width()
main_window = QMainWindow()
screen_x = screen_geometry.x() + screen_geometry.width() // 2 - WIDTH_WINDOW // 2
screen_y = screen_geometry.y() + screen_geometry.height() // 2 - HEIGHT_WINDOW // 2
main_window.setGeometry(screen_x, screen_y, WIDTH_WINDOW, HEIGHT_WINDOW)

frame_0 = QFrame(parent=main_window)
frame_0.setObjectName("windowFrame")
frame_0.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)
frame_0.setStyleSheet("background-color: gray; border: 1px solid black;")

horizontal_layout = QHBoxLayout(frame_0)
horizontal_layout.setContentsMargins(0, 0, 0, 0)
horizontal_layout.setSpacing(0)

main_scroll = QScrollArea(parent=frame_0)
main_scroll.setFixedSize(400, HEIGHT_WINDOW)
main_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
main_scroll.setWidgetResizable(False)
main_scroll.setStyleSheet("background-color: gray;")
main_scroll.setFrameShape(QFrame.Shape.NoFrame)
horizontal_layout.addWidget(main_scroll)
horizontal_layout.addStretch()

counter_content = QWidget()
counter_content.setObjectName("counterContent")
counter_content.setStyleSheet("background-color: gray;")
counter_content.setFixedSize(400, HEIGHT_WINDOW)

value_label = QLabel("0", counter_content)
value_label.setObjectName("counterValue")
value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
value_label.setStyleSheet("color: white; font-size: 24px; font-weight: 400;")
value_label.setGeometry(0, HEIGHT_WINDOW // 2 - 30, 400, 60)
main_scroll.setWidget(counter_content)
create_buttons(counter_content, value_label)
main_window.setCentralWidget(frame_0)

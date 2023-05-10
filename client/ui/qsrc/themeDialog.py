"""
...
\n
Copyright © 2023 Kalynovsky Valentin. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from configparser import ConfigParser

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QColorDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QColor
import qdarktheme

from src import IMPORTANT_DATA

# todo завершить окошко, логику, документацию, сохранение цветов в .ini

def set_button_color_rainbow_gradient_stylesheet():
	return """
		background: qlineargradient(
			x1:0, y1:0, x2:1, y2:0, stop:0 #FF0000, stop:0.15 #FF7F00, stop:0.33 #FFFF00,
			stop:0.49 #00FF00, stop:0.67 #0000FF, stop:0.84 #4B0082, stop:1 #8B00FF
		);
		border-radius: 12px;
		padding: 8px 8px;
	"""

def set_button_color_stylesheet(color: str):
	return f"""
		background-color: '{color}';
		border-radius: 12px;
		padding: 8px 8px;
	"""

def setAppearance(theme: str):
	IMPORTANT_DATA.appearance = theme
	qdarktheme.setup_theme(theme=IMPORTANT_DATA.appearance, custom_colors={"primary": IMPORTANT_DATA.accent_color})

def setCustomColor():
	color = QColorDialog.getColor()
	if color.isValid():
		IMPORTANT_DATA.accent_color = color.name()
		qdarktheme.setup_theme(theme=IMPORTANT_DATA.appearance, custom_colors={"primary": IMPORTANT_DATA.accent_color})

def setAccentColor(color: str):
	IMPORTANT_DATA.accent_color = color
	qdarktheme.setup_theme(theme=IMPORTANT_DATA.appearance, custom_colors={"primary": IMPORTANT_DATA.accent_color})

class ThemeDialog(QDialog):
	"""
	A class that describes the dialog box for reading a COM port.
	"""

	def __init__(self):
		super(ThemeDialog, self).__init__()

		# Adding layouts
		self.main_layout = QVBoxLayout()
		self.appearance_layout = QHBoxLayout()
		self.color_horizontal_layout = QHBoxLayout()

		self.appearance_label = QLabel("Select appearance ", self)
		self.appearance_layout.addWidget(self.appearance_label)

		self.combo_box = QComboBox()
		self.combo_box.addItems(qdarktheme.get_themes())
		self.combo_box.setCurrentText(IMPORTANT_DATA.appearance)
		self.combo_box.currentTextChanged.connect(setAppearance)
		self.appearance_layout.addWidget(self.combo_box)
		self.main_layout.addLayout(self.appearance_layout)

		self.accent_label = QLabel("Select accent color ", self)
		self.color_horizontal_layout.addWidget(self.accent_label)

		self.color_dialog_button = QPushButton()
		self.color_dialog_button.setStyleSheet(set_button_color_rainbow_gradient_stylesheet())
		self.color_dialog_button.clicked.connect(setCustomColor)
		self.color_horizontal_layout.addWidget(self.color_dialog_button)

		self.blue_color_button = QPushButton()
		self.blue_color_button.setStyleSheet(set_button_color_stylesheet("#007BFF"))
		self.blue_color_button.clicked.connect(lambda: setAccentColor("#007BFF"))
		self.color_horizontal_layout.addWidget(self.blue_color_button)

		self.purple_color_button = QPushButton()
		self.purple_color_button.setStyleSheet(set_button_color_stylesheet("#5856D6"))
		self.purple_color_button.clicked.connect(lambda: setAccentColor("#5856D6"))
		self.color_horizontal_layout.addWidget(self.purple_color_button)

		self.pink_color_button = QPushButton()
		self.pink_color_button.setStyleSheet(set_button_color_stylesheet("#FF2D55"))
		self.pink_color_button.clicked.connect(lambda: setAccentColor("#FF2D55"))
		self.color_horizontal_layout.addWidget(self.pink_color_button)

		self.red_color_button = QPushButton()
		self.red_color_button.setStyleSheet(set_button_color_stylesheet("#FF3B30"))
		self.red_color_button.clicked.connect(lambda: setAccentColor("#FF3B30"))
		self.color_horizontal_layout.addWidget(self.red_color_button)

		self.orange_color_button = QPushButton()
		self.orange_color_button.setStyleSheet(set_button_color_stylesheet("#FF9500"))
		self.orange_color_button.clicked.connect(lambda: setAccentColor("#FF9500"))
		self.color_horizontal_layout.addWidget(self.orange_color_button)

		self.yellow_color_button = QPushButton()
		self.yellow_color_button.setStyleSheet(set_button_color_stylesheet("#FFCC00"))
		self.yellow_color_button.clicked.connect(lambda: setAccentColor("#FFCC00"))
		self.color_horizontal_layout.addWidget(self.yellow_color_button)

		self.green_color_button = QPushButton()
		self.green_color_button.setStyleSheet(set_button_color_stylesheet("#34C759"))
		self.green_color_button.clicked.connect(lambda: setAccentColor("#34C759"))
		self.color_horizontal_layout.addWidget(self.green_color_button)

		self.graphite_color_button = QPushButton()
		self.graphite_color_button.setStyleSheet(set_button_color_stylesheet("#808080"))
		self.graphite_color_button.clicked.connect(lambda: setAccentColor("#808080"))
		self.color_horizontal_layout.addWidget(self.graphite_color_button)

		self.main_layout.addLayout(self.appearance_layout)
		self.main_layout.addLayout(self.color_horizontal_layout)

		# Dialog window customization
		self.setLayout(self.main_layout)
		self.setWindowIcon(QIcon("./icon/theme.png"))
		self.setWindowTitle("Set theme")
		self.setWindowFlags(Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowStaysOnTopHint)
		self.setFixedSize(800, 80)
		self.setWindowModality(Qt.WindowModality.WindowModal)  # make the window modal

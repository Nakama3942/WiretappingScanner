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

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QColorDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QColor
import qdarktheme

from src import IMPORTANT_DATA

# todo завершить окошко, логику, документацию, сохранение цветов в .ini

def set_button_color_stylesheet(color: str):
	return f"""
		background-color: '{color}';
		border-radius: 12px;
		padding: 8px 8px;
	"""

class ThemeDialog(QDialog):
	"""
	A class that describes the dialog box for reading a COM port.
	"""

	def __init__(self):
		super(ThemeDialog, self).__init__()

		# Adding layouts
		self.layout = QVBoxLayout()
		self.h_layout = QHBoxLayout()

		self.combo_box = QComboBox()
		self.combo_box.addItems(qdarktheme.get_themes())
		self.combo_box.setCurrentText(IMPORTANT_DATA.appearance)
		self.combo_box.currentTextChanged.connect(self.setAppearance)
		self.layout.addWidget(self.combo_box)

		self.color_button = QPushButton()
		self.color_button.setStyleSheet(
			"""
			background: qlineargradient(
				x1:0, y1:0, x2:1, y2:0, stop:0 #FF0000, stop:0.15 #FF7F00, stop:0.33 #FFFF00,
				stop:0.49 #00FF00, stop:0.67 #0000FF, stop:0.84 #4B0082, stop:1 #8B00FF
			);
			border-radius: 12px;
			padding: 8px 8px;
			"""
		)
		self.color_button.clicked.connect(self.showColorDialog)
		self.h_layout.addWidget(self.color_button)

		self.custom_color_button = QPushButton()
		self.custom_color_button.setStyleSheet(set_button_color_stylesheet(IMPORTANT_DATA.custom_color))
		self.custom_color_button.clicked.connect(lambda: self.setColorDialog(IMPORTANT_DATA.custom_color))
		self.h_layout.addWidget(self.custom_color_button)

		self.button1 = QPushButton()
		self.button1.setStyleSheet(set_button_color_stylesheet("#007BFF"))
		self.button1.clicked.connect(lambda: self.setColorDialog("#007BFF"))
		self.h_layout.addWidget(self.button1)

		self.button2 = QPushButton()
		self.button2.setStyleSheet(set_button_color_stylesheet("#5856D6"))
		self.button2.clicked.connect(lambda: self.setColorDialog("#5856D6"))
		self.h_layout.addWidget(self.button2)

		self.button3 = QPushButton()
		self.button3.setStyleSheet(set_button_color_stylesheet("#FF2D55"))
		self.button3.clicked.connect(lambda: self.setColorDialog("#FF2D55"))
		self.h_layout.addWidget(self.button3)

		self.button4 = QPushButton()
		self.button4.setStyleSheet(set_button_color_stylesheet("#FF3B30"))
		self.button4.clicked.connect(lambda: self.setColorDialog("#FF3B30"))
		self.h_layout.addWidget(self.button4)

		self.button5 = QPushButton()
		self.button5.setStyleSheet(set_button_color_stylesheet("#FF9500"))
		self.button5.clicked.connect(lambda: self.setColorDialog("#FF9500"))
		self.h_layout.addWidget(self.button5)

		self.button6 = QPushButton()
		self.button6.setStyleSheet(set_button_color_stylesheet("#FFCC00"))
		self.button6.clicked.connect(lambda: self.setColorDialog("#FFCC00"))
		self.h_layout.addWidget(self.button6)

		self.button7 = QPushButton()
		self.button7.setStyleSheet(set_button_color_stylesheet("#34C759"))
		self.button7.clicked.connect(lambda: self.setColorDialog("#34C759"))
		self.h_layout.addWidget(self.button7)

		self.button8 = QPushButton()
		self.button8.setStyleSheet(set_button_color_stylesheet("#808080"))
		self.button8.clicked.connect(lambda: self.setColorDialog("#808080"))
		self.h_layout.addWidget(self.button8)


		#
		# self.button10 = QPushButton()
		# self.button10.setStyleSheet(
		# 	"""
		# 	background-color: '#FFA500';
		# 	border-radius: 12px;
		# 	padding: 8px 8px;
		# 	"""
		# )
		# self.button10.clicked.connect(lambda: self.setColorDialog("#FFA500"))
		# self.h_layout.addWidget(self.button10)

		self.layout.addLayout(self.h_layout)

		# Dialog window customization
		self.setLayout(self.layout)
		self.setWindowIcon(QIcon("./icon/theme.png"))
		self.setWindowTitle("Set theme")
		self.setWindowFlags(Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowStaysOnTopHint)
		self.setFixedSize(320, 80)
		self.setWindowModality(Qt.WindowModality.WindowModal)  # make the window modal

	def setAppearance(self, theme: str):
		IMPORTANT_DATA.appearance = theme
		qdarktheme.setup_theme(theme=IMPORTANT_DATA.appearance, custom_colors={"primary": IMPORTANT_DATA.last_color})

	def setColorDialog(self, color: str):
		IMPORTANT_DATA.accent_color = color
		IMPORTANT_DATA.last_color = color
		qdarktheme.setup_theme(theme=IMPORTANT_DATA.appearance, custom_colors={"primary": IMPORTANT_DATA.accent_color})

	def showColorDialog(self):
		color = QColorDialog.getColor()
		if color.isValid():
			IMPORTANT_DATA.custom_color = color.name()
			IMPORTANT_DATA.last_color = color.name()
			self.custom_color_button.setStyleSheet(set_button_color_stylesheet(IMPORTANT_DATA.custom_color))
			qdarktheme.setup_theme(theme=IMPORTANT_DATA.appearance, custom_colors={"primary": IMPORTANT_DATA.custom_color})

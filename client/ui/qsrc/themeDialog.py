"""
Implementation of setting program appearance and accent color.
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

from os import listdir
from configparser import ConfigParser

from PyQt6.QtWidgets import QDialog, QGridLayout, QHBoxLayout, QSizePolicy, QLabel, QComboBox, QPushButton, QColorDialog
from PyQt6.QtCore import pyqtSignal, Qt, QSize
from PyQt6.QtGui import QIcon, QColor, QFontDatabase
import qdarktheme

from src import IMPORTANT_DATA

def _set_button_color_rainbow_gradient_stylesheet() -> str:
	"""
	A function that returns the StyleSheet for the gradient button.

	:return: StyleSheet for the gradient button
	"""
	return """
		background: qlineargradient(
			x1:0, y1:0, x2:1, y2:0, stop:0 #FF0000, stop:0.15 #FF7F00, stop:0.33 #FFFF00,
			stop:0.49 #00FF00, stop:0.67 #0000FF, stop:0.84 #4B0082, stop:1 #8B00FF
		);
		border-radius: 15px;
		padding: 8px 8px;
	"""

def _set_button_color_stylesheet(color: str) -> str:
	"""
	A function that returns the StyleSheet for a regular colored button.

	:param color: Button color
	:return: StyleSheet for a regular colored button
	"""
	return f"""
		background-color: '{color}';
		border-radius: 15px;
		padding: 8px 8px;
	"""

def _setAppearance(theme: str) -> None:
	"""
	The function sets the theme of the application.

	:param theme: The theme of the application
	"""
	IMPORTANT_DATA.appearance = theme
	qdarktheme.setup_theme(theme=IMPORTANT_DATA.appearance, custom_colors={"primary": IMPORTANT_DATA.accent_color})

def _setCustomColor() -> None:
	"""
	The function sets the application's custom accent color.
	"""
	color = QColorDialog.getColor()
	if color.isValid():
		IMPORTANT_DATA.accent_color = color.name()
		qdarktheme.setup_theme(theme=IMPORTANT_DATA.appearance, custom_colors={"primary": IMPORTANT_DATA.accent_color})

def _setAccentColor(color: str) -> None:
	"""
	The function sets the accent color of the application.

	:param color: The accent color of the application
	"""
	IMPORTANT_DATA.accent_color = color
	qdarktheme.setup_theme(theme=IMPORTANT_DATA.appearance, custom_colors={"primary": IMPORTANT_DATA.accent_color})

class ThemeDialog(QDialog):
	"""
	A class that describes the dialog box for reading a COM port.
	"""

	font_changed = pyqtSignal()

	def __init__(self):
		super(ThemeDialog, self).__init__()

		# Adding layouts
		self.main_layout = QGridLayout()
		self.color_horizontal_layout = QHBoxLayout()
		self.font_layout = QHBoxLayout()

		# Adding strings
		self.appearance_label = QLabel("Select appearance", self)
		self.main_layout.addWidget(self.appearance_label, 0, 0)
		self.accent_label = QLabel("Select accent color", self)
		self.main_layout.addWidget(self.accent_label, 1, 0)
		self.font_label = QLabel("Select a service font", self)
		self.main_layout.addWidget(self.font_label, 2, 0)

		# Adding a Theme Picker ComboBox
		self.appearance_combo_box = QComboBox()
		self.appearance_combo_box.addItems(qdarktheme.get_themes())
		self.appearance_combo_box.setCurrentText(IMPORTANT_DATA.appearance)
		self.appearance_combo_box.currentTextChanged.connect(_setAppearance)
		self.main_layout.addWidget(self.appearance_combo_box, 0, 1)

		# A button to set a custom accent color
		self.color_dialog_button = QPushButton()
		self.color_dialog_button.setMinimumSize(QSize(30, 30))
		self.color_dialog_button.setMaximumSize(QSize(30, 30))
		self.color_dialog_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.color_dialog_button.setStyleSheet(_set_button_color_rainbow_gradient_stylesheet())
		self.color_dialog_button.clicked.connect(_setCustomColor)
		self.color_horizontal_layout.addWidget(self.color_dialog_button)

		# A button to set a blue accent color
		self.blue_color_button = QPushButton()
		self.blue_color_button.setMinimumSize(QSize(30, 30))
		self.blue_color_button.setMaximumSize(QSize(30, 30))
		self.blue_color_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.blue_color_button.setStyleSheet(_set_button_color_stylesheet("#007BFF"))
		self.blue_color_button.clicked.connect(lambda: _setAccentColor("#007BFF"))
		self.color_horizontal_layout.addWidget(self.blue_color_button)

		# A button to set a purple accent color
		self.purple_color_button = QPushButton()
		self.purple_color_button.setMinimumSize(QSize(30, 30))
		self.purple_color_button.setMaximumSize(QSize(30, 30))
		self.purple_color_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.purple_color_button.setStyleSheet(_set_button_color_stylesheet("#5856D6"))
		self.purple_color_button.clicked.connect(lambda: _setAccentColor("#5856D6"))
		self.color_horizontal_layout.addWidget(self.purple_color_button)

		# A button to set a pink accent color
		self.pink_color_button = QPushButton()
		self.pink_color_button.setMinimumSize(QSize(30, 30))
		self.pink_color_button.setMaximumSize(QSize(30, 30))
		self.pink_color_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.pink_color_button.setStyleSheet(_set_button_color_stylesheet("#FF2D55"))
		self.pink_color_button.clicked.connect(lambda: _setAccentColor("#FF2D55"))
		self.color_horizontal_layout.addWidget(self.pink_color_button)

		# A button to set a red accent color
		self.red_color_button = QPushButton()
		self.red_color_button.setMinimumSize(QSize(30, 30))
		self.red_color_button.setMaximumSize(QSize(30, 30))
		self.red_color_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.red_color_button.setStyleSheet(_set_button_color_stylesheet("#FF3B30"))
		self.red_color_button.clicked.connect(lambda: _setAccentColor("#FF3B30"))
		self.color_horizontal_layout.addWidget(self.red_color_button)

		# A button to set a orange accent color
		self.orange_color_button = QPushButton()
		self.orange_color_button.setMinimumSize(QSize(30, 30))
		self.orange_color_button.setMaximumSize(QSize(30, 30))
		self.orange_color_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.orange_color_button.setStyleSheet(_set_button_color_stylesheet("#FF9500"))
		self.orange_color_button.clicked.connect(lambda: _setAccentColor("#FF9500"))
		self.color_horizontal_layout.addWidget(self.orange_color_button)

		# A button to set a yellow accent color
		self.yellow_color_button = QPushButton()
		self.yellow_color_button.setMinimumSize(QSize(30, 30))
		self.yellow_color_button.setMaximumSize(QSize(30, 30))
		self.yellow_color_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.yellow_color_button.setStyleSheet(_set_button_color_stylesheet("#FFCC00"))
		self.yellow_color_button.clicked.connect(lambda: _setAccentColor("#FFCC00"))
		self.color_horizontal_layout.addWidget(self.yellow_color_button)

		# A button to set a green accent color
		self.green_color_button = QPushButton()
		self.green_color_button.setMinimumSize(QSize(30, 30))
		self.green_color_button.setMaximumSize(QSize(30, 30))
		self.green_color_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.green_color_button.setStyleSheet(_set_button_color_stylesheet("#34C759"))
		self.green_color_button.clicked.connect(lambda: _setAccentColor("#34C759"))
		self.color_horizontal_layout.addWidget(self.green_color_button)

		# A button to set a graphite accent color
		self.graphite_color_button = QPushButton()
		self.graphite_color_button.setMinimumSize(QSize(30, 30))
		self.graphite_color_button.setMaximumSize(QSize(30, 30))
		self.graphite_color_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.graphite_color_button.setStyleSheet(_set_button_color_stylesheet("#808080"))
		self.graphite_color_button.clicked.connect(lambda: _setAccentColor("#808080"))
		self.color_horizontal_layout.addWidget(self.graphite_color_button)
		self.main_layout.addLayout(self.color_horizontal_layout, 1, 1)

		# Adding a Services Font ComboBox
		self.font_combo_box = QComboBox()
		self.update_font_combo_box()
		self.font_combo_box.setCurrentText(IMPORTANT_DATA.service_font)
		self.font_combo_box.currentTextChanged.connect(self.font_changed_emit)
		self.font_layout.addWidget(self.font_combo_box)

		# A button to update a font_combo_box
		self.update_font_combo_box_button = QPushButton()
		self.update_font_combo_box_button.setMinimumSize(QSize(120, 30))
		self.update_font_combo_box_button.setMaximumSize(QSize(120, 30))
		self.update_font_combo_box_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.update_font_combo_box_button.setText("Update the font list")
		self.update_font_combo_box_button.setToolTip("Update the custom user font list")
		self.update_font_combo_box_button.clicked.connect(self.update_font_combo_box_button_clicked)
		self.font_layout.addWidget(self.update_font_combo_box_button)
		self.main_layout.addLayout(self.font_layout, 2, 1)

		# Dialog window customization
		self.setLayout(self.main_layout)
		self.setWindowIcon(QIcon("./icon/theme.png"))
		self.setWindowTitle("Set theme")
		self.setWindowFlags(Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowStaysOnTopHint)
		self.setFixedSize(470, 150)
		self.setWindowModality(Qt.WindowModality.WindowModal)

	def font_changed_emit(self, font_name: str) -> None:
		"""
		Emit the signal which user of choose the font.

		:param font_name: Name of the chose font
		"""
		IMPORTANT_DATA.service_font = font_name
		self.font_changed.emit()

	def update_font_combo_box(self) -> None:
		"""
		The method update the list custom users fonts.
		"""
		self.font_combo_box.clear()
		font_list = []
		for i in range(0, IMPORTANT_DATA.count_user_font):
			font_list.append(QFontDatabase.applicationFontFamilies(i)[0])
		self.font_combo_box.addItems(font_list)

	def update_font_combo_box_button_clicked(self) -> None:
		"""
		The method update the program fonts database.
		"""
		font_list = listdir("font")
		QFontDatabase.removeAllApplicationFonts()
		IMPORTANT_DATA.count_user_font = 0
		for font_file in font_list:
			if QFontDatabase.addApplicationFont(f"./font/{font_file}"):
				IMPORTANT_DATA.count_user_font += 1
		self.update_font_combo_box()

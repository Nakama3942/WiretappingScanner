"""
Implementation of ultrasound generation.
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

from platform import system

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QDialogButtonBox
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QIcon, QFont, QRegularExpressionValidator

class UltrasoundDialog(QDialog):
	"""
	Ultrasound generator interface class.
	"""
	def __init__(self):
		super(UltrasoundDialog, self).__init__()

		# Adding layouts
		self.layout = QVBoxLayout()

		# Adding font
		self.font = QFont("Monospace") if system() == "Linux" else QFont("Courier New")

		# Adding an input field for generating ultrasound frequency
		self.frequency_field = QLineEdit(self)
		self.frequency_field.setFont(self.font)
		self.frequency_field.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9]\\d{0,4}|100000")))
		self.frequency_field.setPlaceholderText("Enter signal frequency")
		self.frequency_field.setToolTip(
			"The value must be between 20000 and 100000 Hertz\n"
			"If the field is left blank, the value will be set to 50000 Hertz\n"
			"Value less than 20000 Hertz will be rounded up to 20000 Hertz"
		)
		self.layout.addWidget(self.frequency_field)

		# Adding an input field for the generation time of ultrasound
		self.duration_field = QLineEdit(self)
		self.duration_field.setFont(self.font)
		self.duration_field.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9]|10")))
		self.duration_field.setPlaceholderText("Enter signal duration")
		self.duration_field.setToolTip(
			"The value must be between 1 and 10 seconds\n"
			"If the field is left blank, the value will be set to 5 second"
		)
		self.layout.addWidget(self.duration_field)

		# Adding dialog buttons
		self.butt_box = QDialogButtonBox()
		self.butt_box.setOrientation(Qt.Orientation.Horizontal)
		self.butt_box.setStandardButtons(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
		self.butt_box.setCenterButtons(True)
		self.butt_box.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.butt_box_ok_clicked)
		self.butt_box.button(QDialogButtonBox.StandardButton.Cancel).clicked.connect(self.butt_box_cancel_clicked)
		self.layout.addWidget(self.butt_box)

		# Dialog window customization
		self.setLayout(self.layout)
		self.setWindowIcon(QIcon("./icon/ultrasound.png"))
		self.setWindowTitle('Ultrasound Dialog')
		self.setWindowFlags(Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowStaysOnTopHint)
		self.setFixedSize(270, 100)
		self.setWindowModality(Qt.WindowModality.WindowModal)  # make the window modal

	def butt_box_ok_clicked(self) -> None:
		"""
		Ultrasound generation method.
		"""
		if self.frequency_field.text() == "":
			self.frequency_field.setText("50000")
		if self.duration_field.text() == "":
			self.frequency_field.setText("5")
		if int(self.frequency_field.text()) < 20000:
			self.frequency_field.setText("20000")
		# todo realize ultrasound generation
		self.done(QDialogButtonBox.StandardButton.Ok.value)

	def butt_box_cancel_clicked(self) -> None:
		"""
		Ultrasound generation cancel method.
		"""
		self.done(QDialogButtonBox.StandardButton.Cancel.value)

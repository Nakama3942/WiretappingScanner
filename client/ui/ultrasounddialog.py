"""
The logic of the ultrasound generation dialog box.
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

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog

from ui.raw import Ui_UltrasoundDialog


class UltrasoundDialog(QDialog, Ui_UltrasoundDialog):
	def __init__(self):
		super(UltrasoundDialog, self).__init__()
		self.setupUi(self)

		# Tracing dialog button clicks
		self.dialogButtonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).clicked.connect(self.box_Ok_Clicked)
		self.dialogButtonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).clicked.connect(self.box_Cancel_Clicked)

	def box_Ok_Clicked(self):
		self.done(QtWidgets.QDialogButtonBox.StandardButton.Ok.value)

	def box_Cancel_Clicked(self):
		self.done(QtWidgets.QDialogButtonBox.StandardButton.Cancel.value)

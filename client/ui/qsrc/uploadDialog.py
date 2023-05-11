"""
Implementation of esp32 flashing.
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

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

class UploadDialog(QDialog):
	"""
	ESP32 flashing class.
	"""
	def __init__(self):
		super(UploadDialog, self).__init__()

		# Adding layouts
		self.layout = QVBoxLayout()

		# Adding data fields
		self.ssid_field = QLineEdit(self)
		self.ssid_field.setPlaceholderText("Enter your ssid")
		self.password_field = QLineEdit(self)
		self.password_field.setPlaceholderText("Enter your password")
		self.layout.addWidget(self.ssid_field)
		self.layout.addWidget(self.password_field)

		# Adding a flashing button
		self.upload_butt = QPushButton("Upload", self)
		self.upload_butt.setIcon(QIcon("./icon/processor.png"))
		self.upload_butt.setIconSize(QSize(30, 30))
		self.upload_butt.clicked.connect(self.upload_butt_clicked)
		self.layout.addWidget(self.upload_butt)

		# Dialog window customization
		self.setLayout(self.layout)
		self.setWindowIcon(QIcon("./icon/upload.png"))
		self.setWindowTitle('Upload firmware')
		self.setWindowFlags(Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowStaysOnTopHint)
		self.setFixedSize(250, 120)
		self.setWindowModality(Qt.WindowModality.WindowModal)

	def upload_butt_clicked(self) -> None:
		"""
		ESP32 flashing.
		"""
		data = b""
		with open("./firmware/Wiretapping Scanner Firmware.bin", "rb") as binary:
			data = binary.read()

		password = b"\x45\x6E\x74\x65\x72\x20\x79\x6F\x75\x72\x20\x70\x61\x73\x73\x77\x6F\x72\x64"
		new_password = bytes(self.password_field.text().encode("ascii"))
		data = data.replace(password, new_password)

		ssid = b"\x45\x6E\x74\x65\x72\x20\x79\x6F\x75\x72\x20\x73\x73\x69\x64"
		new_ssid = bytes(self.ssid_field.text().encode("ascii"))
		data = data.replace(ssid, new_ssid)

		with open("./firmware/Wiretapping Scanner Firmware.bin", "wb") as binary:
			binary.seek(0)
			binary.write(data)

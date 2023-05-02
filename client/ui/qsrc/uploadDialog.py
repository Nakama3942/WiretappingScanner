from platform import system

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

class UploadDialog(QDialog):
	def __init__(self):
		super(UploadDialog, self).__init__()

		layout = QVBoxLayout()

		self.ssid_field = QLineEdit(self)
		self.ssid_field.setPlaceholderText("Enter your ssid")
		layout.addWidget(self.ssid_field)

		self.password_field = QLineEdit(self)
		self.password_field.setPlaceholderText("Enter your password")
		layout.addWidget(self.password_field)

		upload_butt = QPushButton("Upload", self)
		upload_butt.setIcon(QIcon("./icon/processor.png"))
		upload_butt.setIconSize(QSize(30, 30))
		layout.addWidget(upload_butt)
		upload_butt.clicked.connect(self.upload_butt_clicked)

		self.setLayout(layout)
		self.setWindowIcon(QIcon("./icon/upload.png"))
		self.setWindowTitle('Upload firmware')
		self.setWindowFlags(Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowStaysOnTopHint)
		self.setFixedSize(250, 120)
		self.setWindowModality(Qt.WindowModality.WindowModal)  # make the window modal

	def upload_butt_clicked(self):
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
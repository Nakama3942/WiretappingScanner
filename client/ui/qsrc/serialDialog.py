"""
Implementation of connection to COM port.
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

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QTextEdit
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt6.QtCore import Qt, QIODevice
from PyQt6.QtGui import QIcon, QFont

class SerialDialog(QDialog):
	"""
	A class that describes the dialog box for reading a COM port.
	"""

	def __init__(self):
		super(SerialDialog, self).__init__()

		# Adding layouts
		self.layout = QVBoxLayout()
		self.h_layout = QHBoxLayout()

		# Adding a ComboBox
		self.label = QLabel('Select COM Port:', self)
		self.combo = QComboBox(self)
		for port in QSerialPortInfo().availablePorts():
			self.combo.addItem(f"{str(port.portName())} - {str(port.description())}")
		self.h_layout.addWidget(self.label)
		self.h_layout.addWidget(self.combo)
		self.layout.addLayout(self.h_layout)

		# Adding a monitoring on/off button
		self.monitoring_butt = QPushButton('Monitoring', self)
		self.monitoring_butt.setCheckable(True)
		self.monitoring_butt.clicked.connect(self.monitoring_butt_clicked)
		self.layout.addWidget(self.monitoring_butt)

		# Adding a text output field intercepted from the COM port
		self.text = QTextEdit(self)
		self.text.setFont(QFont("Monospace")) if system() == "Linux" else self.text.setFont(QFont("Courier New"))
		self.text.setReadOnly(True)
		self.layout.addWidget(self.text)

		# Dialog window customization
		self.setLayout(self.layout)
		self.setWindowIcon(QIcon("./icon/serial_monitor.png"))
		self.setWindowTitle('Serial Monitor')
		self.setWindowFlags(Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowStaysOnTopHint)
		self.setFixedSize(400, 250)
		self.setWindowModality(Qt.WindowModality.WindowModal)  # make the window modal

		# Creating a COM port object
		self.com = QSerialPort()
		self.com.setBaudRate(9600)
		self.com.readyRead.connect(self.serial_write)
		self.string_data: bytes = b''

	def monitoring_butt_clicked(self) -> None:
		"""
		If the monitoring button is pressed - turns monitoring on/off.
		"""
		if self.monitoring_butt.isChecked():
			self.com.setPortName(self.combo.currentText().split(" ")[0])
			self.com.open(QIODevice.OpenModeFlag.ReadOnly)
		else:
			self.com.close()

	def serial_write(self) -> None:
		"""
		When data arrives at the COM port, it saves them in the program.
		"""
		self.string_data += self.com.readLine().data()
		if b'\n' in self.string_data:
			self.text.append(self.string_data.decode().rstrip())
			self.string_data = b''

	def close(self) -> bool:
		"""
		Closes the COM port if it is open.

		:return: See the Qt documentation
		"""
		if self.com.isOpen():
			self.com.close()
		return super().close()

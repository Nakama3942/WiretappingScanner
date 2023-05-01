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

# todo решить проблему первого подключения к КОМ порту

from serial import Serial
from serial.tools.list_ports import comports

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QTextEdit
from PyQt6.QtCore import Qt, QThread
from PyQt6.QtGui import QIcon

class _SerialWriter(QThread):
	def __init__(self, field: QTextEdit):
		super(_SerialWriter, self).__init__()
		self.com = None
		self._field = field

	def run(self) -> None:
		while True:
			line = self.com.readline().decode('ascii', 'ignore').rstrip()  # читаем строку из порта
			if line:  # если строка не пустая
				# print(line)  # выводим её на экран
				self._field.append(line)

	def terminate(self) -> None:
		super().terminate()
		self.com.close()

class SerialDialog(QDialog):
	def __init__(self):
		super(SerialDialog, self).__init__()
		# self.logger.notice(message_text="Unimplemented")
		# self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
		# window = QDialog(self)
		layout = QVBoxLayout()
		h_layout = QHBoxLayout()

		label = QLabel('Select COM Port:', self)
		h_layout.addWidget(label)

		self.combo = QComboBox(self)
		ports = list(comports())
		for port in ports:
			# print(port.device)
			self.combo.addItem(str(port))
		h_layout.addWidget(self.combo)

		layout.addLayout(h_layout)

		monitoring_butt = QPushButton('Monitoring', self)
		layout.addWidget(monitoring_butt)
		monitoring_butt.clicked.connect(self.monitoring_butt_clicked)

		self.text = QTextEdit(self)
		self.text.setReadOnly(True)
		layout.addWidget(self.text)

		self.setLayout(layout)
		self.setWindowIcon(QIcon("./icon/serial_monitor.png"))
		self.setWindowTitle('Serial Monitor')
		self.setWindowFlags(Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowStaysOnTopHint)
		self.setFixedSize(400, 250)
		self.setWindowModality(Qt.WindowModality.WindowModal)  # make the window modal
		# window.show()

		self.writer = _SerialWriter(self.text)

	def monitoring_butt_clicked(self):
		if self.writer.com is None:
			self.writer.com = Serial(self.combo.currentText().split(" ")[0], 9600)  # указываем порт и скорость передачи
		self.writer.start()

	def close(self):
		if self.writer.com is not None:
			self.writer.terminate()
		super().close()

	# 	self.offset = None
	# def mousePressEvent(self, event):
	# 	if event.button() == Qt.MouseButton.LeftButton:
	# 		self.offset = event.globalPosition().toPoint() - self.pos()
	# def mouseMoveEvent(self, event):
	# 	if event.buttons() == Qt.MouseButton.LeftButton:
	# 		self.move(event.globalPosition().toPoint() - self.offset)
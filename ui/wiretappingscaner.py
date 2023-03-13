#  Copyright © 2023 Kalynovsky Valentin. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import time

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QStyle, QSystemTrayIcon, QMenu, QFrame
from PyQt6.QtGui import QIcon, QFont, QAction, QKeyEvent, QCloseEvent, QFontDatabase
from PyQt6.QtCore import QThread, pyqtSignal

from ui.raw import Ui_WindowWiretappingScaner
from ui import UltrasoundDialog

from qt_colored_logger import LoggerQ
from src import IMPORTANT_DATA, getHost


class Detector(QThread):
	update_data_signal = pyqtSignal()

	def __init__(self):
		super(Detector, self).__init__()

	def run(self):
		# In the future, connection to the device will be implemented here
		while True:
			# Data acquisition simulation
			IMPORTANT_DATA.radio_signal = 101.4
			IMPORTANT_DATA.radio_amplitude = 20
			IMPORTANT_DATA.compass_radius = 70
			IMPORTANT_DATA.infrared_signal = 0.9
			IMPORTANT_DATA.infrared_data = "2 (Exit)"
			IMPORTANT_DATA.ultrasound_signal = 10778
			self.update_data_signal.emit()
			time.sleep(0.3)
			IMPORTANT_DATA.radio_signal = 97.5
			IMPORTANT_DATA.radio_amplitude = 28
			IMPORTANT_DATA.compass_radius = 76
			IMPORTANT_DATA.infrared_signal = 17.1
			IMPORTANT_DATA.infrared_data = "5 (Clear)"
			IMPORTANT_DATA.ultrasound_signal = 96333
			self.update_data_signal.emit()
			time.sleep(0.3)

	def terminate(self):
		# In the future, disconnection from the device will be implemented here
		super().terminate()


class WiretappingScaner(QMainWindow, Ui_WindowWiretappingScaner):
	def __init__(self):
		super(WiretappingScaner, self).__init__()
		self.setupUi(self)

		# Constant
		self.shift_bool = False
		self.logger = LoggerQ(status_message=False)

		# Set window to center
		qr = self.frameGeometry()
		qr.moveCenter(self.screen().availableGeometry().center())
		self.move(qr.topLeft())
		IMPORTANT_DATA.window_height = self.height()
		IMPORTANT_DATA.window_width = self.width()

		# Setting service font
		QFontDatabase.addApplicationFont("/font/fixedsys.ttf")
		self.font = QFont("fixedsys", 10)
		self.consoleBrowser.setFont(self.font)

		# Taking out devices connected to the router
		for i in getHost():
			self.IPBox.addItem(f"IP {i[0]} (MAC {i[1]})")
		self.statusbar.showMessage(f"STATUS\tDISCONNECT")

		# It's a tracking of button clicks in the window
		self.buttConnect.clicked.connect(self.buttConnect_clicked)
		self.buttDisconnect.clicked.connect(self.buttDisconnect_clicked)
		self.tabWidget.tabBarClicked.connect(self.tabWidget_Clicked)
		self.UltrasoundDrawFrame.gen_sound.connect(self.ultrasound_Gen)
		self.UltrasoundDrawFrame.play_sound.connect(self.ultrasound_Play)

		# Initialization of QSystemTrayIcon
		self.tray_icon = QSystemTrayIcon(self)
		self.tray_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon))
		show_action = QAction("Show", self)
		show_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton))
		show_action.triggered.connect(self.tray_Hide)
		radio_action = QAction("Radio", self)
		radio_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		radio_action.triggered.connect(lambda: self.openTab(0))
		compass_action = QAction("Compass", self)
		compass_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		compass_action.triggered.connect(lambda: self.openTab(1))
		IR_action = QAction("InfraRed radiation", self)
		IR_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		IR_action.triggered.connect(lambda: self.openTab(2))
		US_action = QAction("Ultrasound", self)
		US_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		US_action.triggered.connect(lambda: self.openTab(3))
		channel_action = QAction("Link quality", self)
		channel_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		channel_action.triggered.connect(lambda: self.openTab(4))
		close_action = QAction("Quit", self)
		close_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton))
		close_action.triggered.connect(self.close)
		tray_menu = QMenu()
		tray_menu.addAction(show_action)
		tray_menu.addAction(radio_action)
		tray_menu.addAction(compass_action)
		tray_menu.addAction(IR_action)
		tray_menu.addAction(US_action)
		tray_menu.addAction(channel_action)
		tray_menu.addAction(close_action)
		self.tray_icon.setContextMenu(tray_menu)

		# Initialization of process of tracking
		self.detector = Detector()
		self.detector.update_data_signal.connect(self.detect_update_data_signal)

		# Tab selection simulation - start renderer
		# (without this, the program refuses to work after the connection)
		self.tabWidget_Clicked(0)

	def tray_Show(self):
		self.tray_icon.show()
		self.hide()

	def tray_Hide(self):
		self.tray_icon.hide()
		self.show()

	def openTab(self, index):
		self.tray_Hide()
		self.tabWidget.setCurrentIndex(index)
		self.tabWidget_Clicked(index)

	def buttConnect_clicked(self):
		self.detector.start()
		IMPORTANT_DATA.IPAddr = self.IPBox.currentText().split(" ")[1]
		IMPORTANT_DATA.Port = "12556"
		IMPORTANT_DATA.SerialNum = "AQWZE-BCE-YPA-MORH"
		IMPORTANT_DATA.connect = True
		self.statusbar.showMessage(f"STATUS:\tCONNECT to {IMPORTANT_DATA.IPAddr}:{IMPORTANT_DATA.Port}")
		self.consoleBrowser.append(self.logger.INFO(message_text=f"CONNECT to {IMPORTANT_DATA.IPAddr}:{IMPORTANT_DATA.Port}"))
		self.statusLine.setText("Connected")
		self.statusLine.setStyleSheet("color: rgb(0, 150, 0);\nfont: italic;\nfont-size: 18px;")
		self.labelIPaddr.setText(IMPORTANT_DATA.IPAddr)
		self.labelPort.setText(IMPORTANT_DATA.Port)
		self.labelSerialNum.setText(IMPORTANT_DATA.SerialNum)
		self.widgetSettings.setEnabled(True)

	def buttDisconnect_clicked(self):
		self.detector.terminate()
		self.clearWidget()
		IMPORTANT_DATA.IPAddr = "000.000.000.000"
		IMPORTANT_DATA.Port = "00000"
		IMPORTANT_DATA.SerialNum = "AAAAA-AAA-AAA-AAAA"
		IMPORTANT_DATA.connect = False
		self.statusbar.showMessage(f"STATUS:\tDISCONNECT")
		self.consoleBrowser.append(self.logger.INFO(message_text=f"DISCONNECT"))
		self.statusLine.setText("Disconnect")
		self.statusLine.setStyleSheet("color: rgb(200, 0, 0);\nfont: italic;\nfont-size: 18px;")
		self.labelIPaddr.setText(IMPORTANT_DATA.IPAddr)
		self.labelPort.setText(IMPORTANT_DATA.Port)
		self.labelSerialNum.setText(IMPORTANT_DATA.SerialNum)
		self.widgetSettings.setEnabled(False)

	def clearWidget(self):
		self.RadioDrawFrame.update()
		self.CompassDrawFrame.update()
		self.UltrasoundDrawFrame.update()
		self.UltrasoundDrawFrame.update()
		self.FreeChannelDrawFrame.update()

	def tabWidget_Clicked(self, index):
		match index:
			case 0:
				IMPORTANT_DATA.tab = 0
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.text1 = "Radio signal (MHz): "
				IMPORTANT_DATA.text2 = "Radio amplitude: "
				self.RadioDrawFrame.repaint()
			case 1:
				IMPORTANT_DATA.tab = 1
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.tpixmap = "./icon/magnet.png"
				IMPORTANT_DATA.text1 = "Compass degree: "
				self.CompassDrawFrame.repaint()
			case 2:
				IMPORTANT_DATA.tab = 2
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.text1 = "Infrared signal (THz): "
				IMPORTANT_DATA.text2 = "Infrared signal data: "
				self.IRDrawFrame.repaint()
			case 3:
				IMPORTANT_DATA.tab = 3
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.text1 = "Ultrasound (Hz): "
				self.UltrasoundDrawFrame.repaint()
			case 4:
				IMPORTANT_DATA.tab = 4
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.text1 = "UNFINISHED"
				self.FreeChannelDrawFrame.repaint()

	def ultrasound_Gen(self):
		gen_dialog = UltrasoundDialog()
		gen_dialog.show()
		result: int = gen_dialog.exec()
		match result:
			case QtWidgets.QDialogButtonBox.StandardButton.Ok.value:
				# Unimplemented
				self.consoleBrowser.append(self.logger.ERROR(message_text="1 (Unimplemented)"))
			case QtWidgets.QDialogButtonBox.StandardButton.Cancel.value:
				# Unimplemented
				self.consoleBrowser.append(self.logger.ERROR(message_text="2 (Unimplemented)"))
			case _:
				# Unimplemented
				self.consoleBrowser.append(self.logger.ERROR(message_text="3 (Unimplemented)"))

	def ultrasound_Play(self):
		# Unimplemented
		self.consoleBrowser.append(self.logger.ERROR(message_text="4 (Unimplemented)"))

	def detect_update_data_signal(self):
		match IMPORTANT_DATA.tab:
			case 0:
				self.RadioDrawFrame.repaint()
				self.consoleBrowser.append(self.logger.INFO(message_text=f"{IMPORTANT_DATA.radio_signal} MHz radio signal detected"))
			case 1:
				self.CompassDrawFrame.repaint()
				self.consoleBrowser.append(self.logger.INFO(message_text=f"Compass deviation - {IMPORTANT_DATA.compass_radius} degrees"))
			case 2:
				self.IRDrawFrame.repaint()
				self.consoleBrowser.append(self.logger.INFO(message_text=f"{IMPORTANT_DATA.infrared_signal} THz infrared signal detected"))
			case 3:
				self.UltrasoundDrawFrame.repaint()
				self.consoleBrowser.append(self.logger.INFO(message_text=f"{IMPORTANT_DATA.ultrasound_signal} Hz ultrasound signal detected"))
			case 4:
				self.FreeChannelDrawFrame.repaint()
				self.consoleBrowser.append(self.logger.ERROR(message_text=f"Opened is unfinished 5th tab"))

	def keyPressEvent(self, event: QKeyEvent):
		self.shift_bool = (event.key() == QtCore.Qt.Key.Key_Shift)

	def closeEvent(self, event: QCloseEvent):
		# Program termination should occur in the tray, and not in the system menu
		# If the program is hidden, then the tray is available, not the system menu
		# Completion is allowed in the system menu if shift is pressed
		if self.isHidden() or self.shift_bool:
			# So can end the program
			self.detector.terminate()
			# event.accept()  # For some reason it doesn't work
			QApplication.instance().exit(0)
		else:
			# Else - hide in tray
			self.tray_Show()
			event.ignore()

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

from queue import Queue
from threading import Thread

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QStyle, QSystemTrayIcon, QMenu, QFrame, QProgressDialog
from PyQt6.QtCore import QRegularExpression, Qt, QCoreApplication
from PyQt6.QtGui import QRegularExpressionValidator, QIcon, QFont, QAction, QKeyEvent, QCloseEvent, QFontDatabase

from ui.raw import Ui_WindowWiretappingScaner
from ui import UltrasoundDialog
from ui.qsrc import Detector

from mighty_logger import Logger
from src import IMPORTANT_DATA, gotNmap, getHost, lastIndex

class WiretappingScaner(QMainWindow, Ui_WindowWiretappingScaner):
	def __init__(self):
		super(WiretappingScaner, self).__init__()
		self.setupUi(self)

		# Constant
		self.shift_bool = False
		self.logger = Logger(program_name="WiretappingScaner", status_message_global_entry=False, log_environment="html")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

		# Set window to center
		qr = self.frameGeometry()
		qr.moveCenter(self.screen().availableGeometry().center())
		self.move(qr.topLeft())
		self.reloadTool.setIcon(QIcon("./icon/search.png"))
		self.statusbar.showMessage(f"STATUS\tDISCONNECT")
		IMPORTANT_DATA.window_height = self.height()
		IMPORTANT_DATA.window_width = self.width()

		# It's creating a validator for the input field of the list of ports
		rx = QRegularExpression(r'^192\.168\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
		validator = QRegularExpressionValidator(rx, self)
		self.IPLine.setValidator(validator)

		# Setting service font
		QFontDatabase.addApplicationFont("/font/fixedsys.ttf")
		self.font = QFont("fixedsys", 13)
		self.consoleBrowser.setFont(self.font)

		# It's a tracking of button clicks in the window
		self.reloadTool.clicked.connect(self.reloadTool_clicked)
		self.buttConnect.clicked.connect(self.buttConnect_clicked)
		self.buttDisconnect.clicked.connect(self.buttDisconnect_clicked)
		self.buttWidgetScreenshot.clicked.connect(self.buttWidgetScreenshot_clicked)
		self.buttProgramScreenshot.clicked.connect(self.buttProgramScreenshot_clicked)
		self.buttSaveLog.clicked.connect(self.buttSaveLog_clicked)
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
		ir_action = QAction("InfraRed radiation", self)
		ir_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		ir_action.triggered.connect(lambda: self.openTab(2))
		us_action = QAction("Ultrasound", self)
		us_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		us_action.triggered.connect(lambda: self.openTab(3))
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
		tray_menu.addAction(ir_action)
		tray_menu.addAction(us_action)
		tray_menu.addAction(channel_action)
		tray_menu.addAction(close_action)
		self.tray_icon.setContextMenu(tray_menu)

		# Initialization of process of tracking
		self.detector = Detector(self.logger)
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

	def reloadTool_clicked(self):
		if gotNmap():
			progress_dialog = QProgressDialog()  # вынести в поток
			progress_dialog.setRange(0, 0)
			progress_dialog.setLabelText("Please wait...")
			progress_dialog.setWindowTitle("Progress")
			progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
			progress_dialog.setCancelButton(None)

			queue = Queue()
			external_process = Thread(target=getHost, args=(queue,))
			external_process.start()

			progress_dialog.show()  # вынести в поток
			QCoreApplication.processEvents()

			external_process.join(timeout=self.timeoutSpin.value())
			hosts = queue.get()
			if external_process.is_alive():
				external_process.terminate()
				self.logger.error(message_text=f"Timeout expired")
				self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
			else:
				for i in hosts:
					self.IPBox.addItem(f"IP {i[0]} (MAC {i[1]})")
				self.reloadTool.setIcon(QIcon("./icon/reload.png"))

		else:
			self.logger.error(message_text=f"Nmap is not installed")
			self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def buttConnect_clicked(self):
		try:
			if self.IPLine.text() == "":
				self.IPLine.setText(self.IPBox.currentText().split(" ")[1])
			IMPORTANT_DATA.IPAddr = self.IPLine.text()
			IMPORTANT_DATA.Port = "12556"
			self.detector.set_ip(self.IPLine.text())
			if not self.detector.con():
				self.buttDisconnect.trouble = True
				self.logger.fail(message_text=f"Connection Failed")
				self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
				self.buttDisconnect.click()
				return
			self.detector.start()  # Starts the process of connecting to the Detector and receiving data
			IMPORTANT_DATA.SerialNum = "AQWZE-BCE-YPA-MORH"  # Will be moved to Detector later
			IMPORTANT_DATA.connect = True # Will be moved to Detector later
		except:
			self.buttDisconnect.trouble = True
			self.logger.fail(message_text=f"Connection not established: no connected devices")
			self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
			self.buttDisconnect.click()
		else:
			self.buttDisconnect.trouble = False
			self.logger.success(message_text=f"CONNECT to {IMPORTANT_DATA.IPAddr}:{IMPORTANT_DATA.Port}")
			self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
			self.statusbar.showMessage(f"STATUS:\tCONNECT to {IMPORTANT_DATA.IPAddr}:{IMPORTANT_DATA.Port}")
			self.statusLine.setText("Connected")
			self.statusLine.setStyleSheet("color: rgb(0, 150, 0);\nfont: italic;\nfont-size: 18px;")
			self.labelIPaddr.setText(IMPORTANT_DATA.IPAddr)
			self.labelPort.setText(IMPORTANT_DATA.Port)
			self.labelSerialNum.setText(IMPORTANT_DATA.SerialNum)
			self.groupSettings.setEnabled(True)

	def buttDisconnect_clicked(self):
		if not self.buttDisconnect.trouble:
			self.detector.coff()
			self.detector.terminate()
			self.clearWidget()
			IMPORTANT_DATA.IPAddr = "000.000.000.000"
			IMPORTANT_DATA.Port = "00000"
			IMPORTANT_DATA.SerialNum = "AAAAA-AAA-AAA-AAAA"
			IMPORTANT_DATA.connect = False
			self.logger.info(message_text=f"DISCONNECT")
			self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
			self.statusbar.showMessage(f"STATUS:\tDISCONNECT")
			self.statusLine.setText("Disconnect")
			self.statusLine.setStyleSheet("color: rgb(200, 0, 0);\nfont: italic;\nfont-size: 18px;")
			self.labelIPaddr.setText(IMPORTANT_DATA.IPAddr)
			self.labelPort.setText(IMPORTANT_DATA.Port)
			self.labelSerialNum.setText(IMPORTANT_DATA.SerialNum)
			self.groupSettings.setEnabled(False)

	def clearWidget(self):
		self.RadioDrawFrame.update()
		self.CompassDrawFrame.update()
		self.UltrasoundDrawFrame.update()
		self.UltrasoundDrawFrame.update()
		self.FreeChannelDrawFrame.update()
		self.StethoscopeDrawFrame.update()

	def buttWidgetScreenshot_clicked(self):
		match IMPORTANT_DATA.tab:
			case 0:
				self.RadioDrawFrame.grab().save(lastIndex("RadioDrawFrameScreen.png", "{:07}"))
			case 1:
				self.CompassDrawFrame.grab().save(lastIndex("CompassDrawFrameScreen.png", "{:07}"))
			case 2:
				self.IRDrawFrame.grab().save(lastIndex("IRDrawFrameScreen.png", "{:07}"))
			case 3:
				self.UltrasoundDrawFrame.grab().save(lastIndex("UltrasoundDrawFrameScreen.png", "{:07}"))
			case 4:
				self.FreeChannelDrawFrame.grab().save(lastIndex("FreeChannelDrawFrameScreen.png", "{:07}"))
			case 5:
				self.StethoscopeDrawFrame.grab().save(lastIndex("StethoscopeDrawFrameScreen.png", "{:07}"))
		self.logger.info(message_text=f"Widget screenshot saved")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def buttProgramScreenshot_clicked(self):
		self.grab().save(lastIndex("ProgramScreen.png", "{:07}"))
		self.logger.info(message_text=f"Program screenshot saved")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def buttSaveLog_clicked(self):
		self.logger.buffer().save("log.html")
		self.logger.info(message_text=f"Log saved")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def tabWidget_Clicked(self, index):
		match index:
			case 0:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.text1 = "Radio signal (MHz): "
				IMPORTANT_DATA.text2 = "Radio amplitude: "
				self.RadioDrawFrame.repaint()
			case 1:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.tpixmap = "./icon/magnet.png"
				IMPORTANT_DATA.text1 = "Compass degree: "
				self.CompassDrawFrame.repaint()
			case 2:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.text1 = "Infrared signal (THz): "
				IMPORTANT_DATA.text2 = "Infrared signal data: "
				self.IRDrawFrame.repaint()
			case 3:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.text1 = "Ultrasound (Hz): "
				self.UltrasoundDrawFrame.repaint()
			case 4:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.text1 = "LINK QUALITY UNFINISHED"
				self.FreeChannelDrawFrame.repaint()
			case 5:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tfont = self.font
				IMPORTANT_DATA.text1 = "STETHOSCOPE UNFINISHED"
				self.StethoscopeDrawFrame.repaint()

	def ultrasound_Gen(self):
		gen_dialog = UltrasoundDialog()
		gen_dialog.show()
		result: int = gen_dialog.exec()
		match result:
			case QtWidgets.QDialogButtonBox.StandardButton.Ok.value:
				# Unimplemented
				self.logger.error(message_text="1 (Unimplemented)")
			case QtWidgets.QDialogButtonBox.StandardButton.Cancel.value:
				# Unimplemented
				self.logger.error(message_text="2 (Unimplemented)")
			case _:
				# Unimplemented
				self.logger.error(message_text="3 (Unimplemented)")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def ultrasound_Play(self):
		# Unimplemented
		self.logger.error(message_text="4 (Unimplemented)")
		self.logger.debug(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.debug_performance(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.performance(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.event(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.audit(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.metrics(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.user(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.message(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.info(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.notice(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.warning(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.critical(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.success(message_text="Отсылочка на мою библиотеку журналирования")
		self.logger.fail(message_text="Отсылочка на мою библиотеку журналирования")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def detect_update_data_signal(self):
		match IMPORTANT_DATA.tab:
			case 0:
				self.RadioDrawFrame.repaint()
				self.logger.info(message_text=f"{IMPORTANT_DATA.radio_signal} MHz radio signal detected")
			case 1:
				self.CompassDrawFrame.repaint()
				self.logger.info(message_text=f"Compass deviation - {IMPORTANT_DATA.compass_radius} degrees")
			case 2:
				self.IRDrawFrame.repaint()
				self.logger.info(message_text=f"{IMPORTANT_DATA.infrared_signal} THz infrared signal detected")
			case 3:
				self.UltrasoundDrawFrame.repaint()
				self.logger.info(message_text=f"{IMPORTANT_DATA.ultrasound_signal} Hz ultrasound signal detected")
			case 4:
				self.FreeChannelDrawFrame.repaint()
				self.logger.error(message_text=f"Opened is unfinished 5th tab")
			case 5:
				self.StethoscopeDrawFrame.repaint()
				self.logger.error(message_text=f"Opened is unfinished 6th tab")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def keyPressEvent(self, event: QKeyEvent):
		self.shift_bool = (event.key() == QtCore.Qt.Key.Key_Shift)

	def closeEvent(self, event: QCloseEvent):
		# Program termination should occur in the tray, and not in the system menu
		# If the program is hidden, then the tray is available, not the system menu
		# Completion is allowed in the system menu if shift is pressed or not connected
		if self.isHidden() or self.shift_bool or not IMPORTANT_DATA.connect:
			# So can end the program
			self.detector.coff()
			self.detector.terminate()
			# event.accept()  # For some reason it doesn't work
			QApplication.instance().exit(0)
		else:
			# Else - hide in tray
			self.tray_Show()
			event.ignore()

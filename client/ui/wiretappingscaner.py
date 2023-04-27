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

# todo
#  5. Завершить README.md и About.md

from time import sleep
from markdown_it import MarkdownIt

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QStyle, QSystemTrayIcon, QMenu, QFrame, QProgressDialog, QMessageBox
from PyQt6.QtCore import QRegularExpression, Qt, QDir
from PyQt6.QtGui import QRegularExpressionValidator, QIcon, QFont, QAction, QKeyEvent, QCloseEvent, QFontDatabase, QPixmap

from ui.raw import Ui_WindowWiretappingScaner
from ui import UltrasoundDialog
from ui.qsrc import Detector

from mighty_logger import Logger
from src import IMPORTANT_DATA, getHost, lastIndex

class WiretappingScaner(QMainWindow, Ui_WindowWiretappingScaner):
	def __init__(self):
		super(WiretappingScaner, self).__init__()
		self.setupUi(self)

		# Constant
		self.shift_bool = False

		# Set window to center
		qr = self.frameGeometry()
		qr.moveCenter(self.screen().availableGeometry().center())
		self.move(qr.topLeft())
		self.statusbar.showMessage(f"STATUS\tDISCONNECT")
		IMPORTANT_DATA.window_height = self.height()
		IMPORTANT_DATA.window_width = self.width()

		# Icon initialization
		QDir.addSearchPath('icons', 'icon/')
		self.setWindowIcon(QIcon('icons:wiretapping_scaner.png'))

		self.reloadTool.setIcon(QIcon("./icon/search.png"))
		self.aboutTool.setIcon(QIcon("./icon/about.png"))

		self.tabWidget.setTabIcon(0, QIcon("./icon/radio.png"))
		self.tabWidget.setTabIcon(1, QIcon("./icon/compass.png"))
		self.tabWidget.setTabIcon(2, QIcon("./icon/infrared.png"))
		self.tabWidget.setTabIcon(3, QIcon("./icon/ultrasound.png"))
		self.tabWidget.setTabIcon(4, QIcon("./icon/wifi.png"))
		self.tabWidget.setTabIcon(5, QIcon("./icon/stethoscope.png"))

		# It's creating a validator for the input field of the list of ports
		rx = QRegularExpression(r'^192\.168\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
		validator = QRegularExpressionValidator(rx, self)
		self.IPLine.setValidator(validator)

		# Setting service font
		QFontDatabase.addApplicationFont("/font/fixedsys.ttf")
		self.font = QFont("fixedsys", 13)
		self.consoleBrowser.setFont(self.font)
		IMPORTANT_DATA.tfont = self.font

		# It's a tracking of button clicks in the window
		self.reloadTool.clicked.connect(self.reloadTool_clicked)
		self.aboutTool.clicked.connect(self.aboutTool_clicked)
		self.buttConnect.clicked.connect(self.buttConnect_clicked)
		self.buttDisconnect.clicked.connect(self.buttDisconnect_clicked)
		self.buttWidgetScreenshot.clicked.connect(self.buttWidgetScreenshot_clicked)
		self.buttProgramScreenshot.clicked.connect(self.buttProgramScreenshot_clicked)
		self.buttSaveLog.clicked.connect(self.buttSaveLog_clicked)
		self.tabWidget.tabBarClicked.connect(self.tabWidget_Clicked)
		# self.UltrasoundDrawFrame.gen_sound.connect(self.ultrasound_Gen)
		# self.UltrasoundDrawFrame.play_sound.connect(self.ultrasound_Play)

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

		self.logger = Logger(program_name="WiretappingScaner", status_message_global_entry=False, log_environment="html")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

		# Initialization of process of tracking
		self.detector = Detector()
		self.detector.starting_signal.connect(self.detect_starting_signal)
		self.detector.starting_error_signal.connect(self.detect_starting_error_signal)
		self.detector.update_data_signal.connect(self.detect_update_data_signal)
		self.detector.update_data_error_signal.connect(self.detect_update_data_error_signal)
		self.detector.stopping_signal.connect(self.detect_stopping_signal)
		self.detector.stopping_error_signal.connect(self.detect_stopping_error_signal)

		# Tab selection simulation - start renderer
		# (without this, the program refuses to work after the connection)
		self.tabWidget_Clicked(0)

		# Canceled again...
		self.tabWidget.setTabVisible(5, False)

	def tray_Show(self):
		self.tray_icon.show()
		self.hide()
		self.logger.user(message_text="Program closed to tray")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def tray_Hide(self):
		self.tray_icon.hide()
		self.show()
		self.logger.user(message_text="Program opened from tray")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def openTab(self, index):
		self.tray_Hide()
		self.tabWidget.setCurrentIndex(index)
		self.tabWidget_Clicked(index)

	def reloadTool_clicked(self):
		if IMPORTANT_DATA.connect:
			self.logger.fail(message_text="Can't use Nmap while connected")
			self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
			return
		self.IPBox.clear()
		wait = QMessageBox()
		wait.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint)
		wait.setModal(True)
		wait.setWindowTitle("Information")
		wait.setIcon(QMessageBox.Icon.Information)
		wait.setText("<font size=14>Please wait...</font>")
		wait.setInformativeText("The process of determining the static IP addresses of the local network is in progress")
		wait.setStandardButtons(QMessageBox.StandardButton.NoButton)
		wait.show()
		QApplication.processEvents()

		result, hosts_list, error = getHost(self.timeoutSpin.value())
		if result:
			for i in hosts_list:
				self.IPBox.addItem(f"IP {i[0]} (MAC {i[1]})")
			self.reloadTool.setIcon(QIcon("./icon/reload.png"))
		else:
			err = QMessageBox()
			err.setWindowTitle("Error")
			err.setWindowIcon(QIcon("./icon/wiretapping_scaner.png"))
			err.setIcon(QMessageBox.Icon.Critical)
			err.setText("<font size=14 color='red'>Error...</font>")
			err.setInformativeText(f"<font color='darkred'>{error}</font>")
			err.setStandardButtons(QMessageBox.StandardButton.Cancel)
			ret: int = err.exec()
			match ret:
				case QMessageBox.StandardButton.Cancel:
					self.logger.error(message_text=error)
					self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
		wait.close()

	def aboutTool_clicked(self):
		with open('About.md', 'r') as f:
			text = f.read()
			md = MarkdownIt()
			html = md.render(text)

		about_program_container = QMessageBox()
		about_program_container.setWindowIcon(QIcon("./icon/about.png"))
		about_program = QMessageBox()
		about_program.about(about_program_container, "About program", html)

		self.logger.user(message_text="Viewed information about the program")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def buttConnect_clicked(self):
		if not self.buttConnect.trouble:
			if self.IPLine.text() == "":
				if self.IPBox.count() == 0:
					raise ConnectionError("IP address is not specified")
				else:
					self.IPLine.setText(self.IPBox.currentText().split(" ")[1])
			IMPORTANT_DATA.IPAddr = self.IPLine.text()
			IMPORTANT_DATA.Port = "12556"
			self.detector.set_ip(self.IPLine.text())
			self.detector.start()  # Starts the process of connecting to the Detector and receiving data

	def detect_starting_signal(self):
		self.logger.success(message_text=f"CONNECT to {IMPORTANT_DATA.IPAddr}:{IMPORTANT_DATA.Port}")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
		self.statusbar.showMessage(f"STATUS:\tCONNECT to {IMPORTANT_DATA.IPAddr}:{IMPORTANT_DATA.Port}")
		self.statusLine.setText("Connected")
		self.statusLine.setStyleSheet("color: rgb(0, 150, 0);\nfont: italic;\nfont-size: 18px;")
		self.labelIPaddr.setText(IMPORTANT_DATA.IPAddr)
		self.labelPort.setText(IMPORTANT_DATA.Port)
		self.labelSerialNum.setText(IMPORTANT_DATA.SerialNum)
		self.tabWidget.setEnabled(True)
		self.groupSettings.setEnabled(True)
		self.buttDisconnect.trouble = False

	def detect_starting_error_signal(self, error: str):
		err = QMessageBox()
		err.setWindowTitle("Error")
		err.setWindowIcon(QIcon("./icon/wiretapping_scaner.png"))
		err.setIcon(QMessageBox.Icon.Warning)
		err.setText("<font size=14 color='red'>Error...</font>")
		err.setInformativeText(f"<font color='darkred'>{error}</font>")
		err.setStandardButtons(QMessageBox.StandardButton.Cancel)
		ret: int = err.exec()
		match ret:
			case QMessageBox.StandardButton.Cancel:
				self.logger.fail(message_text=error)
				self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
		self.buttDisconnect.trouble = True
		self.buttDisconnect.click()

	def detect_update_data_signal(self):
		match IMPORTANT_DATA.tab:
			case 0:
				self.RadioDrawFrame.customRepaint()
				self.logger.metrics(message_text=f"{IMPORTANT_DATA.radio_signal_spectrum_width} MHz radio signal spectrum width detected")
			case 1:
				self.CompassDrawFrame.customRepaint()
				self.logger.metrics(message_text=f"Compass deviation - {IMPORTANT_DATA.compass_north_direction} degrees")
			case 2:
				self.IRDrawFrame.customRepaint()
				self.logger.fail(message_text=f"The sensor is broken")
			case 3:
				self.UltrasoundDrawFrame.customRepaint()
				self.logger.metrics(message_text=f"{IMPORTANT_DATA.ultrasound_frequency_of_wavefront} Hz ultrasound frequency of wavefront detected")
			case 4:
				self.FreeChannelDrawFrame.customRepaint()
				self.logger.metrics(message_text=f"{IMPORTANT_DATA.link_signal_strength} Hz link quality detected")
			case 5:
				self.StethoscopeDrawFrame.customRepaint()
				self.logger.metrics(message_text=f"{IMPORTANT_DATA.stethoscope_sound_frequency} Hz stethoscope frequency detected")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def detect_update_data_error_signal(self, error: str):
		self.logger.fail(message_text=error)
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def buttDisconnect_clicked(self):
		if not self.buttDisconnect.trouble:
			self.detector.stop()

	def detect_stopping_signal(self):
		self.detector.terminate()
		self.clearWidget()
		IMPORTANT_DATA.IPAddr = "000.000.000.000"
		IMPORTANT_DATA.Port = "00000"
		self.logger.success(message_text=f"DISCONNECT")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
		self.statusbar.showMessage(f"STATUS:\tDISCONNECT")
		self.statusLine.setText("Disconnect")
		self.statusLine.setStyleSheet("color: rgb(200, 0, 0);\nfont: italic;\nfont-size: 18px;")
		self.labelIPaddr.setText(IMPORTANT_DATA.IPAddr)
		self.labelPort.setText(IMPORTANT_DATA.Port)
		self.labelSerialNum.setText(IMPORTANT_DATA.SerialNum)
		self.tabWidget.setEnabled(False)
		self.groupSettings.setEnabled(False)
		self.buttConnect.trouble = False

	def detect_stopping_error_signal(self, error: str):
		err = QMessageBox()
		err.setWindowTitle("Error")
		err.setWindowIcon(QIcon("./icon/wiretapping_scaner.png"))
		err.setIcon(QMessageBox.Icon.Warning)
		err.setText("<font size=14 color='red'>Error...</font>")
		err.setInformativeText(f"<font color='darkred'>{error}</font>")
		err.setStandardButtons(QMessageBox.StandardButton.Cancel)
		ret: int = err.exec()
		match ret:
			case QMessageBox.StandardButton.Cancel:
				self.logger.fail(message_text=error)
				self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
		self.buttConnect.trouble = True
		self.buttConnect.click()

	def clearWidget(self):
		self.RadioDrawFrame.customUpdate()
		self.CompassDrawFrame.customUpdate()
		self.IRDrawFrame.customUpdate()
		self.UltrasoundDrawFrame.customUpdate()
		self.FreeChannelDrawFrame.customUpdate()
		self.StethoscopeDrawFrame.customUpdate()

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
		self.logger.event(message_text=f"Widget screenshot saved")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def buttProgramScreenshot_clicked(self):
		self.grab().save(lastIndex("ProgramScreen.png", "{:07}"))
		self.logger.event(message_text=f"Program screenshot saved")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def buttSaveLog_clicked(self):
		self.logger.buffer().save("log.html")
		self.logger.event(message_text=f"Log saved")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def tabWidget_Clicked(self, index):
		match index:
			case 0:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tpixmap1 = "./icon/pulse.png"
				IMPORTANT_DATA.text1 = "Radio impulse (s): "
				IMPORTANT_DATA.tpixmap2 = "./icon/wave.png"
				IMPORTANT_DATA.text2 = "Signal noise (dB): "
				IMPORTANT_DATA.tpixmap3 = "./icon/spectrum_width.png"
				IMPORTANT_DATA.text3 = "Signal Spectrum Width (Hz): "
				IMPORTANT_DATA.tpixmap4 = "./icon/signal_duration.png"
				IMPORTANT_DATA.text4 = "Signal duration (s): "
				IMPORTANT_DATA.tpixmap5 = "./icon/transfer_rate.png"
				IMPORTANT_DATA.text5 = "Transfer rate (bps): "
				IMPORTANT_DATA.tpixmap6 = "./icon/fork.png"
				IMPORTANT_DATA.text6 = "Antenna impedance (Ω): "
				IMPORTANT_DATA.tpixmap7 = "./icon/direction.png"
				IMPORTANT_DATA.text7 = "Antenna directivity (dBi): "
				IMPORTANT_DATA.tpixmap8 = "./icon/signal_strength_0.png"
				IMPORTANT_DATA.text8 = "Signal strength (dB): "
				self.RadioDrawFrame.customRepaint()
			case 1:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tpixmap1 = "./icon/magnet.png"
				IMPORTANT_DATA.text1 = "A magnetic field (μT): "
				IMPORTANT_DATA.tpixmap2 = "./icon/angle.png"
				IMPORTANT_DATA.text2 = "Tilt angle (°): "
				IMPORTANT_DATA.tpixmap3 = "./icon/north_direction.png"
				IMPORTANT_DATA.text3 = "North direction (°): "
				IMPORTANT_DATA.tpixmap4 = "./icon/field_strength.png"
				IMPORTANT_DATA.text4 = "Field strength (A/m): "
				IMPORTANT_DATA.tpixmap5 = "./icon/temperature.png"
				IMPORTANT_DATA.text5 = "Temperature (°C): "
				self.CompassDrawFrame.customRepaint()
			case 2:
				IMPORTANT_DATA.tab = index
				# IMPORTANT_DATA.tpixmap1 = "./icon/sinus.png"
				IMPORTANT_DATA.text1 = "The sensor is broken"
				# IMPORTANT_DATA.tpixmap2 = "./icon/wavelength.png"
				# IMPORTANT_DATA.text2 = "Wavelength (μm): "
				# IMPORTANT_DATA.tpixmap3 = "./icon/signal_strength_0.png"
				# IMPORTANT_DATA.text3 = "Signal strength (dB): "
				# IMPORTANT_DATA.tpixmap4 = "./icon/signal_power.png"
				# IMPORTANT_DATA.text4 = "Signal power (dBm): "
				# IMPORTANT_DATA.tpixmap5 = "./icon/angle.png"
				# IMPORTANT_DATA.text5 = "Reception angle (°): "
				# IMPORTANT_DATA.tpixmap6 = "./icon/transfer_rate.png"
				# IMPORTANT_DATA.text6 = "Transfer rate (bps): "
				self.IRDrawFrame.customRepaint()
			case 3:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tpixmap1 = "./icon/sinus.png"
				IMPORTANT_DATA.text1 = "Frequency of wavefront (Hz): "
				IMPORTANT_DATA.tpixmap2 = "./icon/wavelength.png"
				IMPORTANT_DATA.text2 = "Wavelength (mm): "
				IMPORTANT_DATA.tpixmap3 = "./icon/signal_strength_0.png"
				IMPORTANT_DATA.text3 = "Signal strength (dB): "
				IMPORTANT_DATA.tpixmap4 = "./icon/signal_power.png"
				IMPORTANT_DATA.text4 = "Signal power (dBm): "
				IMPORTANT_DATA.tpixmap5 = "./icon/wave.png"
				IMPORTANT_DATA.text5 = "Resolution (mm): "
				IMPORTANT_DATA.tpixmap6 = "./icon/transfer_rate.png"
				IMPORTANT_DATA.text6 = "Transfer rate (bps): "
				self.UltrasoundDrawFrame.customRepaint()
			case 4:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tpixmap1 = "./icon/transfer_rate.png"
				IMPORTANT_DATA.text1 = "Transfer rate (bps): "
				IMPORTANT_DATA.tpixmap2 = "./icon/spectrum_width.png"
				IMPORTANT_DATA.text2 = "Frequency range (Hz): "
				IMPORTANT_DATA.tpixmap3 = "./icon/signal_strength_0.png"
				IMPORTANT_DATA.text3 = "Signal strength (dB): "
				IMPORTANT_DATA.tpixmap4 = "./icon/signal_power.png"
				IMPORTANT_DATA.text4 = "Signal power (dBm): "
				IMPORTANT_DATA.tpixmap5 = "./icon/wave.png"
				IMPORTANT_DATA.text5 = "Signal noise (dBm): "
				IMPORTANT_DATA.tpixmap6 = "./icon/spectrum_width.png"
				IMPORTANT_DATA.text6 = "Signal Spectrum Width (Hz): "
				IMPORTANT_DATA.tpixmap7 = "./icon/interference.png"
				IMPORTANT_DATA.text7 = "Interference level (dB): "
				IMPORTANT_DATA.tpixmap8 = "./icon/warning.png"
				IMPORTANT_DATA.text8 = "Bit error rate (-): "
				IMPORTANT_DATA.tpixmap9 = "./icon/engine.png"
				IMPORTANT_DATA.text9 = "Transmission power (dBm): "
				self.FreeChannelDrawFrame.customRepaint()
			case 5:
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.tpixmap1 = "./icon/amplitude.png"
				IMPORTANT_DATA.text1 = "Sound amplitude (dB): "
				IMPORTANT_DATA.tpixmap2 = "./icon/sinus.png"
				IMPORTANT_DATA.text2 = "Sound frequency (Hz): "
				IMPORTANT_DATA.tpixmap3 = "./icon/sound_pressure.png"
				IMPORTANT_DATA.text3 = "Sound pressure (Pa): "
				IMPORTANT_DATA.tpixmap4 = "./icon/direction.png"
				IMPORTANT_DATA.text4 = "Sound direction (°): "
				IMPORTANT_DATA.tpixmap5 = "./icon/transfer_rate.png"
				IMPORTANT_DATA.text5 = "Transfer rate (bps): "
				self.StethoscopeDrawFrame.customRepaint()

	# def ultrasound_Gen(self):
	# 	gen_dialog = UltrasoundDialog()
	# 	gen_dialog.show()
	# 	result: int = gen_dialog.exec()
	# 	match result:
	# 		case QtWidgets.QDialogButtonBox.StandardButton.Ok.value:
	# 			# Unimplemented
	# 			self.logger.error(message_text="1 (Unimplemented)")
	# 		case QtWidgets.QDialogButtonBox.StandardButton.Cancel.value:
	# 			# Unimplemented
	# 			self.logger.error(message_text="2 (Unimplemented)")
	# 		case _:
	# 			# Unimplemented
	# 			self.logger.error(message_text="3 (Unimplemented)")
	# 	self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
	#
	# def ultrasound_Play(self):
	# 	# Unimplemented
	# 	self.logger.error(message_text="4 (Unimplemented)")
	# 	self.logger.debug(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.debug_performance(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.performance(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.event(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.audit(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.metrics(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.user(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.message(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.info(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.notice(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.warning(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.critical(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.success(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.logger.fail(message_text="Отсылочка на мою библиотеку журналирования")
	# 	self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def keyPressEvent(self, event: QKeyEvent):
		self.shift_bool = (event.key() == QtCore.Qt.Key.Key_Shift)

	def closeEvent(self, event: QCloseEvent):
		# Program termination should occur in the tray, and not in the system menu
		# If the program is hidden, then the tray is available, not the system menu
		# Completion is allowed in the system menu if shift is pressed or not connected
		if not IMPORTANT_DATA.connect:
			QApplication.instance().exit(0)
		elif self.isHidden() or self.shift_bool:
			# So can end the program
			self.buttDisconnect_clicked()
			# event.accept()  # For some reason it doesn't work
			QApplication.instance().exit(0)
		else:
			# Else - hide in tray
			self.tray_Show()
			event.ignore()

"""
Responsible for displaying the graphical interface and linking ALL program components.
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

from markdown_it import MarkdownIt
from mighty_logger import Logger
from configparser import ConfigParser

from PyQt6.QtWidgets import QApplication, QMainWindow, QStyle, QSystemTrayIcon, QMenu, QMessageBox, QDialogButtonBox
from PyQt6.QtCore import QRegularExpression, Qt
from PyQt6.QtGui import QRegularExpressionValidator, QIcon, QFont, QAction, QCloseEvent, QFontDatabase

from ui.raw.ui_wiretappingscaner import Ui_WindowWiretappingScaner
from ui.qsrc.detector import Detector
from ui.qsrc.serialDialog import SerialDialog
from ui.qsrc.themeDialog import ThemeDialog
from ui.qsrc.uploadDialog import UploadDialog
from ui.qsrc.usDialog import UltrasoundDialog
from src import getHost, lastIndex, IMPORTANT_DATA

class WiretappingScaner(QMainWindow, Ui_WindowWiretappingScaner):
	"""
	Class with the interface and logic of the main program window.
	"""

	def __init__(self):
		super(WiretappingScaner, self).__init__()
		self.setupUi(self)

		# self.setStyleSheet(load_stylesheet("style/OneDark-Pro.json"))

		# Set window to center
		qr = self.frameGeometry()
		qr.moveCenter(self.screen().availableGeometry().center())
		self.move(qr.topLeft())
		self.statusbar.showMessage(f"STATUS\tDISCONNECT")
		IMPORTANT_DATA.window_height = self.height()
		IMPORTANT_DATA.window_width = self.width()

		# Icons setting
		self.setWindowIcon(QIcon("./icon/wiretapping_scaner.png"))
		self.aboutTool.setIcon(QIcon("./icon/about.png"))
		self.themeTool.setIcon(QIcon("./icon/theme.png"))
		self.serialTool.setIcon(QIcon("./icon/serial_monitor.png"))
		self.uploadTool.setIcon(QIcon("./icon/upload.png"))
		self.reloadTool.setIcon(QIcon("./icon/search.png"))
		self.tabWidget.setTabIcon(0, QIcon("./icon/radio.png"))
		self.tabWidget.setTabIcon(1, QIcon("./icon/compass.png"))
		self.tabWidget.setTabIcon(2, QIcon("./icon/infrared.png"))
		self.tabWidget.setTabIcon(3, QIcon("./icon/ultrasound.png"))
		self.tabWidget.setTabIcon(4, QIcon("./icon/wifi.png"))
		self.tabWidget.setTabIcon(5, QIcon("./icon/stethoscope.png"))

		# It's creating a validator for the input field of the list of ports
		self.IPLine.setValidator(
			QRegularExpressionValidator(
				QRegularExpression(
					r"^192\.168\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
				), self
			)
		)

		# Setting service font
		QFontDatabase.addApplicationFont("/font/fixedsys.ttf")
		self.font = QFont("fixedsys", 13)
		self.consoleBrowser.setFont(self.font)
		IMPORTANT_DATA.tfont = self.font

		# It's a tracking of button clicks in the window
		self.aboutTool.clicked.connect(self.aboutTool_clicked)
		self.themeTool.clicked.connect(self.themeTool_clicked)
		self.serialTool.clicked.connect(self.serialTool_clicked)
		self.uploadTool.clicked.connect(self.uploadTool_clicked)
		self.reloadTool.clicked.connect(self.reloadTool_clicked)
		self.buttConnect.clicked.connect(self.buttConnect_clicked)
		self.buttDisconnect.clicked.connect(self.buttDisconnect_clicked)
		self.frameshotButt.clicked.connect(self.frameshotButt_clicked)
		self.programshotButt.clicked.connect(self.programshotButt_clicked)
		self.logshotButt.clicked.connect(self.logshotButt_clicked)
		self.tabWidget.tabBarClicked.connect(self.tabWidget_Clicked)
		self.UltrasoundDrawFrame.gen_sound.connect(self.ultrasound_Gen)
		self.UltrasoundDrawFrame.play_sound.connect(self.ultrasound_Play)

		# Initialization of QSystemTrayIcon
		self.tray_icon = QSystemTrayIcon(self)
		self.tray_icon.setIcon(QIcon("./icon/wiretapping_scaner.png"))
		self.show_action = QAction("Show", self)
		self.show_action.setIcon(QIcon("./icon/open.png"))
		self.show_action.triggered.connect(self.tray_Hide)
		self.data_action = QAction("Data", self)
		self.data_action.setIcon(QIcon("./icon/fork.png"))
		self.data_action.triggered.connect(self.tray_Hide)
		self.radio_action = QAction("Switch to Radio tab", self)
		self.radio_action.setIcon(QIcon("./icon/radio.png"))
		self.radio_action.triggered.connect(lambda: self.switch_tab(0))
		self.compass_action = QAction("Switch to Compass tab", self)
		self.compass_action.setIcon(QIcon("./icon/compass.png"))
		self.compass_action.triggered.connect(lambda: self.switch_tab(1))
		self.ir_action = QAction("Switch to Infrared tab", self)
		self.ir_action.setIcon(QIcon("./icon/infrared.png"))
		self.ir_action.triggered.connect(lambda: self.switch_tab(2))
		self.us_action = QAction("Switch to Ultrasound tab", self)
		self.us_action.setIcon(QIcon("./icon/ultrasound.png"))
		self.us_action.triggered.connect(lambda: self.switch_tab(3))
		self.channel_action = QAction("Switch to Link quality tab", self)
		self.channel_action.setIcon(QIcon("./icon/wifi.png"))
		self.channel_action.triggered.connect(lambda: self.switch_tab(4))
		# self.stethoscope_action = QAction("Switch to Stethoscope tab", self)
		# self.stethoscope_action.setIcon(QIcon("./icon/stethoscope.png"))
		# self.stethoscope_action.triggered.connect(lambda: self.switch_tab(5))
		self.connect_action = QAction("Connect to last connection", self)
		self.connect_action.setIcon(QIcon("./icon/link.png"))
		self.connect_action.triggered.connect(lambda: self.buttConnect.click())
		self.disconnect_action = QAction("Disconnect from this connection", self)
		self.disconnect_action.setIcon(QIcon("./icon/remove_link.png"))
		self.disconnect_action.triggered.connect(lambda: self.buttDisconnect.click())
		self.tray_menu = QMenu()
		self.tray_menu.setTitle("Wiretapping Scanner")
		self.tray_menu.addAction(self.show_action)
		self.tray_menu.addSeparator()
		self.tray_menu.addAction(self.data_action)
		self.tray_menu.addSeparator()
		self.tray_menu.addAction(self.radio_action)
		self.tray_menu.addAction(self.compass_action)
		self.tray_menu.addAction(self.ir_action)
		self.tray_menu.addAction(self.us_action)
		self.tray_menu.addAction(self.channel_action)
		# self.tray_menu.addAction(self.stethoscope_action)
		self.tray_menu.addSeparator()
		self.tray_menu.addAction(self.disconnect_action)
		self.tray_icon.setContextMenu(self.tray_menu)

		# Initialization of Logger
		self.logger = Logger(
			program_name="WiretappingScaner",
			status_message_global_entry=False,
			log_environment="html"
		)
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

		# Initialization of process of tracking
		self.detector = Detector()
		self.detector.starting_signal.connect(self.detect_starting_signal)
		self.detector.starting_error_signal.connect(self.detect_starting_error_signal)
		self.detector.update_data_signal.connect(self.detect_update_data_signal)
		self.detector.update_data_error_signal.connect(self.detect_update_data_error_signal)
		self.detector.stopping_signal.connect(self.detect_stopping_signal)
		self.detector.stopping_error_signal.connect(self.detect_stopping_error_signal)

		# Initialization of dialog windows
		self.serial_dialog = SerialDialog()
		self.theme_dialog = ThemeDialog()
		self.upload_dialog = UploadDialog()
		self.us_dialog = UltrasoundDialog()

		# Tab selection simulation - start renderer
		# (without this, the program refuses to work after the connection)
		self.tabWidget_Clicked(0)

		# Canceled again...
		self.tabWidget.setTabVisible(5, False)

	def tray_Show(self) -> None:
		"""
		The method minimizes the program to tray.
		"""
		self.tray_icon.show()
		self.hide()
		self.logger.user(message_text="Program closed to tray")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def tray_Hide(self) -> None:
		"""
		The method maximizes the program from the tray.
		"""
		self.tray_icon.hide()
		self.show()
		self.logger.user(message_text="Program opened from tray")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def switch_tab(self, index: int) -> None:
		"""
		Method for switching tabs from tray.

		:param index: Tab number to active
		"""
		self.tabWidget.setCurrentIndex(index)
		self.tabWidget.tabBarClicked.emit(index)

	def aboutTool_clicked(self) -> None:
		"""
		The method displays information about the program.
		"""
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

	def themeTool_clicked(self) -> None:
		"""
		///
		"""
		if self.themeTool.isChecked():
			self.theme_dialog.show()
		else:
			self.theme_dialog.close()

	def serialTool_clicked(self) -> None:
		"""
		The method displays the COM port monitoring dialog box.
		"""
		if self.serialTool.isChecked():
			self.serial_dialog.show()
		else:
			self.serial_dialog.hide()

	def uploadTool_clicked(self) -> None:
		"""
		The method displays the flashing ESP32 dialog.
		"""
		if self.uploadTool.isChecked():
			# self.upload_dialog.show()
			warn = QMessageBox()
			warn.setWindowTitle("Problem tools")
			warn.setWindowIcon(QIcon("./icon/upload.png"))
			warn.setIcon(QMessageBox.Icon.Critical)
			warn.setText("<font size=14 color='red'>Error...</font>")
			warn.setInformativeText(
				"<font color='darkred'>"
				"The esptools library requires the Visual Studio development tools, which developers do not have - development stopped..."
				"</font>")
			warn.setStandardButtons(QMessageBox.StandardButton.Cancel)
			ret: int = warn.exec()
			match ret:
				case QMessageBox.StandardButton.Cancel:
					return
		else:
			# self.upload_dialog.close()
			pass

	def reloadTool_clicked(self) -> None:
		"""
		The method responsible for running and processing the results of Nmap.
		"""
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

		result, hosts_list, error = getHost(self.hostLine.text(), self.timeoutSpin.value())
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

	def buttConnect_clicked(self) -> None:
		"""
		The method that is executed after the Connect button is clicked.
		"""
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

	def detect_starting_signal(self) -> None:
		"""
		The method that is triggered after a successful connection.
		"""
		self.tray_menu.removeAction(self.connect_action)
		self.tray_menu.addAction(self.disconnect_action)
		self.logger.success(message_text=f"CONNECT to {IMPORTANT_DATA.IPAddr}:{IMPORTANT_DATA.Port}")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
		self.statusbar.showMessage(f"STATUS:\tCONNECT to {IMPORTANT_DATA.IPAddr}:{IMPORTANT_DATA.Port}")
		self.statusLine.setText("Connected")
		self.statusLine.setStyleSheet("color: rgb(0, 150, 0);\nfont: italic;\nfont-size: 18px;")
		self.labelIPaddr.setText(IMPORTANT_DATA.IPAddr)
		self.labelPort.setText(IMPORTANT_DATA.Port)
		self.labelSerialNum.setText(IMPORTANT_DATA.SerialNum)
		self.setWindowTitle(f"{IMPORTANT_DATA.IPAddr} Server : {self.windowTitle()}")
		self.tabWidget.setEnabled(True)
		self.groupSettings.setEnabled(True)
		self.buttDisconnect.trouble = False

	def detect_starting_error_signal(self, error: str) -> None:
		"""
		The method that is triggered after a failed connection.

		:param error: Error message
		"""
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

	def detect_update_data_signal(self) -> None:
		"""
		The method that is triggered after the data has been successfully received.
		"""
		match IMPORTANT_DATA.tab:
			case 0:
				text = f"{IMPORTANT_DATA.radio_signal_spectrum_width} MHz radio signal spectrum width detected"
				self.RadioDrawFrame.customRepaint()
				self.data_action.setText(text)
				self.logger.metrics(message_text=text)
			case 1:
				text = f"Compass deviation - {IMPORTANT_DATA.compass_north_direction} degrees"
				self.CompassDrawFrame.customRepaint()
				self.data_action.setText(text)
				self.logger.metrics(message_text=text)
			case 2:
				text = f"The sensor is broken"
				self.IRDrawFrame.customRepaint()
				self.data_action.setText(text)
				self.logger.fail(message_text=text)
			case 3:
				text = f"{IMPORTANT_DATA.ultrasound_frequency_of_wavefront} Hz ultrasound frequency of wavefront detected"
				self.UltrasoundDrawFrame.customRepaint()
				self.data_action.setText(text)
				self.logger.metrics(message_text=text)
			case 4:
				text = f"{IMPORTANT_DATA.link_signal_strength} Hz link quality detected"
				self.FreeChannelDrawFrame.customRepaint()
				self.data_action.setText(text)
				self.logger.metrics(message_text=text)
			case 5:
				text = f"{IMPORTANT_DATA.stethoscope_sound_frequency} Hz stethoscope frequency detected"
				self.StethoscopeDrawFrame.customRepaint()
				self.data_action.setText(text)
				self.logger.metrics(message_text=text)
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def detect_update_data_error_signal(self, error: str) -> None:
		"""
		The method that is triggered after the data has been failed received.
		"""
		self.logger.fail(message_text=error)
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def buttDisconnect_clicked(self) -> None:
		"""
		The method that is executed after the Disconnect button is clicked.
		"""
		if not self.buttDisconnect.trouble:
			self.detector.stop()

	def detect_stopping_signal(self) -> None:
		"""
		The method that is triggered after a successful disconnection.
		"""
		self.detector.terminate()
		self.clearWidget()
		self.tray_menu.removeAction(self.disconnect_action)
		self.tray_menu.addAction(self.connect_action)
		IMPORTANT_DATA.IPAddr = "000.000.000.000"
		IMPORTANT_DATA.Port = "00000"
		self.logger.success(message_text=f"DISCONNECT")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
		self.statusbar.showMessage(f"STATUS:\tDISCONNECT")
		self.statusLine.setText("Disconnected")
		self.statusLine.setStyleSheet("color: rgb(200, 0, 0);\nfont: italic;\nfont-size: 18px;")
		self.labelIPaddr.setText(IMPORTANT_DATA.IPAddr)
		self.labelPort.setText(IMPORTANT_DATA.Port)
		self.labelSerialNum.setText(IMPORTANT_DATA.SerialNum)
		self.setWindowTitle(f"{' '.join(self.windowTitle().split(' ')[-3:])}")
		self.tabWidget.setEnabled(False)
		self.groupSettings.setEnabled(False)
		self.buttConnect.trouble = False

	def detect_stopping_error_signal(self, error: str) -> None:
		"""
		The method that is triggered after a failed disconnection.

		:param error: Error message
		"""
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

	def clearWidget(self) -> None:
		"""
		Frame clearing method.
		"""
		self.RadioDrawFrame.customUpdate()
		self.CompassDrawFrame.customUpdate()
		self.IRDrawFrame.customUpdate()
		self.UltrasoundDrawFrame.customUpdate()
		self.FreeChannelDrawFrame.customUpdate()
		self.StethoscopeDrawFrame.customUpdate()

	def frameshotButt_clicked(self) -> None:
		"""
		The method that is called after the Save Frameshot button is clicked.
		"""
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

	def programshotButt_clicked(self) -> None:
		"""
		The method that is called after the Save Programshot button is clicked.
		"""
		self.grab().save(lastIndex("ProgramScreen.png", "{:07}"))
		self.logger.event(message_text=f"Program screenshot saved")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def logshotButt_clicked(self) -> None:
		"""
		The method that is called after the Save Log button is clicked.
		"""
		self.logger.buffer().save("log.html")
		self.logger.event(message_text=f"Log saved")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def tabWidget_Clicked(self, index: int) -> None:
		"""
		The method that is called when one of the tabs is clicked.

		:param index: Tab number
		"""
		match index:
			case 0:
				# Setting texts for the first tab
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
				# Setting texts for the second tab
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
				# Setting texts for the third tab
				IMPORTANT_DATA.tab = index
				IMPORTANT_DATA.text1 = "The sensor is broken"
				# IMPORTANT_DATA.tpixmap1 = "./icon/sinus.png"
				# IMPORTANT_DATA.text1 = "Frequency of wavefront (Hz): "
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
				# Setting texts for the fourth tab
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
				# Setting texts for the fifth tab
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
				# Setting texts for the sixth tab
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

	def ultrasound_Gen(self) -> None:
		"""
		A method that displays the ultrasound generation window.
		"""
		# Unimplemented
		self.us_dialog.show()
		result: int = self.us_dialog.exec()
		match result:
			case QDialogButtonBox.StandardButton.Ok.value:
				self.logger.error(message_text="Unimplemented 'OK'")
			case QDialogButtonBox.StandardButton.Cancel.value:
				self.logger.error(message_text="Unimplemented 'CANCEL'")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
		self.logger.notice(message_text="No ultrasound generation module")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def ultrasound_Play(self) -> None:
		"""
		A method that reproduces the intercepted ultrasound.
		"""
		# Unimplemented
		self.logger.notice(message_text="Unimplemented")
		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])

	def closeEvent(self, event: QCloseEvent) -> None:
		"""
		The program termination logic has been slightly redefined.

		:param event: See the Qt documentation
		"""
		# When the connection is established, the program cannot be terminated!
		# You need to close the connection yourself before terminating the program.
		# Instead of finishing (when the connection is established), the program is minimized to tray.
		if not IMPORTANT_DATA.connect:
			config = ConfigParser()
			config.add_section('Color')
			config.set('Color', 'appearance', IMPORTANT_DATA.appearance)
			config.set('Color', 'accent_color', IMPORTANT_DATA.accent_color)
			with open('data/config.ini', 'w') as config_file:
				config.write(config_file)

			self.serial_dialog.close()
			QApplication.instance().exit(0)
		else:
			self.tray_Show()
			event.ignore()

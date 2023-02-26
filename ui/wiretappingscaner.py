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
# import configparser
# import pickle
# import os
# import keyboard
#
# from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import QApplication,\
# 							QMainWindow,\
# 							QMessageBox,\
# 							QSystemTrayIcon,\
# 							QStyle,\
# 							QMenu
# from PyQt6.QtCore import Qt, QDir
# from PyQt6.QtGui import QIcon, QAction, QCloseEvent

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QStyle, QSystemTrayIcon, QMenu
# from PyQt6.QtCore import QDir
from PyQt6.QtGui import QIcon, QFont, QAction, QKeyEvent, QCloseEvent
from PyQt6.QtCore import QThread, pyqtSignal

from ui.raw.ui_wiretappingscaner import Ui_WindowWiretappingScaner
from ui.ultrasounddialog import UltrasoundDialog

from src.state import Draws


class Detector(QThread):
	data_signal = pyqtSignal(dict)
#
	def __init__(self):
		super(Detector, self).__init__()
		self.wiretapping_data = {"data_radio_signal": 0.0,
								 "data_radio_amplitude": 0,
								 "data_compass_radius": 0,
								 "data_infrared_signal": 0.0,
								 "data_infrared_data": "",
								 "data_ultrasound_signal": 0.0}
#
	def run(self):
		self.detect_signal()
#
	def terminate(self):
		super().terminate()
#
	def detect_signal(self):
		while True:
			self.wiretapping_data["data_radio_signal"] = 101.4
			self.wiretapping_data["data_radio_amplitude"] = 20
			self.wiretapping_data["data_compass_radius"] = 70
			self.wiretapping_data["data_infrared_signal"] = 0.9
			self.wiretapping_data["data_infrared_data"] = "2 (Exit)"
			self.wiretapping_data["data_ultrasound_signal"] = 10778
			self.data_signal.emit(self.wiretapping_data)
			time.sleep(0.3)
			self.wiretapping_data["data_radio_signal"] = 97.5
			self.wiretapping_data["data_radio_amplitude"] = 28
			self.wiretapping_data["data_compass_radius"] = 76
			self.wiretapping_data["data_infrared_signal"] = 17.1
			self.wiretapping_data["data_infrared_data"] = "5 (Clear)"
			self.wiretapping_data["data_ultrasound_signal"] = 96333
			self.data_signal.emit(self.wiretapping_data)
			time.sleep(0.3)


class WiretappingScaner(QMainWindow, Ui_WindowWiretappingScaner):
	def __init__(self):
		super(WiretappingScaner, self).__init__()
		self.setupUi(self)

		# Constant
		self.exit_bool = False

		# Set window to center
		qr = self.frameGeometry()
		qr.moveCenter(self.screen().availableGeometry().center())
		self.move(qr.topLeft())
		Draws.window_height = self.height()
		Draws.window_width = self.width()

		# It's a tracking of button clicks in the window
	# self.checkMouseClick.stateChanged.connect(self.checkMouseClick_Changed)
	# self.checkMouseRelease.stateChanged.connect(self.checkMouseRelease_Changed)
	# self.checkMouseMove.stateChanged.connect(self.checkMouseMove_Changed)
	# self.comboScheme.currentTextChanged.connect(self.comboScheme_CurrentIndexChanged)
		self.tabWidget.tabBarClicked.connect(self.tabWidget_Clicked)
		self.UltrasoundDrawFrame.gen_sound.connect(self.ultrasound_Gen)
		self.UltrasoundDrawFrame.play_sound.connect(self.ultrasound_Play)
	# self.buttResetLogging.clicked.connect(self.buttResetLogging_Clicked)
	# self.buttResetAll.clicked.connect(self.buttResetAll_Clicked)
	# self.buttSaveLoggingAction.clicked.connect(self.buttSaveLoggingAction_Clicked)
	# self.buttSaveLoggingMoving.clicked.connect(self.buttSaveLoggingMoving_Clicked)

		# Initialization of QSystemTrayIcon
		self.tray_icon = QSystemTrayIcon(self)
		self.tray_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon))
		show_action = QAction("Відобразити", self)
		show_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton))
		show_action.triggered.connect(self.tray_Hide)
		radio_action = QAction("Радіо", self)
		radio_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		radio_action.triggered.connect(lambda: self.openTab(0))
		compass_action = QAction("Компас", self)
		compass_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		compass_action.triggered.connect(lambda: self.openTab(1))
		IR_action = QAction("ІЧ випромінювання", self)
		IR_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		IR_action.triggered.connect(lambda: self.openTab(2))
		US_action = QAction("Ультразвук", self)
		US_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		US_action.triggered.connect(lambda: self.openTab(3))
		channel_action = QAction("Вільний канал", self)
		channel_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		channel_action.triggered.connect(lambda: self.openTab(4))
		stethoscope_action = QAction("Стетоскоп", self)
		stethoscope_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
		stethoscope_action.triggered.connect(lambda: self.openTab(5))
		close_action = QAction("Завершити", self)
		close_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton))
		close_action.triggered.connect(self.close)
		tray_menu = QMenu()
		tray_menu.addAction(show_action)
		tray_menu.addAction(radio_action)
		tray_menu.addAction(compass_action)
		tray_menu.addAction(IR_action)
		tray_menu.addAction(US_action)
		tray_menu.addAction(channel_action)
		tray_menu.addAction(stethoscope_action)
		tray_menu.addAction(close_action)
		self.tray_icon.setContextMenu(tray_menu)

		# Initialization of process of tracking
		self.detector = Detector()
		self.detector.start()
		self.detector.data_signal.connect(self.detect_data_signal)

		self.tabWidget_Clicked(0)

	def tray_Show(self):
		self.tray_icon.show()
		self.hide()

	def openTab(self, index):
		self.tray_Hide()
		self.tabWidget.setCurrentIndex(index)
		self.tabWidget_Clicked(index)

	def tray_Hide(self):
		self.tray_icon.hide()
		self.show()
#
# def checkMouseClick_Changed(self):
# 	if self.checkMouseClick.isChecked():
# 		self.checkMouseClickCoord.setEnabled(True)
# 	else:
# 		self.checkMouseClickCoord.setEnabled(False)
#
# def checkMouseRelease_Changed(self):
# 	if self.checkMouseRelease.isChecked():
# 		self.checkMouseReleaseCoord.setEnabled(True)
# 	else:
# 		self.checkMouseReleaseCoord.setEnabled(False)
#
# def checkMouseMove_Changed(self):
# 	if self.checkMouseMove.isChecked():
# 		self.textBrowserLoggingMoving.append(self.printer.start_track_moving_string())
# 	else:
# 		self.textBrowserLoggingMoving.append(self.printer.stop_track_moving_string())
#
# def comboScheme_CurrentIndexChanged(self, new_color_scheme: str, changed: bool = True):
# 	for item in schemes:
# 		if item['SCHEME_NAME'] == new_color_scheme:
# 			self.current_scheme['SCHEME_NAME'] = item['SCHEME_NAME']
# 			self.current_scheme['processing_data'] = item['processing_data']
# 			self.current_scheme['hide_show'] = item['hide_show']
# 			self.current_scheme['color_scheme_change'] = item['color_scheme_change']
# 			self.current_scheme['reboot'] = item['reboot']
# 			self.current_scheme['export'] = item['export']
# 			self.current_scheme['key_pressed'] = item['key_pressed']
# 			self.current_scheme['mouse_clicked'] = item['mouse_clicked']
# 			self.current_scheme['mouse_clicked_coord'] = item['mouse_clicked_coord']
# 			self.current_scheme['mouse_released'] = item['mouse_released']
# 			self.current_scheme['mouse_released_coord'] = item['mouse_released_coord']
# 			self.current_scheme['mouse_scrolled'] = item['mouse_scrolled']
# 			self.current_scheme['mouse_scrolled_coord'] = item['mouse_scrolled_coord']
# 			self.current_scheme['moving_tracking'] = item['moving_tracking']
# 			self.current_scheme['mouse_moved'] = item['mouse_moved']
# 			self.current_scheme['mouse_moved_coord'] = item['mouse_moved_coord']
#
# 			self.printer.reinit(self.current_scheme)
# 			if changed:
# 				self.textBrowserLoggingAction.append(self.printer.change_scheme_string())
# 			break
#
	def tabWidget_Clicked(self, index):
		match index:
			case 0:
				Draws.tab = 0
				font = QFont("JetBrains Mono")
				Draws.tfont = font
				Draws.text1 = "Radio signal (MHz): "
				Draws.text2 = "Radio amplitude: "
				self.RadioDrawFrame.repaint()
			case 1:
				Draws.tab = 1
				font = QFont("Arial")
				Draws.tfont = font
				Draws.tpixmap = "./icon/magnet.png"
				Draws.text1 = "Compass gradus: "
				self.CompassDrawFrame.repaint()
			case 2:
				Draws.tab = 2
				font = QFont("JetBrains Mono")
				Draws.tfont = font
				Draws.text1 = "Infrared signal (THz): "
				Draws.text2 = "Infrared signal data: "
				self.IRDrawFrame.repaint()
			case 3:
				Draws.tab = 3
				font = QFont()
				font.setPointSize(15)
				Draws.tfont = font
				Draws.text1 = "Ultrasound (Hz): "
				self.UltrasoundDrawFrame.repaint()
			case 4:
				Draws.tab = 4
				font = QFont()
				font.setPointSize(20)
				font.setBold(True)
				Draws.tfont = font
				Draws.text1 = "Hello 4"
				self.FreeChannelDrawFrame.repaint()
			case 5:
				Draws.tab = 5
				font = QFont()
				font.setPointSize(25)
				Draws.tfont = font
				Draws.text1 = "Hello 5"
				self.StethoscopeDrawFrame.repaint()

	def ultrasound_Gen(self):
		gen_dialog = UltrasoundDialog()
		gen_dialog.show()
		result: int = gen_dialog.exec()
		match result:
			case QtWidgets.QDialogButtonBox.StandardButton.Ok.value:
				print(1)
			case QtWidgets.QDialogButtonBox.StandardButton.Cancel.value:
				print(2)
			case _:
				print(3)

	def ultrasound_Play(self):
		print(4)
#
# def buttResetLogging_Clicked(self):
# 	self.button_manager.terminate()
# 	self.saveData()
# 	os.remove("data/KeyLog.save")
# 	self.REBOOT = True
# 	self.close()
#
# def buttResetAll_Clicked(self):
# 	self.button_manager.terminate()
# 	os.remove("data/config.ini")
# 	os.remove("data/KeyLog.save")
# 	os.rmdir("data")
# 	self.REBOOT = True
# 	self.close()
#
# def buttSaveLoggingAction_Clicked(self):
# 	with open("key.log", "wt") as save:
# 		save.write(self.textBrowserLoggingAction.toPlainText())
# 		self.textBrowserLoggingAction.append(self.printer.export_action_string())
#
# def buttSaveLoggingMoving_Clicked(self):
# 	with open("mov.log", "wt") as save:
# 		save.write(self.textBrowserLoggingMoving.toPlainText())
# 		self.textBrowserLoggingAction.append(self.printer.export_moving_string())
#
	def detect_data_signal(self, data: dict):
		Draws.radio_signal = data["data_radio_signal"]
		Draws.radio_amplitude = data["data_radio_amplitude"]
		Draws.compass_radius = data["data_compass_radius"]
		Draws.infrared_signal = data["data_infrared_signal"]
		Draws.infrared_data = data["data_infrared_data"]
		Draws.ultrasound_signal = data["data_ultrasound_signal"]
		match Draws.tab:
			case 0:
				self.RadioDrawFrame.repaint()
			case 1:
				self.CompassDrawFrame.repaint()
			case 2:
				self.IRDrawFrame.repaint()
			case 3:
				self.UltrasoundDrawFrame.repaint()
			case 4:
				self.FreeChannelDrawFrame.repaint()
			case 5:
				self.StethoscopeDrawFrame.repaint()

	def keyPressEvent(self, event: QKeyEvent):
		self.exit_bool = (False, True)[event.key() == QtCore.Qt.Key.Key_Shift]

	def closeEvent(self, event: QCloseEvent):
		# Завершение программы должно происходить в трее, а не в системном меню
		# Если программа скрыта, значит доступен трей, а не системное меню
		# Допустимо завершение в системном меню, если нажат shift
		if self.isHidden() or self.exit_bool:
			# Значит можно завершать программу
			self.detector.terminate()
			# event.accept()  # Почему-то не работает
			QApplication.instance().exit(0)
		else:
			# Иначе - скрыть в трей
			self.tray_Show()
			event.ignore()
#
# def saveData(self):
# 	config = configparser.ConfigParser()
# 	config.add_section('Settings')
# 	config.set('Settings', 'tracking_keyboard_click', str(self.checkKeyboardClick.isChecked()))
# 	config.set('Settings', 'tracking_mouse_click', str(self.checkMouseClick.isChecked()))
# 	config.set('Settings', 'tracking_mouse_click_coord', str(self.checkMouseClickCoord.isChecked()))
# 	config.set('Settings', 'tracking_mouse_release', str(self.checkMouseRelease.isChecked()))
# 	config.set('Settings', 'tracking_mouse_release_coord', str(self.checkMouseReleaseCoord.isChecked()))
# 	config.set('Settings', 'tracking_mouse_scroll', str(self.checkMouseScroll.isChecked()))
# 	config.set('Settings', 'tracking_mouse_move', str(self.checkMouseMove.isChecked()))
# 	config.add_section('ColorScheme')
# 	config.set('ColorScheme', 'current_scheme', str(self.comboScheme.currentText()))
# 	with open('data/config.ini', 'w') as config_file:
# 		config.write(config_file)
#
# 	with open("data/KeyLog.save", "wb") as save:
# 		data = [self.textBrowserLoggingAction.toHtml(), self.textBrowserLoggingMoving.toHtml()]
# 		pickle.dump(data, save)

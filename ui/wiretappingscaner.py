#  Copyright © 2022 Kalynovsky Valentin. All rights reserved.
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
# from pynput import keyboard, mouse
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

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
# from PyQt6.QtCore import QDir
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QThread, pyqtSignal

from ui.raw.ui_wiretappingscaner import Ui_WindowWiretappingScaner

from src.state import Draws


class Detector(QThread):
	radio_signal = pyqtSignal(str)
# 	mouse_clicked = pyqtSignal(int, int, str)
# 	mouse_released = pyqtSignal(int, int, str)
# 	mouse_move = pyqtSignal(int, int)
# 	mouse_scroll = pyqtSignal(int, int, int, int)
#
	def __init__(self):
		super(Detector, self).__init__()
# 		self._keyboardListener = keyboard.Listener(on_press=self._keyboard_click)
# 		self._mouseListener = mouse.Listener(on_move=self._mouse_move, on_click=self._mouse_click, on_scroll=self._mouse_scroll)
#
	def run(self):
		self.detect_radio()
		# self._keyboardListener.start()
		# self._mouseListener.start()
#
# 	def terminate(self):
# 		self._keyboardListener.stop()
# 		self._mouseListener.stop()
# 		super().terminate()
#
	def detect_radio(self):
		while True:
			self.radio_signal.emit("101.4")
			time.sleep(0.3)
			self.radio_signal.emit("97.5")
			time.sleep(0.3)
#
# 	def _mouse_move(self, x, y):
# 		self.mouse_move.emit(x, y)
#
# 	def _mouse_click(self, x, y, button, pressed):
# 		if pressed:
# 			self.mouse_clicked.emit(x, y, str(button.name))
# 		else:
# 			self.mouse_released.emit(x, y, str(button.name))
#
# 	def _mouse_scroll(self, x, y, dx, dy):
# 		self.mouse_scroll.emit(x, y, dx, dy)


class WiretappingScaner(QMainWindow, Ui_WindowWiretappingScaner):
	def __init__(self):
		super(WiretappingScaner, self).__init__()
		self.setupUi(self)

		# Set window to center
		qr = self.frameGeometry()
		qr.moveCenter(self.screen().availableGeometry().center())
		self.move(qr.topLeft())

		self.text = "..."

		# It's a tracking of button clicks in the window
	# self.toolTray.clicked.connect(self.toolTray_Clicked)
	# self.checkMouseClick.stateChanged.connect(self.checkMouseClick_Changed)
	# self.checkMouseRelease.stateChanged.connect(self.checkMouseRelease_Changed)
	# self.checkMouseMove.stateChanged.connect(self.checkMouseMove_Changed)
	# self.comboScheme.currentTextChanged.connect(self.comboScheme_CurrentIndexChanged)
		self.tabWidget.tabBarClicked.connect(self.tabRadio_Clicked)
	# self.buttResetLogging.clicked.connect(self.buttResetLogging_Clicked)
	# self.buttResetAll.clicked.connect(self.buttResetAll_Clicked)
	# self.buttSaveLoggingAction.clicked.connect(self.buttSaveLoggingAction_Clicked)
	# self.buttSaveLoggingMoving.clicked.connect(self.buttSaveLoggingMoving_Clicked)

	# # Initialization of QSystemTrayIcon
	# self.toolTray.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))
	# self.tray_icon = QSystemTrayIcon(self)
	# self.tray_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon))
	# show_action = QAction("Show", self)
	# show_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton))
	# show_action.triggered.connect(self.tray_Show)
	# output_action = QAction("Output action to log", self)
	# output_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView))
	# output_action.triggered.connect(self.tray_ActionOutput)
	# output_moving = QAction("Output moving to log", self)
	# output_moving.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView))
	# output_moving.triggered.connect(self.tray_MovingOutput)
	# close_action = QAction("Close", self)
	# close_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton))
	# close_action.triggered.connect(self.tray_Close)
	# tray_menu = QMenu()
	# tray_menu.addAction(show_action)
	# tray_menu.addAction(output_action)
	# tray_menu.addAction(output_moving)
	# tray_menu.addAction(close_action)
	# self.tray_icon.setContextMenu(tray_menu)

		# Initialization of process of tracking
		self.detector = Detector()
		self.detector.start()
		self.detector.radio_signal.connect(self.detect_radio_signal)
		# self.button_manager.mouse_clicked.connect(self.mouse_Clicked)
		# self.button_manager.mouse_released.connect(self.mouse_Released)
		# self.button_manager.mouse_move.connect(self.mouse_Move)
		# self.button_manager.mouse_scroll.connect(self.mouse_Scroll)

		self.tabRadio_Clicked(0)

# def tray_Show(self):
# 	self.tray_icon.hide()
# 	self.show()
# 	self.textBrowserLoggingAction.append(self.printer.show_program_string())
#
# def tray_ActionOutput(self):
# 	self.buttSaveLoggingAction_Clicked()
# 	os.startfile("key.log")
#
# def tray_MovingOutput(self):
# 	self.buttSaveLoggingMoving_Clicked()
# 	os.startfile("mov.log")
#
# def tray_Close(self):
# 	self.tray_Show()
# 	self.close()
#
# def toolTray_Clicked(self):
# 	self.tray_icon.show()
# 	self.hide()
# 	self.textBrowserLoggingAction.append(self.printer.hide_program_string())
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
	def tabRadio_Clicked(self, index):
		match index:
			case 0:
				Draws.tab = 0
				font = QFont("JetBrains Mono")
				Draws.tfont = font
				Draws.text = "Radio signal: "
				self.RadioDrawFrame.repaint()
			case 1:
				Draws.tab = 1
				font = QFont("Arial")
				Draws.tfont = font
				Draws.text = "Hello 1"
				self.CompassDrawFrame.repaint()
			case 2:
				Draws.tab = 2
				font = QFont("Times")
				Draws.tfont = font
				Draws.text = "Hello 2"
				self.IRDrawFrame.repaint()
			case 3:
				Draws.tab = 3
				font = QFont()
				font.setPointSize(15)
				Draws.tfont = font
				Draws.text = "Hello 3"
				self.UltrasoundDrawFrame.repaint()
			case 4:
				Draws.tab = 4
				font = QFont()
				font.setPointSize(20)
				font.setBold(True)
				Draws.tfont = font
				Draws.text = "Hello 4"
				self.FreeChannelDrawFrame.repaint()
			case 5:
				Draws.tab = 5
				font = QFont()
				font.setPointSize(25)
				Draws.tfont = font
				Draws.text = "Hello 5"
				self.StethoscopeDrawFrame.repaint()
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
	def detect_radio_signal(self, data_radio_signal: str):
		Draws.radio_signal = data_radio_signal
		self.RadioDrawFrame.repaint()
#
# def mouse_Clicked(self, x: int, y: int, button: str):
# 	if self.checkMouseClick.isChecked():
# 		if self.checkMouseClickCoord.isChecked():
# 			self.textBrowserLoggingAction.append(self.printer.mouse_click_coord_string(x, y, button))
# 		else:
# 			self.textBrowserLoggingAction.append(self.printer.mouse_click_string(button))
#
# def mouse_Released(self, x: int, y: int, button: str):
# 	if self.checkMouseRelease.isChecked():
# 		if self.checkMouseReleaseCoord.isChecked():
# 			self.textBrowserLoggingAction.append(self.printer.mouse_release_coord_string(x, y, button))
# 		else:
# 			self.textBrowserLoggingAction.append(self.printer.mouse_release_string(button))
#
# def mouse_Move(self, x: int, y: int):
# 	if self.checkMouseMove.isChecked():
# 		self.textBrowserLoggingMoving.append(self.printer.mouse_move_string(x, y))
#
# def mouse_Scroll(self, x: int, y: int, dx: int, dy: int):
# 	if self.checkMouseScroll.isChecked():
# 		self.textBrowserLoggingAction.append(self.printer.mouse_scroll_string(x, y, dx, dy))
#
# def closeEvent(self, event: QCloseEvent):
# 	self.textBrowserLoggingAction.append(self.printer.stop_track_string())
# 	self.button_manager.terminate()
# 	# Saving
# 	if not self.REBOOT:
# 		self.saveData()
# 	# Closing
# 	super().closeEvent(event)
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

"""
An experimental training ground for a set of practices for adapting
to the conditions of the absence of Qt Designer.
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

from PyQt6.QtWidgets import QApplication,        QMainWindow,         QHBoxLayout, QVBoxLayout, QGridLayout,        QSizePolicy,        QSpacerItem,        QToolButton, QPushButton,         QComboBox, QSpinBox, QCheckBox, QLineEdit, QLabel, QDial,           QGroupBox,            QTabWidget, QScrollArea, QFrame,           QTextBrowser,            QWidget, QStatusBar, QDockWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QKeySequence

from ui.qsrc.drawFrame import DrawFrame
from ui.qsrc.inactiveButton import InactiveButton

from src.state import IMPORTANT_DATA

class WiretappingScaner(QMainWindow):
	"""
	Class with the interface and logic of the main program window.
	"""

	def __init__(self):
		super(WiretappingScaner, self).__init__()

		# Central widget of window
		font = QFont()
		font.setPointSize(10)

		h_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
		v_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

		# =====
		# =======
		# =========
		# ===========
		#  Central widget of window
		# ===========
		# =========
		# =======
		# =====
		# =====
		# =======
		# =========
		#  Правая половина окна
		# =========
		# =======
		# =====
		# =====
		# =======
		#  Верхняя панель tool кнопок
		# =======
		# =====
		self.serialTool = QToolButton()
		self.serialTool.setIcon(QIcon("./icon/serial_monitor.png"))
		self.serialTool.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.serialTool.setMinimumSize(QSize(32, 32))
		self.serialTool.setMaximumSize(QSize(32, 32))
		self.serialTool.setFont(font)
		self.serialTool.setText("Serial monitor")
		self.serialTool.setToolTip("Serial monitor")
		self.serialTool.setIconSize(QSize(30, 30))
		self.serialTool.setCheckable(True)

		self.uploadTool = QToolButton()
		self.uploadTool.setIcon(QIcon("./icon/upload.png"))
		self.uploadTool.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.uploadTool.setMinimumSize(QSize(32, 32))
		self.uploadTool.setMaximumSize(QSize(32, 32))
		self.uploadTool.setFont(font)
		self.uploadTool.setText("Upload")
		self.uploadTool.setToolTip("Upload")
		self.uploadTool.setIconSize(QSize(30, 30))
		self.uploadTool.setCheckable(True)

		self.serial_layout = QHBoxLayout()
		self.serial_layout.addItem(h_spacer)
		self.serial_layout.addWidget(self.serialTool)
		self.serial_layout.addWidget(self.uploadTool)

		self.first_line = QFrame()
		self.first_line.setFrameShape(QFrame.Shape.HLine)
		self.first_line.setFrameShadow(QFrame.Shadow.Sunken)

		# =====
		# =======
		#  GroupBox
		# =======
		# =====
		# =====
		#  Destination
		# =====
		self.IPBox = QComboBox()
		self.IPBox.setToolTip("IP list")

		self.aboutTool = QToolButton()
		self.aboutTool.setIcon(QIcon("./icon/about.png"))
		self.aboutTool.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.aboutTool.setMinimumSize(QSize(32, 32))
		self.aboutTool.setMaximumSize(QSize(32, 32))
		self.aboutTool.setText("About")
		self.aboutTool.setToolTip("Serial monitor")
		self.aboutTool.setIconSize(QSize(30, 30))
		self.aboutTool.setCheckable(True)

		self.reloadTool = QToolButton()
		self.reloadTool.setIcon(QIcon("./icon/search.png"))
		self.reloadTool.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.reloadTool.setMinimumSize(QSize(32, 32))
		self.reloadTool.setMaximumSize(QSize(32, 32))
		self.reloadTool.setText("Update list")
		self.reloadTool.setToolTip("About program")
		self.reloadTool.setIconSize(QSize(30, 30))

		self.timeoutSpin = QSpinBox()
		self.timeoutSpin.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.timeoutSpin.setMinimumSize(QSize(60, 32))
		self.timeoutSpin.setMaximumSize(QSize(60, 32))
		self.timeoutSpin.setToolTip("Timeout")
		self.timeoutSpin.setStyleSheet(
			"font-size: 16px;"
		)
		self.timeoutSpin.setWrapping(True)
		self.timeoutSpin.setSuffix("s")
		self.timeoutSpin.setMinimum(3)
		self.timeoutSpin.setMaximum(20)
		self.timeoutSpin.setValue(5)

		self.tool_layout = QHBoxLayout()
		self.tool_layout.addWidget(self.aboutTool)
		self.tool_layout.addItem(h_spacer)
		self.tool_layout.addWidget(self.reloadTool)
		self.tool_layout.addWidget(self.timeoutSpin)

		self.IPLine = QLineEdit()
		self.IPLine.setStyleSheet(
			"font-size: 16px;"
		)
		self.IPLine.setMaxLength(15)
		self.IPLine.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		self.IPLine.setPlaceholderText("192.168.XXX.XXX")
		self.IPLine.setClearButtonEnabled(True)

		self.line_after_destination = QFrame()
		self.line_after_destination.setFrameShape(QFrame.Shape.HLine)
		self.line_after_destination.setFrameShadow(QFrame.Shadow.Sunken)

		# =====
		#  Connection
		# =====
		self.buttConnect = InactiveButton()
		self.buttConnect.setText("Connect")
		self.buttConnect.setToolTip("Connect to device")
		self.buttConnect.setStyleSheet(
			"color: rgb(0, 150, 0);\n"
			"font: bold;\n"
			"font-size: 20px;"
		)
		self.buttConnect.setShortcut("Return")
		self.buttConnect.setCheckable(True)
		self.buttConnect.setAutoExclusive(True)

		self.buttDisconnect = InactiveButton()
		self.buttDisconnect.setText("Disconnect")
		self.buttDisconnect.setToolTip("Disconnect from device")
		self.buttDisconnect.setStyleSheet(
			"color: rgb(200, 0, 0);"
			"font: bold;\n"
			"font-size: 20px;"
		)
		self.buttDisconnect.setShortcut("Esc")
		self.buttDisconnect.setCheckable(True)
		self.buttDisconnect.setChecked(True)
		self.buttDisconnect.setAutoExclusive(True)

		self.line_after_connection = QFrame()
		self.line_after_connection.setFrameShape(QFrame.Shape.HLine)
		self.line_after_connection.setFrameShadow(QFrame.Shadow.Sunken)

		# =====
		#  Information
		# =====
		self.statusLine = QLineEdit()
		self.statusLine.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		self.statusLine.setText("Disconnected")
		self.statusLine.setToolTip("Status")
		self.statusLine.setStyleSheet(
			"color: rgb(200, 0, 0);\n"
			"font: italic;\n"
			"font-size: 18px;"
		)
		self.statusLine.setReadOnly(True)

		self.label1 = QLabel()
		self.label1.setText("IP address:")

		self.label_ip_addr = QLabel()
		self.label_ip_addr.setText("000.000.000.000")

		self.address_layout = QHBoxLayout()
		self.address_layout.addWidget(self.label1)
		self.address_layout.addItem(h_spacer)
		self.address_layout.addWidget(self.label_ip_addr)

		self.label2 = QLabel()
		self.label2.setText("Port:")

		self.label_port = QLabel()
		self.label_port.setText("00000")

		self.port_layout = QHBoxLayout()
		self.port_layout.addWidget(self.label2)
		self.port_layout.addItem(h_spacer)
		self.port_layout.addWidget(self.label_port)

		self.label3 = QLabel()
		self.label3.setText("Serial number:")

		self.label_serial_num = QLabel()
		self.label_serial_num.setText("AAAAA-AAA-AAA-AAAA")

		self.serial_num_layout = QHBoxLayout()
		self.serial_num_layout.addWidget(self.label3)
		self.serial_num_layout.addItem(h_spacer)
		self.serial_num_layout.addWidget(self.label_serial_num)

		self.line_after_information = QFrame()
		self.line_after_information.setFrameShape(QFrame.Shape.HLine)
		self.line_after_information.setFrameShadow(QFrame.Shadow.Sunken)

		# =====
		#  Buttons
		# =====
		self.frameshotButt = QPushButton()
		self.frameshotButt.setText("Frameshot")
		self.frameshotButt.setToolTip("Makes the frameshot")

		self.programshotButt = QPushButton()
		self.programshotButt.setText("Programshot")
		self.programshotButt.setToolTip("Makes the programshot")

		self.logshotButt = QPushButton()
		self.logshotButt.setText("Logshot")
		self.logshotButt.setToolTip("Saves the log")
		self.logshotButt.setShortcut("Ctrl+S")

		self.line_after_buttons = QFrame()
		self.line_after_buttons.setFrameShape(QFrame.Shape.HLine)
		self.line_after_buttons.setFrameShadow(QFrame.Shadow.Sunken)

		# =====
		#  Settings
		# =====
		self.checkPlaySound = QCheckBox()
		self.checkPlaySound.setText("Play sound")

		self.checkRemoteMode = QCheckBox()
		self.checkRemoteMode.setText("Remote mode")

		self.line_after_first_main_settings = QFrame()
		self.line_after_first_main_settings.setFrameShape(QFrame.Shape.HLine)
		self.line_after_first_main_settings.setFrameShadow(QFrame.Shadow.Sunken)

		self.main_settings_layout = QVBoxLayout()
		self.main_settings_layout.addWidget(self.checkPlaySound)
		self.main_settings_layout.addWidget(self.checkRemoteMode)
		self.main_settings_layout.addWidget(self.line_after_first_main_settings)
		self.main_settings_layout.addItem(v_spacer)

		self.line_middle_of_settings = QFrame()
		self.line_middle_of_settings.setFrameShape(QFrame.Shape.VLine)
		self.line_middle_of_settings.setFrameShadow(QFrame.Shadow.Sunken)

		self.label4 = QLabel()
		self.label4.setText("Brightness")

		self.dialBrightness = QDial()
		self.dialBrightness.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.dialBrightness.setMinimumSize(QSize(60, 60))
		self.dialBrightness.setMaximumSize(QSize(60, 60))
		self.dialBrightness.setMinimum(0)
		self.dialBrightness.setMaximum(100)
		self.dialBrightness.setValue(80)

		self.brightness_layout = QHBoxLayout()
		self.brightness_layout.addWidget(self.label4)
		self.brightness_layout.addWidget(self.dialBrightness)

		self.line_after_buttons = QFrame()
		self.line_after_buttons.setFrameShape(QFrame.Shape.HLine)
		self.line_after_buttons.setFrameShadow(QFrame.Shadow.Sunken)

		self.additional_settings_layout = QVBoxLayout()
		self.additional_settings_layout.addLayout(self.brightness_layout)
		self.additional_settings_layout.addWidget(self.line_after_buttons)

		self.group_settings_layout = QHBoxLayout()
		self.group_settings_layout.addLayout(self.main_settings_layout)
		self.group_settings_layout.addWidget(self.line_middle_of_settings)
		self.group_settings_layout.addLayout(self.additional_settings_layout)
		self.group_settings = QGroupBox()
		self.group_settings.setTitle("Settings")
		self.group_settings.setLayout(self.group_settings_layout)

		# =====
		#  Сборка интерфейса в один GroupBox
		# =====
		self.connection_scroll_area_widget_contents_layout = QVBoxLayout()
		self.connection_scroll_area_widget_contents_layout.addWidget(self.IPBox)
		self.connection_scroll_area_widget_contents_layout.addLayout(self.tool_layout)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.IPLine)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.line_after_destination)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.buttConnect)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.buttDisconnect)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.line_after_connection)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.statusLine)
		self.connection_scroll_area_widget_contents_layout.addLayout(self.address_layout)
		self.connection_scroll_area_widget_contents_layout.addLayout(self.port_layout)
		self.connection_scroll_area_widget_contents_layout.addLayout(self.serial_num_layout)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.line_after_information)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.frameshotButt)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.programshotButt)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.logshotButt)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.line_after_buttons)
		self.connection_scroll_area_widget_contents_layout.addWidget(self.group_settings)
		self.connection_scroll_area_widget_contents = QWidget()
		self.connection_scroll_area_widget_contents.setLayout(self.connection_scroll_area_widget_contents_layout)
		self.connection_scroll_area = QScrollArea()
		self.connection_scroll_area.setWidgetResizable(True)
		self.connection_scroll_area.setWidget(self.connection_scroll_area_widget_contents)
		self.connection_layout = QVBoxLayout()
		self.connection_layout.addWidget(self.connection_scroll_area)
		self.connectionGroupBox = QGroupBox()
		self.connectionGroupBox.setTitle("Connection")
		self.connectionGroupBox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
		self.connectionGroupBox.setMinimumSize(QSize(340, 370))
		self.connectionGroupBox.setMaximumSize(QSize(340, 16777215))
		self.connectionGroupBox.setFont(font)
		self.connectionGroupBox.setLayout(self.connection_layout)

		# =====
		# =======
		#  Сборка правой половины окна
		# =======
		# =====
		self.right_layout = QVBoxLayout()
		self.right_layout.addLayout(self.serial_layout)
		self.right_layout.addWidget(self.first_line)
		self.right_layout.addWidget(self.connectionGroupBox)

		# =====
		# =======
		# =========
		#  Левая половина окна
		# =========
		# =======
		# =====
		# =====
		#  вкладки
		# =====
		self.RadioDrawFrame = DrawFrame()
		self.RadioDrawFrame.setToolTip("Drawing zone")
		self.RadioDrawFrame.setMinimumSize(800, 600)
		self.RadioDrawFrame.setMaximumSize(800, 600)
		self.RadioDrawFrame.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.RadioDrawFrame.setFrameShape(QFrame.Shape.NoFrame)
		self.radio_scroll_area_widget_contents_layout = QGridLayout()
		self.radio_scroll_area_widget_contents_layout.addWidget(self.RadioDrawFrame)
		self.radio_scroll_area_widget_contents = QWidget()
		self.radio_scroll_area_widget_contents.setLayout(self.radio_scroll_area_widget_contents_layout)
		self.radio_scroll_area = QScrollArea()
		self.radio_scroll_area.setWidgetResizable(True)
		self.radio_scroll_area.setWidget(self.radio_scroll_area_widget_contents)
		self.radio_layout = QVBoxLayout()
		self.radio_layout.addWidget(self.radio_scroll_area)
		self.tabRadio = QWidget()
		self.tabRadio.setToolTip("Radio tab")
		self.tabRadio.setLayout(self.radio_layout)

		self.CompassDrawFrame = DrawFrame()
		self.CompassDrawFrame.setToolTip("Drawing zone")
		self.CompassDrawFrame.setMinimumSize(800, 600)
		self.CompassDrawFrame.setMaximumSize(800, 600)
		self.CompassDrawFrame.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.CompassDrawFrame.setFrameShape(QFrame.Shape.NoFrame)
		self.compass_scroll_area_widget_contents_layout = QGridLayout()
		self.compass_scroll_area_widget_contents_layout.addWidget(self.CompassDrawFrame)
		self.compass_scroll_area_widget_contents = QWidget()
		self.compass_scroll_area_widget_contents.setLayout(self.compass_scroll_area_widget_contents_layout)
		self.compass_scroll_area = QScrollArea()
		self.compass_scroll_area.setWidgetResizable(True)
		self.compass_scroll_area.setWidget(self.compass_scroll_area_widget_contents)
		self.compass_layout = QVBoxLayout()
		self.compass_layout.addWidget(self.compass_scroll_area)
		self.tabCompass = QWidget()
		self.tabCompass.setToolTip("Radio tab")
		self.tabCompass.setLayout(self.compass_layout)

		self.IRDrawFrame = DrawFrame()
		self.IRDrawFrame.setToolTip("Drawing zone")
		self.IRDrawFrame.setMinimumSize(800, 600)
		self.IRDrawFrame.setMaximumSize(800, 600)
		self.IRDrawFrame.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.IRDrawFrame.setFrameShape(QFrame.Shape.NoFrame)
		self.ir_scroll_area_widget_contents_layout = QGridLayout()
		self.ir_scroll_area_widget_contents_layout.addWidget(self.IRDrawFrame)
		self.ir_scroll_area_widget_contents = QWidget()
		self.ir_scroll_area_widget_contents.setLayout(self.ir_scroll_area_widget_contents_layout)
		self.ir_scroll_area = QScrollArea()
		self.ir_scroll_area.setWidgetResizable(True)
		self.ir_scroll_area.setWidget(self.ir_scroll_area_widget_contents)
		self.ir_layout = QVBoxLayout()
		self.ir_layout.addWidget(self.ir_scroll_area)
		self.tabIR = QWidget()
		self.tabIR.setToolTip("Radio tab")
		self.tabIR.setLayout(self.ir_layout)

		self.UltrasoundDrawFrame = DrawFrame()
		self.UltrasoundDrawFrame.setToolTip("Drawing zone")
		self.UltrasoundDrawFrame.setMinimumSize(800, 600)
		self.UltrasoundDrawFrame.setMaximumSize(800, 600)
		self.UltrasoundDrawFrame.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.UltrasoundDrawFrame.setFrameShape(QFrame.Shape.NoFrame)
		self.ultrasound_scroll_area_widget_contents_layout = QGridLayout()
		self.ultrasound_scroll_area_widget_contents_layout.addWidget(self.UltrasoundDrawFrame)
		self.ultrasound_scroll_area_widget_contents = QWidget()
		self.ultrasound_scroll_area_widget_contents.setLayout(self.ultrasound_scroll_area_widget_contents_layout)
		self.ultrasound_scroll_area = QScrollArea()
		self.ultrasound_scroll_area.setWidgetResizable(True)
		self.ultrasound_scroll_area.setWidget(self.ultrasound_scroll_area_widget_contents)
		self.ultrasound_layout = QVBoxLayout()
		self.ultrasound_layout.addWidget(self.ultrasound_scroll_area)
		self.tabUltrasound = QWidget()
		self.tabUltrasound.setToolTip("Radio tab")
		self.tabUltrasound.setLayout(self.ultrasound_layout)

		self.FreeChannelDrawFrame = DrawFrame()
		self.FreeChannelDrawFrame.setToolTip("Drawing zone")
		self.FreeChannelDrawFrame.setMinimumSize(800, 600)
		self.FreeChannelDrawFrame.setMaximumSize(800, 600)
		self.FreeChannelDrawFrame.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.FreeChannelDrawFrame.setFrameShape(QFrame.Shape.NoFrame)
		self.free_channel_scroll_area_widget_contents_layout = QGridLayout()
		self.free_channel_scroll_area_widget_contents_layout.addWidget(self.FreeChannelDrawFrame)
		self.free_channel_scroll_area_widget_contents = QWidget()
		self.free_channel_scroll_area_widget_contents.setLayout(self.free_channel_scroll_area_widget_contents_layout)
		self.free_channel_scroll_area = QScrollArea()
		self.free_channel_scroll_area.setWidgetResizable(True)
		self.free_channel_scroll_area.setWidget(self.free_channel_scroll_area_widget_contents)
		self.free_channel_layout = QVBoxLayout()
		self.free_channel_layout.addWidget(self.free_channel_scroll_area)
		self.tabFreeChannel = QWidget()
		self.tabFreeChannel.setToolTip("Radio tab")
		self.tabFreeChannel.setLayout(self.free_channel_layout)

		self.StethoscopeDrawFrame = DrawFrame()
		self.StethoscopeDrawFrame.setToolTip("Drawing zone")
		self.StethoscopeDrawFrame.setMinimumSize(800, 600)
		self.StethoscopeDrawFrame.setMaximumSize(800, 600)
		self.StethoscopeDrawFrame.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		self.StethoscopeDrawFrame.setFrameShape(QFrame.Shape.NoFrame)
		self.stethoscope_scroll_area_widget_contents_layout = QGridLayout()
		self.stethoscope_scroll_area_widget_contents_layout.addWidget(self.StethoscopeDrawFrame)
		self.stethoscope_scroll_area_widget_contents = QWidget()
		self.stethoscope_scroll_area_widget_contents.setLayout(self.stethoscope_scroll_area_widget_contents_layout)
		self.stethoscope_scroll_area = QScrollArea()
		self.stethoscope_scroll_area.setWidgetResizable(True)
		self.stethoscope_scroll_area.setWidget(self.stethoscope_scroll_area_widget_contents)
		self.stethoscope_layout = QVBoxLayout()
		self.stethoscope_layout.addWidget(self.stethoscope_scroll_area)
		self.tabStethoscope = QWidget()
		self.tabStethoscope.setToolTip("Radio tab")
		self.tabStethoscope.setLayout(self.stethoscope_layout)

		# =====
		#  Сборка TabWidget
		# =====
		self.tab_widget = QTabWidget()
		self.tab_widget.addTab(self.tabRadio, "Radio")
		self.tab_widget.setTabIcon(0, QIcon("./icon/radio.png"))
		self.tab_widget.addTab(self.tabCompass, "Compass")
		self.tab_widget.setTabIcon(1, QIcon("./icon/compass.png"))
		self.tab_widget.addTab(self.tabIR, "IR")
		self.tab_widget.setTabIcon(2, QIcon("./icon/infrared.png"))
		self.tab_widget.addTab(self.tabUltrasound, "US")
		self.tab_widget.setTabIcon(3, QIcon("./icon/ultrasound.png"))
		self.tab_widget.addTab(self.tabFreeChannel, "Link quality")
		self.tab_widget.setTabIcon(4, QIcon("./icon/wifi.png"))
		self.tab_widget.addTab(self.tabStethoscope, "Stethoscope")
		self.tab_widget.setTabIcon(5, QIcon("./icon/stethoscope.png"))
		self.tab_widget.setMinimumSize(430, 410)
		self.tab_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
		font = QFont()
		font.setPointSize(12)
		self.tab_widget.setFont(font)
		self.tab_widget.setCurrentIndex(0)
		self.tab_widget.setIconSize(QSize(30, 30))

		# =====
		# =======
		# =========
		# ===========
		#  Сборка центрального виджета
		# ===========
		# =========
		# =======
		# =====
		self.main_layout = QHBoxLayout()
		self.main_layout.addWidget(self.tab_widget)
		self.main_layout.addLayout(self.right_layout)
		self.central_widget = QWidget()
		self.central_widget.setLayout(self.main_layout)

		# =====
		# =======
		# =========
		# ===========
		#  Status bar of window
		# ===========
		# =========
		# =======
		# =====
		self.statusbar = QStatusBar()

		# =====
		# =======
		# =========
		# ===========
		#  Dock widget of window
		# ===========
		# =========
		# =======
		# =====
		self.console_browser = QTextBrowser()
		self.console_browser.setStyleSheet(
			"background-color: rgb(0, 0, 0);\n"
			"color: rgb(255, 255, 255);"
		)
		self.dock_vertical_layout = QVBoxLayout()
		self.dock_vertical_layout.addWidget(self.console_browser)
		self.dockWidgetContents = QWidget()
		self.dockWidgetContents.setToolTip("Log console")
		self.dockWidgetContents.setLayout(self.dock_vertical_layout)
		self.dock_widget = QDockWidget()
		self.dock_widget.setMinimumSize(800, 150)
		self.dock_widget.setFloating(False)
		self.dock_widget.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
		self.dock_widget.setWindowTitle("Log Console")
		self.dock_widget.setWidget(self.dockWidgetContents)

		# =====
		# =======
		# =========
		# ===========
		#  Program window customization
		# ===========
		# =========
		# =======
		# =====
		self.setCentralWidget(self.central_widget)
		self.setStatusBar(self.statusbar)
		self.addDockWidget(Qt.DockWidgetArea(8), self.dock_widget)
		self.setWindowIcon(QIcon('./icon/wiretapping_scaner.png'))
		self.setWindowTitle("Wiretapping Scaner Client")
		self.setMinimumSize(800, 600)
		self.setWindowModality(Qt.WindowModality.NonModal)

		# Set window to center
		qr = self.frameGeometry()
		qr.moveCenter(self.screen().availableGeometry().center())
		self.move(qr.topLeft())
		self.statusbar.showMessage(f"STATUS\tDISCONNECT")
		IMPORTANT_DATA.window_height = self.height()
		IMPORTANT_DATA.window_width = self.width()

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	ui = WiretappingScaner()
	ui.show()
	sys.exit(app.exec())


#
# from markdown_it import MarkdownIt
# from mighty_logger import Logger
#
# from PyQt6.QtWidgets import QApplication, QMainWindow, QStyle, QSystemTrayIcon, QMenu, QMessageBox, QDialogButtonBox
# from PyQt6.QtCore import QRegularExpression, Qt
# from PyQt6.QtGui import QRegularExpressionValidator, QIcon, QFont, QAction, QCloseEvent, QFontDatabase
#
# from ui.raw.ui_wiretappingscaner import Ui_WindowWiretappingScaner
# from ui.qsrc.detector import Detector
# from ui.qsrc.serialDialog import SerialDialog
# from ui.qsrc.uploadDialog import UploadDialog
# from ui.qsrc.usDialog import UltrasoundDialog
# from src.get_hosts import getHost
# from src.search_algorithms import lastIndex
#
#
# class WiretappingScaner(QMainWindow, Ui_WindowWiretappingScaner):
# 	"""
# 	Class with the interface and logic of the main program window.
# 	"""
#
# 	def __init__(self):
# 		super(WiretappingScaner, self).__init__()
# 		self.setupUi(self)
#

#
# 		# Icons setting
# 		self.setWindowIcon(QIcon('./icon/wiretapping_scaner.png'))



#
# 		# It's creating a validator for the input field of the list of ports
# 		self.IPLine.setValidator(
# 			QRegularExpressionValidator(
# 				QRegularExpression(
# 					r"^192\.168\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
# 				), self
# 			)
# 		)
#
# 		# Setting service font
# 		QFontDatabase.addApplicationFont("/font/fixedsys.ttf")
# 		self.font = QFont("fixedsys", 13)
# 		self.consoleBrowser.setFont(self.font)
# 		IMPORTANT_DATA.tfont = self.font
#
# 		# It's a tracking of button clicks in the window
# 		self.reloadTool.clicked.connect(self.reloadTool_clicked)
# 		self.aboutTool.clicked.connect(self.aboutTool_clicked)
# 		self.buttConnect.clicked.connect(self.buttConnect_clicked)
# 		self.buttDisconnect.clicked.connect(self.buttDisconnect_clicked)
# 		self.buttWidgetScreenshot.clicked.connect(self.buttWidgetScreenshot_clicked)
# 		self.buttProgramScreenshot.clicked.connect(self.buttProgramScreenshot_clicked)
# 		self.buttSaveLog.clicked.connect(self.buttSaveLog_clicked)
# 		self.tabWidget.tabBarClicked.connect(self.tabWidget_Clicked)
# 		self.UltrasoundDrawFrame.gen_sound.connect(self.ultrasound_Gen)
# 		self.UltrasoundDrawFrame.play_sound.connect(self.ultrasound_Play)
# 		self.serialTool.clicked.connect(self.serialTool_clicked)
# 		self.uploadTool.clicked.connect(self.uploadTool_clicked)
#
# 		# Initialization of QSystemTrayIcon
# 		self.tray_icon = QSystemTrayIcon(self)
# 		self.tray_icon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon))
# 		show_action = QAction("Show", self)
# 		show_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton))
# 		show_action.triggered.connect(self.tray_Hide)
# 		# todo добавить кнопку с отображением данных
# 		tray_menu = QMenu()
# 		tray_menu.addAction(show_action)
# 		self.tray_icon.setContextMenu(tray_menu)
#
# 		# Initialization of Logger
# 		self.logger = Logger(program_name="WiretappingScaner", status_message_global_entry=False, log_environment="html")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 		# Initialization of process of tracking
# 		self.detector = Detector()
# 		self.detector.starting_signal.connect(self.detect_starting_signal)
# 		self.detector.starting_error_signal.connect(self.detect_starting_error_signal)
# 		self.detector.update_data_signal.connect(self.detect_update_data_signal)
# 		self.detector.update_data_error_signal.connect(self.detect_update_data_error_signal)
# 		self.detector.stopping_signal.connect(self.detect_stopping_signal)
# 		self.detector.stopping_error_signal.connect(self.detect_stopping_error_signal)
#
# 		# Initialization of dialog windows
# 		self.serial_dialog = SerialDialog()
# 		self.upload_dialog = UploadDialog()
# 		self.us_dialog = UltrasoundDialog()
#
# 		# Tab selection simulation - start renderer
# 		# (without this, the program refuses to work after the connection)
# 		self.tabWidget_Clicked(0)
#
# 		# Canceled again...
# 		self.tabWidget.setTabVisible(5, False)
#
# 	def tray_Show(self) -> None:
# 		"""
# 		The method minimizes the program to tray.
# 		"""
# 		self.tray_icon.show()
# 		self.hide()
# 		self.logger.user(message_text="Program closed to tray")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 	def tray_Hide(self) -> None:
# 		"""
# 		The method maximizes the program from the tray.
# 		"""
# 		self.tray_icon.hide()
# 		self.show()
# 		self.logger.user(message_text="Program opened from tray")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 	def serialTool_clicked(self) -> None:
# 		"""
# 		The method displays the COM port monitoring dialog box.
# 		"""
# 		if self.serialTool.isChecked():
# 			self.serial_dialog.show()
# 		else:
# 			self.serial_dialog.hide()
#
# 	def uploadTool_clicked(self) -> None:
# 		"""
# 		The method displays the flashing ESP32 dialog.
# 		"""
# 		if self.uploadTool.isChecked():
# 			# self.upload_dialog.show()
# 			warn = QMessageBox()
# 			warn.setWindowTitle("Problem tools")
# 			warn.setWindowIcon(QIcon("./icon/upload.png"))
# 			warn.setIcon(QMessageBox.Icon.Critical)
# 			warn.setText("<font size=14 color='red'>Error...</font>")
# 			warn.setInformativeText(
# 				"<font color='darkred'>The esptools library requires the Visual Studio development tools, which developers do not have - development stopped...</font>")
# 			warn.setStandardButtons(QMessageBox.StandardButton.Cancel)
# 			ret: int = warn.exec()
# 			match ret:
# 				case QMessageBox.StandardButton.Cancel:
# 					return
# 		else:
# 			# self.upload_dialog.close()
# 			pass
#
# 	def aboutTool_clicked(self) -> None:
# 		"""
# 		The method displays information about the program.
# 		"""
# 		with open('About.md', 'r') as f:
# 			text = f.read()
# 			md = MarkdownIt()
# 			html = md.render(text)
#
# 		about_program_container = QMessageBox()
# 		about_program_container.setWindowIcon(QIcon("./icon/about.png"))
# 		about_program = QMessageBox()
# 		about_program.about(about_program_container, "About program", html)
#
# 		self.logger.user(message_text="Viewed information about the program")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 	def reloadTool_clicked(self) -> None:
# 		"""
# 		The method responsible for running and processing the results of Nmap.
# 		"""
# 		if IMPORTANT_DATA.connect:
# 			self.logger.fail(message_text="Can't use Nmap while connected")
# 			self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
# 			return
# 		self.IPBox.clear()
# 		wait = QMessageBox()
# 		wait.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint)
# 		wait.setModal(True)
# 		wait.setWindowTitle("Information")
# 		wait.setIcon(QMessageBox.Icon.Information)
# 		wait.setText("<font size=14>Please wait...</font>")
# 		wait.setInformativeText("The process of determining the static IP addresses of the local network is in progress")
# 		wait.setStandardButtons(QMessageBox.StandardButton.NoButton)
# 		wait.show()
# 		QApplication.processEvents()
#
# 		result, hosts_list, error = getHost(self.timeoutSpin.value())
# 		if result:
# 			for i in hosts_list:
# 				self.IPBox.addItem(f"IP {i[0]} (MAC {i[1]})")
# 			self.reloadTool.setIcon(QIcon("./icon/reload.png"))
# 		else:
# 			err = QMessageBox()
# 			err.setWindowTitle("Error")
# 			err.setWindowIcon(QIcon("./icon/wiretapping_scaner.png"))
# 			err.setIcon(QMessageBox.Icon.Critical)
# 			err.setText("<font size=14 color='red'>Error...</font>")
# 			err.setInformativeText(f"<font color='darkred'>{error}</font>")
# 			err.setStandardButtons(QMessageBox.StandardButton.Cancel)
# 			ret: int = err.exec()
# 			match ret:
# 				case QMessageBox.StandardButton.Cancel:
# 					self.logger.error(message_text=error)
# 					self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
# 		wait.close()
#
# 	def buttConnect_clicked(self) -> None:
# 		"""
# 		The method that is executed after the Connect button is clicked.
# 		"""
# 		if not self.buttConnect.trouble:
# 			if self.IPLine.text() == "":
# 				if self.IPBox.count() == 0:
# 					raise ConnectionError("IP address is not specified")
# 				else:
# 					self.IPLine.setText(self.IPBox.currentText().split(" ")[1])
# 			IMPORTANT_DATA.IPAddr = self.IPLine.text()
# 			IMPORTANT_DATA.Port = "12556"
# 			self.detector.set_ip(self.IPLine.text())
# 			self.detector.start()  # Starts the process of connecting to the Detector and receiving data
#
# 	def detect_starting_signal(self) -> None:
# 		"""
# 		The method that is triggered after a successful connection.
# 		"""
# 		self.logger.success(message_text=f"CONNECT to {IMPORTANT_DATA.IPAddr}:{IMPORTANT_DATA.Port}")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
# 		self.statusbar.showMessage(f"STATUS:\tCONNECT to {IMPORTANT_DATA.IPAddr}:{IMPORTANT_DATA.Port}")
# 		self.statusLine.setText("Connected")
# 		self.statusLine.setStyleSheet("color: rgb(0, 150, 0);\nfont: italic;\nfont-size: 18px;")
# 		self.labelIPaddr.setText(IMPORTANT_DATA.IPAddr)
# 		self.labelPort.setText(IMPORTANT_DATA.Port)
# 		self.labelSerialNum.setText(IMPORTANT_DATA.SerialNum)
# 		self.setWindowTitle(f"{IMPORTANT_DATA.IPAddr} Server : {self.windowTitle()}")
# 		self.tabWidget.setEnabled(True)
# 		self.groupSettings.setEnabled(True)
# 		self.buttDisconnect.trouble = False
#
# 	def detect_starting_error_signal(self, error: str) -> None:
# 		"""
# 		The method that is triggered after a failed connection.
#
# 		:param error: Error message
# 		"""
# 		err = QMessageBox()
# 		err.setWindowTitle("Error")
# 		err.setWindowIcon(QIcon("./icon/wiretapping_scaner.png"))
# 		err.setIcon(QMessageBox.Icon.Warning)
# 		err.setText("<font size=14 color='red'>Error...</font>")
# 		err.setInformativeText(f"<font color='darkred'>{error}</font>")
# 		err.setStandardButtons(QMessageBox.StandardButton.Cancel)
# 		ret: int = err.exec()
# 		match ret:
# 			case QMessageBox.StandardButton.Cancel:
# 				self.logger.fail(message_text=error)
# 				self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
# 		self.buttDisconnect.trouble = True
# 		self.buttDisconnect.click()
#
# 	def detect_update_data_signal(self) -> None:
# 		"""
# 		The method that is triggered after the data has been successfully received.
# 		"""
# 		match IMPORTANT_DATA.tab:
# 			case 0:
# 				self.RadioDrawFrame.customRepaint()
# 				self.logger.metrics(message_text=f"{IMPORTANT_DATA.radio_signal_spectrum_width} MHz radio signal spectrum width detected")
# 			case 1:
# 				self.CompassDrawFrame.customRepaint()
# 				self.logger.metrics(message_text=f"Compass deviation - {IMPORTANT_DATA.compass_north_direction} degrees")
# 			case 2:
# 				self.IRDrawFrame.customRepaint()
# 				self.logger.fail(message_text=f"The sensor is broken")
# 			case 3:
# 				self.UltrasoundDrawFrame.customRepaint()
# 				self.logger.metrics(message_text=f"{IMPORTANT_DATA.ultrasound_frequency_of_wavefront} Hz ultrasound frequency of wavefront detected")
# 			case 4:
# 				self.FreeChannelDrawFrame.customRepaint()
# 				self.logger.metrics(message_text=f"{IMPORTANT_DATA.link_signal_strength} Hz link quality detected")
# 			case 5:
# 				self.StethoscopeDrawFrame.customRepaint()
# 				self.logger.metrics(message_text=f"{IMPORTANT_DATA.stethoscope_sound_frequency} Hz stethoscope frequency detected")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 	def detect_update_data_error_signal(self, error: str) -> None:
# 		"""
# 		The method that is triggered after the data has been failed received.
# 		"""
# 		self.logger.fail(message_text=error)
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 	def buttDisconnect_clicked(self) -> None:
# 		"""
# 		The method that is executed after the Disconnect button is clicked.
# 		"""
# 		if not self.buttDisconnect.trouble:
# 			self.detector.stop()
#
# 	def detect_stopping_signal(self) -> None:
# 		"""
# 		The method that is triggered after a successful disconnection.
# 		"""
# 		self.detector.terminate()
# 		self.clearWidget()
# 		IMPORTANT_DATA.IPAddr = "000.000.000.000"
# 		IMPORTANT_DATA.Port = "00000"
# 		self.logger.success(message_text=f"DISCONNECT")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
# 		self.statusbar.showMessage(f"STATUS:\tDISCONNECT")
# 		self.statusLine.setText("Disconnected")
# 		self.statusLine.setStyleSheet("color: rgb(200, 0, 0);\nfont: italic;\nfont-size: 18px;")
# 		self.labelIPaddr.setText(IMPORTANT_DATA.IPAddr)
# 		self.labelPort.setText(IMPORTANT_DATA.Port)
# 		self.labelSerialNum.setText(IMPORTANT_DATA.SerialNum)
# 		self.setWindowTitle(f"{' '.join(self.windowTitle().split(' ')[-3:])}")
# 		self.tabWidget.setEnabled(False)
# 		self.groupSettings.setEnabled(False)
# 		self.buttConnect.trouble = False
#
# 	def detect_stopping_error_signal(self, error: str) -> None:
# 		"""
# 		The method that is triggered after a failed disconnection.
#
# 		:param error: Error message
# 		"""
# 		err = QMessageBox()
# 		err.setWindowTitle("Error")
# 		err.setWindowIcon(QIcon("./icon/wiretapping_scaner.png"))
# 		err.setIcon(QMessageBox.Icon.Warning)
# 		err.setText("<font size=14 color='red'>Error...</font>")
# 		err.setInformativeText(f"<font color='darkred'>{error}</font>")
# 		err.setStandardButtons(QMessageBox.StandardButton.Cancel)
# 		ret: int = err.exec()
# 		match ret:
# 			case QMessageBox.StandardButton.Cancel:
# 				self.logger.fail(message_text=error)
# 				self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
# 		self.buttConnect.trouble = True
# 		self.buttConnect.click()
#
# 	def clearWidget(self) -> None:
# 		"""
# 		Frame clearing method.
# 		"""
# 		self.RadioDrawFrame.customUpdate()
# 		self.CompassDrawFrame.customUpdate()
# 		self.IRDrawFrame.customUpdate()
# 		self.UltrasoundDrawFrame.customUpdate()
# 		self.FreeChannelDrawFrame.customUpdate()
# 		self.StethoscopeDrawFrame.customUpdate()
#
# 	def buttWidgetScreenshot_clicked(self) -> None:
# 		"""
# 		The method that is called after the Save Frameshot button is clicked.
# 		"""
# 		match IMPORTANT_DATA.tab:
# 			case 0:
# 				self.RadioDrawFrame.grab().save(lastIndex("RadioDrawFrameScreen.png", "{:07}"))
# 			case 1:
# 				self.CompassDrawFrame.grab().save(lastIndex("CompassDrawFrameScreen.png", "{:07}"))
# 			case 2:
# 				self.IRDrawFrame.grab().save(lastIndex("IRDrawFrameScreen.png", "{:07}"))
# 			case 3:
# 				self.UltrasoundDrawFrame.grab().save(lastIndex("UltrasoundDrawFrameScreen.png", "{:07}"))
# 			case 4:
# 				self.FreeChannelDrawFrame.grab().save(lastIndex("FreeChannelDrawFrameScreen.png", "{:07}"))
# 			case 5:
# 				self.StethoscopeDrawFrame.grab().save(lastIndex("StethoscopeDrawFrameScreen.png", "{:07}"))
# 		self.logger.event(message_text=f"Widget screenshot saved")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 	def buttProgramScreenshot_clicked(self) -> None:
# 		"""
# 		The method that is called after the Save Programshot button is clicked.
# 		"""
# 		self.grab().save(lastIndex("ProgramScreen.png", "{:07}"))
# 		self.logger.event(message_text=f"Program screenshot saved")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 	def buttSaveLog_clicked(self) -> None:
# 		"""
# 		The method that is called after the Save Log button is clicked.
# 		"""
# 		self.logger.buffer().save("log.html")
# 		self.logger.event(message_text=f"Log saved")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 	def tabWidget_Clicked(self, index: int) -> None:
# 		"""
# 		The method that is called when one of the tabs is clicked.
#
# 		:param index: Tab number
# 		"""
# 		match index:
# 			case 0:
# 				# Setting texts for the first tab
# 				IMPORTANT_DATA.tab = index
# 				IMPORTANT_DATA.tpixmap1 = "./icon/pulse.png"
# 				IMPORTANT_DATA.text1 = "Radio impulse (s): "
# 				IMPORTANT_DATA.tpixmap2 = "./icon/wave.png"
# 				IMPORTANT_DATA.text2 = "Signal noise (dB): "
# 				IMPORTANT_DATA.tpixmap3 = "./icon/spectrum_width.png"
# 				IMPORTANT_DATA.text3 = "Signal Spectrum Width (Hz): "
# 				IMPORTANT_DATA.tpixmap4 = "./icon/signal_duration.png"
# 				IMPORTANT_DATA.text4 = "Signal duration (s): "
# 				IMPORTANT_DATA.tpixmap5 = "./icon/transfer_rate.png"
# 				IMPORTANT_DATA.text5 = "Transfer rate (bps): "
# 				IMPORTANT_DATA.tpixmap6 = "./icon/fork.png"
# 				IMPORTANT_DATA.text6 = "Antenna impedance (Ω): "
# 				IMPORTANT_DATA.tpixmap7 = "./icon/direction.png"
# 				IMPORTANT_DATA.text7 = "Antenna directivity (dBi): "
# 				IMPORTANT_DATA.tpixmap8 = "./icon/signal_strength_0.png"
# 				IMPORTANT_DATA.text8 = "Signal strength (dB): "
# 				self.RadioDrawFrame.customRepaint()
# 			case 1:
# 				# Setting texts for the second tab
# 				IMPORTANT_DATA.tab = index
# 				IMPORTANT_DATA.tpixmap1 = "./icon/magnet.png"
# 				IMPORTANT_DATA.text1 = "A magnetic field (μT): "
# 				IMPORTANT_DATA.tpixmap2 = "./icon/angle.png"
# 				IMPORTANT_DATA.text2 = "Tilt angle (°): "
# 				IMPORTANT_DATA.tpixmap3 = "./icon/north_direction.png"
# 				IMPORTANT_DATA.text3 = "North direction (°): "
# 				IMPORTANT_DATA.tpixmap4 = "./icon/field_strength.png"
# 				IMPORTANT_DATA.text4 = "Field strength (A/m): "
# 				IMPORTANT_DATA.tpixmap5 = "./icon/temperature.png"
# 				IMPORTANT_DATA.text5 = "Temperature (°C): "
# 				self.CompassDrawFrame.customRepaint()
# 			case 2:
# 				# Setting texts for the third tab
# 				IMPORTANT_DATA.tab = index
# 				IMPORTANT_DATA.text1 = "The sensor is broken"
# 				# IMPORTANT_DATA.tpixmap1 = "./icon/sinus.png"
# 				# IMPORTANT_DATA.text1 = "Frequency of wavefront (Hz): "
# 				# IMPORTANT_DATA.tpixmap2 = "./icon/wavelength.png"
# 				# IMPORTANT_DATA.text2 = "Wavelength (μm): "
# 				# IMPORTANT_DATA.tpixmap3 = "./icon/signal_strength_0.png"
# 				# IMPORTANT_DATA.text3 = "Signal strength (dB): "
# 				# IMPORTANT_DATA.tpixmap4 = "./icon/signal_power.png"
# 				# IMPORTANT_DATA.text4 = "Signal power (dBm): "
# 				# IMPORTANT_DATA.tpixmap5 = "./icon/angle.png"
# 				# IMPORTANT_DATA.text5 = "Reception angle (°): "
# 				# IMPORTANT_DATA.tpixmap6 = "./icon/transfer_rate.png"
# 				# IMPORTANT_DATA.text6 = "Transfer rate (bps): "
# 				self.IRDrawFrame.customRepaint()
# 			case 3:
# 				# Setting texts for the fourth tab
# 				IMPORTANT_DATA.tab = index
# 				IMPORTANT_DATA.tpixmap1 = "./icon/sinus.png"
# 				IMPORTANT_DATA.text1 = "Frequency of wavefront (Hz): "
# 				IMPORTANT_DATA.tpixmap2 = "./icon/wavelength.png"
# 				IMPORTANT_DATA.text2 = "Wavelength (mm): "
# 				IMPORTANT_DATA.tpixmap3 = "./icon/signal_strength_0.png"
# 				IMPORTANT_DATA.text3 = "Signal strength (dB): "
# 				IMPORTANT_DATA.tpixmap4 = "./icon/signal_power.png"
# 				IMPORTANT_DATA.text4 = "Signal power (dBm): "
# 				IMPORTANT_DATA.tpixmap5 = "./icon/wave.png"
# 				IMPORTANT_DATA.text5 = "Resolution (mm): "
# 				IMPORTANT_DATA.tpixmap6 = "./icon/transfer_rate.png"
# 				IMPORTANT_DATA.text6 = "Transfer rate (bps): "
# 				self.UltrasoundDrawFrame.customRepaint()
# 			case 4:
# 				# Setting texts for the fifth tab
# 				IMPORTANT_DATA.tab = index
# 				IMPORTANT_DATA.tpixmap1 = "./icon/transfer_rate.png"
# 				IMPORTANT_DATA.text1 = "Transfer rate (bps): "
# 				IMPORTANT_DATA.tpixmap2 = "./icon/spectrum_width.png"
# 				IMPORTANT_DATA.text2 = "Frequency range (Hz): "
# 				IMPORTANT_DATA.tpixmap3 = "./icon/signal_strength_0.png"
# 				IMPORTANT_DATA.text3 = "Signal strength (dB): "
# 				IMPORTANT_DATA.tpixmap4 = "./icon/signal_power.png"
# 				IMPORTANT_DATA.text4 = "Signal power (dBm): "
# 				IMPORTANT_DATA.tpixmap5 = "./icon/wave.png"
# 				IMPORTANT_DATA.text5 = "Signal noise (dBm): "
# 				IMPORTANT_DATA.tpixmap6 = "./icon/spectrum_width.png"
# 				IMPORTANT_DATA.text6 = "Signal Spectrum Width (Hz): "
# 				IMPORTANT_DATA.tpixmap7 = "./icon/interference.png"
# 				IMPORTANT_DATA.text7 = "Interference level (dB): "
# 				IMPORTANT_DATA.tpixmap8 = "./icon/warning.png"
# 				IMPORTANT_DATA.text8 = "Bit error rate (-): "
# 				IMPORTANT_DATA.tpixmap9 = "./icon/engine.png"
# 				IMPORTANT_DATA.text9 = "Transmission power (dBm): "
# 				self.FreeChannelDrawFrame.customRepaint()
# 			case 5:
# 				# Setting texts for the sixth tab
# 				IMPORTANT_DATA.tab = index
# 				IMPORTANT_DATA.tpixmap1 = "./icon/amplitude.png"
# 				IMPORTANT_DATA.text1 = "Sound amplitude (dB): "
# 				IMPORTANT_DATA.tpixmap2 = "./icon/sinus.png"
# 				IMPORTANT_DATA.text2 = "Sound frequency (Hz): "
# 				IMPORTANT_DATA.tpixmap3 = "./icon/sound_pressure.png"
# 				IMPORTANT_DATA.text3 = "Sound pressure (Pa): "
# 				IMPORTANT_DATA.tpixmap4 = "./icon/direction.png"
# 				IMPORTANT_DATA.text4 = "Sound direction (°): "
# 				IMPORTANT_DATA.tpixmap5 = "./icon/transfer_rate.png"
# 				IMPORTANT_DATA.text5 = "Transfer rate (bps): "
# 				self.StethoscopeDrawFrame.customRepaint()
#
# 	def ultrasound_Gen(self) -> None:
# 		"""
# 		A method that displays the ultrasound generation window.
# 		"""
# 		# Unimplemented
# 		self.us_dialog.show()
# 		result: int = self.us_dialog.exec()
# 		match result:
# 			case QDialogButtonBox.StandardButton.Ok.value:
# 				self.logger.error(message_text="Unimplemented 'OK'")
# 			case QDialogButtonBox.StandardButton.Cancel.value:
# 				self.logger.error(message_text="Unimplemented 'CANCEL'")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
# 		self.logger.notice(message_text="No ultrasound generation module")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 	def ultrasound_Play(self) -> None:
# 		"""
# 		A method that reproduces the intercepted ultrasound.
# 		"""
# 		# Unimplemented
# 		self.logger.notice(message_text="Unimplemented")
# 		self.consoleBrowser.append(self.logger.buffer().get_data()[-1])
#
# 	def closeEvent(self, event: QCloseEvent) -> None:
# 		"""
# 		The program termination logic has been slightly redefined.
#
# 		:param event: See the Qt documentation
# 		"""
# 		# When the connection is established, the program cannot be terminated!
# 		# You need to close the connection yourself before terminating the program.
# 		# Instead of finishing (when the connection is established), the program is minimized to tray.
# 		if not IMPORTANT_DATA.connect:
# 			self.serial_dialog.close()
# 			QApplication.instance().exit(0)
# 		else:
# 			self.tray_Show()
# 			event.ignore()

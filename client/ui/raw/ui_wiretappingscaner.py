# Form implementation generated from reading ui file 'WiretappingScaner.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WindowWiretappingScaner(object):
    def setupUi(self, WindowWiretappingScaner):
        WindowWiretappingScaner.setObjectName("WindowWiretappingScaner")
        WindowWiretappingScaner.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WindowWiretappingScaner.sizePolicy().hasHeightForWidth())
        WindowWiretappingScaner.setSizePolicy(sizePolicy)
        WindowWiretappingScaner.setMinimumSize(QtCore.QSize(800, 600))
        WindowWiretappingScaner.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(WindowWiretappingScaner)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(430, 410))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabRadio = QtWidgets.QWidget()
        self.tabRadio.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabRadio.setObjectName("tabRadio")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabRadio)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea1 = QtWidgets.QScrollArea(self.tabRadio)
        self.scrollArea1.setWidgetResizable(True)
        self.scrollArea1.setObjectName("scrollArea1")
        self.scrollAreaWidgetContents1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents1.setGeometry(QtCore.QRect(0, 0, 818, 618))
        self.scrollAreaWidgetContents1.setObjectName("scrollAreaWidgetContents1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.RadioDrawFrame = DrawFrame(self.scrollAreaWidgetContents1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RadioDrawFrame.sizePolicy().hasHeightForWidth())
        self.RadioDrawFrame.setSizePolicy(sizePolicy)
        self.RadioDrawFrame.setMinimumSize(QtCore.QSize(800, 600))
        self.RadioDrawFrame.setMaximumSize(QtCore.QSize(800, 600))
        self.RadioDrawFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.RadioDrawFrame.setLineWidth(1)
        self.RadioDrawFrame.setObjectName("RadioDrawFrame")
        self.gridLayout_2.addWidget(self.RadioDrawFrame, 0, 0, 1, 1)
        self.scrollArea1.setWidget(self.scrollAreaWidgetContents1)
        self.verticalLayout_2.addWidget(self.scrollArea1)
        self.tabWidget.addTab(self.tabRadio, "")
        self.tabCompass = QtWidgets.QWidget()
        self.tabCompass.setObjectName("tabCompass")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabCompass)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea2 = QtWidgets.QScrollArea(self.tabCompass)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setObjectName("scrollArea2")
        self.scrollAreaWidgetContents2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents2.setGeometry(QtCore.QRect(0, 0, 818, 618))
        self.scrollAreaWidgetContents2.setObjectName("scrollAreaWidgetContents2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.CompassDrawFrame = DrawFrame(self.scrollAreaWidgetContents2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CompassDrawFrame.sizePolicy().hasHeightForWidth())
        self.CompassDrawFrame.setSizePolicy(sizePolicy)
        self.CompassDrawFrame.setMinimumSize(QtCore.QSize(800, 600))
        self.CompassDrawFrame.setMaximumSize(QtCore.QSize(800, 600))
        self.CompassDrawFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.CompassDrawFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.CompassDrawFrame.setObjectName("CompassDrawFrame")
        self.gridLayout_4.addWidget(self.CompassDrawFrame, 0, 0, 1, 1)
        self.scrollArea2.setWidget(self.scrollAreaWidgetContents2)
        self.verticalLayout_3.addWidget(self.scrollArea2)
        self.tabWidget.addTab(self.tabCompass, "")
        self.tabIR = QtWidgets.QWidget()
        self.tabIR.setObjectName("tabIR")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabIR)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea3 = QtWidgets.QScrollArea(self.tabIR)
        self.scrollArea3.setWidgetResizable(True)
        self.scrollArea3.setObjectName("scrollArea3")
        self.scrollAreaWidgetContents3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents3.setGeometry(QtCore.QRect(0, 0, 818, 618))
        self.scrollAreaWidgetContents3.setObjectName("scrollAreaWidgetContents3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.IRDrawFrame = DrawFrame(self.scrollAreaWidgetContents3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IRDrawFrame.sizePolicy().hasHeightForWidth())
        self.IRDrawFrame.setSizePolicy(sizePolicy)
        self.IRDrawFrame.setMinimumSize(QtCore.QSize(800, 600))
        self.IRDrawFrame.setMaximumSize(QtCore.QSize(800, 600))
        self.IRDrawFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.IRDrawFrame.setObjectName("IRDrawFrame")
        self.gridLayout_5.addWidget(self.IRDrawFrame, 0, 0, 1, 1)
        self.scrollArea3.setWidget(self.scrollAreaWidgetContents3)
        self.verticalLayout_4.addWidget(self.scrollArea3)
        self.tabWidget.addTab(self.tabIR, "")
        self.tabUltrasound = QtWidgets.QWidget()
        self.tabUltrasound.setObjectName("tabUltrasound")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabUltrasound)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea4 = QtWidgets.QScrollArea(self.tabUltrasound)
        self.scrollArea4.setWidgetResizable(True)
        self.scrollArea4.setObjectName("scrollArea4")
        self.scrollAreaWidgetContents4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents4.setGeometry(QtCore.QRect(0, 0, 818, 618))
        self.scrollAreaWidgetContents4.setObjectName("scrollAreaWidgetContents4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.UltrasoundDrawFrame = DrawFrame(self.scrollAreaWidgetContents4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UltrasoundDrawFrame.sizePolicy().hasHeightForWidth())
        self.UltrasoundDrawFrame.setSizePolicy(sizePolicy)
        self.UltrasoundDrawFrame.setMinimumSize(QtCore.QSize(800, 600))
        self.UltrasoundDrawFrame.setMaximumSize(QtCore.QSize(800, 600))
        self.UltrasoundDrawFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.UltrasoundDrawFrame.setObjectName("UltrasoundDrawFrame")
        self.gridLayout_6.addWidget(self.UltrasoundDrawFrame, 0, 0, 1, 1)
        self.scrollArea4.setWidget(self.scrollAreaWidgetContents4)
        self.verticalLayout_5.addWidget(self.scrollArea4)
        self.tabWidget.addTab(self.tabUltrasound, "")
        self.tabFreeChannel = QtWidgets.QWidget()
        self.tabFreeChannel.setObjectName("tabFreeChannel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabFreeChannel)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea5 = QtWidgets.QScrollArea(self.tabFreeChannel)
        self.scrollArea5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.scrollArea5.setWidgetResizable(True)
        self.scrollArea5.setObjectName("scrollArea5")
        self.scrollAreaWidgetContents5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents5.setGeometry(QtCore.QRect(0, 0, 818, 618))
        self.scrollAreaWidgetContents5.setObjectName("scrollAreaWidgetContents5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.FreeChannelDrawFrame = DrawFrame(self.scrollAreaWidgetContents5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FreeChannelDrawFrame.sizePolicy().hasHeightForWidth())
        self.FreeChannelDrawFrame.setSizePolicy(sizePolicy)
        self.FreeChannelDrawFrame.setMinimumSize(QtCore.QSize(800, 600))
        self.FreeChannelDrawFrame.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FreeChannelDrawFrame.setFont(font)
        self.FreeChannelDrawFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.FreeChannelDrawFrame.setObjectName("FreeChannelDrawFrame")
        self.gridLayout_7.addWidget(self.FreeChannelDrawFrame, 0, 0, 1, 1)
        self.scrollArea5.setWidget(self.scrollAreaWidgetContents5)
        self.verticalLayout_6.addWidget(self.scrollArea5)
        self.tabWidget.addTab(self.tabFreeChannel, "")
        self.tabStethoscope = QtWidgets.QWidget()
        self.tabStethoscope.setObjectName("tabStethoscope")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabStethoscope)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea6 = QtWidgets.QScrollArea(self.tabStethoscope)
        self.scrollArea6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.scrollArea6.setWidgetResizable(True)
        self.scrollArea6.setObjectName("scrollArea6")
        self.scrollAreaWidgetContents6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents6.setGeometry(QtCore.QRect(0, 0, 818, 618))
        self.scrollAreaWidgetContents6.setObjectName("scrollAreaWidgetContents6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.StethoscopeDrawFrame = DrawFrame(self.scrollAreaWidgetContents6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StethoscopeDrawFrame.sizePolicy().hasHeightForWidth())
        self.StethoscopeDrawFrame.setSizePolicy(sizePolicy)
        self.StethoscopeDrawFrame.setMinimumSize(QtCore.QSize(800, 600))
        self.StethoscopeDrawFrame.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StethoscopeDrawFrame.setFont(font)
        self.StethoscopeDrawFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.StethoscopeDrawFrame.setObjectName("StethoscopeDrawFrame")
        self.gridLayout_8.addWidget(self.StethoscopeDrawFrame, 0, 0, 1, 1)
        self.scrollArea6.setWidget(self.scrollAreaWidgetContents6)
        self.verticalLayout_7.addWidget(self.scrollArea6)
        self.tabWidget.addTab(self.tabStethoscope, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.connectionGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectionGroupBox.sizePolicy().hasHeightForWidth())
        self.connectionGroupBox.setSizePolicy(sizePolicy)
        self.connectionGroupBox.setMinimumSize(QtCore.QSize(340, 410))
        self.connectionGroupBox.setMaximumSize(QtCore.QSize(340, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.connectionGroupBox.setFont(font)
        self.connectionGroupBox.setCheckable(False)
        self.connectionGroupBox.setObjectName("connectionGroupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.connectionGroupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea = QtWidgets.QScrollArea(self.connectionGroupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 301, 560))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.IPBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.IPBox.setObjectName("IPBox")
        self.verticalLayout.addWidget(self.IPBox)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.aboutTool = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.aboutTool.setMinimumSize(QtCore.QSize(30, 30))
        self.aboutTool.setMaximumSize(QtCore.QSize(30, 30))
        self.aboutTool.setIconSize(QtCore.QSize(30, 30))
        self.aboutTool.setObjectName("aboutTool")
        self.horizontalLayout1.addWidget(self.aboutTool)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout1.addItem(spacerItem)
        self.reloadTool = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.reloadTool.setMinimumSize(QtCore.QSize(30, 30))
        self.reloadTool.setMaximumSize(QtCore.QSize(30, 30))
        self.reloadTool.setIconSize(QtCore.QSize(30, 30))
        self.reloadTool.setObjectName("reloadTool")
        self.horizontalLayout1.addWidget(self.reloadTool)
        self.timeoutSpin = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.timeoutSpin.setMinimumSize(QtCore.QSize(60, 30))
        self.timeoutSpin.setMaximumSize(QtCore.QSize(60, 30))
        self.timeoutSpin.setStyleSheet("font-size: 16px;")
        self.timeoutSpin.setWrapping(True)
        self.timeoutSpin.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.timeoutSpin.setMinimum(3)
        self.timeoutSpin.setMaximum(20)
        self.timeoutSpin.setProperty("value", 5)
        self.timeoutSpin.setObjectName("timeoutSpin")
        self.horizontalLayout1.addWidget(self.timeoutSpin)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.IPLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.IPLine.setStyleSheet("font-size: 16px;")
        self.IPLine.setMaxLength(15)
        self.IPLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.IPLine.setClearButtonEnabled(True)
        self.IPLine.setObjectName("IPLine")
        self.verticalLayout.addWidget(self.IPLine)
        self.line1 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line1.setObjectName("line1")
        self.verticalLayout.addWidget(self.line1)
        self.verticalLayout1 = QtWidgets.QVBoxLayout()
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.buttConnect = InactiveButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.buttConnect.setFont(font)
        self.buttConnect.setStyleSheet("color: rgb(0, 150, 0);\n"
"font: bold;\n"
"font-size: 20px;")
        self.buttConnect.setCheckable(True)
        self.buttConnect.setAutoExclusive(True)
        self.buttConnect.setObjectName("buttConnect")
        self.verticalLayout1.addWidget(self.buttConnect)
        self.buttDisconnect = InactiveButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.buttDisconnect.setFont(font)
        self.buttDisconnect.setStyleSheet("color: rgb(200, 0, 0);\n"
"font: bold;\n"
"font-size: 20px;")
        self.buttDisconnect.setCheckable(True)
        self.buttDisconnect.setChecked(True)
        self.buttDisconnect.setAutoExclusive(True)
        self.buttDisconnect.setObjectName("buttDisconnect")
        self.verticalLayout1.addWidget(self.buttDisconnect)
        self.verticalLayout.addLayout(self.verticalLayout1)
        self.line2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line2.setObjectName("line2")
        self.verticalLayout.addWidget(self.line2)
        self.statusLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.statusLine.setFont(font)
        self.statusLine.setStyleSheet("color: rgb(200, 0, 0);\n"
"font: italic;\n"
"font-size: 18px;")
        self.statusLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.statusLine.setReadOnly(True)
        self.statusLine.setObjectName("statusLine")
        self.verticalLayout.addWidget(self.statusLine)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.label1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.horizontalLayout2.addWidget(self.label1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout2.addItem(spacerItem1)
        self.labelIPaddr = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelIPaddr.setObjectName("labelIPaddr")
        self.horizontalLayout2.addWidget(self.labelIPaddr)
        self.verticalLayout.addLayout(self.horizontalLayout2)
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label2.setObjectName("label2")
        self.horizontalLayout3.addWidget(self.label2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout3.addItem(spacerItem2)
        self.labelPort = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelPort.setObjectName("labelPort")
        self.horizontalLayout3.addWidget(self.labelPort)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.horizontalLayout4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout4.setObjectName("horizontalLayout4")
        self.label3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label3.setObjectName("label3")
        self.horizontalLayout4.addWidget(self.label3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout4.addItem(spacerItem3)
        self.labelSerialNum = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelSerialNum.setObjectName("labelSerialNum")
        self.horizontalLayout4.addWidget(self.labelSerialNum)
        self.verticalLayout.addLayout(self.horizontalLayout4)
        self.line3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line3.setLineWidth(1)
        self.line3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line3.setObjectName("line3")
        self.verticalLayout.addWidget(self.line3)
        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.buttWidgetScreenshot = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttWidgetScreenshot.sizePolicy().hasHeightForWidth())
        self.buttWidgetScreenshot.setSizePolicy(sizePolicy)
        self.buttWidgetScreenshot.setObjectName("buttWidgetScreenshot")
        self.verticalLayout2.addWidget(self.buttWidgetScreenshot)
        self.buttProgramScreenshot = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttProgramScreenshot.sizePolicy().hasHeightForWidth())
        self.buttProgramScreenshot.setSizePolicy(sizePolicy)
        self.buttProgramScreenshot.setObjectName("buttProgramScreenshot")
        self.verticalLayout2.addWidget(self.buttProgramScreenshot)
        self.buttSaveLog = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttSaveLog.sizePolicy().hasHeightForWidth())
        self.buttSaveLog.setSizePolicy(sizePolicy)
        self.buttSaveLog.setObjectName("buttSaveLog")
        self.verticalLayout2.addWidget(self.buttSaveLog)
        self.verticalLayout.addLayout(self.verticalLayout2)
        self.line4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line4.setObjectName("line4")
        self.verticalLayout.addWidget(self.line4)
        self.groupSettings = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupSettings.setEnabled(False)
        self.groupSettings.setObjectName("groupSettings")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupSettings)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout3 = QtWidgets.QVBoxLayout()
        self.verticalLayout3.setObjectName("verticalLayout3")
        self.checkPlaySound = QtWidgets.QCheckBox(self.groupSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkPlaySound.sizePolicy().hasHeightForWidth())
        self.checkPlaySound.setSizePolicy(sizePolicy)
        self.checkPlaySound.setObjectName("checkPlaySound")
        self.verticalLayout3.addWidget(self.checkPlaySound)
        self.checkRemoteMode = QtWidgets.QCheckBox(self.groupSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkRemoteMode.sizePolicy().hasHeightForWidth())
        self.checkRemoteMode.setSizePolicy(sizePolicy)
        self.checkRemoteMode.setObjectName("checkRemoteMode")
        self.verticalLayout3.addWidget(self.checkRemoteMode)
        self.line6 = QtWidgets.QFrame(self.groupSettings)
        self.line6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line6.setObjectName("line6")
        self.verticalLayout3.addWidget(self.line6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout3.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout3)
        self.line5 = QtWidgets.QFrame(self.groupSettings)
        self.line5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line5.setObjectName("line5")
        self.horizontalLayout_3.addWidget(self.line5)
        self.verticalLayout4 = QtWidgets.QVBoxLayout()
        self.verticalLayout4.setObjectName("verticalLayout4")
        self.horizontalLayout5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout5.setObjectName("horizontalLayout5")
        self.label4 = QtWidgets.QLabel(self.groupSettings)
        self.label4.setObjectName("label4")
        self.horizontalLayout5.addWidget(self.label4)
        self.dialBrightness = QtWidgets.QDial(self.groupSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialBrightness.sizePolicy().hasHeightForWidth())
        self.dialBrightness.setSizePolicy(sizePolicy)
        self.dialBrightness.setMinimumSize(QtCore.QSize(60, 60))
        self.dialBrightness.setMaximumSize(QtCore.QSize(60, 60))
        self.dialBrightness.setMaximum(100)
        self.dialBrightness.setProperty("value", 80)
        self.dialBrightness.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dialBrightness.setObjectName("dialBrightness")
        self.horizontalLayout5.addWidget(self.dialBrightness)
        self.verticalLayout4.addLayout(self.horizontalLayout5)
        self.line7 = QtWidgets.QFrame(self.groupSettings)
        self.line7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line7.setObjectName("line7")
        self.verticalLayout4.addWidget(self.line7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout4.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout4)
        self.verticalLayout.addWidget(self.groupSettings)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.connectionGroupBox)
        WindowWiretappingScaner.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowWiretappingScaner)
        self.statusbar.setObjectName("statusbar")
        WindowWiretappingScaner.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(WindowWiretappingScaner)
        self.dockWidget.setMinimumSize(QtCore.QSize(800, 150))
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.consoleBrowser = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.consoleBrowser.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.consoleBrowser.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.consoleBrowser.setObjectName("consoleBrowser")
        self.verticalLayout_10.addWidget(self.consoleBrowser)
        self.dockWidget.setWidget(self.dockWidgetContents)
        WindowWiretappingScaner.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)

        self.retranslateUi(WindowWiretappingScaner)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WindowWiretappingScaner)

    def retranslateUi(self, WindowWiretappingScaner):
        _translate = QtCore.QCoreApplication.translate
        WindowWiretappingScaner.setWindowTitle(_translate("WindowWiretappingScaner", "Wiretapping Scaner"))
        self.tabRadio.setToolTip(_translate("WindowWiretappingScaner", "Radio tab"))
        self.RadioDrawFrame.setToolTip(_translate("WindowWiretappingScaner", "Drawing zone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRadio), _translate("WindowWiretappingScaner", "Radio"))
        self.tabCompass.setToolTip(_translate("WindowWiretappingScaner", "Compass tab"))
        self.CompassDrawFrame.setToolTip(_translate("WindowWiretappingScaner", "Drawing zone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCompass), _translate("WindowWiretappingScaner", "Compass"))
        self.tabIR.setToolTip(_translate("WindowWiretappingScaner", "Infrared tab"))
        self.IRDrawFrame.setToolTip(_translate("WindowWiretappingScaner", "Drawing zone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIR), _translate("WindowWiretappingScaner", "IR"))
        self.tabUltrasound.setToolTip(_translate("WindowWiretappingScaner", "Ultrasound tab"))
        self.UltrasoundDrawFrame.setToolTip(_translate("WindowWiretappingScaner", "Drawing zone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUltrasound), _translate("WindowWiretappingScaner", "US"))
        self.tabFreeChannel.setToolTip(_translate("WindowWiretappingScaner", "Link quality tab"))
        self.FreeChannelDrawFrame.setToolTip(_translate("WindowWiretappingScaner", "Drawing zone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFreeChannel), _translate("WindowWiretappingScaner", "Link quality"))
        self.tabStethoscope.setToolTip(_translate("WindowWiretappingScaner", "Stethoscope tab"))
        self.StethoscopeDrawFrame.setToolTip(_translate("WindowWiretappingScaner", "Drawing zone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStethoscope), _translate("WindowWiretappingScaner", "Stethoscope"))
        self.connectionGroupBox.setTitle(_translate("WindowWiretappingScaner", "Connection"))
        self.IPBox.setToolTip(_translate("WindowWiretappingScaner", "IP list"))
        self.aboutTool.setToolTip(_translate("WindowWiretappingScaner", "About program"))
        self.aboutTool.setText(_translate("WindowWiretappingScaner", "About"))
        self.reloadTool.setToolTip(_translate("WindowWiretappingScaner", "<html><head/><body><p>Update IP list</p><p><span style=\" color:#ff0000;\">Attention: nmap is required!</span></p></body></html>"))
        self.reloadTool.setText(_translate("WindowWiretappingScaner", "Update list"))
        self.timeoutSpin.setToolTip(_translate("WindowWiretappingScaner", "Timeout"))
        self.timeoutSpin.setSuffix(_translate("WindowWiretappingScaner", " s"))
        self.IPLine.setPlaceholderText(_translate("WindowWiretappingScaner", "192.168.XXX.XXX"))
        self.buttConnect.setToolTip(_translate("WindowWiretappingScaner", "Connect to device"))
        self.buttConnect.setText(_translate("WindowWiretappingScaner", "Connect"))
        self.buttConnect.setShortcut(_translate("WindowWiretappingScaner", "Return"))
        self.buttDisconnect.setToolTip(_translate("WindowWiretappingScaner", "Disconnect from device"))
        self.buttDisconnect.setText(_translate("WindowWiretappingScaner", "Disconnect"))
        self.buttDisconnect.setShortcut(_translate("WindowWiretappingScaner", "Esc"))
        self.statusLine.setToolTip(_translate("WindowWiretappingScaner", "Status"))
        self.statusLine.setText(_translate("WindowWiretappingScaner", "Disconnected"))
        self.label1.setText(_translate("WindowWiretappingScaner", "IP address:"))
        self.labelIPaddr.setText(_translate("WindowWiretappingScaner", "000.000.000.000"))
        self.label2.setText(_translate("WindowWiretappingScaner", "Port:"))
        self.labelPort.setText(_translate("WindowWiretappingScaner", "00000"))
        self.label3.setText(_translate("WindowWiretappingScaner", "Serial number:"))
        self.labelSerialNum.setText(_translate("WindowWiretappingScaner", "AAAAA-AAA-AAA-AAAA"))
        self.buttWidgetScreenshot.setToolTip(_translate("WindowWiretappingScaner", "Makes the widget screenshots"))
        self.buttWidgetScreenshot.setText(_translate("WindowWiretappingScaner", "Widget screenshot"))
        self.buttProgramScreenshot.setToolTip(_translate("WindowWiretappingScaner", "Makes the program screenshots"))
        self.buttProgramScreenshot.setText(_translate("WindowWiretappingScaner", "Program screenshot"))
        self.buttSaveLog.setToolTip(_translate("WindowWiretappingScaner", "Makes the log"))
        self.buttSaveLog.setText(_translate("WindowWiretappingScaner", "Save log"))
        self.buttSaveLog.setShortcut(_translate("WindowWiretappingScaner", "Ctrl+S"))
        self.groupSettings.setTitle(_translate("WindowWiretappingScaner", "Settings"))
        self.checkPlaySound.setText(_translate("WindowWiretappingScaner", "Play sound"))
        self.checkRemoteMode.setText(_translate("WindowWiretappingScaner", "Remote mode"))
        self.label4.setText(_translate("WindowWiretappingScaner", "Brightness"))
        self.dockWidget.setWindowTitle(_translate("WindowWiretappingScaner", "Log Console"))
        self.dockWidgetContents.setToolTip(_translate("WindowWiretappingScaner", "Log console"))
from ui.qsrc.drawFrame import DrawFrame
from ui.qsrc.inactiveButton import InactiveButton


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowWiretappingScaner = QtWidgets.QMainWindow()
    ui = Ui_WindowWiretappingScaner()
    ui.setupUi(WindowWiretappingScaner)
    WindowWiretappingScaner.show()
    sys.exit(app.exec())
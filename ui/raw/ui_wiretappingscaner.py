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
        WindowWiretappingScaner.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(WindowWiretappingScaner)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tabRadio = QtWidgets.QWidget()
        self.tabRadio.setObjectName("tabRadio")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabRadio)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RadioDrawFrame = DrawFrame(self.tabRadio)
        self.RadioDrawFrame.setObjectName("RadioDrawFrame")
        self.verticalLayout_2.addWidget(self.RadioDrawFrame)
        self.tabWidget.addTab(self.tabRadio, "")
        self.tabCompass = QtWidgets.QWidget()
        self.tabCompass.setObjectName("tabCompass")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabCompass)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.CompassDrawFrame = DrawFrame(self.tabCompass)
        self.CompassDrawFrame.setObjectName("CompassDrawFrame")
        self.verticalLayout_3.addWidget(self.CompassDrawFrame)
        self.tabWidget.addTab(self.tabCompass, "")
        self.tabIR = QtWidgets.QWidget()
        self.tabIR.setObjectName("tabIR")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabIR)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.IRDrawFrame = DrawFrame(self.tabIR)
        self.IRDrawFrame.setObjectName("IRDrawFrame")
        self.verticalLayout_4.addWidget(self.IRDrawFrame)
        self.tabWidget.addTab(self.tabIR, "")
        self.tabUltrasound = QtWidgets.QWidget()
        self.tabUltrasound.setObjectName("tabUltrasound")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabUltrasound)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.UltrasoundDrawFrame = DrawFrame(self.tabUltrasound)
        self.UltrasoundDrawFrame.setObjectName("UltrasoundDrawFrame")
        self.verticalLayout_5.addWidget(self.UltrasoundDrawFrame)
        self.tabWidget.addTab(self.tabUltrasound, "")
        self.tabFreeChannel = QtWidgets.QWidget()
        self.tabFreeChannel.setEnabled(False)
        self.tabFreeChannel.setObjectName("tabFreeChannel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabFreeChannel)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.FreeChannelDrawFrame = DrawFrame(self.tabFreeChannel)
        self.FreeChannelDrawFrame.setObjectName("FreeChannelDrawFrame")
        self.verticalLayout_6.addWidget(self.FreeChannelDrawFrame)
        self.tabWidget.addTab(self.tabFreeChannel, "")
        self.tabStethoscope = QtWidgets.QWidget()
        self.tabStethoscope.setEnabled(False)
        self.tabStethoscope.setObjectName("tabStethoscope")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabStethoscope)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.StethoscopeDrawFrame = DrawFrame(self.tabStethoscope)
        self.StethoscopeDrawFrame.setObjectName("StethoscopeDrawFrame")
        self.verticalLayout_7.addWidget(self.StethoscopeDrawFrame)
        self.tabWidget.addTab(self.tabStethoscope, "")
        self.verticalLayout.addWidget(self.tabWidget)
        WindowWiretappingScaner.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowWiretappingScaner)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        WindowWiretappingScaner.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowWiretappingScaner)
        self.statusbar.setObjectName("statusbar")
        WindowWiretappingScaner.setStatusBar(self.statusbar)

        self.retranslateUi(WindowWiretappingScaner)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WindowWiretappingScaner)

    def retranslateUi(self, WindowWiretappingScaner):
        _translate = QtCore.QCoreApplication.translate
        WindowWiretappingScaner.setWindowTitle(_translate("WindowWiretappingScaner", "Wiretapping Scaner"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRadio), _translate("WindowWiretappingScaner", "Радіо"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCompass), _translate("WindowWiretappingScaner", "Компас"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIR), _translate("WindowWiretappingScaner", "ІЧ випромінювання"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUltrasound), _translate("WindowWiretappingScaner", "Ультразвук"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFreeChannel), _translate("WindowWiretappingScaner", "Вільний канал"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStethoscope), _translate("WindowWiretappingScaner", "Стетоскоп"))
from src.drawer import DrawFrame


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowWiretappingScaner = QtWidgets.QMainWindow()
    ui = Ui_WindowWiretappingScaner()
    ui.setupUi(WindowWiretappingScaner)
    WindowWiretappingScaner.show()
    sys.exit(app.exec())

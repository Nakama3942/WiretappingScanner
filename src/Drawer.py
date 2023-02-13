from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QPixmap, QColor, QFont

from src.state import Draws


class DrawFrame(QFrame):
	def paintEvent(self, event):
		match Draws.tab:
			case 0:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text)
				qp.drawText(250, 100, Draws.radio_signal)
			case 1:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawPixmap(QPoint(200, 200), QPixmap(Draws.tpixmap))
				qp.drawText(100, 100, Draws.text)
			case 2:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text)
			case 3:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text)
			case 4:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text)
			case 5:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text)
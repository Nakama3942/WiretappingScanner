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

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QPixmap, QColor, QFont

from src.state import Draws
from src.signals import RadioSignal, CompassSignal


class DrawFrame(QFrame):
	def paintEvent(self, event):
		match Draws.tab:
			case 0:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text1)
				qp.drawText(250, 100, str(Draws.radio_signal))
				qp.drawText(100, 150, Draws.text2)
				qp.drawText(250, 150, str(Draws.radio_amplitude))
				qp.drawPath(RadioSignal(10))
			case 1:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawPixmap(QPoint(200, 200), QPixmap(Draws.tpixmap))
				compass, x, y = CompassSignal()
				qp.drawPath(compass)
				qp.drawLine(400, 400, x, y)
				qp.drawText(100, 100, Draws.text)
				qp.drawText(250, 100, str(Draws.compass_radius))
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
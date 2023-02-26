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

from math import pi, sin, cos

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QPoint, pyqtSignal
from PyQt6.QtGui import QPainter, QPainterPath, QPixmap, QColor, QFont, QMouseEvent

from src.state import Draws
from src.signals import RadioSignal


class DrawFrame(QFrame):
	gen_sound = pyqtSignal()
	play_sound = pyqtSignal()

	def paintEvent(self, event):
		match Draws.tab:
			case 0:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text1)
				qp.drawText(250, 100, str(Draws.radio_signal))
				qp.drawText(100, 150, Draws.text2)
				qp.drawText(250, 150, str(Draws.radio_amplitude))
				qp.drawPath(RadioSignal(10))  # Рисование синуса радиовоны
			case 1:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawPixmap(QPoint(200, 200), QPixmap(Draws.tpixmap))
				qp.drawText(100, 100, Draws.text1)
				qp.drawText(250, 100, str(Draws.compass_radius))
				# Рисование компаса
				circle = QPainterPath()
				circle.addEllipse(300, 300, 200, 200)
				qp.drawPath(circle)
				qp.drawLine(400,
							400,
							int(400 + 90 * cos(((Draws.compass_radius - 90) * pi) / 180)),
							int(400 + 90 * sin(((Draws.compass_radius - 90) * pi) / 180)))
			case 2:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text1)
				qp.drawText(300, 100, str(Draws.infrared_signal))
				qp.drawText(100, 150, Draws.text2)
				qp.drawText(300, 150, Draws.infrared_data)
			case 3:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text1)
				qp.drawText(250, 100, str(Draws.ultrasound_signal))
				# Button 1
				qp.drawRect(100, 200, 200, 50)
				qp.fillRect(100, 200, 200, 50, QColor(50, 50, 50, 40))
				qp.drawText(130, 232, "Generate sound")
				# Button 2
				qp.drawRect(400, 200, 200, 50)
				qp.fillRect(400, 200, 200, 50, QColor(50, 50, 50, 40))
				qp.drawText(455, 232, "Play sound")
			case 4:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text1)
			case 5:
				qp = QPainter(self)
				qp.setFont(Draws.tfont)
				qp.drawText(100, 100, Draws.text1)

	def mousePressEvent(self, event: QMouseEvent):
		# print(event.pos())
		if Draws.tab == 3:
			if 100 <= event.pos().x() <= 300 and 200 <= event.pos().y() <= 250:
				self.gen_sound.emit()
			elif 400 <= event.pos().x() <= 600 and 200 <= event.pos().y() <= 250:
				self.play_sound.emit()

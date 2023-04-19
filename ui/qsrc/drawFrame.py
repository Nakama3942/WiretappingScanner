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

from src import IMPORTANT_DATA, RadioSignal


class DrawFrame(QFrame):
	gen_sound = pyqtSignal()
	play_sound = pyqtSignal()
	draw = False

	def paintEvent(self, event):
		if IMPORTANT_DATA.connect and self.draw:
			qp = QPainter(self)
			qp.drawRect(0, 0, 799, 599)  # Drawing a border widget frame
			qp.setFont(IMPORTANT_DATA.tfont)
			match IMPORTANT_DATA.tab:
				case 0:
					qp.drawPixmap(QPoint(100, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(140, 100, IMPORTANT_DATA.text1)
					qp.drawText(360, 100, str(IMPORTANT_DATA.radio_impulse))

					qp.drawPixmap(QPoint(100, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(140, 140, IMPORTANT_DATA.text2)
					qp.drawText(360, 140, str(IMPORTANT_DATA.radio_noise))

					qp.drawPixmap(QPoint(100, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(140, 180, IMPORTANT_DATA.text3)
					qp.drawText(360, 180, str(IMPORTANT_DATA.radio_signal_spectrum_width))

					qp.drawPixmap(QPoint(100, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(140, 220, IMPORTANT_DATA.text4)
					qp.drawText(360, 220, str(IMPORTANT_DATA.radio_signal_duration))

					qp.drawPixmap(QPoint(100, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(140, 260, IMPORTANT_DATA.text5)
					qp.drawText(360, 260, str(IMPORTANT_DATA.radio_transfer_rate))

					qp.drawPixmap(QPoint(100, 280), QPixmap(IMPORTANT_DATA.tpixmap6))
					qp.drawText(140, 300, IMPORTANT_DATA.text6)
					qp.drawText(360, 300, str(IMPORTANT_DATA.radio_antenna_impedance))

					qp.drawPixmap(QPoint(100, 320), QPixmap(IMPORTANT_DATA.tpixmap7))
					qp.drawText(140, 340, IMPORTANT_DATA.text7)
					qp.drawText(360, 340, str(IMPORTANT_DATA.radio_antenna_directivity))

					qp.drawPixmap(QPoint(100, 360), QPixmap(IMPORTANT_DATA.tpixmap8))
					qp.drawText(140, 380, IMPORTANT_DATA.text8)
					qp.drawText(360, 380, str(IMPORTANT_DATA.radio_signal_strength))

					qp.drawPath(RadioSignal(10))  # Drawing the sine of a radio wave
				case 1:
					qp.drawPixmap(QPoint(100, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(140, 100, IMPORTANT_DATA.text1)
					qp.drawText(360, 100, str(IMPORTANT_DATA.compass_magnetic_field))

					qp.drawPixmap(QPoint(100, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(140, 140, IMPORTANT_DATA.text2)
					qp.drawText(360, 140, str(IMPORTANT_DATA.compass_tilt_angle))

					qp.drawPixmap(QPoint(100, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(140, 180, IMPORTANT_DATA.text3)
					qp.drawText(360, 180, str(IMPORTANT_DATA.compass_north_direction))

					qp.drawPixmap(QPoint(100, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(140, 220, IMPORTANT_DATA.text4)
					qp.drawText(360, 220, str(IMPORTANT_DATA.compass_field_strength))

					qp.drawPixmap(QPoint(100, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(140, 260, IMPORTANT_DATA.text5)
					qp.drawText(360, 260, str(IMPORTANT_DATA.compass_temperature))

					# Compass drawing
					circle = QPainterPath()
					circle.addEllipse(300, 300, 200, 200)
					qp.drawPath(circle)
					qp.drawLine(400,
								400,
								int(400 + 90 * cos(((IMPORTANT_DATA.compass_north_direction - 90) * pi) / 180)),
								int(400 + 90 * sin(((IMPORTANT_DATA.compass_north_direction - 90) * pi) / 180)))
				case 2:
					qp.drawPixmap(QPoint(100, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(140, 100, IMPORTANT_DATA.text1)
					qp.drawText(360, 100, str(IMPORTANT_DATA.infrared_wavelength))

					qp.drawPixmap(QPoint(100, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(140, 140, IMPORTANT_DATA.text2)
					qp.drawText(360, 140, str(IMPORTANT_DATA.infrared_signal_strength))

					qp.drawPixmap(QPoint(100, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(140, 180, IMPORTANT_DATA.text3)
					qp.drawText(360, 180, str(IMPORTANT_DATA.infrared_signal_power))

					qp.drawPixmap(QPoint(100, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(140, 220, IMPORTANT_DATA.text4)
					qp.drawText(360, 220, str(IMPORTANT_DATA.infrared_reception_angle))

					qp.drawPixmap(QPoint(100, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(140, 260, IMPORTANT_DATA.text5)
					qp.drawText(360, 260, str(IMPORTANT_DATA.infrared_transfer_rate))
				case 3:
					qp.drawPixmap(QPoint(100, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(140, 100, IMPORTANT_DATA.text1)
					qp.drawText(360, 100, str(IMPORTANT_DATA.ultrasound_wavelength))

					qp.drawPixmap(QPoint(100, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(140, 140, IMPORTANT_DATA.text2)
					qp.drawText(360, 140, str(IMPORTANT_DATA.ultrasound_signal_strength))

					qp.drawPixmap(QPoint(100, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(140, 180, IMPORTANT_DATA.text3)
					qp.drawText(360, 180, str(IMPORTANT_DATA.ultrasound_signal_power))

					qp.drawPixmap(QPoint(100, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(140, 220, IMPORTANT_DATA.text4)
					qp.drawText(360, 220, str(IMPORTANT_DATA.ultrasound_resolution))

					qp.drawPixmap(QPoint(100, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(140, 260, IMPORTANT_DATA.text5)
					qp.drawText(360, 260, str(IMPORTANT_DATA.ultrasound_transfer_rate))
					# # Button 1
					# qp.drawRect(100, 200, 200, 50)
					# qp.fillRect(100, 200, 200, 50, QColor(50, 50, 50, 40))
					# qp.drawText(130, 232, "Generate sound")
					# # Button 2
					# qp.drawRect(400, 200, 200, 50)
					# qp.fillRect(400, 200, 200, 50, QColor(50, 50, 50, 40))
					# qp.drawText(455, 232, "Play sound")
				case 4:
					qp.drawPixmap(QPoint(100, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(140, 100, IMPORTANT_DATA.text1)
					qp.drawText(360, 100, str(IMPORTANT_DATA.link_transfer_rate))

					qp.drawPixmap(QPoint(100, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(140, 140, IMPORTANT_DATA.text2)
					qp.drawText(360, 140, str(IMPORTANT_DATA.link_frequency_range))

					qp.drawPixmap(QPoint(100, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(140, 180, IMPORTANT_DATA.text3)
					qp.drawText(360, 180, str(IMPORTANT_DATA.link_signal_strength))

					qp.drawPixmap(QPoint(100, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(140, 220, IMPORTANT_DATA.text4)
					qp.drawText(360, 220, str(IMPORTANT_DATA.link_signal_power))

					qp.drawPixmap(QPoint(100, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(140, 260, IMPORTANT_DATA.text5)
					qp.drawText(360, 260, str(IMPORTANT_DATA.link_noise))

					qp.drawPixmap(QPoint(100, 280), QPixmap(IMPORTANT_DATA.tpixmap6))
					qp.drawText(140, 300, IMPORTANT_DATA.text6)
					qp.drawText(360, 300, str(IMPORTANT_DATA.link_signal_spectrum_width))

					qp.drawPixmap(QPoint(100, 320), QPixmap(IMPORTANT_DATA.tpixmap7))
					qp.drawText(140, 340, IMPORTANT_DATA.text7)
					qp.drawText(360, 340, str(IMPORTANT_DATA.link_interference_level))

					qp.drawPixmap(QPoint(100, 360), QPixmap(IMPORTANT_DATA.tpixmap8))
					qp.drawText(140, 380, IMPORTANT_DATA.text8)
					qp.drawText(360, 380, str(IMPORTANT_DATA.link_bit_error_rate))

					qp.drawPixmap(QPoint(100, 400), QPixmap(IMPORTANT_DATA.tpixmap9))
					qp.drawText(140, 420, IMPORTANT_DATA.text9)
					qp.drawText(360, 420, str(IMPORTANT_DATA.link_transmission_power))
				case 5:
					qp.drawPixmap(QPoint(100, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(140, 100, IMPORTANT_DATA.text1)
					qp.drawText(360, 100, str(IMPORTANT_DATA.stethoscope_sound_amplitude))

					qp.drawPixmap(QPoint(100, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(140, 140, IMPORTANT_DATA.text2)
					qp.drawText(360, 140, str(IMPORTANT_DATA.stethoscope_sound_frequency))

					qp.drawPixmap(QPoint(100, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(140, 180, IMPORTANT_DATA.text3)
					qp.drawText(360, 180, str(IMPORTANT_DATA.stethoscope_sound_pressure))

					qp.drawPixmap(QPoint(100, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(140, 220, IMPORTANT_DATA.text4)
					qp.drawText(360, 220, str(IMPORTANT_DATA.stethoscope_sound_direction))

					qp.drawPixmap(QPoint(100, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(140, 260, IMPORTANT_DATA.text5)
					qp.drawText(360, 260, str(IMPORTANT_DATA.stethoscope_transfer_rate))

	def customRepaint(self):
		self.draw = True
		super().repaint()
		self.draw = False

	def customUpdate(self):
		self.draw = True
		super().update()
		self.draw = False

	# def mousePressEvent(self, event: QMouseEvent):
	# 	if IMPORTANT_DATA.tab == 3:
	# 		if 100 <= event.pos().x() <= 300 and 200 <= event.pos().y() <= 250:
	# 			self.gen_sound.emit()
	# 		elif 400 <= event.pos().x() <= 600 and 200 <= event.pos().y() <= 250:
	# 			self.play_sound.emit()

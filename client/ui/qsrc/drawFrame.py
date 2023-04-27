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
from PyQt6.QtCore import QPoint, QPointF, pyqtSignal, Qt
from PyQt6.QtGui import QPainter, QPainterPath, QPixmap, QColor, QFont, QMouseEvent, QTransform, QPolygonF, QBrush

from src import IMPORTANT_DATA, sinus, rotatePath

class DrawFrame(QFrame):
	gen_sound = pyqtSignal()
	play_sound = pyqtSignal()
	draw = False

	def paintEvent(self, event):
		if IMPORTANT_DATA.connect and self.draw:
			qp = QPainter(self)
			qp.drawRect(0, 0, 799, 599)  # Drawing a border widget frame
			qp.setFont(IMPORTANT_DATA.tfont)

			qp.setRenderHint(QPainter.RenderHint.Antialiasing, True)
			qp.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)

			match IMPORTANT_DATA.tab:
				case 0:
					qp.drawPixmap(QPoint(230, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(270, 100, IMPORTANT_DATA.text1)
					qp.drawText(510, 100, str(IMPORTANT_DATA.radio_impulse))

					qp.drawPixmap(QPoint(230, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(270, 140, IMPORTANT_DATA.text2)
					qp.drawText(510, 140, str(IMPORTANT_DATA.radio_noise))

					qp.drawPixmap(QPoint(230, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(270, 180, IMPORTANT_DATA.text3)
					qp.drawText(510, 180, str(IMPORTANT_DATA.radio_signal_spectrum_width))

					qp.drawPixmap(QPoint(230, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(270, 220, IMPORTANT_DATA.text4)
					qp.drawText(510, 220, str(IMPORTANT_DATA.radio_signal_duration))

					qp.drawPixmap(QPoint(230, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(270, 260, IMPORTANT_DATA.text5)
					qp.drawText(510, 260, str(IMPORTANT_DATA.radio_transfer_rate))

					qp.drawPixmap(QPoint(230, 280), QPixmap(IMPORTANT_DATA.tpixmap6))
					qp.drawText(270, 300, IMPORTANT_DATA.text6)
					qp.drawText(510, 300, str(IMPORTANT_DATA.radio_antenna_impedance))

					qp.drawPixmap(QPoint(230, 320), QPixmap(IMPORTANT_DATA.tpixmap7))
					qp.drawText(270, 340, IMPORTANT_DATA.text7)
					qp.drawText(510, 340, str(IMPORTANT_DATA.radio_antenna_directivity))

					if 5 < IMPORTANT_DATA.radio_signal_strength <= 40:
						IMPORTANT_DATA.tpixmap8 = IMPORTANT_DATA.tpixmap8.replace("0", "1")
					elif 40 < IMPORTANT_DATA.radio_signal_strength <= 80:
						IMPORTANT_DATA.tpixmap8 = IMPORTANT_DATA.tpixmap8.replace("0", "2")
					elif 80 < IMPORTANT_DATA.radio_signal_strength:
						IMPORTANT_DATA.tpixmap8 = IMPORTANT_DATA.tpixmap8.replace("0", "3")
					else:
						pass

					qp.drawPixmap(QPoint(230, 360), QPixmap(IMPORTANT_DATA.tpixmap8))
					qp.drawText(270, 380, IMPORTANT_DATA.text8)
					qp.drawText(510, 380, str(IMPORTANT_DATA.radio_signal_strength))

					qp.drawPath(sinus(  # Drawing the sine of a radio wave
						10,
						IMPORTANT_DATA.window_width,
						IMPORTANT_DATA.radio_signal_spectrum_width,
						IMPORTANT_DATA.radio_signal_strength
					))
				case 1:
					qp.drawPixmap(QPoint(230, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(270, 100, IMPORTANT_DATA.text1)
					qp.drawText(510, 100, str(IMPORTANT_DATA.compass_magnetic_field))

					qp.drawPixmap(QPoint(230, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(270, 140, IMPORTANT_DATA.text2)
					qp.drawText(510, 140, str(IMPORTANT_DATA.compass_tilt_angle))

					qp.drawPixmap(QPoint(230, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(270, 180, IMPORTANT_DATA.text3)
					qp.drawText(510, 180, str(IMPORTANT_DATA.compass_north_direction))

					qp.drawPixmap(QPoint(230, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(270, 220, IMPORTANT_DATA.text4)
					qp.drawText(510, 220, str(IMPORTANT_DATA.compass_field_strength))

					qp.drawPixmap(QPoint(230, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(270, 260, IMPORTANT_DATA.text5)
					qp.drawText(510, 260, str(IMPORTANT_DATA.compass_temperature))

					# Compass drawing
					circle = QPainterPath()
					circle.addEllipse(300, 300, 200, 200)
					qp.drawPath(circle)
					qp.drawText(395, 315, "N")
					qp.drawText(485, 405, "E")
					qp.drawText(395, 495, "S")
					qp.drawText(305, 405, "W")

					# Создаем один объект QPainterPath для обоих полигонов
					# треугольников с координатами относительно центра (400, 400)
					triangle_path = QPainterPath()
					triangle_path.addPolygon(QPolygonF([
						QPointF(390, 400),
						QPointF(400, 310),
						QPointF(410, 400),
					]))

					# Рисуем красный треугольник (стрелка на север)
					qp.setBrush(QColor('red'))
					qp.drawPath(rotatePath(triangle_path, IMPORTANT_DATA.compass_north_direction))

					# Рисуем синий треугольник (стрелка на юг)
					qp.setBrush(QColor('blue'))
					qp.drawPath(rotatePath(triangle_path, IMPORTANT_DATA.compass_north_direction + 180))

					# Забавно неработающий код
					# triangle_polygon = QPolygonF([
					# 	QPointF(390, 400),
					# 	QPointF(400, 310),
					# 	QPointF(410, 400),
					# ])
					#
					# angle = (IMPORTANT_DATA.compass_north_direction - 90) * pi / 180
					#
					# rotation_matrix = QTransform().rotateRadians(-angle)
					#
					# rotated_triangle = rotation_matrix.map(triangle_polygon)
					#
					# triangle_path = QPainterPath()
					# triangle_path.addPolygon(rotated_triangle)
					#
					# brush = QBrush(QColor('red'))
					# qp.setBrush(brush)
					# qp.drawPath(triangle_path)

				case 2:
					qp.drawText(320, 100, IMPORTANT_DATA.text1)
					# qp.drawPixmap(QPoint(230, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					# qp.drawText(270, 100, IMPORTANT_DATA.text1)
					# qp.drawText(510, 100, str(IMPORTANT_DATA.infrared_frequency_of_wavefront))

					# qp.drawPixmap(QPoint(230, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					# qp.drawText(270, 140, IMPORTANT_DATA.text2)
					# qp.drawText(510, 140, str(IMPORTANT_DATA.infrared_wavelength))
					#
					# if 5 < IMPORTANT_DATA.infrared_signal_strength <= 40:
					# 	IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace("0", "1")
					# elif 40 < IMPORTANT_DATA.infrared_signal_strength <= 80:
					# 	IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace("0", "2")
					# elif 80 < IMPORTANT_DATA.infrared_signal_strength:
					# 	IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace("0", "3")
					# else:
					# 	pass
					#
					# qp.drawPixmap(QPoint(230, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					# qp.drawText(270, 180, IMPORTANT_DATA.text3)
					# qp.drawText(510, 180, str(IMPORTANT_DATA.infrared_signal_strength))
					#
					# qp.drawPixmap(QPoint(230, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					# qp.drawText(270, 220, IMPORTANT_DATA.text4)
					# qp.drawText(510, 220, str(IMPORTANT_DATA.infrared_signal_power))
					#
					# qp.drawPixmap(QPoint(230, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					# qp.drawText(270, 260, IMPORTANT_DATA.text5)
					# qp.drawText(510, 260, str(IMPORTANT_DATA.infrared_reception_angle))
					#
					# qp.drawPixmap(QPoint(230, 280), QPixmap(IMPORTANT_DATA.tpixmap6))
					# qp.drawText(270, 300, IMPORTANT_DATA.text6)
					# qp.drawText(510, 300, str(IMPORTANT_DATA.infrared_transfer_rate))
					#
					# qp.drawPath(sinus(  # Drawing the sine of a radio wave
					# 	10,
					# 	IMPORTANT_DATA.window_width,
					# 	IMPORTANT_DATA.infrared_frequency_of_wavefront,
					# 	IMPORTANT_DATA.infrared_signal_strength
					# ))
				case 3:
					qp.drawPixmap(QPoint(230, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(270, 100, IMPORTANT_DATA.text1)
					qp.drawText(510, 100, str(IMPORTANT_DATA.ultrasound_frequency_of_wavefront))

					qp.drawPixmap(QPoint(230, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(270, 140, IMPORTANT_DATA.text2)
					qp.drawText(510, 140, str(IMPORTANT_DATA.ultrasound_wavelength))

					if 5 < IMPORTANT_DATA.ultrasound_signal_strength <= 40:
						IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace("0", "1")
					elif 40 < IMPORTANT_DATA.ultrasound_signal_strength <= 80:
						IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace("0", "2")
					elif 80 < IMPORTANT_DATA.ultrasound_signal_strength:
						IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace("0", "3")
					else:
						pass

					qp.drawPixmap(QPoint(230, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(270, 180, IMPORTANT_DATA.text3)
					qp.drawText(510, 180, str(IMPORTANT_DATA.ultrasound_signal_strength))

					qp.drawPixmap(QPoint(230, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(270, 220, IMPORTANT_DATA.text4)
					qp.drawText(510, 220, str(IMPORTANT_DATA.ultrasound_signal_power))

					qp.drawPixmap(QPoint(230, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(270, 260, IMPORTANT_DATA.text5)
					qp.drawText(510, 260, str(IMPORTANT_DATA.ultrasound_resolution))

					qp.drawPixmap(QPoint(230, 280), QPixmap(IMPORTANT_DATA.tpixmap6))
					qp.drawText(270, 300, IMPORTANT_DATA.text6)
					qp.drawText(510, 300, str(IMPORTANT_DATA.ultrasound_transfer_rate))

					qp.drawPath(sinus(  # Drawing the sine of a radio wave
						10,
						IMPORTANT_DATA.window_width,
						IMPORTANT_DATA.ultrasound_frequency_of_wavefront,
						IMPORTANT_DATA.ultrasound_signal_strength
					))

					# Button 1
					qp.drawRect(150, 350, 200, 50)
					qp.fillRect(150, 350, 200, 50, QColor(50, 50, 50, 40))
					qp.drawText(180, 382, "Generate sound")
					# Button 2
					qp.drawRect(450, 350, 200, 50)
					qp.fillRect(450, 350, 200, 50, QColor(50, 50, 50, 40))
					qp.drawText(505, 382, "Play sound")
				case 4:
					qp.drawPixmap(QPoint(230, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(270, 100, IMPORTANT_DATA.text1)
					qp.drawText(510, 100, str(IMPORTANT_DATA.link_transfer_rate))

					qp.drawPixmap(QPoint(230, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(270, 140, IMPORTANT_DATA.text2)
					qp.drawText(510, 140, str(IMPORTANT_DATA.link_frequency_range))

					if 5 < IMPORTANT_DATA.link_signal_strength <= 40:
						IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace("0", "1")
					elif 40 < IMPORTANT_DATA.link_signal_strength <= 80:
						IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace("0", "2")
					elif 80 < IMPORTANT_DATA.link_signal_strength:
						IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace("0", "3")
					else:
						pass

					qp.drawPixmap(QPoint(230, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(270, 180, IMPORTANT_DATA.text3)
					qp.drawText(510, 180, str(IMPORTANT_DATA.link_signal_strength))

					qp.drawPixmap(QPoint(230, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(270, 220, IMPORTANT_DATA.text4)
					qp.drawText(510, 220, str(IMPORTANT_DATA.link_signal_power))

					qp.drawPixmap(QPoint(230, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(270, 260, IMPORTANT_DATA.text5)
					qp.drawText(510, 260, str(IMPORTANT_DATA.link_noise))

					qp.drawPixmap(QPoint(230, 280), QPixmap(IMPORTANT_DATA.tpixmap6))
					qp.drawText(270, 300, IMPORTANT_DATA.text6)
					qp.drawText(510, 300, str(IMPORTANT_DATA.link_signal_spectrum_width))

					qp.drawPixmap(QPoint(230, 320), QPixmap(IMPORTANT_DATA.tpixmap7))
					qp.drawText(270, 340, IMPORTANT_DATA.text7)
					qp.drawText(510, 340, str(IMPORTANT_DATA.link_interference_level))

					qp.drawPixmap(QPoint(230, 360), QPixmap(IMPORTANT_DATA.tpixmap8))
					qp.drawText(270, 380, IMPORTANT_DATA.text8)
					qp.drawText(510, 380, str(IMPORTANT_DATA.link_bit_error_rate))

					qp.drawPixmap(QPoint(230, 400), QPixmap(IMPORTANT_DATA.tpixmap9))
					qp.drawText(270, 420, IMPORTANT_DATA.text9)
					qp.drawText(510, 420, str(IMPORTANT_DATA.link_transmission_power))

					qp.drawPath(sinus(  # Drawing the sine of a radio wave
						10,
						IMPORTANT_DATA.window_width,
						IMPORTANT_DATA.link_signal_spectrum_width,
						IMPORTANT_DATA.link_signal_strength
					))
				case 5:
					qp.drawPixmap(QPoint(230, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(270, 100, IMPORTANT_DATA.text1)
					qp.drawText(510, 100, str(IMPORTANT_DATA.stethoscope_sound_amplitude))

					qp.drawPixmap(QPoint(230, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(270, 140, IMPORTANT_DATA.text2)
					qp.drawText(510, 140, str(IMPORTANT_DATA.stethoscope_sound_frequency))

					qp.drawPixmap(QPoint(230, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(270, 180, IMPORTANT_DATA.text3)
					qp.drawText(510, 180, str(IMPORTANT_DATA.stethoscope_sound_pressure))

					qp.drawPixmap(QPoint(230, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(270, 220, IMPORTANT_DATA.text4)
					qp.drawText(510, 220, str(IMPORTANT_DATA.stethoscope_sound_direction))

					qp.drawPixmap(QPoint(230, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(270, 260, IMPORTANT_DATA.text5)
					qp.drawText(510, 260, str(IMPORTANT_DATA.stethoscope_transfer_rate))

					qp.drawPath(sinus(  # Drawing the sine of a radio wave
						10,
						IMPORTANT_DATA.window_width,
						IMPORTANT_DATA.stethoscope_sound_frequency,
						IMPORTANT_DATA.stethoscope_sound_amplitude
					))

	def customRepaint(self):
		self.draw = True
		super().repaint()
		self.draw = False

	def customUpdate(self):
		self.draw = True
		super().update()
		self.draw = False

	def mousePressEvent(self, event: QMouseEvent):
		if IMPORTANT_DATA.tab == 3:
			if 150 <= event.pos().x() <= 350 and 350 <= event.pos().y() <= 400:
				self.gen_sound.emit()
			elif 450 <= event.pos().x() <= 650 and 350 <= event.pos().y() <= 400:
				self.play_sound.emit()

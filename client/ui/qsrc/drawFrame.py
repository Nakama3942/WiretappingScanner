"""
Draws a frame with data when a receive signal is caught.
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

from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QPoint, QPointF, pyqtSignal
from PyQt6.QtGui import QPaintEvent, QMouseEvent, QPainter, QPainterPath, QPixmap, QColor, QPolygonF

from ui.qsrc.painterProgramFunctions import sinus, rotatePath
from src import IMPORTANT_DATA

class DrawFrame(QFrame):
	"""
	The class of the frame being drawn.
	"""
	gen_sound = pyqtSignal()
	play_sound = pyqtSignal()

	def paintEvent(self, event: QPaintEvent) -> None:
		"""
		Frame drawing event.

		:param event: See the Qt documentation
		"""
		if IMPORTANT_DATA.connect:
			# Painter setup
			qp = QPainter(self)
			qp.drawRect(0, 0, 799, 599)  # Drawing a border widget frame
			qp.setFont(IMPORTANT_DATA.tfont)
			qp.setRenderHint(QPainter.RenderHint.Antialiasing, True)
			qp.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)

			match IMPORTANT_DATA.tab:
				case 0:
					# Drawing a radio data frame
					qp.drawPixmap(QPoint(180, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(220, 100, IMPORTANT_DATA.text1)
					qp.drawText(560, 100, str(IMPORTANT_DATA.radio_impulse))

					qp.drawPixmap(QPoint(180, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(220, 140, IMPORTANT_DATA.text2)
					qp.drawText(560, 140, str(IMPORTANT_DATA.radio_noise))

					qp.drawPixmap(QPoint(180, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(220, 180, IMPORTANT_DATA.text3)
					qp.drawText(560, 180, str(IMPORTANT_DATA.radio_signal_spectrum_width))

					qp.drawPixmap(QPoint(180, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(220, 220, IMPORTANT_DATA.text4)
					qp.drawText(560, 220, str(IMPORTANT_DATA.radio_signal_duration))

					qp.drawPixmap(QPoint(180, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(220, 260, IMPORTANT_DATA.text5)
					qp.drawText(560, 260, str(IMPORTANT_DATA.radio_transfer_rate))

					qp.drawPixmap(QPoint(180, 280), QPixmap(IMPORTANT_DATA.tpixmap6))
					qp.drawText(220, 300, IMPORTANT_DATA.text6)
					qp.drawText(560, 300, str(IMPORTANT_DATA.radio_antenna_impedance))

					qp.drawPixmap(QPoint(180, 320), QPixmap(IMPORTANT_DATA.tpixmap7))
					qp.drawText(220, 340, IMPORTANT_DATA.text7)
					qp.drawText(560, 340, str(IMPORTANT_DATA.radio_antenna_directivity))

					replacement_map = {
						(5, 40): '1',
						(40, 80): '2',
						(80, float('inf')): '3'
					}
					digit_to_replace = next(
						(digit for digit in ['0', '1', '2', '3'] if IMPORTANT_DATA.tpixmap3.count(digit)),
						None
					)
					if digit_to_replace:
						found_range = False
						for (lower, upper), replacement in replacement_map.items():
							if lower < IMPORTANT_DATA.link_signal_strength <= upper:
								IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace(digit_to_replace, replacement)
								found_range = True
								break
						if not found_range:
							IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace(digit_to_replace, '0')

					qp.drawPixmap(QPoint(180, 360), QPixmap(IMPORTANT_DATA.tpixmap8))
					qp.drawText(220, 380, IMPORTANT_DATA.text8)
					qp.drawText(560, 380, str(IMPORTANT_DATA.radio_signal_strength))

					qp.drawPath(sinus(  # Drawing the sinus of a radio wave
						10,
						IMPORTANT_DATA.window_width,
						IMPORTANT_DATA.radio_signal_spectrum_width,
						IMPORTANT_DATA.radio_signal_strength
					))
				case 1:
					# Drawing a compass data frame
					qp.drawPixmap(QPoint(180, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(220, 100, IMPORTANT_DATA.text1)
					qp.drawText(560, 100, str(IMPORTANT_DATA.compass_magnetic_field))

					qp.drawPixmap(QPoint(180, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(220, 140, IMPORTANT_DATA.text2)
					qp.drawText(560, 140, str(IMPORTANT_DATA.compass_tilt_angle))

					qp.drawPixmap(QPoint(180, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(220, 180, IMPORTANT_DATA.text3)
					qp.drawText(560, 180, str(IMPORTANT_DATA.compass_north_direction))

					qp.drawPixmap(QPoint(180, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(220, 220, IMPORTANT_DATA.text4)
					qp.drawText(560, 220, str(IMPORTANT_DATA.compass_field_strength))

					qp.drawPixmap(QPoint(180, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(220, 260, IMPORTANT_DATA.text5)
					qp.drawText(560, 260, str(IMPORTANT_DATA.compass_temperature))

					# Compass drawing
					circle = QPainterPath()
					circle.addEllipse(300, 300, 200, 200)
					qp.drawPath(circle)
					qp.drawText(395, 315, "N")
					qp.drawText(485, 405, "E")
					qp.drawText(395, 495, "S")
					qp.drawText(305, 405, "W")

					# Create one QPainterPath object for both triangle polygons
					# with coordinates relative to the center (400, 400)
					triangle_path = QPainterPath()
					triangle_path.addPolygon(QPolygonF([
						QPointF(390, 400),
						QPointF(400, 310),
						QPointF(410, 400),
					]))

					# Draw a red triangle (arrow to the north)
					qp.setBrush(QColor('red'))
					qp.drawPath(rotatePath(triangle_path, 400, 400, IMPORTANT_DATA.compass_north_direction))

					# Draw a blue triangle (arrow to the south)
					qp.setBrush(QColor('blue'))
					qp.drawPath(rotatePath(triangle_path, 400, 400, IMPORTANT_DATA.compass_north_direction + 180))

					# Funny broken code
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
					# Drawing an infrared data frame
					qp.drawPixmap(QPoint(180, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(220, 100, IMPORTANT_DATA.text1)
					qp.drawText(560, 100, str(IMPORTANT_DATA.infrared_frequency_of_wavefront))

					qp.drawPixmap(QPoint(180, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(220, 140, IMPORTANT_DATA.text2)
					qp.drawText(560, 140, str(IMPORTANT_DATA.infrared_wavelength))

					replacement_map = {
						(5, 40): '1',
						(40, 80): '2',
						(80, float('inf')): '3'
					}
					digit_to_replace = next(
						(digit for digit in ['0', '1', '2', '3'] if IMPORTANT_DATA.tpixmap3.count(digit)),
						None
					)
					if digit_to_replace:
						found_range = False
						for (lower, upper), replacement in replacement_map.items():
							if lower < IMPORTANT_DATA.link_signal_strength <= upper:
								IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace(digit_to_replace, replacement)
								found_range = True
								break
						if not found_range:
							IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace(digit_to_replace, '0')

					qp.drawPixmap(QPoint(180, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(220, 180, IMPORTANT_DATA.text3)
					qp.drawText(560, 180, str(IMPORTANT_DATA.infrared_signal_strength))

					qp.drawPixmap(QPoint(180, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(220, 220, IMPORTANT_DATA.text4)
					qp.drawText(560, 220, str(IMPORTANT_DATA.infrared_signal_power))

					qp.drawPixmap(QPoint(180, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(220, 260, IMPORTANT_DATA.text5)
					qp.drawText(560, 260, str(IMPORTANT_DATA.infrared_reception_angle))

					qp.drawPixmap(QPoint(180, 280), QPixmap(IMPORTANT_DATA.tpixmap6))
					qp.drawText(220, 300, IMPORTANT_DATA.text6)
					qp.drawText(560, 300, str(IMPORTANT_DATA.infrared_transfer_rate))

					qp.drawPath(sinus(  # Drawing the sinus of an infrared wave
						10,
						IMPORTANT_DATA.window_width,
						IMPORTANT_DATA.infrared_frequency_of_wavefront,
						IMPORTANT_DATA.infrared_signal_strength
					))
				case 3:
					# Drawing an ultrasound data frame
					qp.drawPixmap(QPoint(80, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(120, 100, IMPORTANT_DATA.text1)
					qp.drawText(460, 100, str(IMPORTANT_DATA.ultrasound_frequency_of_wavefront))

					qp.drawPixmap(QPoint(80, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(120, 140, IMPORTANT_DATA.text2)
					qp.drawText(460, 140, str(IMPORTANT_DATA.ultrasound_wavelength))

					replacement_map = {
						(5, 40): '1',
						(40, 80): '2',
						(80, float('inf')): '3'
					}
					digit_to_replace = next(
						(digit for digit in ['0', '1', '2', '3'] if IMPORTANT_DATA.tpixmap3.count(digit)),
						None
					)
					if digit_to_replace:
						found_range = False
						for (lower, upper), replacement in replacement_map.items():
							if lower < IMPORTANT_DATA.link_signal_strength <= upper:
								IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace(digit_to_replace, replacement)
								found_range = True
								break
						if not found_range:
							IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace(digit_to_replace, '0')

					qp.drawPixmap(QPoint(80, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(120, 180, IMPORTANT_DATA.text3)
					qp.drawText(460, 180, str(IMPORTANT_DATA.ultrasound_signal_strength))

					qp.drawPixmap(QPoint(80, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(120, 220, IMPORTANT_DATA.text4)
					qp.drawText(460, 220, str(IMPORTANT_DATA.ultrasound_signal_power))

					qp.drawPixmap(QPoint(80, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(120, 260, IMPORTANT_DATA.text5)
					qp.drawText(460, 260, str(IMPORTANT_DATA.ultrasound_resolution))

					qp.drawPixmap(QPoint(80, 280), QPixmap(IMPORTANT_DATA.tpixmap6))
					qp.drawText(120, 300, IMPORTANT_DATA.text6)
					qp.drawText(460, 300, str(IMPORTANT_DATA.ultrasound_transfer_rate))

					qp.drawPath(sinus(  # Drawing the sinus of an ultrasound wave
						10,
						IMPORTANT_DATA.window_width,
						IMPORTANT_DATA.ultrasound_frequency_of_wavefront,
						IMPORTANT_DATA.ultrasound_signal_strength
					))

					# Button 1
					qp.drawRect(550, 120, 200, 50)
					qp.fillRect(550, 120, 200, 50, QColor(50, 50, 50, 40))
					qp.drawText(580, 152, "Generate sound")
					# Button 2
					qp.drawRect(550, 220, 200, 50)
					qp.fillRect(550, 220, 200, 50, QColor(50, 50, 50, 40))
					qp.drawText(595, 252, "Play sound")
				case 4:
					# Drawing a link quality data frame
					qp.drawPixmap(QPoint(180, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(220, 100, IMPORTANT_DATA.text1)
					qp.drawText(560, 100, str(IMPORTANT_DATA.link_transfer_rate))

					qp.drawPixmap(QPoint(180, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(220, 140, IMPORTANT_DATA.text2)
					qp.drawText(560, 140, str(IMPORTANT_DATA.link_frequency_range))

					replacement_map = {
						(5, 40): '1',
						(40, 80): '2',
						(81, float('inf')): '3'
					}
					digit_to_replace = next(
						(digit for digit in ['0', '1', '2', '3'] if IMPORTANT_DATA.tpixmap3.count(digit)),
						None
					)
					if digit_to_replace:
						found_range = False
						for (lower, upper), replacement in replacement_map.items():
							if lower < IMPORTANT_DATA.link_signal_strength <= upper:
								IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace(digit_to_replace, replacement)
								found_range = True
								break
						if not found_range:
							IMPORTANT_DATA.tpixmap3 = IMPORTANT_DATA.tpixmap3.replace(digit_to_replace, '0')

					qp.drawPixmap(QPoint(180, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(220, 180, IMPORTANT_DATA.text3)
					qp.drawText(560, 180, str(IMPORTANT_DATA.link_signal_strength))

					qp.drawPixmap(QPoint(180, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(220, 220, IMPORTANT_DATA.text4)
					qp.drawText(560, 220, str(IMPORTANT_DATA.link_signal_power))

					qp.drawPixmap(QPoint(180, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(220, 260, IMPORTANT_DATA.text5)
					qp.drawText(560, 260, str(IMPORTANT_DATA.link_noise))

					qp.drawPixmap(QPoint(180, 280), QPixmap(IMPORTANT_DATA.tpixmap6))
					qp.drawText(220, 300, IMPORTANT_DATA.text6)
					qp.drawText(560, 300, str(IMPORTANT_DATA.link_signal_spectrum_width))

					qp.drawPixmap(QPoint(180, 320), QPixmap(IMPORTANT_DATA.tpixmap7))
					qp.drawText(220, 340, IMPORTANT_DATA.text7)
					qp.drawText(560, 340, str(IMPORTANT_DATA.link_interference_level))

					qp.drawPixmap(QPoint(180, 360), QPixmap(IMPORTANT_DATA.tpixmap8))
					qp.drawText(220, 380, IMPORTANT_DATA.text8)
					qp.drawText(560, 380, str(IMPORTANT_DATA.link_bit_error_rate))

					qp.drawPixmap(QPoint(180, 400), QPixmap(IMPORTANT_DATA.tpixmap9))
					qp.drawText(220, 420, IMPORTANT_DATA.text9)
					qp.drawText(560, 420, str(IMPORTANT_DATA.link_transmission_power))

					qp.drawPath(sinus(  # Drawing the sinus of a link wave
						10,
						IMPORTANT_DATA.window_width,
						IMPORTANT_DATA.link_signal_spectrum_width,
						IMPORTANT_DATA.link_signal_strength
					))
				case 5:
					# Drawing a stethoscope data frame
					qp.drawPixmap(QPoint(180, 80), QPixmap(IMPORTANT_DATA.tpixmap1))
					qp.drawText(220, 100, IMPORTANT_DATA.text1)
					qp.drawText(560, 100, str(IMPORTANT_DATA.stethoscope_sound_amplitude))

					qp.drawPixmap(QPoint(180, 120), QPixmap(IMPORTANT_DATA.tpixmap2))
					qp.drawText(220, 140, IMPORTANT_DATA.text2)
					qp.drawText(560, 140, str(IMPORTANT_DATA.stethoscope_sound_frequency))

					qp.drawPixmap(QPoint(180, 160), QPixmap(IMPORTANT_DATA.tpixmap3))
					qp.drawText(220, 180, IMPORTANT_DATA.text3)
					qp.drawText(560, 180, str(IMPORTANT_DATA.stethoscope_sound_pressure))

					qp.drawPixmap(QPoint(180, 200), QPixmap(IMPORTANT_DATA.tpixmap4))
					qp.drawText(220, 220, IMPORTANT_DATA.text4)
					qp.drawText(560, 220, str(IMPORTANT_DATA.stethoscope_sound_direction))

					qp.drawPixmap(QPoint(180, 240), QPixmap(IMPORTANT_DATA.tpixmap5))
					qp.drawText(220, 260, IMPORTANT_DATA.text5)
					qp.drawText(560, 260, str(IMPORTANT_DATA.stethoscope_transfer_rate))

					qp.drawPath(sinus(  # Drawing the sinus of a sound wave
						10,
						IMPORTANT_DATA.window_width,
						IMPORTANT_DATA.stethoscope_sound_frequency,
						IMPORTANT_DATA.stethoscope_sound_amplitude
					))

	def mousePressEvent(self, event: QMouseEvent) -> None:
		"""
		Tracking clicks on drawn buttons.

		:param event: See the Qt documentation
		"""
		if IMPORTANT_DATA.tab == 3:
			if 550 <= event.pos().x() <= 750 and 120 <= event.pos().y() <= 170:
				self.gen_sound.emit()
			elif 550 <= event.pos().x() <= 750 and 220 <= event.pos().y() <= 270:
				self.play_sound.emit()

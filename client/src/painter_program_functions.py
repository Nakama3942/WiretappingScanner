"""
Stores functions for drawing some details.
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

from PyQt6.QtGui import QPainterPath, QTransform
from math import sin

def sinus(grid, window_width, spectrum_width, amplitude):
	# Формула синусоиды: y = A * sin (ωx + φ) + k
	# Формула длины волны по частоте: λ = c / v
	# A - амплитуда, которую можно понимать как высоту волны
	# ωx - угловая скорость, которую можно понимать как плотность волны
	#     (frequency = pi / radio_signal)
	# Вместо ωx мы используем λ
	#     (frequency = c / radio_signal)
	# φ - начальная фаза
	# k - смещение по оси Y

	# amplitude = IMPORTANT_DATA.radio_signal_strength				# A
	frequency = 300_000_000 / (spectrum_width * 1_000_000 * grid)	# λ
	initphase = 0													# φ
	offset = 500													# k

	wave = QPainterPath()
	is_start = True
	for x in range(0, window_width):  # x - значения (0 ~ frequency) до синусоиды
		# waveY изменяется при изменении значения x, получая таким образом синусоидальную кривую
		waveY = (amplitude * sin(frequency * x + initphase)) + offset
		if is_start:
			# Координата первой точки: (0, высота)
			wave.moveTo(x, waveY)
			is_start = False
		else:
			# Рисование линии от последней точки рисования до (x, waveY)
			wave.lineTo(x, waveY)

	return wave

def rotatePath(path, degrees):
	# Создаем объект QTransform для поворота пути
	transform = QTransform()
	transform.translate(400, 400)
	transform.rotate(degrees)
	transform.translate(-400, -400)

	# Поворачиваем путь и возвращаем результат
	return transform.map(path)

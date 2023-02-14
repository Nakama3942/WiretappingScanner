from PyQt6.QtGui import QPainter, QPainterPath
from math import pi, sin, cos

from src.state import Draws

def RadioSignal(grid):
	# Формула синусоиды: y = A * sin (ωx + φ) + k
	# Формула длины волны по частоте: λ = c / v
	# A - амплитуда, которую можно понимать как высоту волны
	# ωx - угловая скорость, которую можно понимать как плотность волны
	#     (frequency = pi / radio_signal)
	# Вместо ωx мы используем λ
	#     (frequency = c / radio_signal)
	# φ - начальная фаза
	# k - смещение по оси Y
	amplitude = Draws.radio_amplitude									# A
	frequency = 300_000_000 / (Draws.radio_signal * 1_000_000 * grid)	# λ
	initphase = 0														# φ
	offset = 450														# k

	wave = QPainterPath()
	is_start = True
	for x in range(0, Draws.window_width):  # x - значения (0 ~ frequency) до синусоиды
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


def CompassSignal():
	circle = QPainterPath()
	circle.addEllipse(300, 300, 200, 200)

	x_coord = 400 + 90 * cos(((Draws.compass_radius - 90) * pi) / 180)
	y_coord = 400 + 90 * sin(((Draws.compass_radius - 90) * pi) / 180)

	return circle, int(x_coord), int(y_coord)

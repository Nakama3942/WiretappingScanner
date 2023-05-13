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

from math import sin

from PyQt6.QtGui import QPainterPath, QTransform

def sinus(grid: int, window_width: int, spectrum_width: float, amplitude: float, init_phase: int = 0, y_offset: int = 500) -> QPainterPath:
	"""
	Sinus drawing function.\n
	Sinus wave formula: y = A * sin (ωx + φ) + k\n
	Wavelength formula by frequency: λ = c / v\n
	A - amplitude, which can be understood as the height of the wave\n
	ωx - angular velocity, which can be understood as wave density\n
	- (frequency = pi / radio_signal)\n
	Instead of ωx we use λ\n
	- (frequency = c / radio_signal)\n
	φ - initial phase\n
	k - Y offset

	:param grid: The size of the canvas (grid) on which the sinus is drawn
	:param window_width: Window width
	:param spectrum_width: Wave spectrum width
	:param amplitude: Amplitude of wave
	:param init_phase: Initial phase of wave
	:param y_offset: Wave offset along Y coordinates
	:return: the drawn sinus
	"""
	try:
		frequency = 300_000_000 / (spectrum_width * 1_000_000 * grid)
	except ZeroDivisionError:
		frequency = 0
	# |   amplitude : A   |   frequency : λ   |   init_phase : φ   |   offset : k   |

	wave = QPainterPath()
	wave.moveTo(0, y_offset)
	for x in range(1, window_width):
		# Draw line from last drawing point to new (x, y)
		wave.lineTo(x, (amplitude * sin(frequency * x + init_phase)) + y_offset)

	return wave

def rotatePath(path: QPainterPath, translate_dx: float, translate_dy: float, degrees: float) -> QPainterPath:
	"""
	The function to rotate the drawing object.

	:param path: The path to be turned
	:param translate_dx: Offset relative to X
	:param translate_dy: Offset relative to Y
	:param degrees: Degree of rotation
	:return: a new path
	"""
	# Create a QTransform object to rotate the path
	transform = QTransform()
	transform.translate(translate_dx, translate_dy)
	transform.rotate(degrees)
	transform.translate(-translate_dx, -translate_dy)

	# Rotate the path and return the result
	return transform.map(path)

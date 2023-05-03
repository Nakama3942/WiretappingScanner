"""
Data store.
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

class IMPORTANT_DATA:
	# Global settings
	tab = 0
	window_height = 0
	window_width = 0
	connect = False
	IPAddr = "000.000.000.000"
	Port = "00000"
	SerialNum = "AAAAA-AAA-AAA-AAAA"

	# Local settings
	tfont = None
	text1 = ""
	text2 = ""
	text3 = ""
	text4 = ""
	text5 = ""
	text6 = ""
	text7 = ""
	text8 = ""
	text9 = ""
	text10 = ""
	reserve_text1 = ""
	reserve_text2 = ""
	reserve_text3 = ""
	tpixmap1 = ""
	tpixmap2 = ""
	tpixmap3 = ""
	tpixmap4 = ""
	tpixmap5 = ""
	tpixmap6 = ""
	tpixmap7 = ""
	tpixmap8 = ""
	tpixmap9 = ""
	tpixmap10 = ""
	tpixmap11 = ""
	tpixmap12 = ""

	# Radio wiretapping data
	radio_impulse = 0							# seconds (s)
	radio_noise = 0.0							# decibel (dB)
	radio_signal_spectrum_width = 0.0			# hertz (Hz)
	radio_signal_duration = 0					# seconds (s)
	radio_transfer_rate = 0						# bits per second (bps)
	radio_antenna_impedance = 0					# ohm (Ω)
	radio_antenna_directivity = 0.0				# decibel (dBi)
	radio_signal_strength = 0.0					# decibel (dB)

	# Compass wiretapping data
	compass_magnetic_field = 0					# microtesla (μT)
	compass_tilt_angle = 0						# degrees (°)
	compass_north_direction = 0					# degrees (°)
	compass_field_strength = 0.0				# ampere-vits per meter (A/m)
	compass_temperature = 0						# degree Celsius (°C)

	# Infrared wiretapping data
	infrared_frequency_of_wavefront = 0.0		# hertz (Hz)
	infrared_wavelength = 0.0					# micrometers (μm)
	infrared_signal_strength = 0.0				# decibel (dB)
	infrared_signal_power = 0.0					# decibel milliwatt (dBm)
	infrared_reception_angle = 0				# degrees (°)
	infrared_transfer_rate = 0					# bits per second (bps)

	# Ultrasound wiretapping data
	ultrasound_frequency_of_wavefront = 0.0		# hertz (Hz)
	ultrasound_wavelength = 0.0					# millimeters (mm)
	ultrasound_signal_strength = 0.0			# decibel (dB)
	ultrasound_signal_power = 0.0				# decibel milliwatt (dBm)
	ultrasound_resolution = 0.0					# millimeters (mm)
	ultrasound_transfer_rate = 0				# bits per second (bps)

	# Link quality wiretapping data
	link_transfer_rate = 0						# bits per second (bps)
	link_frequency_range = 0					# hertz (Hz)
	link_signal_strength = 0.0					# decibel (dB)
	link_signal_power = 0.0						# decibel milliwatt (dBm)
	link_noise = 0.0							# decibel milliwatt (dBm)
	link_signal_spectrum_width = 0.0			# hertz (Hz)
	link_interference_level = 0.0				# decibel (dB)
	link_bit_error_rate = 0						# proportion of erroneously transmitted bits (-)
	link_transmission_power = 0.0				# decibel milliwatt (dBm)

	# Stethoscope wiretapping data
	stethoscope_sound_amplitude = 0.0			# decibel (dB)
	stethoscope_sound_frequency = 0.0			# hertz (Hz)
	stethoscope_sound_pressure = 0				# pascal (Pa)
	stethoscope_sound_direction = 0				# degrees (°)
	stethoscope_transfer_rate = 0				# bits per second (bps)

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

import time

from PyQt6.QtCore import QThread, pyqtSignal

from src import Connector, IMPORTANT_DATA

class Detector(QThread):
	update_data_signal = pyqtSignal()

	def __init__(self, logger):
		super(Detector, self).__init__()
		self._log = logger
		self._connector = Connector()

	def set_ip(self, ip: str):
		self._connector.set_ip(ip)

	def con(self) -> None:
		try:
			IMPORTANT_DATA.SerialNum = self._connector.connect()
			IMPORTANT_DATA.connect = True
		except ValueError as err:  # Если не пройдена верификация подключения
			raise ValueError(str(err))
		# except:  # Если не установлено соединение
		# 	return False

	def coff(self) -> None:
		try:
			self._connector.disconnect()
			IMPORTANT_DATA.SerialNum = "AAAAA-AAA-AAA-AAAA"
			IMPORTANT_DATA.connect = False
		except ValueError as err:  # Если не пройдена верификация подключения
			raise ValueError(str(err))

	def run(self):
		while True:
			try:
				data_list = self._connector.request()
				IMPORTANT_DATA.radio_impulse = int(data_list[0].decode("utf-8"))
				IMPORTANT_DATA.radio_noise = float(data_list[1].decode("utf-8"))
				IMPORTANT_DATA.radio_signal_spectrum_width = float(data_list[2].decode("utf-8"))
				IMPORTANT_DATA.radio_signal_duration = int(data_list[3].decode("utf-8"))
				IMPORTANT_DATA.radio_transfer_rate = int(data_list[4].decode("utf-8"))
				IMPORTANT_DATA.radio_antenna_impedance = int(data_list[5].decode("utf-8"))
				IMPORTANT_DATA.radio_antenna_directivity = float(data_list[6].decode("utf-8"))
				IMPORTANT_DATA.radio_signal_strength = float(data_list[7].decode("utf-8"))
				IMPORTANT_DATA.compass_magnetic_field = int(data_list[8].decode("utf-8"))
				IMPORTANT_DATA.compass_tilt_angle = int(data_list[9].decode("utf-8"))
				IMPORTANT_DATA.compass_north_direction = int(data_list[10].decode("utf-8"))
				IMPORTANT_DATA.compass_field_strength = float(data_list[11].decode("utf-8"))
				IMPORTANT_DATA.compass_temperature = int(data_list[12].decode("utf-8"))
				IMPORTANT_DATA.infrared_frequency_of_wavefront = float(data_list[13].decode("utf-8"))
				IMPORTANT_DATA.infrared_wavelength = float(data_list[14].decode("utf-8"))
				IMPORTANT_DATA.infrared_signal_strength = float(data_list[15].decode("utf-8"))
				IMPORTANT_DATA.infrared_signal_power = float(data_list[16].decode("utf-8"))
				IMPORTANT_DATA.infrared_reception_angle = int(data_list[17].decode("utf-8"))
				IMPORTANT_DATA.infrared_transfer_rate = int(data_list[18].decode("utf-8"))
				IMPORTANT_DATA.ultrasound_frequency_of_wavefront = float(data_list[19].decode("utf-8"))
				IMPORTANT_DATA.ultrasound_wavelength = float(data_list[20].decode("utf-8"))
				IMPORTANT_DATA.ultrasound_signal_strength = float(data_list[21].decode("utf-8"))
				IMPORTANT_DATA.ultrasound_signal_power = float(data_list[22].decode("utf-8"))
				IMPORTANT_DATA.ultrasound_resolution = float(data_list[23].decode("utf-8"))
				IMPORTANT_DATA.ultrasound_transfer_rate = int(data_list[24].decode("utf-8"))
				IMPORTANT_DATA.link_transfer_rate = int(data_list[25].decode("utf-8"))
				IMPORTANT_DATA.link_frequency_range = int(data_list[26].decode("utf-8"))
				IMPORTANT_DATA.link_signal_strength = float(data_list[27].decode("utf-8"))
				IMPORTANT_DATA.link_signal_power = float(data_list[28].decode("utf-8"))
				IMPORTANT_DATA.link_noise = float(data_list[29].decode("utf-8"))
				IMPORTANT_DATA.link_signal_spectrum_width = float(data_list[30].decode("utf-8"))
				IMPORTANT_DATA.link_interference_level = float(data_list[31].decode("utf-8"))
				IMPORTANT_DATA.link_bit_error_rate = int(data_list[32].decode("utf-8"))
				IMPORTANT_DATA.link_transmission_power = float(data_list[33].decode("utf-8"))
				IMPORTANT_DATA.stethoscope_sound_amplitude = float(data_list[34].decode("utf-8"))
				IMPORTANT_DATA.stethoscope_sound_frequency = float(data_list[35].decode("utf-8"))
				IMPORTANT_DATA.stethoscope_sound_pressure = int(data_list[36].decode("utf-8"))
				IMPORTANT_DATA.stethoscope_sound_direction = int(data_list[37].decode("utf-8"))
				IMPORTANT_DATA.stethoscope_transfer_rate = int(data_list[38].decode("utf-8"))
				self.update_data_signal.emit()
			except ValueError as err:  # Если не пройдена верификация данных
				self._log.fail(message_text=str(err))
				# self.consoleBrowser.append(self._log.buffer().get_data()[-1])
			time.sleep(0.3)

	def terminate(self):
		if not self._connector.isConnected:
			super().terminate()
		else:
			raise ConnectionError("The process cannot be terminated while the connection is established")

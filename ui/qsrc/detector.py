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
				IMPORTANT_DATA.radio_signal = float(data_list[0].decode("utf-8"))
				IMPORTANT_DATA.radio_amplitude = int(data_list[1].decode("utf-8"))
				IMPORTANT_DATA.compass_radius = int(data_list[2].decode("utf-8"))
				IMPORTANT_DATA.infrared_signal = float(data_list[3].decode("utf-8"))
				IMPORTANT_DATA.infrared_data = data_list[4].decode("utf-8")
				IMPORTANT_DATA.ultrasound_signal = int(data_list[5].decode("utf-8"))
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

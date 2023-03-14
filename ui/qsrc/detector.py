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

from src import IMPORTANT_DATA

class Detector(QThread):
	update_data_signal = pyqtSignal()

	def __init__(self):
		super(Detector, self).__init__()

	def run(self):
		# In the future, connection to the device will be implemented here
		while True:
			# Data acquisition simulation
			IMPORTANT_DATA.radio_signal = 101.4
			IMPORTANT_DATA.radio_amplitude = 20
			IMPORTANT_DATA.compass_radius = 70
			IMPORTANT_DATA.infrared_signal = 0.9
			IMPORTANT_DATA.infrared_data = "2 (Exit)"
			IMPORTANT_DATA.ultrasound_signal = 10778
			self.update_data_signal.emit()
			time.sleep(0.3)
			IMPORTANT_DATA.radio_signal = 97.5
			IMPORTANT_DATA.radio_amplitude = 28
			IMPORTANT_DATA.compass_radius = 76
			IMPORTANT_DATA.infrared_signal = 17.1
			IMPORTANT_DATA.infrared_data = "5 (Clear)"
			IMPORTANT_DATA.ultrasound_signal = 96333
			self.update_data_signal.emit()
			time.sleep(0.3)

	def terminate(self):
		# In the future, disconnection from the device will be implemented here
		super().terminate()

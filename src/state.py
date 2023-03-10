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

class Draws:
	# Global settings
	tab = 0
	window_height = 0
	window_width = 0
	connect = False
	IPAddr = "000.000.000.000"
	Port = "00000"

	# Extra settings
	tfont = None
	text1 = ""
	text2 = ""
	tpixmap = ""

	# Radio wiretapping data
	radio_signal = 0.0
	radio_amplitude = 0
	radio_initphase = 0

	# Compass wiretapping data
	compass_radius = 0

	# Infrared wiretapping data
	infrared_signal = 0.0
	infrared_data = ""

	# Ultrasound wiretapping data
	ultrasound_signal = 0.0

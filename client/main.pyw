"""
The main file that starts the program.
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

import os, sys
from configparser import ConfigParser

from PyQt6.QtWidgets import QApplication
from qdarktheme import setup_theme

from ui import WiretappingScaner

from src import IMPORTANT_DATA

if __name__ == '__main__':
	if not os.path.exists('data'):
		os.makedirs('data')

	if not os.path.isfile("data/config.ini"):
		IMPORTANT_DATA.appearance = "dark"
		IMPORTANT_DATA.accent_color = "#34C759"
	else:
		config = ConfigParser()
		config.read("data/config.ini")
		IMPORTANT_DATA.appearance = config.get("Color", "appearance")
		IMPORTANT_DATA.accent_color = config.get("Color", "accent_color")

	app = QApplication(sys.argv)
	setup_theme(theme=IMPORTANT_DATA.appearance, custom_colors={"primary": IMPORTANT_DATA.accent_color})
	ui = WiretappingScaner()
	ui.show()
	sys.exit(app.exec())

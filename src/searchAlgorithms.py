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

import os

def lastIndex(file_name: str, number_format: str) -> str:
	"""
	Imagine that we need to do a numbered search through a file with one name, for example,
	IRDrawFrameScreen.png, and the numbering, respectively, will be IRDrawFrameScreen0001.png,
	IRDrawFrameScreen0002.png, etc. The function will do everything for the programmer. It is
	enough to pass the file name (it is also possible with the full path to the file) and the
	numeric enumeration format (in our case '{:04}'). We get the line:
	`lastIndex('IRDrawFrameScreen.png', '{:04}')`
	This function will return the next file number after the last one (this is very convenient
	for saving a file) in the same format (i.e. string) that you need to use in the name of
	the new file, so that the next time the algorithm continues to work:
	`f"IRDrawFrameScreen{lastIndex('IRDrawFrameScreen.png', '{:04}')}.png"')`
	This is the name of the new file. You can save:
	`self.IRDrawFrame.grab().save(f"IRDrawFrameScreen{lastIndex('IRDrawFrameScreen.png', '{:04}')}.png")`
	Another example:
	`with open(f"log{lastIndex('log.txt', '{:07}')}.txt", "wt") as save: save.write(self.consoleBrowser.toPlainText())`

	:param file_name: Name (possibly path) of the file
	:param number_format: Digital format
	:return: The next file number in the format
	"""
	value = 0
	parts_file_name = file_name.split(".")
	for i in range(1, 0xffffffff):
		path = f"{parts_file_name[0]}{number_format.format(i)}" if len(parts_file_name) == 1 else \
			f"{'.'.join(parts_file_name[:-1])}{number_format.format(i)}.{parts_file_name[-1]}"
		if not os.path.isfile(path):
			value = i
			break
	return number_format.format(value)

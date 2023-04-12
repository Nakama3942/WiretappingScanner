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

import socket

class Connector:
	def __init__(self, ip: str = '192.168.0.0'):
		self._ip = ip
		self._port = 12556
		self._sock: socket = None
		self.isConnected = False

	def set_ip(self, ip: str):
		if not self.isConnected:
			self._ip = ip

	def connect(self) -> bool:
		self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self._sock.connect((self._ip, self._port))
			self._sock.sendall(b'LED ON')
			self.isConnected = True
			return True
		except:
			return False

	def disconnect(self) -> bool:
		try:
			self._sock.sendall(b'LED OFF')
			self._sock.close()
			self.isConnected = False
			return True
		except:
			return False

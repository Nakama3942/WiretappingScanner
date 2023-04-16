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

import socket, re

def _verify(connection_packet: bytes) -> str:
	serial_number = ""
	if connection_packet.startswith(b"\x08\x07\x00\x01") and connection_packet.endswith(b"\x04\x1b"):
		if not re.search(b"\x08\x07\x00\x01", connection_packet):
			ValueError("Broken header")

		if not re.search(b"\x08\x07\x00\x01(.+?)\x05\x02", connection_packet):
			ValueError("There is data between program and serial number")

		if program_name := re.search(b"\x05\x02(.+?)\x03", connection_packet):
			if program_name != b"WIRETAPPING-SCANER":
				ValueError("Broken program name")

		if not re.search(b"\x03(.+?)\x1b\x01", connection_packet):
			ValueError("There is data between program and serial number")

		if serial_match := re.search(b"\x1b\x01(.+?)\x18\x1a", connection_packet):
			if re.match(b'^[A-Z0-9]{5}-[A-Z0-9]{3}-[A-Z0-9]{3}-[A-Z0-9]{4}$', serial_match.group(1)):
				serial_number = serial_match.group(1).decode("utf-8")
			else:
				ValueError("Serial number format is invalid")

		if not re.search(b"\x18\x1a(.+?)\x16\x01", connection_packet):
			ValueError("There is data between program and serial number")

		if device_status := re.search(b"\x16\x01(.+?)\x04", connection_packet):
			if device_status != b"OK":
				ValueError("Status is not OK")

		if not re.search(b"\x04(.+?)\x1b", connection_packet):
			ValueError("There is data between program and serial number")

		if not re.search(b"\x1b", connection_packet):
			ValueError("Broken end")
	else:
		ValueError("Invalid packet")
	return serial_number

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
			self._sock.sendall(b'CON')
			# got connection packet data
			# b"\x08\x07\x00\x01\x05\x02\x57\x49\x52\x45\x54\x41\x50\x50\x49\x4e\x47\x2d\x53\x43\x41\x4e\x45\x52\x03\x1b\x01\x41\x51\x57\x5a\x45\x2d\x42\x43\x45\x2d\x59\x50\x41\x2d\x4d\x4f\x52\x48\x18\x1a\x16\x01\x4f\x4b\x04\x1b"
			self.isConnected = True
			return True
		except:
			return False

	def request(self) -> bool:
		try:
			# Заполнение данными будет тут
			self._sock.sendall(b'EXC')
			return True
		except:
			return False

	def disconnect(self) -> bool:
		try:
			self._sock.sendall(b'COFF')
			self._sock.close()
			self.isConnected = False
			return True
		except:
			return False

if __name__ == "__main__":
	data_bytes = b"\x08\x07\x00\x01\x05\x02\x57\x49\x52\x45\x54\x41\x50\x50\x49\x4e\x47\x2d\x53\x43\x41\x4e\x45\x52\x03\x1b\x01\x41\x51\x57\x5a\x45\x2d\x42\x43\x45\x2d\x59\x50\x41\x2d\x4d\x4f\x52\x48\x18\x1a\x16\x01\x4f\x4b\x04\x1b"
	print(_verify(data_bytes))

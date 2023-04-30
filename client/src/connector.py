"""
Stores a class that connects software to a device and generalizes commands and data.
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

import socket, re

def _connection_verify(connection_packet: bytes) -> str:
	serial_number = ""
	if connection_packet.startswith(b"\x08\x07\x00\x01") and connection_packet.endswith(b"\x1b"):
		if not re.search(b"\x08\x07\x00\x01\x05\x02", connection_packet):
			raise ValueError("Broken header")
		if re.search(b"\x05\x02(.+?)\x03", connection_packet).group(1) != b"WIRETAPPING-SCANER":
			raise ValueError("Broken program name")
		if not re.search(b"\x03\x05\x01", connection_packet):
			raise ValueError("There is data between program name and serial number")
		if not re.search(b"\x18\x1a\x16\x01", connection_packet):
			raise ValueError("There is data between serial number and device status")
		if re.search(b"\x16\x01(.+?)\x04", connection_packet).group(1) != b"OK":
				raise ValueError("Status is not OK")
		if not re.search(b"\x04\x1b", connection_packet):
			raise ValueError("Broken footer")
		if serial_match := re.search(b"\x05\x01(.+?)\x18\x1a", connection_packet):
			if re.match(b'^[A-Z0-9]{5}-[A-Z0-9]{3}-[A-Z0-9]{3}-[A-Z0-9]{4}$', serial_match.group(1)):
				serial_number = serial_match.group(1).decode("utf-8")
			else:
				raise ValueError("Serial number format is invalid")
	else:
		raise ValueError("Invalid packet")
	return serial_number

def _data_verify(data_packet: bytes) -> list:
	data = []
	if data_packet.startswith(b"\x08\x07\x16") and data_packet.endswith(b"\x1f\x1b"):
		if not re.search(b"\x08\x07\x16\x1e", data_packet):
			raise ValueError("Broken header")
		if not re.search(b"\x1e\x1f\x1b", data_packet):
			raise ValueError("Broken footer")
		for datas in data_packet.split(b"\x1e")[1:-1]:
			data.append(datas)
	else:
		raise ValueError("Invalid packet")
	return data

def _disconnection_verify(disconnection_packet: bytes) -> bool:
	if disconnection_packet.startswith(b"\x08\x07\x00\x04") and disconnection_packet.endswith(b"\x18\x1b"):
		if not re.search(b"\x08\x07\x00\x04\x16\x01", disconnection_packet):
			raise ValueError("Broken header")
		if re.search(b"\x16\x01(.+?)\x04", disconnection_packet).group(1) != b"STOP":
			raise ValueError("Status is not STOP")
		if not re.search(b"\x04\x18\x1b", disconnection_packet):
			raise ValueError("Broken footer")
	else:
		raise ValueError("Invalid packet")
	return True

class Connector:
	def __init__(self, ip: str = '192.168.0.0'):
		self._ip = ip
		self._port = 12556
		self._sock: socket = None
		self.isConnected = False

	def set_ip(self, ip: str):
		if not self.isConnected:
			self._ip = ip

	def connect(self) -> str:
		try:
			self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self._sock.connect((self._ip, self._port))
			self._sock.sendall(b'CON_ON')
			connection_bytes = self._sock.recv(53)
			serial = _connection_verify(connection_bytes)  # Верификация ответа
			self.isConnected = True
			return serial
		except ValueError as err:  # Если не пройдена верификация подключения
			raise ValueError(str(err))

	def request(self) -> list:
		try:
			self._sock.sendall(b'EXEC_REQ')
			# data_bytes = self._sock.recv(142)
			buffer_size = 256
			data_bytes = b''
			while True:
				chunk = self._sock.recv(1)  # чтение одного байта
				if not chunk:
					break  # если нет данных, выходим из цикла
				data_bytes += chunk
				if len(data_bytes) >= buffer_size or chunk == b'\x1b':
					break  # достигнут максимальный размер буфера или найден символ окончания пакета
			return _data_verify(data_bytes)  # Верификация ответа
		except ValueError as err:  # Если не пройдена верификация данных
			raise ValueError(str(err))

	def disconnect(self) -> None:
		try:
			self._sock.sendall(b'CON_OFF')
			disconnection_bytes = self._sock.recv(13)
			if _disconnection_verify(disconnection_bytes):  # Верификация ответа
				self._sock.close()
			self.isConnected = False
		except ValueError as err:  # Если не пройдена верификация отключения
			raise ValueError(str(err))

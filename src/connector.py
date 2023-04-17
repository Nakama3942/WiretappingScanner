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

def _connection_verify(connection_packet: bytes) -> str:
	serial_number = ""
	if connection_packet.startswith(b"\x08\x07\x00\x01") and connection_packet.endswith(b"\x1b"):
		if not re.search(b"\x08\x07\x00\x01\x05\x02", connection_packet):
			raise ValueError("Broken header")

		if re.search(b"\x05\x02(.+?)\x03", connection_packet).group(1) != b"WIRETAPPING-SCANER":
			raise ValueError("Broken program name")

		if not re.search(b"\x03\x05\x01", connection_packet):
			raise ValueError("There is data between program name and serial number")

		if serial_match := re.search(b"\x05\x01(.+?)\x18\x1a", connection_packet):
			if re.match(b'^[A-Z0-9]{5}-[A-Z0-9]{3}-[A-Z0-9]{3}-[A-Z0-9]{4}$', serial_match.group(1)):
				serial_number = serial_match.group(1).decode("utf-8")
			else:
				raise ValueError("Serial number format is invalid")

		if not re.search(b"\x18\x1a\x16\x01", connection_packet):
			raise ValueError("There is data between serial number and device status")

		if re.search(b"\x16\x01(.+?)\x04", connection_packet).group(1) != b"OK":
				raise ValueError("Status is not OK")

		if not re.search(b"\x04\x1b", connection_packet):
			raise ValueError("Broken footer")
	else:
		raise ValueError("Invalid packet")
	return serial_number

def _data_verify(data_packet: bytes) -> list:
	data = []
	if data_packet.startswith(b"\x08\x07\x16") and data_packet.endswith(b"\x1f\x1b"):
		if not re.search(b"\x08\x07\x16\x1e", data_packet):
			raise ValueError("Broken header")
		for datas in data_packet.split(b"\x1e")[1:-1]:
			data.append(datas)
		if not re.search(b"\x1e\x1f\x1b", data_packet):
			raise ValueError("Broken footer")
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

# Temporary class
class Connector:
	def __init__(self, ip: str = '192.168.0.0'):
		self._ip = ip
		self._port = 12556
		self._sock: socket = None
		self.isConnected = False
		self.__tempCount = 0  # Потом удалить

	def set_ip(self, ip: str):
		if not self.isConnected:
			self._ip = ip

	def connect(self) -> str:
		try:
			# Симуляция соединения
			# Симуляция подключения
			# Симуляция отправки сигнала
			connection_bytes = b"\x08\x07\x00\x01\x05\x02\x57\x49\x52\x45\x54\x41\x50\x50\x49\x4e\x47\x2d\x53\x43\x41\x4e\x45\x52\x03\x05\x01\x41\x51\x57\x5a\x45\x2d\x42\x43\x45\x2d\x59\x50\x41\x2d\x4d\x4f\x52\x48\x18\x1a\x16\x01\x4f\x4b\x04\x1b"  # Симуляция получения ответа
			serial = _connection_verify(connection_bytes)  # Верификация ответа
			self.isConnected = True
			return serial
		except ValueError as err:  # Если не пройдена верификация подключения
			raise ValueError(str(err))
		# except:  # Если не установлено соединение
		# 	return False

	# Real
	# def request(self) -> list:
	# 	try:
	# 		# Симуляция отправки сигнала
	# 		data_bytes = b"\x08\x07\x16\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x00\x1e\x00\x00\x00\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x1f\x1b"  # Симуляция получения ответа
	# 		return _data_verify(data_bytes)  # Верификация ответа
	# 	except ValueError as err:  # Если не пройдена верификация данных
	# 		raise ValueError(str(err))

	# Temporary
	def request(self) -> list:
		try:
			if self.__tempCount == 0:
				data_bytes = b"\x08\x07\x16\x1e\x31\x30\x31\x2e\x34\x1e\x32\x30\x1e\x37\x30\x1e\x30\x2e\x39\x1e\x32\x20\x28\x45\x78\x69\x74\x29\x1e\x31\x30\x37\x37\x38\x1e\x1f\x1b"
				self.__tempCount += 1
			else:
				data_bytes = b"\x08\x07\x16\x1e\x39\x37\x2e\x35\x1e\x32\x38\x1e\x37\x36\x1e\x31\x37\x2e\x31\x1e\x35\x20\x28\x43\x6c\x65\x61\x72\x29\x1e\x39\x36\x33\x33\x33\x1e\x1f\x1b"
				self.__tempCount -= 1
			return _data_verify(data_bytes)
		except ValueError as err:
			raise ValueError(str(err))

	def disconnect(self) -> None:
		try:
			# Симуляция отправки сигнала
			disconnection_bytes = b"\x08\x07\x00\x04\x16\x01\x53\x54\x4f\x50\x04\x18\x1b"  # Симуляция получения ответа
			if _disconnection_verify(disconnection_bytes):  # Верификация ответа
				pass # Симуляция отключения
			self.isConnected = False
		except ValueError as err:  # Если не пройдена верификация отключения
			raise ValueError(str(err))

# Real class:
# class Connector:
# 	def __init__(self, ip: str = '192.168.0.0'):
# 		self._ip = ip
# 		self._port = 12556
# 		self._sock: socket = None
# 		self.isConnected = False
#
# 	def set_ip(self, ip: str):
# 		if not self.isConnected:
# 			self._ip = ip
#
# 	def connect(self) -> bool:
# 		self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 		try:
# 			self._sock.connect((self._ip, self._port))
# 			self._sock.sendall(b'CON')
# 			self.isConnected = True
# 			return True
# 		except:
# 			return False
#
# 	def request(self) -> bool:
# 		try:
# 			# Заполнение данными будет тут
# 			self._sock.sendall(b'EXC')
# 			return True
# 		except:
# 			return False
#
# 	def disconnect(self) -> bool:
# 		try:
# 			self._sock.sendall(b'COFF')
# 			self._sock.close()
# 			self.isConnected = False
# 			return True
# 		except:
# 			return False

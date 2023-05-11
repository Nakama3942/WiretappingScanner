"""
Stores a class that connects software to a device and generalizes commands and data.
\n
To create package standards, I was inspired by the following ASCII table:
https://www.asciitable.com/
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

from socket import socket, AF_INET, SOCK_STREAM
from re import search, match

def _connection_verify(connection_packet: bytes) -> str:
	"""
	Connection package validation function.

	:param connection_packet: Connection package
	:return: the serial number of the device
	"""
	serial_number = ""
	if connection_packet.startswith(b"\x08\x07\x00\x01") and connection_packet.endswith(b"\x1b"):
		if not search(b"\x08\x07\x00\x01\x05\x02", connection_packet):
			raise ValueError("Broken header")
		if search(b"\x05\x02(.+?)\x03", connection_packet).group(1) != b"WIRETAPPING-SCANER":
			raise ValueError("Broken program name")
		if not search(b"\x03\x05\x01", connection_packet):
			raise ValueError("There is data between program name and serial number")
		if not search(b"\x18\x1a\x16\x01", connection_packet):
			raise ValueError("There is data between serial number and device status")
		if search(b"\x16\x01(.+?)\x04", connection_packet).group(1) != b"OK":
			raise ValueError("Status is not OK")
		if not search(b"\x04\x1b", connection_packet):
			raise ValueError("Broken footer")
		if serial_match := search(b"\x05\x01(.+?)\x18\x1a", connection_packet):
			if match(b'^[A-Z0-9]{5}-[A-Z0-9]{3}-[A-Z0-9]{3}-[A-Z0-9]{4}$', serial_match.group(1)):
				serial_number = serial_match.group(1).decode("utf-8")
			else:
				raise ValueError("Serial number format is invalid")
	else:
		raise ValueError("Invalid packet")
	return serial_number

def _data_verify(data_packet: bytes) -> list:
	"""
	Data package validation function.

	:param data_packet: Data package
	:return: a list of data
	"""
	data = []
	if data_packet.startswith(b"\x08\x07\x16") and data_packet.endswith(b"\x1f\x1b"):
		if not search(b"\x08\x07\x16\x1e", data_packet):
			raise ValueError("Broken header")
		if not search(b"\x1e\x1f\x1b", data_packet):
			raise ValueError("Broken footer")
		for datas in data_packet.split(b"\x1e")[1:-1]:
			data.append(datas)
	else:
		raise ValueError("Invalid packet")
	return data

def _disconnection_verify(disconnection_packet: bytes) -> bool:
	"""
	Disconnection package validation function.

	:param disconnection_packet: Disconnection package
	:return: the result of the disconnection
	"""
	if disconnection_packet.startswith(b"\x08\x07\x00\x04") and disconnection_packet.endswith(b"\x18\x1b"):
		if not search(b"\x08\x07\x00\x04\x16\x01", disconnection_packet):
			raise ValueError("Broken header")
		if search(b"\x16\x01(.+?)\x04", disconnection_packet).group(1) != b"STOP":
			raise ValueError("Status is not STOP")
		if not search(b"\x04\x18\x1b", disconnection_packet):
			raise ValueError("Broken footer")
	else:
		raise ValueError("Invalid packet")
	return True

class Connector:
	"""
	Class for configuring and establishing a connection with the Wiretapping Scanner device.
	"""

	def __init__(self):
		self._ip = ""
		self._port = 12556
		self._sock = None
		self.isConnected = False

	def set_ip(self, ip: str) -> None:
		"""
		Sets the IP address of the esp32.

		:param ip: IP address of the esp32 in the local network
		"""
		if not self.isConnected:
			self._ip = ip

	def connect(self) -> str:
		"""
		It establishes a connection with the device, receives a response packet, checks it, and
		if the whole packet is received, the connection is considered reliable and the received
		serial number of the device is returned.

		:return: the serial number of the device
		"""
		try:
			self._sock = socket(AF_INET, SOCK_STREAM)
			self._sock.connect((self._ip, self._port))
			self._sock.sendall(b'CON')
			connection_bytes = self._sock.recv(53)
			serial = _connection_verify(connection_bytes)  # Response verification
			self.isConnected = True
			return serial
		except ValueError as err:
			raise ValueError(str(err))

	def request(self) -> list:
		"""
		Sends a request to receive data and reads the packet byte by byte. After
		the method starts parsing the packet into a list of bytes and returns it.

		:return: a list of data
		"""
		try:
			self._sock.sendall(b'EXR')
			buffer_size = 256
			data_bytes = b''
			while True:
				chunk = self._sock.recv(1)  # Reading one byte
				if not chunk:
					break  # If there is no data, exit the loop
				data_bytes += chunk
				if len(data_bytes) >= buffer_size or chunk == b'\x1b':
					break  # Maximum buffer size reached or end-of-packet byte found
			return _data_verify(data_bytes)  # Response verification
		except ValueError as err:
			raise ValueError(str(err))

	def disconnect(self) -> None:
		"""
		Sends a disconnect request and, in case of a positive response, disconnects the connection.
		"""
		try:
			self._sock.sendall(b'COFF')
			disconnection_bytes = self._sock.recv(13)
			if _disconnection_verify(disconnection_bytes):  # Response verification
				self._sock.close()
			self.isConnected = False
		except ValueError as err:
			raise ValueError(str(err))

"""
A wrapper over a library that processes packages.
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

# import ctypes
#
# class Package:
# 	def __init__(self):
# 		# загрузить библиотеку
# 		self.result = None
# 		self.output_data = None
# 		self.bytes = None
# 		self.package = ctypes.cdll.LoadLibrary('./package.dll')
# 		self.array_type = None
# 		# объявить аргументы и типы возвращаемых значений функций
# 		self.package.packaging.argtypes = [ctypes.POINTER(ctypes.c_int * 10), ctypes.c_int]
# 		self.package.packaging.restype = ctypes.POINTER(ctypes.c_ubyte * 40)
# 		self.package.unpackaging.argtypes = [ctypes.POINTER(ctypes.c_ubyte * 40), ctypes.c_int]
# 		self.package.unpackaging.restype = ctypes.POINTER(ctypes.c_int * 10)
#
# 	def packaging(self, data, size):
# 		self.array_type = ctypes.c_int * size
# 		input_data = self.array_type(*data)
# 		byte_array = ctypes.cast(input_data, ctypes.POINTER(ctypes.c_int * 10))
# 		self.bytes = self.package.packaging(byte_array, ctypes.c_int(size))
# 		print(list(byte_array.contents))
# 		print(list(self.bytes.contents))
# 		return self.bytes
#
# 	def unpackaging(self, my_bytes, size):
# 		self.output_data = self.package.unpackaging(my_bytes, ctypes.c_int(size))
# 		self.result = ctypes.cast(self.output_data, ctypes.POINTER(self.array_type)).contents
# 		return self.result
#
# if __name__ == "__main__":
# 	data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 	pack = Package()
# 	b = pack.packaging(data1, 10)
# 	# for i in list(b):
# 	# 	print(hex(i))
# 	res = pack.unpackaging(b, 40)
# 	for i in list(res):
# 		print(hex(i))

def unpack_bytes(bytes_pack):
	result = []
	for i in range(0, len(bytes_pack), 4):
		result.append(int.from_bytes(bytes=bytes_pack[i:i + 4], byteorder='big'))
	return result

if __name__ == "__main__":
	# [15, 19, 99, 197, 50, 50, 51, 99, 17000, 99]
	data = b"\x00\x00\x00\x0f\x00\x00\x00\x13\x00\x00\x00\x63\x00\x00\x00\xc5\x00\x00\x00\x32\x00\x00\x00\x32\x00\x00\x00\x33\x00\x00\x00\x63\x00\x00\x42\x68\x00\x00\x00\x63"
	print(unpack_bytes(data))

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

import nmap

def getHost():
	hosts = []

	scanner = nmap.PortScanner()
	scanner.scan(hosts='192.168.0.0/24', arguments='-sn -T5 -v')

	for host in scanner.all_hosts():
		if 'mac' in scanner[host]['addresses']:
			if scanner[host]['status']['state'] == 'up':
				mac_address = scanner[host]['addresses']['mac']
				ip_address = scanner[host]['addresses']['ipv4']
				# print(f"IP: {ip_address}\tMAC: {mac_address}")  # Test
				hosts.append((ip_address, mac_address))
		else:
			if scanner[host]['status']['state'] == 'up':
				ip_address = scanner[host]['addresses']['ipv4']
				# print(f"IP: {ip_address}")  # Test
				hosts.append((ip_address, None))

	return hosts

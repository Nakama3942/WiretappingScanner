"""
A function that uses Nmap to find hosts on a local network.
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

from subprocess import run, PIPE, TimeoutExpired
from nmap import PortScanner, PortScannerError
from glob import glob

# def gotNmap() -> bool:
# 	try:
# 		result = run(['nmap', '--version'], stdout=PIPE, stderr=PIPE)
# 		if result.returncode == 0:
# 			return True
# 		else:
# 			return False
# 	except FileNotFoundError:
# 		return False

def getHost(_timeout: int):
	hosts = []
	scanner = PortScanner()
	try:
		# scanner.scan(hosts=f'192.168.{glob("*.ip")[0].split(".")[0]}.0/24', arguments='-sn -T5 -v', timeout=_timeout)
		cmd = f'nmap 192.168.{glob("*.ip")[0].split(".")[0]}.0/24 -sn -T5 -v -oX -'
		result = run(cmd.split(), stdout=PIPE, stderr=PIPE, timeout=_timeout, shell=True)
		if not result.returncode:
			scanner.analyse_nmap_xml_scan(result.stdout.decode('utf-8'))
		else:
			raise PortScannerError(f"Error executing nmap: {result.stderr.decode('utf-8')}")
	except TimeoutExpired:
		return False, [], "Timeout expired"
	except PortScannerError as error:
		return False, [], str(error)
	except FileNotFoundError:
		return False, [], "Nmap is not installed"

	for host in scanner.all_hosts():
		if 'mac' in scanner[host]['addresses']:
			if scanner[host]['status']['state'] == 'up':
				mac_address = scanner[host]['addresses']['mac']
				ip_address = scanner[host]['addresses']['ipv4']
				hosts.append((ip_address, mac_address))
		else:
			if scanner[host]['status']['state'] == 'up':
				ip_address = scanner[host]['addresses']['ipv4']
				hosts.append((ip_address, None))
	return True, hosts, ""

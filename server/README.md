<div align="center">

[![GitHub license](https://img.shields.io/github/license/Nakama3942/WiretappingScanner?color=gold&style=for-the-badge)](https://github.com/Nakama3942/WiretappingScanner/blob/master/LICENSE)

</div>

# Wiretapping Scanner Firmware
### Content
- [Wiretapping Scanner Firmware](#wiretapping-scanner-firmware)
	- [Content](#content)
	- [Overview](#overview)
	- [LICENSE](#license)
	- [Installation](#installation)
	- [Authors](#authors)

## Overview
Device firmware that allows you to read data from sensors and allows esp32 to act as a packet server. However, local work is also supported.

## LICENSE

The full text of the license can be found at the following [link](https://github.com/Nakama3942/WiretappingScanner/blob/master/LICENSE).

> Copyright © 2023 Kalynovsky Valentin, Babii Eduard. All rights reserved.
>
> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
> You may obtain a copy of the License at
>
> http://www.apache.org/licenses/LICENSE-2.0
>
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and
> limitations under the License.

## Installation
To use the project, you need to assemble the device and flash it. The assembly diagram is presented at the root of the project.

The device does not provide for connecting and using a keyboard to enter a password, therefore, this data must be specified in the firmware itself. To do this, after copying the contents of the *WiretappingScanner_Firmware.ino* file to the ArduinoIDE sketch in the *WIFI section* of the firmware, enter the network name and network password in the *ssid* and *password* constants, respectively. After that, you can flash esp32. In the *monitor* at a *frequency of 9600*, you can view the *IP address of the esp32*, which can be used to connect in the program.

## Authors

<table align="center" style="border-width: 10; border-style: ridge">
	<tr>
		<td align="center" width="200"><a href="https://github.com/Nakama3942"><img src="https://avatars.githubusercontent.com/u/73797846?s=400&u=a9b7688ac521d739825d7003a5bd599aab74cb76&v=4" width="150px;" alt=""/><br /><sub><b>Kalynovsky Valentin</b></sub></a><sub><br />"Ideological inspirer and Author", connector</sub></td>
		<td align="center" width="200"><a href="https://github.com/Eduard-stack245"><img src="https://avatars.githubusercontent.com/u/75859740?v=4" width="150px;" alt=""/><br /><sub><b>Babii Eduard</b></sub></a><sub><br />data</sub></td>
	    <!--<td></td>-->
	</tr>
<!--
	<tr>
		<td></td>
		<td></td>
	</tr>
-->
</table>

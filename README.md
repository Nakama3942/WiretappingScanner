<div align="center">

[![template](https://img.shields.io/badge/Repository-template-darkred?style=for-the-badge)](https://github.com/Nakama3942/template_rep)
[![GitHub license](https://img.shields.io/github/license/Nakama3942/WiretappingScanner?color=gold&style=for-the-badge)](https://github.com/Nakama3942/WiretappingScanner/blob/master/LICENSE)
[![CHANGELOG](https://img.shields.io/badge/here-CHANGELOG-yellow?style=for-the-badge)](https://github.com/Nakama3942/WiretappingScanner/blob/master/CHANGELOG.md)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/Nakama3942/WiretappingScanner?label=latest%20release&logo=github&style=for-the-badge)

![GitHub last commit](https://img.shields.io/github/last-commit/Nakama3942/WiretappingScanner?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/Nakama3942/WiretappingScanner?style=for-the-badge)

![GitHub repo size](https://img.shields.io/github/repo-size/Nakama3942/WiretappingScanner?color=darkgreen&style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Nakama3942/WiretappingScanner?color=darkgreen&style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/Nakama3942/WiretappingScanner?style=for-the-badge)

</div>

# Wiretapping Scanner
### Content
- [Wiretapping Scanner](#wiretapping-scanner)
	- [Content](#content)
	- [Overview](#overview)
	- [LICENSE](#license)
	- [Installation](#installation)
	- [Troubleshooting](#troubleshooting)
	- [Authors](#authors)

## Overview
A project that allows you to track surveillance. It has radio, ultrasonic, infrared wave sensors, a ~~stethoscope~~, compass and can determine the quality of the communication signal.

- [Content](#content)

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
The project is archived in the release. It contains three repositories: software, firmware, and documentation with a device assembly scheme.

The software does not require installation. The device must be assembled according to the provided scheme. After assembly, the device must be flashed with the provided firmware. Before flashing esp32, you need to specify the name of the network and the password to which the connection will be made.

## Analyzed data
- Radio wiretapping data
	- radio impulse : seconds (s)
	- noise : decibel (dB)
	- signal spectrum width : hertz (Hz)
	- signal duration : seconds (s)
	- transfer rate : bits per second (bps)
	- antenna impedance : ohm (Ω)
	- antenna directivity : decibel (dBi)
	- signal strength : decibel (dB)

- Compass wiretapping data
	- magnetic field : microtesla (μT)
	- tilt angle : degrees (°)
	- north direction : degrees (°)
	- field strength : ampere-vits per meter (A/m)
	- temperature : degree Celsius (°C)

- Infrared wiretapping data
	- frequency of wavefront : hertz (Hz)
	- wavelength : micrometers (μm)
	- signal strength : decibel (dB)
	- signal power : decibel milliwatt (dBm)
	- reception angle : degrees (°)
	- transfer rate : bits per second (bps)

- Ultrasound wiretapping data
	- frequency of wavefront : hertz (Hz)
	- wavelength : millimeters (mm)
	- signal strength : decibel (dB)
	- signal power : decibel milliwatt (dBm)
	- resolution : millimeters (mm)
	- transfer rate : bits per second (bps)

- Link quality wiretapping data
	- transfer rate : bits per second (bps)
	- frequency range : hertz (Hz)
	- signal strength : decibel (dB)
	- signal power : decibel milliwatt (dBm)
	- noise : decibel milliwatt (dBm)
	- signal spectrum width : hertz (Hz)
	- interference level : decibel (dB)
	- bit error rate : proportion of erroneously transmitted bits (-)
	- transmission power : decibel milliwatt (dBm)

- Stethoscope wiretapping data
	- sound amplitude : decibel (dB)
	- sound frequency : hertz (Hz)
	- sound pressure : pascal (Pa)
	- sound direction : degrees (°)
	- transfer rate : bits per second (bps)


## Schemes
### Device assembly
<img src="docs/Wiretapping Scanner Schematic.svg">

### Repo
<img src="docs/Wiretapping Scanner-Wiretapping Scanner Repository.drawio.svg">

### File relationship
<img src="docs/Wiretapping Scanner-Software file tree.drawio.svg">

### Connection
<img src="docs/Wiretapping Scanner-Connection establishment algorithm.drawio.svg">

### Data transfer
<img src="docs/Wiretapping Scanner-Data establishment algorithm.drawio.svg">

### Disconnection
<img src="docs/Wiretapping Scanner-Disconnection establishment algorithm.drawio.svg">

### Firmware algorithm
<img src="docs/Wiretapping Scanner-Firmware algorithm.drawio.svg">

## Troubleshooting
All functionality has been tested by Author, but if you have problems using it, the code does not work, have suggestions for optimization or advice for improving the style of the code and the name - I invite you [here](https://github.com/Nakama3942/WiretappingScanner/blob/master/CONTRIBUTING.md) and [here](https://github.com/Nakama3942/WiretappingScanner/blob/master/CODE_OF_CONDUCT.md).

- [Content](#content)

## Authors

<table align="center" style="border-width: 10; border-style: ridge">
	<tr>
		<td align="center" width="200"><a href="https://github.com/Nakama3942"><img src="https://avatars.githubusercontent.com/u/73797846?s=400&u=a9b7688ac521d739825d7003a5bd599aab74cb76&v=4" width="150px;" alt=""/><br /><sub><b>Kalynovsky Valentin</b></sub></a><sub><br />"Ideological inspirer and Author", developer of software and connector</sub></td>
		<td align="center" width="200"><a href="https://github.com/Eduard-stack245"><img src="https://avatars.githubusercontent.com/u/75859740?v=4" width="150px;" alt=""/><br /><sub><b>Babii Eduard</b></sub></a><sub><br />"Manager", developer of device assembly and him firmware</sub></td>
	    <!--<td></td>-->
	</tr>
<!--
	<tr>
		<td></td>
		<td></td>
	</tr>
-->
</table>

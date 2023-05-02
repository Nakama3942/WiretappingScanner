/*
Firmware with the implementation of data collection and transmission.
\n
Copyright © 2023 Kalynovsky Valentin, Babii Eduard. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

// ========================================================================
//                                 INCLUDES
// ========================================================================

#include <WiFi.h>

// ========================================================================
//                                   WIFI
// ========================================================================

const char* ssid = "Enter your ssid";
const char* password = "Enter your password";

// ========================================================================
//                                   TEMP
// ========================================================================

int temp = 0; // Временное решение

// ========================================================================
//                                   DATA
// ========================================================================

// Radio wiretapping data
int radio_impulse = 0;							// seconds (s)
float radio_noise = 0.0;						// decibel (dB)
float radio_signal_spectrum_width = 0.0;		// hertz (Hz)
int radio_signal_duration = 0;					// seconds (s)
int radio_transfer_rate = 0;					// bits per second (bps)
int radio_antenna_impedance = 0;				// ohm (Ω)
float radio_antenna_directivity = 0.0;			// decibel (dBi)
float radio_signal_strength = 0.0;				// decibel (dB)

// Compass wiretapping data
int compass_magnetic_field = 0;					// microtesla (μT)
int compass_tilt_angle = 0;						// degrees (°)
int compass_north_direction = 0;				// degrees (°)
float compass_field_strength = 0.0;				// ampere-vits per meter (A/m)
int compass_temperature = 0;					// degree Celsius (°C)

// Infrared wiretapping data
float infrared_frequency_of_wavefront = 0.0;	// hertz (Hz)
float infrared_wavelength = 0.0;				// micrometers (μm)
float infrared_signal_strength = 0.0;			// decibel (dB)
float infrared_signal_power = 0.0;				// decibel milliwatt (dBm)
int infrared_reception_angle = 0;				// degrees (°)
int infrared_transfer_rate = 0;					// bits per second (bps)

// Ultrasound wiretapping data
float ultrasound_frequency_of_wavefront = 0.0;	// hertz (Hz)
float ultrasound_wavelength = 0.0;				// millimeters (mm)
float ultrasound_signal_strength = 0.0;			// decibel (dB)
float ultrasound_signal_power = 0.0;			// decibel milliwatt (dBm)
float ultrasound_resolution = 0.0;				// millimeters (mm)
int ultrasound_transfer_rate = 0;				// bits per second (bps)

// Link quality wiretapping data
int link_transfer_rate = 0;						// bits per second (bps)
int link_frequency_range = 0;					// hertz (Hz)
float link_signal_strength = 0.0;				// decibel (dB)
float link_signal_power = 0.0;					// decibel milliwatt (dBm)
float link_noise = 0.0;							// decibel milliwatt (dBm)
float link_signal_spectrum_width = 0.0;			// hertz (Hz)
float link_interference_level = 0.0;			// decibel (dB)
int link_bit_error_rate = 0;					// proportion of erroneously transmitted bits (-)
float link_transmission_power = 0.0;			// decibel milliwatt (dBm)

// Stethoscope wiretapping data
float stethoscope_sound_amplitude = 0.0;		// decibel (dB)
float stethoscope_sound_frequency = 0.0;		// hertz (Hz)
int stethoscope_sound_pressure = 0;				// pascal (Pa)
int stethoscope_sound_direction = 0;			// degrees (°)
int stethoscope_transfer_rate = 0;				// bits per second (bps)

// ========================================================================
//                               DATA GETTING
// ========================================================================

void radio()
{
	if (temp == 0)
	{
		radio_impulse = 1;
		radio_noise = 2.2;
		radio_signal_spectrum_width = 97.1;
		radio_signal_duration = 4;
		radio_transfer_rate = 5;
		radio_antenna_impedance = 6;
		radio_antenna_directivity = 7.7;
		radio_signal_strength = 20.0;
	}
	else
	{
		radio_impulse = 5;
		radio_noise = 6.6;
		radio_signal_spectrum_width = 101.4;
		radio_signal_duration = 8;
		radio_transfer_rate = 9;
		radio_antenna_impedance = 1;
		radio_antenna_directivity = 2.2;
		radio_signal_strength = 28.1;
	}
}

void compass()
{
	if (temp == 0)
	{
		compass_magnetic_field = 9;
		compass_tilt_angle = 70;
		compass_north_direction = 270;
		compass_field_strength = 3.3;
		compass_temperature = 4;
	}
	else
	{
		compass_magnetic_field = 4;
		compass_tilt_angle = 240;
		compass_north_direction = 76;
		compass_field_strength = 7.7;
		compass_temperature = 8;
	}
}

void infrared()
{
	if (temp == 0)
	{
		infrared_frequency_of_wavefront = 55.9;
		infrared_wavelength = 5.5;
		infrared_signal_strength = 95.2;
		infrared_signal_power = 7.7;
		infrared_reception_angle = 8;
		infrared_transfer_rate = 9;
	}
	else
	{
		infrared_frequency_of_wavefront = 99.2;
		infrared_wavelength = 9.9;
		infrared_signal_strength = 97.1;
		infrared_signal_power = 2.2;
		infrared_reception_angle = 3;
		infrared_transfer_rate = 4;
	}
}

void ultrasound()
{
	if (temp == 0)
	{
		ultrasound_frequency_of_wavefront = 69.2;
		ultrasound_wavelength = 1.1;
		ultrasound_signal_strength = 29.2;
		ultrasound_signal_power = 3.3;
		ultrasound_resolution = 4.4;
		ultrasound_transfer_rate = 5;
	}
	else
	{
		ultrasound_frequency_of_wavefront = 69.3;
		ultrasound_wavelength = 5.5;
		ultrasound_signal_strength = 31.6;
		ultrasound_signal_power = 7.7;
		ultrasound_resolution = 8.8;
		ultrasound_transfer_rate = 9;
	}
}

void link_quality()
{
	if (temp == 0)
	{
		link_transfer_rate = 6;
		link_frequency_range = 7;
		link_signal_strength = 29.9;
		link_signal_power = 9.9;
		link_noise = 1.1;
		link_signal_spectrum_width = 79.9;
		link_interference_level = 3.3;
		link_bit_error_rate = 4;
		link_transmission_power = 5.5;
	}
	else
	{
		link_transfer_rate = 1;
		link_frequency_range = 2;
		link_signal_strength = 39.9;
		link_signal_power = 4.4;
		link_noise = 5.5;
		link_signal_spectrum_width = 61.2;
		link_interference_level = 7.7;
		link_bit_error_rate = 8;
		link_transmission_power = 9.9;
	}
}

void stethoscope()
{
	if (temp == 0)
	{
		stethoscope_sound_amplitude = 36.6;
		stethoscope_sound_frequency = 76.6;
		stethoscope_sound_pressure = 8;
		stethoscope_sound_direction = 9;
		stethoscope_transfer_rate = 1;
	}
	else
	{
		stethoscope_sound_amplitude = 37.8;
		stethoscope_sound_frequency = 88.9;
		stethoscope_sound_pressure = 3;
		stethoscope_sound_direction = 4;
		stethoscope_transfer_rate = 5;
	}
}

// ========================================================================
//                              DATA PACKAGING
// ========================================================================

uint8_t* connection_packet()
{
	uint8_t *packet_data = new uint8_t[53] {0x08, 0x07, 0x00, 0x01, 0x05, 0x02, 0x57, 0x49, 0x52, 0x45, 0x54, 0x41, 0x50, 0x50, 0x49, 0x4e, 0x47, 0x2d, 0x53, 0x43, 0x41, 0x4e, 0x45, 0x52, 0x03, 0x05, 0x01, 0x41, 0x51, 0x57, 0x5a, 0x45, 0x2d, 0x42, 0x43, 0x45, 0x2d, 0x59, 0x50, 0x41, 0x2d, 0x4d, 0x4f, 0x52, 0x48, 0x18, 0x1a, 0x16, 0x01, 0x4f, 0x4b, 0x04, 0x1b};
	return packet_data;
}

uint8_t* data_packet(int *size)
{
	String packet = "\x08\x07\x16\x1e"
	+ String(radio_impulse) + "\x1e"
	+ String(radio_noise, 1) + "\x1e"
	+ String(radio_signal_spectrum_width, 1) + "\x1e"
	+ String(radio_signal_duration) + "\x1e"
	+ String(radio_transfer_rate) + "\x1e"
	+ String(radio_antenna_impedance) + "\x1e"
	+ String(radio_antenna_directivity, 1) + "\x1e"
	+ String(radio_signal_strength, 1) + "\x1e"
	+ String(compass_magnetic_field) + "\x1e"
	+ String(compass_tilt_angle) + "\x1e"
	+ String(compass_north_direction) + "\x1e"
	+ String(compass_field_strength, 1) + "\x1e"
	+ String(compass_temperature) + "\x1e"
	+ String(infrared_frequency_of_wavefront, 1) + "\x1e"
	+ String(infrared_wavelength, 1) + "\x1e"
	+ String(infrared_signal_strength, 1) + "\x1e"
	+ String(infrared_signal_power, 1) + "\x1e"
	+ String(infrared_reception_angle) + "\x1e"
	+ String(infrared_transfer_rate) + "\x1e"
	+ String(ultrasound_frequency_of_wavefront, 1) + "\x1e"
	+ String(ultrasound_wavelength, 1) + "\x1e"
	+ String(ultrasound_signal_strength, 1) + "\x1e"
	+ String(ultrasound_signal_power, 1) + "\x1e"
	+ String(ultrasound_resolution, 1) + "\x1e"
	+ String(ultrasound_transfer_rate) + "\x1e"
	+ String(link_transfer_rate) + "\x1e"
	+ String(link_frequency_range) + "\x1e"
	+ String(link_signal_strength, 1) + "\x1e"
	+ String(link_signal_power, 1) + "\x1e"
	+ String(link_noise, 1) + "\x1e"
	+ String(link_signal_spectrum_width, 1) + "\x1e"
	+ String(link_interference_level, 1) + "\x1e"
	+ String(link_bit_error_rate) + "\x1e"
	+ String(link_transmission_power, 1) + "\x1e"
	+ String(stethoscope_sound_amplitude, 1) + "\x1e"
	+ String(stethoscope_sound_frequency, 1) + "\x1e"
	+ String(stethoscope_sound_pressure) + "\x1e"
	+ String(stethoscope_sound_direction) + "\x1e"
	+ String(stethoscope_transfer_rate) + "\x1e\x1f\x1b";
	*size = packet.length();
	uint8_t *packet_data = new uint8_t[*size];
	memcpy(packet_data, packet.c_str(), *size);
	return packet_data;
}

uint8_t* disconnection_packet()
{
	uint8_t *packet_data = new uint8_t[13] {0x08, 0x07, 0x00, 0x04, 0x16, 0x01, 0x53, 0x54, 0x4f, 0x50, 0x04, 0x18, 0x1b};;
	return packet_data;
}

// ========================================================================
//                                 FIRMWARE
// ========================================================================

WiFiServer server(12556); //Connection port

void setup()
{
	Serial.begin(9600);
	delay(10);

	Serial.println();
	Serial.println();
	Serial.print("Connection to " + String(ssid));

	WiFi.begin(ssid, password);

	while (WiFi.status() != WL_CONNECTED)
	{
		delay(500);
		Serial.print(".");
	}

	Serial.println("");
	Serial.println("WiFi connected");
	Serial.print("ESP32 Server: ");
	Serial.println(WiFi.localIP());
	Serial.println("");

	server.begin();
	Serial.println("Server started");
}

void loop()
{
	WiFiClient client = server.available(); //Checking for a client connection
	if (client)
	{
		Serial.println("New client connected");
		while (client.connected())
		{
			if (client.available())
			{
				String command = client.readStringUntil('\n'); //Read command
				Serial.println("Received command: " + command);

				Serial.print("Client IP: ");
				Serial.println(WiFi.localIP());
				Serial.print("Router IP: ");
				Serial.println(WiFi.gatewayIP());

				if (command == "CON") // CONNECTION ON
				{
					client.write(connection_packet(), 53);
				}
				else if (command == "EXR") // EXECUTION REQUEST
				{
					radio();
					compass();
					infrared();
					ultrasound();
					link_quality();
					stethoscope();
					int *size = new int;
					client.write(data_packet(size), *size);
					temp == 0 ? temp++ : temp--; // Временное решение
				}
				else if (command == "COFF") // CONNECTION OFF
				{
					client.write(disconnection_packet(), 13);
				}
			}
		}
	}
}

#include <WiFi.h>

const char* ssid = "F*ck you, not ssid";
const char* password = "F*ck you, not password";
//192.168.0.105

WiFiServer server(12556); //Порт для подключения

void setup()
{
	Serial.begin(9600);
	delay(10);

	Serial.println();
	Serial.println();
	Serial.print("Подключение к ");
	Serial.println(ssid);

	WiFi.begin(ssid, password);

	while (WiFi.status() != WL_CONNECTED) {
		delay(500);
		Serial.print(".");
	}

	Serial.println("");
	Serial.println("WiFi подключен");
	Serial.print("ESP32 Server: ");
	Serial.println(WiFi.localIP());
	Serial.println();

	server.begin();
	Serial.println("Сервер запущен");
}

void loop()
{
	WiFiClient client = server.available(); //Проверить наличие клиентского соединения
	if (client)
		{
		Serial.println("New client connected");
		while (client.connected())
		{
			if (client.available())
			{
				String command = client.readStringUntil('\n'); //Считывание команды
				// command.trim(); //Удалить пробелы
				Serial.print("Received command: ");
				Serial.println(command);

				Serial.print("Client IP: ");
				Serial.println(WiFi.localIP());
				Serial.print("Router IP: ");
				Serial.println(WiFi.gatewayIP());
				// Serial.print("Subnet: ");
				// Serial.println(WiFi.gatewayIP());
				// Serial.print("DNS: ");
				// Serial.println(WiFi.gatewayIP());

				if (command == "CON_ON") // CONECTION ON
				{
					client.write("\x08\x07\x00\x01\x05\x02\x57\x49\x52\x45\x54\x41\x50\x50\x49\x4e\x47\x2d\x53\x43\x41\x4e\x45\x52\x03\x05\x01\x41\x51\x57\x5a\x45\x2d\x42\x43\x45\x2d\x59\x50\x41\x2d\x4d\x4f\x52\x48\x18\x1a\x16\x01\x4f\x4b\x04\x1b", 53);
				}
				if (command == "EXEC_REQ") // EXECUTION REQUEST
				{
					client.write("\x08\x07\x16\x1e\x35\x1e\x36\x2e\x36\x1e\x31\x30\x31\x2e\x34\x1e\x38\x1e\x39\x1e\x31\x1e\x32\x2e\x32\x1e\x32\x38\x2e\x31\x1e\x34\x1e\x32\x34\x30\x1e\x37\x36\x1e\x37\x2e\x37\x1e\x38\x1e\x39\x39\x2e\x32\x1e\x39\x2e\x39\x1e\x39\x37\x2e\x31\x1e\x32\x2e\x32\x1e\x33\x1e\x34\x1e\x36\x39\x2e\x33\x1e\x35\x2e\x35\x1e\x33\x31\x2e\x36\x1e\x37\x2e\x37\x1e\x38\x2e\x38\x1e\x39\x1e\x31\x1e\x32\x1e\x33\x39\x2e\x39\x1e\x34\x2e\x34\x1e\x35\x2e\x35\x1e\x36\x31\x2e\x32\x1e\x37\x2e\x37\x1e\x38\x1e\x39\x2e\x39\x1e\x33\x37\x2e\x38\x1e\x38\x38\x2e\x39\x1e\x33\x1e\x34\x1e\x35\x1e\x1f\x1b");
				}
				if (command == "EXEC_REQCON_OFF" || command == "CON_OFFEXEC_REQ") // Слияние комманд, которое иногда избежать невозможно
				{
					client.write("\x00\x08\x07\x00\x04\x16\x01\x53\x54\x4f\x50\x04\x18\x1b", 14);
				}
				if (command == "CON_OFF") // CONECTION OFF
				{
					client.write("\x08\x07\x00\x04\x16\x01\x53\x54\x4f\x50\x04\x18\x1b", 13);
				}
			}
		}
	}
}

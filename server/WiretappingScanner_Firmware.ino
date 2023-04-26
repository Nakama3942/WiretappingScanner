#include <WiFi.h>

const char* ssid = "F*ck you, not ssid";
const char* password = "F*ck you, not password";

WiFiServer server(12556); //Порт для подключения

void setup()
{
	Serial.begin(9600);
	WiFi.begin(ssid, password); //Подключиться к сети WiFi
	while (WiFi.status() != WL_CONNECTED)
	{
		delay(1);
		Serial.println("Connecting to WiFi...");
	}
	server.begin(); //Запустить сервер
	Serial.println("Server started");
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
				command.trim(); //Удалить пробелы
				Serial.print("Received command: ");
				Serial.println(command);
				if (command == "CON")
				{
					Serial.print("Connect");
				}
				else if (command == "COFF")
				{
					Serial.print("Disconnect");
				}
				else if (command == "EXC")
				{
					Serial.print("Execution request");
				}
			}
		}
	}
	delay(1);
}

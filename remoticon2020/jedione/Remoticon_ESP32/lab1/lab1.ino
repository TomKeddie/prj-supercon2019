#include <WebOTA.h>

// Create a unique ID for the data from each NodeMCU running this code
const char* jediID = "WorkShop-ESP32-Lab1";

// Wi-Fi settings - replace with your Wi-Fi SSID and password
const char* mdns     = "REMOTICON-OTA"; // Used for MDNS resolution
//const char* ssid     = "DemoWiFi";
//const char* password = "DemoWiFi";

// IP address of server running Machinechat JEDI software
// If you changed the JEDI port number, replace 8100 with the new port
//const char* host = "192.168.1.210:8100";

// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(115200);

  Serial.println();
  Serial.println();
  Serial.println();

  for (uint8_t t = 4; t > 0; t--) {
    Serial.printf("[SETUP] WAIT %d...\r\n", t);
    Serial.flush();
    delay(500);
  }

  init_wifi(ssid, password, mdns);

  // Wait for Wi-Fi connection and show progress on serial monitor
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.flush();

  // Defaults to 8080 and "/webota"
  //webota.init(80, "/update");
}

// the loop function runs over and over again forever
void loop() {
  int md = 1000;

  webota.delay(md);
  webota.handle();
}

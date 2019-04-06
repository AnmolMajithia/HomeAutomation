#include <ESP8266WiFi.h>

// Replace with your network credentials
const char* ssid     = "<Wifi Name>";
const char* password = "<Wifi Password>";

// Set web server port number to 80
WiFiServer server(80);

// Variable to store the HTTP request
String header;

// Auxiliar variables to store the current output state
String output5State = "off";
String output4State = "off";
String output0State = "off";
String output2State = "off";

// Assign output variables to GPIO pins
const int output5 = 5;
const int output4 = 4;
const int output0 = 0;
const int output2 = 2;

void setup() {
  Serial.begin(115200);
  // Initialize the output variables as outputs
  pinMode(output5, OUTPUT);
  pinMode(output4, OUTPUT);
  pinMode(output0, OUTPUT);
  pinMode(output2, OUTPUT);
  // Set outputs to LOW
  digitalWrite(output5, LOW);
  digitalWrite(output4, LOW);
  digitalWrite(output0, LOW);
  digitalWrite(output2, LOW);
  
  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop(){
  WiFiClient client = server.available();   // Listen for incoming clients
  
  if (client) {                             // If a new client connects,
    Serial.println("New Client.");          // print a message out in the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    while (client.connected()) {            // loop while the client's connected
    if (client.available()) {             // if there's bytes to read from the client,
    char c = client.read();             // read a byte, then
    Serial.write(c);                    // print it out the serial monitor
    if (c=='1') {
      Serial.println("GPIO 5 on");
      output5State = "on";
      digitalWrite(output5, HIGH);
    } else if (c=='2') {
      Serial.println("GPIO 5 off");
      output5State = "off";
      digitalWrite(output5, LOW);
    } else if (c=='3') {
      Serial.println("GPIO 4 on");
      output4State = "on";
      digitalWrite(output4, HIGH);
    } else if (c=='4') {
      Serial.println("GPIO 4 off");
      output4State = "off";
      digitalWrite(output4, LOW);
    } else if (c=='5') {
      Serial.println("GPIO 0 on");
      output4State = "off";
      digitalWrite(output0, HIGH);
    } else if (c=='6') {
      Serial.println("GPIO 0 off");
      output4State = "off";
      digitalWrite(output0, LOW);
    } else if (c=='7') {
      Serial.println("GPIO 2 on");
      output4State = "off";
      digitalWrite(output2, HIGH);
    } else if (c=='8') {
      Serial.println("GPIO 2 off");
      output4State = "off";
      digitalWrite(output2, LOW);
    }
  }
}
} 


// Clear the header variable
header = "";
// Close the connection
client.stop();
//Serial.println("Client disconnected.");
//Serial.println("");
}

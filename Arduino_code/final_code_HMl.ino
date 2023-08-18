//Importing Libraries:


#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>
#include <Servo.h>

//Defining Network and MQTT Parameters:
byte mac[]    = {  0xDE, 0xED, 0xBA, 0xFE, 45, 0xED };
IPAddress ip(172, 16, 0, 100);
IPAddress server(44, 195, 202, 69);

//Initializing Hardware:
Servo servoMoter;

int led1=2;
int led2=3;
int buzzerpin=4;

//Callback Function:
void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";

  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.println(message);
   if (message.equals("turnonbedroomlight")) {
    // Code to turn on the bedroom light
    digitalWrite(led1, HIGH);
  }else if (message.equals("turnoffbedroomlight")) {
    // Code to turn off the bedroom light
    digitalWrite(led1, LOW);
  }else if (message.equals("turnonkitchenlight")) {
    // Code to turn on the kitchen light
    digitalWrite(led2, HIGH);
  }else if (message.equals("turnoffkitchenlight")) {
    // Code to turn off the kitchen light
    digitalWrite(led2, LOW);
  }else if (message.equals("turnonalllights")) {
    // Code to turn on the all lights
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
  }else if (message.equals("turnoffalllights")) {
    // Code to turn off the all lights
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
  }else if (message.equals("startmachine")) {
    // Code to start buzzzer
      tone(buzzerpin,1000);
  }else if (message.equals("stopmachine")) {
    // Code to to stop buzzer
      noTone(buzzerpin);
  }else if (message.equals("turnonmotor")){
      servoMoter.write(180);
  }else if (message.equals("turnoffmotor")){
      servoMoter.write(-180);
  }else{
    // Invalid command or unrecognized message
    Serial.println("Invalid command or unrecognized message.");
  }
}

/*The callback() function is executed when the Arduino receives a message from the MQTT broker
It converts the received payload (message) into a String and then checks the content of the message
Depending on the received message, it will take appropriate actions such as turning on/off LEDs or 
starting/stopping the buzzer.*/




EthernetClient ethClient;
PubSubClient client(ethClient);

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("arduinoClient45")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic","hello world");
      // ... and resubscribe
      client.subscribe("speech-to-text");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup()
{
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(buzzerpin,OUTPUT);
  servoMoter.attach(1);
  Serial.begin(57600);
  Ethernet.init(17);
  client.setServer(server, 1883);
  client.setCallback(callback);

  Ethernet.begin(mac);
  // Allow the hardware to sort itself out
  delay(1500);
}
/*The setup() function initializes the Arduino's digital pins for LED and buzzer as outputs, 
starts the Serial communication
for debugging purposes, initializes the Ethernet shield with a specific MAC address, 
sets up the MQTT client to connect to the defined server and port, and sets the callback 
function to handle incoming MQTT messages.*/
void loop()
{
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}

/*The loop() function runs continuously. It checks if the MQTT client is connected to the broker; 
if not, it calls the reconnect() function to re-establish the connection.
The client.loop() method is used to handle MQTT-related tasks and ensure communication with the broker.*/
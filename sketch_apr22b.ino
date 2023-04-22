#include <SoftwareSerial.h>
SoftwareSerial BTserial(2, 3); // RX | TX

const long baudRate = 38400;
char c = ' ';
boolean NL = true;

void setup()
{
   Serial.begin(38400);
   Serial.print("Sketch:   ");   Serial.println(__FILE__);
   Serial.print("Uploaded: ");   Serial.println(__DATE__);
   Serial.println(" ");

   BTserial.begin(baudRate);
   Serial.print("BTserial started at "); 
   Serial.println(baudRate);
   //BTserial.print("BTserial started at "); 
   //BTserial.println(baudRate);
   Serial.println(" ");
}

void loop()
{
   // Read from the Bluetooth module and send to the Arduino Serial Monitor
   if (BTserial.available())
   {
      c = BTserial.read();
      Serial.write(c);
   }

   // Read from the Serial Monitor and send to the Bluetooth module
   if (Serial.available())
   {
      c = Serial.read();
      BTserial.write(c);

      // Echo the user input to the main window. The ">" character indicates the user entered text.
      if (NL)
      {
         Serial.print(">");
         NL = false;
      }
      Serial.write(c);
      if (c == 10)
      {
         NL = true;
      }
   }
}
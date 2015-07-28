#include <DHT11.h>
int pin=2;
DHT11 dht11(pin); 
void setup()
{
   Serial.begin(9600);
  while (!Serial) {
      ; // wait for serial port to connect. Needed for Leonardo only
    }
}

void loop()
{
  int err;
  float temp, humi;
  if((err=dht11.read(humi, temp))==0)
  {
    Serial.println("*DHT11*");
    Serial.print("temperature: ");
    Serial.println(temp);
    Serial.print("humidity: ");
    Serial.println(humi);
  }
  else
  {
    Serial.println();
    Serial.print("Error No :");
    Serial.print(err);
    Serial.println();    
  }
  delay(1000); //delay for reread
}




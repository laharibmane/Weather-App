#include "DHT.h"                                              // Including the package DHT sensor library

#define DHTPIN 4                                              // Here the digital pin value '4' will now be referred to as DHTPIN
#define DHTTYPE DHT11                                         // Here the sensor 'DHT11' will be considered as DHTTYPE

DHT dht(DHTPIN,DHTTYPE);                                      // Creating an object of the DHT class



void setup()                                                  // Used to initialise the pinModes and variables
{
    Serial.begin(9600);                                       // Establishing a communication speed of 9600 bps between the sensor and arduino 
    dht.begin();                                              // To initialise the 'dht' object 
}



void loop()                                                   // To repeat the task of getting and printing the data    
{
    delay(2000);                                              // Getting the latest data every 2 seconds

    float h=dht.readHumidity();                               // Getting the humidity value in Percentage
    float t_c=dht.readTemperature();                          // Getting the temperature value in Celcius
    float t_f=dht.readTemperature(true);                      // Getting the temperature value in Fahrenhitre by passing "true" as an argument
    float heat_index=dht.computeHeatIndex(t_c,h,false);       // Finding heat index

    int rain_value=analogRead(A4);                            // Getting rain sensor data which is sensor's resistance in ohm    

    Serial.print("Humidity : ");                              // The Serial object will print Humidity Value
    Serial.print(h);  
    Serial.print(" %     ") ; 

    Serial.print("Temp in C : ");                             // The Serial object will print Temperature in Celcius Value
    Serial.print(t_c);  
    Serial.print(" C     ");

    Serial.print("Temp in F : ");                             // The Serial object will print Temperature in Fahrenhite Value
    Serial.print(t_f);  
    Serial.print(" F     ");

    if (rain_value<700)
    {
        Serial.print("Rain detection : rain_detected ");      // To indicate rain for low resistance
    }
    else
    {
        Serial.print("Rain detection : No_rain_detected ");   //  To indicate no rain for high resistance
    }

    Serial.print("Heat Index : ");                             // The Serial object will print Heat Index in Celcius Value
    Serial.print(heat_index);  
    Serial.print(" C     ");

    Serial.println();                                         // Every new data will be printed in next Line
}

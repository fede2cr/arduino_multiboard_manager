# arduino_multiboard_manager
A JSON config file with board from multiple vendors

## Description
While teaching arduino and also while hacking we have found the need to change
manualy several times a day the configuration of the Additional Board Manager
in the Arduino IDE, so that we can work with boards from vendors like Adafruit,
Sparkfun and also to be able to work with ESP8266 boards.

This is a JSON config file that can be configured in your Arduino IDE to use
multiple boards from multiple vendors.

Use this URL inside the Arduino IDE:

https://raw.githubusercontent.com/fede2cr/arduino_multiboard_manager/master/package_multiboard_index.json


## Current boards

This are some of the boards we can reliably get here in Costa Rica and are used
in different courses in Greencore Solutions.

1. Adafruit
  * URL = https://adafruit.github.io/arduino-board-index/package_adafruit_index.json 

2. ESP Community
  * URL = http://arduino.esp8266.com/stable/package_esp8266com_index.json
  * Note: Dangerous http url!

3. Moteino
  * URL = https://lowpowerlab.github.io/MoteinoCore/package_LowPowerLab_index.json

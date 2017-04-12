# arduino_multiboard_manager
A JSON config file with board from multiple vendors

# OBSOLETE REPO

I found out that what I'm trying to solve with this JSON file, can be done via CLI with one arduino command. The current JSON file will remain in it's place for a couple of months, but I'll remove it eventually.

Use this workaround:
```bash
arduino --pref boardsmanager.additional.urls=http://arduino.esp8266.com/stable/package_esp8266com_index.json,http://static.dev.sifive.com/bsp/arduino/package_sifive_index.json,https://adafruit.github.io/arduino-board-index/package_adafruit_index.json,https://lowpowerlab.github.io/MoteinoCore/package_LowPowerLab_index.json --save-prefs
```

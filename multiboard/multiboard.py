import urllib, json
url = ["https://adafruit.github.io/arduino-board-index/package_adafruit_index.json",
       "http://arduino.esp8266.com/stable/package_esp8266com_index.json",
       "https://lowpowerlab.github.io/MoteinoCore/package_LowPowerLab_index.json"]
output_list = []

for u in url:
    response = urllib.urlopen(u)
    output_list.append(json.loads(response.read()))

print(json.dumps(output_list, indent=4))

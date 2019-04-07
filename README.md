# BlackBox Network sensor
Sometimes you can't reach a certain place by wire and you want to use a wireless signal for polling sensor data.
With an inexpensive ESP8266 or ESP32 and some simple code this is a simple job.

## Prerequisites
For this project you will need one of the following:
* [ESP32](https://www.espressif.com/en/products/hardware/esp32-devkitc/overview) (Recommended)
* [NodeMCU](https://www.nodemcu.com/index_en.html)  (Based on the ESP8266 chip)
* An ESP8266 or ESP32 without USB port is also possible, but you will have to purchase a seperate USB to TTL adapter to program it.

You will also need the following software packages:
* Python and pip

## Installation
First you will have to install the flash tool for the ESP32 or ESP8266 chip.
To install this tool, run ```pip install esptool```

After this you will have to flash the MicroPython firmware onto the ESP chip. You can find the instructions here:
* [For ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
* [For ESP8266](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html)

*If You have problems installing the firmware to the ESP chip, make sure you have the boot modus set to ROM flash. You can 
enable this mode by connecting GPIO0 to GND and connecting the chip to the PC.*

If you succesfully got MicroPython running you will have to close any serial connections to the ESP device and download
ampy for transferring the program via ```pip install ampy```. After this run
```bash
ampy --port <DEVICE_PORT> put boot.py
ampy --port <DEVICE_PORT> put main.py
```

Change the settings.py settings according to your setup. The network settings are described in the settings file.
The sensor list is an array of pin numbers that are checkable. The socket port is the port that will be accessed by the Pi.
If the configuration file is filled in you can upload the settings using.
 ```bash
 ampy --port <DEVICE_PORT> put settings.py
 ```
Everytime you update the settings you will have to reflash this file.
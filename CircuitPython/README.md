# AUTOCHEER DEVICE

code by [Andy Doro](https://andydoro.com/)

using [Adafruit Feather](https://www.adafruit.com/feather) hardware\
will play an MP3 at a specified time each day

sketch can easily be modified to perform some other functions at the specified time, such as operate physical/analog noisemakers

## CircuitPython Version

### HARDWARE

* [Feather M4 Express](https://www.adafruit.com/product/3857) is need because it's fast enough to play back MP3 files

* [Adalogger FeatherWing](https://www.adafruit.com/product/2922) for PCF8523 RTC
  * & [CR1220 coin cell](https://www.adafruit.com/product/380)

* [MicroSD card](https://www.adafruit.com/product/1294) FAT formatted with "cheer.mp3"

* [FeatherWing Doubler](https://www.adafruit.com/product/2890) 
  * or [Feather Stacking Headers](https://www.adafruit.com/product/2830) for a different form factor 

* [Headphone Jack](https://www.adafruit.com/product/1699)



### SOFTWARE
#### LIBRARIES

for RTC:
* adafruit_bus_device folder
* adafruit_register folder
* adafruit_pcf8523.mpy

for SD card:
* adafruit_sdcard.mpy

cheer.mp3, place on FAT formatted SD card and insert into Music Maker\
suggestion: http://www.orangefreesounds.com/street-crowd-cheering-and-applauding/

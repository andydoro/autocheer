# AUTOCHEER DEVICE

code by [Andy Doro](https://andydoro.com/)

using [Adafruit Feather](https://www.adafruit.com/feather) hardware
will play an MP3 at a specified time each day

sketch can easily be modified to perform some other functions at the specified time, such as operate physical/analog noisemakers


## HARDWARE
* any Feather board, e.g. [Feather M0 Basic Proto](https://www.adafruit.com/product/2772)

* [DS3231 Precision RTC FeatherWing](https://www.adafruit.com/product/3028)
  * & [CR1220 coin cell](https://www.adafruit.com/product/380)

* [Music Maker FeatherWing w/ Amp](https://www.adafruit.com/product/3436) for speaker wire output
  * or [Adafruit Music Maker FeatherWing](https://www.adafruit.com/product/3357) for 1/8" audio jack output

* [MicroSD card](https://www.adafruit.com/product/1294) FAT formatted with "cheer.mp3"

* [FeatherWing Tripler](https://www.adafruit.com/product/3417) 
  * or [Feather Stacking Headers](https://www.adafruit.com/product/2830) for a different form factor 



## SOFTWARE
### LIBRARIES
* [VS1053](https://github.com/adafruit/Adafruit_VS1053_Library) for Music Maker
* [RCTlib](https://github.com/adafruit/RTClib) for RTC
* [DST_RTC](https://github.com/andydoro/DST_RTC) for automatic Daylight Saving Time adjustments

cheer.mp3, place on FAT formatted SD card and insert into Music Maker
suggestion: http://www.orangefreesounds.com/street-crowd-cheering-and-applauding/

# AUTOCHEER DEVICE
# code by Andy Doro
# 
# plays an MP3 at a specific time.
# 
# uses native CircuitPython mp3 playback
# should use M4 (or higher)
#
# Adalogger https://www.adafruit.com/product/2922
# 
# TO DO
# ---
# - add stereo playback
#


import time
import board
import audiomp3
import audioio
import digitalio


# For hardware I2C (M0 boards) use this line:
import busio as io

# Or for software I2C (ESP8266) use this line instead:
# import bitbangio as io

#import adafruit_ds3231
import adafruit_pcf8523

# SD card
import adafruit_sdcard
import storage

 
# Use any pin that is not taken by SPI
SD_CS = board.D10 # for M0 and M4 Feathers
 
# Connect to the card and mount the filesystem.
spi = io.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")


i2c = io.I2C(board.SCL, board.SDA)  # Change to the appropriate I2C clock & data
# pins here!

# Create the RTC instance:
#rtc = adafruit_ds3231.DS3231(i2c)
rtc = adafruit_pcf8523.PCF8523(myI2C)

# Lookup table for names of days (nicer printing).
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

data = open("/sd/cheer.mp3", "rb")
mp3 = audiomp3.MP3Decoder(data)
#a = audioio.AudioOut(board.A0)
a = audioio.AudioOut(board.A0, right_channel=board.A1) # stereo sound through A0 & A1

# selected time
# 24 hour time
playhour = 19 
playmin = 0


# pylint: disable-msg=bad-whitespace
# pylint: disable-msg=using-constant-test
# no DST adjustment yet!
if False:  # change to True if you want to set the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2017, 10, 29, 15, 14, 15, 0, -1, -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time
    print("Setting time to:", t)  # uncomment for debugging
    rtc.datetime = t
    print()
# pylint: enable-msg=using-constant-test
# pylint: enable-msg=bad-whitespace

# Main loop:
while True:
    t = rtc.datetime
    # print(t)     # uncomment for debugging
    print(
        "The date is {} {}/{}/{}".format(
            days[int(t.tm_wday)], t.tm_mday, t.tm_mon, t.tm_year
        )
    )
    print("The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))

    if t.tm_hour == playhour and t.tm_min == playmin:
        print("it is time!")
        # play the file
        print("playing")
        a.play(mp3)
        while a.playing:
            pass
        print("stopped")

    time.sleep(1)  # wait a second
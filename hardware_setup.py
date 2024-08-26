# esp32_setup.py Copy to target as color_setup.py

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2020 Peter Hinch

# Pin nos. match my PCB for all displays.

# As written with commented-out lines, supports:
# Adafruit 1.5" 128*128 OLED display: https://www.adafruit.com/product/1431
# Adafruit 1.27" 128*96 display https://www.adafruit.com/product/1673
# Adfruit 1.8" 128*160 Color TFT LCD display https://www.adafruit.com/product/358
# Adfruit 1.44" 128*128 Color TFT LCD display https://www.adafruit.com/product/2088
# Edit the driver import for other displays.

# WIRING (Adafruit pin nos and names).
# ESP   SSD
# 3v3   Vin (10)
# Gnd   Gnd (11)
# IO6  DC (3 DC)
# IO7  CS (5 OC OLEDCS)
# IO10  Rst (4 R RESET)
# IO2  CLK (2 CL SCK)  Hardware SPI1
# IO3  DATA (1 SI MOSI)

from machine import SPI, Pin
import gc

# from drivers.ssd1351.ssd1351_generic import SSD1351 as SSD
from drivers.st7735r.st7735r import ST7735R as SSD
# from drivers.st7735r.st7735r144 import ST7735R as SSD
# from drivers.st7735r.st7735r_4bit import ST7735R as SSD
from gui.core.ugui import Display

height = 80 + 24  # 由于ST7735默认分辨率和0.96寸屏幕分辨率不同，故增加偏移值24
width = 160

pdc = Pin(6, Pin.OUT, value=0)  # Arbitrary pins
pcs = Pin(7, Pin.OUT, value=1)
prst = Pin(10, Pin.OUT, value=1)
# Hardware SPI on native pins for performance. Check DRIVERS.md for optimum baudrate.
spi = SPI(1, 40_000_000, sck=Pin(2), mosi=Pin(3), miso=Pin(12))
gc.collect()
# ssd = SSD(spi, pcs, pdc, prst, height=height)  # Must specify height for SSD1351
ssd = SSD(spi, pcs, pdc, prst, height, width, True)  # The other Adafruit displays use defaults
# On st7735r 1.8 inch display can exchange height and width for portrait mode. See docs.
# The 1.44 inch display is symmetrical so this doesn't apply.

# Define control buttons
nxt = Pin(5, Pin.IN, Pin.PULL_UP)  # Move to next control
sel = Pin(4, Pin.IN, Pin.PULL_UP)  # Operate current control
prev = Pin(9, Pin.IN, Pin.PULL_UP)  # Move to previous control
increase = Pin(13, Pin.IN, Pin.PULL_UP)  # Increase control's value
decrease = Pin(8, Pin.IN, Pin.PULL_UP)  # Decrease control's value
display = Display(ssd, nxt, sel, prev, increase, decrease)

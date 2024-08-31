from machine import SPI, Pin
import gc

from st7735 import ST7735 as SSD
from gui.core.ugui import Display

# 引脚定义
pin_dc = Pin(6, Pin.OUT, value=0)
pin_cs = Pin(7, Pin.OUT, value=1)
pin_rst = Pin(10, Pin.OUT, value=1)
pin_bl = Pin(11, Pin.OUT, value=1)

# 配置SPI接口和频率
spi = SPI(1, 40_000_000, sck=Pin(2), mosi=Pin(3), miso=Pin(12))

# 配置屏幕驱动
ssd = SSD(
    spi, pin_rst, pin_dc, pin_cs, pin_bl,
    width=160, height=80, offset=None, rotate=1
)
gc.collect()

# 配置按键
nxt = Pin(9, Pin.IN, Pin.PULL_UP)  # Move to next control
sel = Pin(4, Pin.IN, Pin.PULL_UP)  # Operate current control
prev = Pin(5, Pin.IN, Pin.PULL_UP)  # Move to previous control
increase = Pin(8, Pin.IN, Pin.PULL_UP)  # Increase control's value
decrease = Pin(13, Pin.IN, Pin.PULL_UP)  # Decrease control's value
display = Display(ssd, nxt, sel, prev, increase, decrease)

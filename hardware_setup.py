from machine import Pin, SPI
import gc
from scr_driver import ScrDriver as SSD

# 显示驱动初始化
spi = SPI(2, baudrate=6000_0000, sck=Pin(18), mosi=Pin(23))
gc.collect()
ssd = SSD(
    spi,
    320, 240,
    reset=Pin(33, Pin.OUT),
    cs=Pin(14, Pin.OUT),
    dc=Pin(27, Pin.OUT),
    backlight=Pin(32, Pin.OUT),
    rotation=0,
    buffer_size=0
)
gc.collect()
from gui.core.ugui import Display

# 按键初始化
nxt = Pin(37, Pin.IN, Pin.PULL_UP)  # Move to next control
sel = Pin(38, Pin.IN, Pin.PULL_UP)  # Operate current control
prev = Pin(39, Pin.IN, Pin.PULL_UP)  # Move to previous control
# increase = Pin(..., Pin.IN, Pin.PULL_UP)  # Increase control's value
# decrease = Pin(..., Pin.IN, Pin.PULL_UP)  # Decrease control's value

# 显示设备初始化
display = Display(ssd, nxt, sel, prev)  # 3-button mode
# display = Display(ssd, nxt, sel, prev, increase, decrease)  # 5-button mode

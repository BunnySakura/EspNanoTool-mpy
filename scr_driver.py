from ili9342c import ILI9342C, color565
from drivers.boolpalette import BoolPalette

import framebuf


class ScrDriver(framebuf.FrameBuffer):
    @staticmethod
    def rgb(r, g, b):
        """GUI库要求驱动实现此方法"""
        return color565(r, g, b)

    def __init__(self, spi, width, height, reset, cs, dc, backlight, rotation, buffer_size):
        self.width = width
        self.height = height

        self.tft = ILI9342C(
            spi, width, height,
            reset=reset,
            cs=cs,
            dc=dc,
            backlight=backlight,
            rotation=rotation,
            buffer_size=buffer_size
        )
        self.tft.init()

        # Attention: 目前无法获取缓冲区内存，如果用ILI9342C，则无法兼容FrameBuffer
        # 如果直接申请内存，由于剩余内存不足，会报错申请失败。
        buffer = bytearray(buffer_size)
        super().__init__(buffer, width, height, framebuf.GS8)

        # GUI库要求驱动有此属性
        mode = framebuf.GS8  # Use 8bit greyscale for 8 bit color.
        self.palette = BoolPalette(mode)

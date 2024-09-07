# The module exposes predefined colors.
BLACK = ...
BLUE = ...
RED = ...
GREEN = ...
CYAN = ...
MAGENTA = ...
YELLOW = ...
WHITE = ...


def color565(r, g, b):
    """
    Pack a color into 2-bytes rgb565 format.

    Args:
        r:
        g:
        b:

    Returns:

    """


def map_bitarray_to_rgb565(bitarray, buffer, width, color=WHITE, bg_color=BLACK):
    """
    Convert a bitarray to the rgb565 color buffer which is suitable for blitting.
    Bit 1 in bitarray is a pixel with `color` and 0 - with `bg_color`.

    Args:
        bitarray:
        buffer:
        width:
        color:
        bg_color:

    Returns:

    """


class ILI9342C:
    def __init__(self, spi, width, height, reset, cs, dc, backlight, rotation, buffer_size):
        """
        Initialize device driver.

        Args:
            spi: spi device
            width: display width
            height: display height
            reset: display height
            dc: dc pin
            cs: cs pin
            backlight: backlight pin
            rotation: 0~7
            buffer_size: 0= buffer dynamically allocated and freed as needed.

        Rotation | Orientation
        -------- | --------------------
           0     | 0 degrees
           1     | 90 degrees
           2     | 180 degrees
           3     | 270 degrees
           4     | 0 degrees mirrored
           5     | 90 degrees mirrored
           6     | 180 degrees mirrored
           7     | 270 degrees mirrored

        Notes:
            If buffer_size is specified it must be large enough to contain the largest
            bitmap and/or JPG used (Rows * Columns *2 bytes).
        """

    def init(self):
        """
        Initialize the display.

        Returns:

        """

    def fill(self, color):
        """
        Fill the entire display with the specified color.

        Args:
            color:

        Returns:

        """

    def pixel(self, x, y, color):
        """
        Set the specified pixel to the given color.

        Args:
            x:
            y:
            color:

        Returns:

        """

    def line(self, x0, y0, x1, y1, color):
        """
        Draws a single line with the provided `color` from (`x0`, `y0`) to (`x1`, `y1`).

        Args:
            x0:
            y0:
            x1:
            y1:
            color:

        Returns:

        """

    def hline(self, x, y, length, color):
        """
        Draws a single horizontal line with the provided `color` and `length` in pixels.
        Along with `vline`, this is a fast version with reduced number of SPI calls.

        Args:
            x:
            y:
            length:
            color:

        Returns:

        """

    def vline(self, x, y, length, color):
        """
        Draws a single horizontal line with the provided `color` and `length` in pixels.

        Args:
            x:
            y:
            length:
            color:

        Returns:

        """

    def rect(self, x, y, width, height, color):
        """
        Draws a rectangle from (`x`, `y`) with corresponding dimensions

        Args:
            x:
            y:
            width:
            height:
            color:

        Returns:

        """

    def fill_rect(self, x, y, width, height, color):
        """
        Fill a rectangle starting from (`x`, `y`) coordinates

        Args:
            x:
            y:
            width:
            height:
            color:

        Returns:

        """

    def blit_buffer(self, buffer, x, y, width, height):
        """
        Copy bytes() or bytearray() content to the screen internal memory.

        Note: every color requires 2 bytes in the array

        Args:
            buffer:
            x:
            y:
            width:
            height:

        Returns:

        """

    def text(self, bitap_font, s, x, y, fg=..., bg=...):
        """
        Write text to the display using the specified bitmap font with the coordinates
        as the upper-left corner of the text.

        The foreground and background colors of the text can be set by the optional arguments fg and bg,
        otherwise the foreground color defaults to `WHITE` and the background color defaults to `BLACK`.

        See the README.md in the fonts directory for example fonts.

        Args:
            bitap_font:
            s:
            x:
            y:
            fg:
            bg:

        Returns:

        """

    def write(self, bitap_font, s, x, y, fg=..., bg=...):
        """
        Write text to the display using the specified proportional or Monospace bitmap font module with the coordinates
        as the upper-left corner of the text.

        The foreground and background colors of the text can be set by the optional arguments fg and bg,
        otherwise the foreground color defaults to `WHITE` and the background color defaults to `BLACK`.

        See the `README.md` in the `truetype/fonts` directory for example fonts.

        Returns the width of the string as printed in pixels.

        The `font2bitmap` utility creates compatible 1 bit per pixel bitmap modules
        from Proportional or Monospaced True Type fonts.

        The character size, foreground, background colors and the characters
        to include in the bitmap module may be specified as parameters.

        Use the -h option for details. If you specify a buffer_size during the display initialization
        it must be large enough to hold the widest character (HEIGHT * MAX_WIDTH * 2).

        Args:
            bitap_font:
            s:
            x:
            y:
            fg:
            bg:

        Returns:

        """

    def write_len(self, bitap_font, s):
        """
        Returns the width of the string in pixels if printed in the specified font.

        Args:
            bitap_font:
            s:

        Returns:

        """

    def draw(self, vector_font, s, x, y, fg=..., bg=...):
        """
        Draw text to the display using the specified hershey vector font with the coordinates
        as the lower-left corner of the text.

        The foreground and background colors of the text can be set by the optional arguments fg and bg,
        otherwise the foreground color defaults to `WHITE` and the background color defaults to `BLACK`.

        See the README.md in the fonts directory for example fonts and the utils directory for a font conversion program.

        Args:
            vector_font:
            s:
            x:
            y:
            fg:
            bg:

        Returns:

        """

    def jpg(self, jpg_filename, x, y, method=...):
        """
        Draw JPG file on the display at the given x and y coordinates as the upper left corner of the image.

        There memory required to decode and display a JPG can be considerable as a full screen 320x240 JPG
        would require at least 3100 bytes for the working area + 320x240x2 bytes of ram to buffer the image.

        Jpg images that would require a buffer larger than available memory can be drawn by passing SLOW for method.

        The SLOW method will draw the image a piece at a time using the Minimum Coded Unit (MCU, typically 8x8 pixels).

        Args:
            jpg_filename:
            x:
            y:
            method:

        Returns:

        """

    def bitmap(self, bitmap, x, y, index=...):
        """
        Draw bitmap using the specified x, y coordinates as the upper-left corner of the of the bitmap.

        The optional index parameter provides a method to select from multiple bitmaps contained a bitmap module.

        The index is used to calculate the offset to the beginning of the desired bitmap using the modules HEIGHT,
        WIDTH and BPP values.

        Args:
            bitmap:
            x:
            y:
            index:

        Returns:

        """

    def width(self):
        """
        Returns the current logical width of the display. (ie a 320x240 display rotated 90 degrees is 240 pixels wide)

        Returns:

        """

    def height(self):
        """
        Returns the current logical height of the display. (ie a 320x240 display rotated 90 degrees is 320 pixels high)

        Returns:

        """

    def rotation(self, r):
        """
        Set the rotates the logical display in a clockwise direction.

        0-Portrait (0 degrees),
        1-Landscape (90 degrees),
        2-Inverse Portrait (180 degrees),
        3-Inverse Landscape (270 degrees)

        Rotations 4-7 are mirrors of Rotations 0-3 for use with ILI9341 Displays 4-Portrait (0 degrees) Mirrored,

        1-Landscape (90 degrees) Mirrored,
        2-Inverse Portrait (180 degrees) Mirrored,
        3-Inverse Landscape (270 degrees) Mirrored.

        Args:
            r:

        Returns:

        """

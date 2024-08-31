# simple.py Minimal micro-gui demo.

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2021 Peter Hinch

# hardware_setup must be imported before other modules because of RAM use.
import hardware_setup  # Create a display instance
from gui.core.ugui import Screen, ssd

from gui.widgets import Label, Button, CloseButton
from gui.core.writer import CWriter

# Font for CWriter
import gui.fonts.arial10 as arial10
from gui.core.colors import *
from gui.widgets.textbox import Textbox

from wifi_connect import WiFi


class BaseScreen(Screen):

    def __init__(self):
        def my_callback(button, arg):
            print('Button pressed', arg)

        super().__init__()
        # verbose default indicates if fast rendering is enabled
        wri = CWriter(ssd, arial10, GREEN, BLACK)
        col = 10
        row = 10
        Label(wri, row, col, 'Simple Demo')
        row = 50
        wifi = WiFi()

        def print_wifi(button, arg):
            result = wifi.scan()
            print(result)
            text_box = Textbox(wri, 10, 10, 100, 3)
            for i in result:
                text_box.append(str(i[0], 'utf-8'))

        Button(wri, row, col, text='Scan', callback=print_wifi, args=('Yes',))
        col += 110
        Button(wri, row, col, text='No', callback=my_callback, args=('No',))
        CloseButton(wri)  # Quit the application


def test():
    print('Simple demo: button presses print to REPL.')
    Screen.change(BaseScreen)  # A class is passed here, not an instance.


if __name__ == "__main__":
    test()

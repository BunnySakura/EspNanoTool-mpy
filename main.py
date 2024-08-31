# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2021 Peter Hinch

# hardware_setup must be imported before other modules because of RAM use.
import hardware_setup  # Create a display instance
from gui.core.ugui import Screen, ssd

from gui.widgets import Label, Button, CloseButton, Listbox
from gui.core.writer import CWriter

# Font for CWriter
import gui.fonts.arial10 as arial10
from gui.core.colors import *

from wifi_connect import WiFiScreen
from clock_scr import ClockScreen


class BaseScreen(Screen):
    def __init__(self):
        super().__init__()
        # verbose default indicates if fast rendering is enabled
        wri = CWriter(ssd, arial10, GREEN, BLACK)
        row = 2
        col = 2
        label = Label(wri, row, col, "EspNanoTool")

        row = row + label.height + 4

        def scr_wifi_connect(lb, cls_new_screen, writer):
            Screen.change(cls_new_screen, args=[writer])

        def scr_clock(lb, cls_new_screen, writer):
            Screen.change(cls_new_screen, args=[writer])

        els = (
            ("WiFi connect", scr_wifi_connect, (WiFiScreen, wri)),
            ("Clock", scr_clock, (ClockScreen, wri)),
            ("test2", print, ("test2",)),
        )
        Listbox(wri, row, col, elements=els, width=ssd.width - 4, bdcolor=RED)

        CloseButton(wri)  # Quit the application


def start():
    print("Main program starting...")
    Screen.change(BaseScreen)  # A class is passed here, not an instance.


if __name__ == "__main__":
    start()

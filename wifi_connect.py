import gc

import hardware_setup  # Create a display instance
from gui.core.ugui import Screen, ssd

from gui.widgets import Label, Button, CloseButton, Listbox, DialogBox
from gui.core.writer import CWriter

# Font for CWriter
import gui.fonts.arial10 as arial10
from gui.core.colors import *

import network


class WiFi:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def scan(self):
        return self.wlan.scan()

    def connect(self, ssid, password):
        self.wlan.connect(ssid, password)


class WiFiScreen(Screen):
    def __init__(self, wri: CWriter):
        super().__init__()
        row = 2
        col = 2
        label = Label(wri, row, col, "Connect to WiFi")

        wifi = WiFi()

        def wifi_connect(lb, ssid, password):
            wifi.connect(ssid, password)
            args = {
                "writer": wri, "row": label.height + 4, "col": 2,
                "elements": (("OK", GREEN),),
            }
            if wifi.wlan.isconnected():
                args["label"] = ssid + " connected.     "
                Screen.change(DialogBox, kwargs=args)
            else:
                args["label"] = ssid + " not connected!     "
                Screen.change(DialogBox, kwargs=args)
            print(args["label"])

        def wifi_scan(button):
            result = wifi.scan()
            print(result)
            els = []
            for i, ele in enumerate(result):
                if ele[0] != b'' and i < 10:
                    ssid = str(ele[0], "utf-8")
                    els.append((ssid, wifi_connect, (ssid, "12345678")))
            print(els)
            Listbox(
                wri, label.height + 4, 2,
                elements=els,
                dlines=3,
                width=ssd.width - 4,
                bdcolor=RED
            )
            gc.collect()

        row = ssd.height - 16 - 4
        Button(wri, row, col, height=16, text="Scan", callback=wifi_scan)

        def back_prev_scr(button):
            Screen.back()

        col = ssd.width - 54
        Button(wri, row, col, height=16, text="Back", callback=back_prev_scr)

        gc.collect()
        CloseButton(wri)

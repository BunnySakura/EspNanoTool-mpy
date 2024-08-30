import network


class WiFi:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def scan(self):
        return self.wlan.scan()

    def connect(self, ssid, password):
        self.wlan.connect(ssid, password)

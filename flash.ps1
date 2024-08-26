mpremote mip install "github:peterhinch/micropython-nano-gui/drivers/st7735r"
mpremote mip install "github:peterhinch/micropython-micro-gui"
mpremote cp hardware_setup.py :
mpremote cp drivers/st7735r/st7735r.py :/lib/drivers/st7735r/st7735r.py
mpremote cp main.py :
mpremote cp boot.py :

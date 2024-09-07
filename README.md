# EspNanoTool-mpy

*一个使用ESP32系列芯片开发的小工具，开发语言为MicroPython。*

## 说明

基础固件源自[ili9342c_mpy]，GUI框架使用纯MicroPython编写的[micropython-micro-gui]，在此感谢其作者的付出，致敬互联网开源精神。

## 构建

全部擦除:

```shell
esptool.py --chip esp32 --port /dev/your/device erase_flash
```

固件烧录：

```shell
esptool.py --chip esp32 --port /dev/your/device --baud 460800 write_flash -z 0x1000 firmware.bin
```

MicroPython应用烧录：

```shell
./flash.ps1
```

## 引用

- [ili9342c_mpy]
- [micropython-micro-gui]

[ili9342c_mpy]: https://github.com/russhughes/ili9342c_mpy

[micropython-micro-gui]: https://github.com/peterhinch/micropython-micro-gui
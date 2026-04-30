## PoC "keyboard jiggler" for AI usage.

This is MicroPython code for a USB RP2350 dongle (I used the [DFRobot Beetle RP2350](https://www.dfrobot.com/product-2913.html) with the `SEEED_XIAO_RP2350-20260406-v1.28.0.uf2` firmware). 

Requires the `usb-device-keyboard` mip module.

Usage:

```
mpremote mip install usb-device-keyboard
mpremote cp main.py :main.py
mpremote reset      # or reset manually
```

Create your own loop as desired!


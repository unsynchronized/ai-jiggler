## PoC "keyboard jiggler" for AI usage.

This is MicroPython code for a USB RP2350 dongle (I used the [DFRobot Beetle RP2350](https://www.dfrobot.com/product-2913.html) with the `SEEED_XIAO_RP2350-20260406-v1.28.0.uf2` firmware). 

It pretends to be a USB keyboard HID, uses macOS Spotlight to open Chrome, creates a new window, navigates to Gemini, and then asks vaguely random questions every 30-60 seconds.

Customize at will!

### Usage

Requires the `usb-device-keyboard` mip module.

Usage:

```
mpremote mip install usb-device-keyboard
mpremote cp main.py :main.py
mpremote reset      # or reset manually
```



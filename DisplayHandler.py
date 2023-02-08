# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7789 import ST7789
import time


class DisplayHandler:
    # First set some parameters used for shapes and text
    BORDER = 20
    FONTSCALE = 2
    BACKGROUND_COLOR = 0x0  # Bright Green
    FOREGROUND_COLOR = 0x0  # Purple
    TEXT_COLOR = 0xFFFF00

    def __init__(self):
        # Release any resources currently in use for the displays
        displayio.release_displays()

        tft_cs = board.GP9
        tft_dc = board.GP8
        spi_mosi = board.GP11
        spi_clk = board.GP10
        spi = busio.SPI(spi_clk, spi_mosi)

        display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.GP12)
        self.display = ST7789(
            display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53
        )

        # Make the display context
        self.splash = displayio.Group()
        self.display.show(self.splash)

        color_bitmap = displayio.Bitmap(self.display.width, self.display.height, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = self.BACKGROUND_COLOR

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        self.splash.append(bg_sprite)

        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(
            self.display.width - self.BORDER * 2, self.display.height - self.BORDER * 2, 1
        )
        inner_palette = displayio.Palette(1)
        inner_palette[0] = self.FOREGROUND_COLOR
        inner_sprite = displayio.TileGrid(
            inner_bitmap, pixel_shader=inner_palette, x=self.BORDER, y=self.BORDER
        )
        self.splash.append(inner_sprite)

    def show_image1(self):
        bitmap = displayio.OnDiskBitmap("dogweird.bmp")
        gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
        self.splash.append(gridtitle)
        # time.sleep(5)

    def show_image2(self):
        bitmap = displayio.OnDiskBitmap("rock_240x135.bmp")
        gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
        self.splash.append(gridtitle)
        # time.sleep(5)

    def show_image3(self):
        bitmap = displayio.OnDiskBitmap("zhongnew.bmp")
        gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
        self.splash.append(gridtitle)
        # time.sleep(5)


if __name__ == "__main__":
    lcd = DisplayHandler()
    lcd.show_image3()

    while True:
        pass

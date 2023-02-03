# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7789 import ST7789
import time

# First set some parameters used for shapes and text
BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0x0  # Bright Green
FOREGROUND_COLOR = 0x0  # Purple
TEXT_COLOR = 0xFFFF00

# Release any resources currently in use for the displays
displayio.release_displays()

tft_cs = board.GP9
tft_dc = board.GP8
spi_mosi = board.GP11
spi_clk = board.GP10
spi = busio.SPI(spi_clk, spi_mosi)

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.GP12)
display = ST7789(
    display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53
)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(
    display.width - BORDER * 2, display.height - BORDER * 2, 1
)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw a label


"""
text = "i love elec 201"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width // 2 - text_width // 2,
    y=display.height // 2,
)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)
"""


"""
text = "*** i love CPEN 291! ***"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width,
    y=display.height // 2,
)
text_group.append(text_area)
splash.append(text_group)

"""



'''
# Convert the image file into a displayio.Bitmap
with open("rick_astley.bmp", "rb") as f:
    image = displayio.OnDiskBitmap(f)

# Create a displayio.TileGrid object with the bitmap
tile_grid = displayio.TileGrid(image, pixel_shader=displayio.ColorConverter(), x=0, y=0)

# Add the TileGrid object to the display's Group
splash.append(tile_grid)
'''

img = "rock_240x135.bmp"
img2 = "dogweird.bmp"
img4 = "zhongnew.bmp"
splash = displayio.Group()
display.show(splash)





while True:
    bitmap = displayio.OnDiskBitmap(img2)
    gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    splash.append(gridtitle)

    time.sleep(5)

    bitmap = displayio.OnDiskBitmap(img)
    gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    splash.append(gridtitle)
    time.sleep(5)

    bitmap = displayio.OnDiskBitmap(img4)
    gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    splash.append(gridtitle)
    time.sleep(5)
    """

    # Convert the image file into a displayio.Bitmap
    with open("alireza.bmp", "rb") as f:
        image = displayio.OnDiskBitmap(f)

    # Create a displayio.TileGrid object with the bitmap
    tile_grid = displayio.TileGrid(image, pixel_shader=displayio.ColorConverter(), x=0, y=0)

    # Add the TileGrid object to the display's Group
    splash.append(tile_grid)
    time.sleep(10)
    splash.remove(tile_grid)

    """



    """
    text = "i love sathish"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)
    time.sleep(3)
    splash.remove(text_group)  # Remove the first text
    text = "i like mieszko"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)
    time.sleep(3)
    splash.remove(text_group)


    """

    """


    for i in range(text_width + display.width):
        text_group.x = display.width - i
        time.sleep(0.001)

    """






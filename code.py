import board
import digitalio
from time import sleep
import time
import pwmio
import microcontroller
import pulseio
import math
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7789 import ST7789

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

img = "rock_240x135.bmp"
img2 = "dogweird.bmp"
img4 = "zhongnew (1).bmp"
img5 = "luis2.bmp"
img6 = "mind2.bmp"
img7 = "guy.bmp"
splash = displayio.Group()
display.show(splash)

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

text = "i love sathish"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width,
    y=display.height // 2,
)
text_group.append(text_area)
splash.append(text_group)

# create a PWMOut object on pin D5
servo_right_foot = pwmio.PWMOut(board.GP2)
servo_left_foot = pwmio.PWMOut(board.GP15)
servo_right_thigh = pwmio.PWMOut(board.GP3)
servo_left_thigh = pwmio.PWMOut(board.GP16)

NUM_ITERATIONS = 3
row_pins = [board.GP28, board.GP27, board.GP26, board.GP22]
col_pins = [board.GP21, board.GP20, board.GP19]

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

rows = []
for pin in row_pins:
    rows.append(digitalio.DigitalInOut(pin))
    rows[-1].direction = digitalio.Direction.INPUT
    rows[-1].pull = digitalio.Pull.UP

cols = []
for pin in col_pins:
    cols.append(digitalio.DigitalInOut(pin))
    cols[-1].direction = digitalio.Direction.OUTPUT
    cols[-1].value = True

def get_keypad_value():
    for col in cols:
        col.value = False
        for row in rows:
            if not row.value:
                col.value = True
                row_index = rows.index(row)
                col_index = cols.index(col)
                return keypad[row_index][col_index]
        col.value = True
    return None

# Create a list of digital input objects




# create a function to set the servo angle
# create a function to set the servo angle
def set_servo_angle(name, angle):
    name.duty_cycle = int(angle / 180 * 2**16)
def ninety():
    servo_left_foot.duty_cycle = int(1/2*2**16)
    servo_right_foot.duty_cycle = int(1/2*2**16)
    servo_right_thigh.duty_cycle = int(1/2*2**16)
    servo_left_thigh.duty_cycle = int(1/2*2**16)
    
def dance_move1():
    """
    text = "i love sathish"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width,
        y=display.height // 2,
    )
    text_group.append(text_area)
    splash.append(text_group)
    

    for i in range(text_width + display.width):
        text_group.x = int(display.width - i/2.0)
        time.sleep(0.001)
    time.sleep(0.1)
    
    """
    bitmap = displayio.OnDiskBitmap(img)
    gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    splash.append(gridtitle)

    time.sleep(5)
    
    
    for i in range(1, NUM_ITERATIONS):
        for k in range (0,5):
            for j in range (1,10):
                set_servo_angle(servo_right_foot, 90 + math.sqrt(100*j))
                set_servo_angle(servo_left_foot, 90 + math.sqrt(100*j))
                set_servo_angle(servo_right_thigh, 125)
                set_servo_angle(servo_left_thigh, 125)
                time.sleep(.01)
            time.sleep(0.25)
        for k in range (0,5):
            for j in range (1,10):
                set_servo_angle(servo_right_foot, 90 )
                set_servo_angle(servo_left_foot, 90 )
                set_servo_angle(servo_right_thigh, 125 - math.sqrt(100*j))
                set_servo_angle(servo_left_thigh, 125 - math.sqrt(100*j))
                time.sleep(.01)
            time.sleep(0.25)     
            
        for k in range (0,5):
            for j in range (1,10):
                set_servo_angle(servo_right_foot, 90 - 1/2*math.sqrt(100*j))
                set_servo_angle(servo_left_foot, 120 - 1/2*math.sqrt(100*j))
                set_servo_angle(servo_right_thigh, 135)
                set_servo_angle(servo_left_thigh, 35)
                time.sleep(.01)
            time.sleep(0.25)       
        for k in range (0,5):
            for j in range (1,10):
                set_servo_angle(servo_right_foot, 90 - math.sqrt(28*j))
                set_servo_angle(servo_left_foot, 90 + 1/2*math.sqrt(14*j))
                set_servo_angle(servo_right_thigh, 125)
                set_servo_angle(servo_left_thigh, 125)
                time.sleep(.01)
            time.sleep(0.25)               
def dance_move2():
    bitmap = displayio.OnDiskBitmap(img2)
    gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    splash.append(gridtitle)

    time.sleep(5)
    for j in range(1,NUM_ITERATIONS):
        time.sleep(.5)
        
        for i in range(90,60,-1):
            set_servo_angle(servo_right_foot, i )
            set_servo_angle(servo_left_foot, 180-i )
            set_servo_angle(servo_right_thigh, i)
            set_servo_angle(servo_left_thigh, 180-i)
            time.sleep(.01)
                
        for i in range(60,90):
            set_servo_angle(servo_right_foot, i )
            set_servo_angle(servo_left_foot, 180-i )
            set_servo_angle(servo_right_thigh, i)
            set_servo_angle(servo_left_thigh, 180-i)
            time.sleep(.01)        
        for i in range(60,90):
            set_servo_angle(servo_right_foot, i+45 )
            set_servo_angle(servo_left_foot, 180-i )
            set_servo_angle(servo_right_thigh, i+45)
            set_servo_angle(servo_left_thigh, 180-i)
            time.sleep(.01) 
        time.sleep(0.5)    
        for i in range(90,60,-1):
            set_servo_angle(servo_right_foot,180- i )
            set_servo_angle(servo_left_foot, i )
            set_servo_angle(servo_right_thigh,180- i)
            set_servo_angle(servo_left_thigh, i)
            time.sleep(.01)
                
        for i in range(60,90):
            set_servo_angle(servo_right_foot, 180-i )
            set_servo_angle(servo_left_foot, i )
            set_servo_angle(servo_right_thigh,180- i)
            set_servo_angle(servo_left_thigh, i)
            time.sleep(.01)        
        for i in range(60,90):
            set_servo_angle(servo_right_foot, 180-i )
            set_servo_angle(servo_left_foot, i+45 )
            set_servo_angle(servo_right_thigh, 180-i)
            set_servo_angle(servo_left_thigh, i+45)
            time.sleep(.01) 
        time.sleep(0.2)    
        ninety();
        time.sleep(0.5)


def dance_move3():
    bitmap = displayio.OnDiskBitmap(img4)
    gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    splash.append(gridtitle)

    time.sleep(5)
    i =0
    while (i<NUM_ITERATIONS):
        for j in range (0,3):
            print("hi")
            set_servo_angle(servo_right_foot, 85)
            set_servo_angle(servo_left_foot, 75)
            set_servo_angle(servo_right_thigh, 90)
            set_servo_angle(servo_left_thigh, 90)
            time.sleep(0.4)
            set_servo_angle(servo_right_foot, 30)
            set_servo_angle(servo_left_foot,150 )
            set_servo_angle(servo_right_thigh, 90)
            set_servo_angle(servo_left_thigh, 90)
            time.sleep(0.4)
        for j in range (0,50):
            set_servo_angle(servo_right_foot, 90 +40*(math.sin(j)))
            set_servo_angle(servo_left_foot,90 + 40*math.sin(j))
            set_servo_angle(servo_right_thigh, 90)
            set_servo_angle(servo_left_thigh, 90)
            time.sleep(0.02)
        for j in range (0,50):
            set_servo_angle(servo_right_foot, 90)
            set_servo_angle(servo_left_foot,90)
            set_servo_angle(servo_right_thigh, 90+40*math.sin(j))
            set_servo_angle(servo_left_thigh, 90+40*math.sin(j))
            time.sleep(0.02)            
        i +=1

def dance_move4():
    bitmap = displayio.OnDiskBitmap(img6)
    gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    splash.append(gridtitle)

    for j in range(1,NUM_ITERATIONS):
        i =0
        while (i<3):
            print("hi")
            set_servo_angle(servo_right_foot, 37)
            set_servo_angle(servo_left_foot, 37)
            set_servo_angle(servo_right_thigh, 57)
            set_servo_angle(servo_left_thigh, 57)
            time.sleep(0.4)
            set_servo_angle(servo_right_foot, 87)
            set_servo_angle(servo_left_foot,77)
            set_servo_angle(servo_right_thigh, 97)
            set_servo_angle(servo_left_thigh, 97)
            time.sleep(0.4)
            i+=1

        time.sleep(0.4)

        i = 0
        while (i<3):
            print ("BYE")
            set_servo_angle(servo_right_foot, 90)
            set_servo_angle(servo_left_foot, 90)
            set_servo_angle(servo_right_thigh, 75)
            set_servo_angle(servo_left_thigh, 75)
            time.sleep(0.6)
            set_servo_angle(servo_right_foot, 90)
            set_servo_angle(servo_left_foot,90)
            set_servo_angle(servo_right_thigh, 120)
            set_servo_angle(servo_left_thigh, 120)
            time.sleep(0.6)
            i +=1
        set_servo_angle(servo_right_foot, 90)
        set_servo_angle(servo_left_foot,90)
        set_servo_angle(servo_right_thigh, 90)
        set_servo_angle(servo_left_thigh, 90)
        time.sleep(0.7)
def dance_move5():
    bitmap = displayio.OnDiskBitmap(img5)
    gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    splash.append(gridtitle)

    time.sleep(5)
    for i in range(1,NUM_ITERATIONS):
        set_servo_angle(servo_right_foot, 110 )
        set_servo_angle(servo_left_foot, 110)
        set_servo_angle(servo_right_thigh, 110)
        set_servo_angle(servo_left_thigh, 110)
        time.sleep(1)
        set_servo_angle(servo_right_foot, 179)
        time.sleep(0.5)
        set_servo_angle(servo_right_foot, 60)
        time.sleep(0.5)
        set_servo_angle(servo_right_foot, 125)
        time.sleep(1)
        set_servo_angle(servo_right_foot, 50)
        set_servo_angle(servo_left_foot, 50)
        set_servo_angle(servo_right_thigh, 50)
        set_servo_angle(servo_left_thigh, 50)
        time.sleep(1)
        set_servo_angle(servo_left_foot, 179)
        time.sleep(0.5)
        set_servo_angle(servo_left_foot, 60)
        time.sleep(0.5)
        set_servo_angle(servo_left_foot, 125)
        time.sleep(1)


def dance_move6():
    bitmap = displayio.OnDiskBitmap(img7)
    gridtitle = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    splash.append(gridtitle)

    time.sleep(5)
    for k in range(0,5):
        for j in range (k,45):
            set_servo_angle(servo_right_foot, j/3+70)
            set_servo_angle(servo_left_foot, j/3+70)
            set_servo_angle(servo_right_thigh, j/2+60)
            set_servo_angle(servo_left_thigh, 120-j/2)
            time.sleep(0.01)
        
    for i in range (1,NUM_ITERATIONS):
        set_servo_angle(servo_right_foot,90 )
        set_servo_angle(servo_left_foot, 90)
        set_servo_angle(servo_right_thigh, 100)
        set_servo_angle(servo_left_thigh, 100)
        time.sleep(0.1)
        set_servo_angle(servo_right_foot, 150)
        set_servo_angle(servo_left_foot, 150)
        set_servo_angle(servo_right_thigh, 100)
        set_servo_angle(servo_left_thigh, 100)
        time.sleep(0.1)
        set_servo_angle(servo_right_foot, 90)
        set_servo_angle(servo_left_foot, 90)
        set_servo_angle(servo_right_thigh, 100)
        set_servo_angle(servo_left_thigh, 100)
        time.sleep(0.1)
                

        for k in range(0,20):
            set_servo_angle(servo_right_foot, 90)
            set_servo_angle(servo_left_foot, 90+k)
            set_servo_angle(servo_right_thigh, 100+2*k)
            set_servo_angle(servo_left_thigh, 100-2*k)
            time.sleep(0.02)
            
        for k in range(0,20):
            set_servo_angle(servo_right_foot, 90)
            set_servo_angle(servo_left_foot, 90)
            set_servo_angle(servo_right_thigh, 100-2*k)
            set_servo_angle(servo_left_thigh, 100+2*k)
            time.sleep(0.02)    
        time.sleep(1)    
        ninety();
        time.sleep(1)
        
        for j in range (0,5):
            for s in range(1,5):
                set_servo_angle(servo_right_foot, 80+2**s)
                set_servo_angle(servo_left_foot, 120-2**s)
                set_servo_angle(servo_right_thigh, 100-2*s)
                set_servo_angle(servo_left_thigh, 100+2*s)
                time.sleep(0.01*s)
            time.sleep(0.2)
            for s in range(1,5):
                set_servo_angle(servo_right_foot, 120-2**s)
                set_servo_angle(servo_left_foot, 80+2**s)
                set_servo_angle(servo_right_thigh, 100+2*s)
                set_servo_angle(servo_left_thigh, 100-2*s)
                time.sleep(0.01*s)            
            time.sleep(0.1)    
            
        for j in range (0,5):
            for s in range(5,0, -1):
                set_servo_angle(servo_right_foot, 120-2**s)
                set_servo_angle(servo_left_foot, 90+2**s)
                set_servo_angle(servo_right_thigh, 100+2*s)
                set_servo_angle(servo_left_thigh, 110-2*s)
                time.sleep(0.01*s) 
            time.sleep(0.2)
            for s in range(1,5):
                set_servo_angle(servo_right_foot, 120+2**s)
                set_servo_angle(servo_left_foot, 120-2**s)
                set_servo_angle(servo_right_thigh, 100-2*s)
                set_servo_angle(servo_left_thigh, 100+2*s)
                time.sleep(0.01*s)            
            time.sleep(0.1)     
                
def all_dancemove():
    dance_move1()
    time.sleep(1)
    dance_move2()
    time.sleep(1)
    dance_move3()
    time.sleep(1)
    dance_move4()
    time.sleep(1)
    dance_move5()
    time.sleep(1)
    dance_move6()

def incorrect_input():
    print("Enter in a valid number!")
    time.sleep(5)

dance_array = [None, dance_move1, dance_move2, dance_move3, dance_move4, dance_move5, dance_move6, incorrect_input, incorrect_input, incorrect_input, incorrect_input, all_dancemove, incorrect_input]

while True:

    key = get_keypad_value()
    ninety();
    if (key == "*"):
        key = 10
    if (key == "#"):
        key = 12
    if (key == 0):
        key = 11

    print(key)
    if key:
        function = dance_array[key]
        if function:
            function()
    time.sleep(0.1)
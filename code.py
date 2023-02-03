import board
import digitalio
from time import sleep
import time
import pwmio
import microcontroller
# create a PWMOut object on pin D5
servo_right_foot = pwmio.PWMOut(board.GP2)
servo_left_foot = pwmio.PWMOut(board.GP12)
servo_right_thigh = pwmio.PWMOut(board.GP3)
servo_left_thigh = pwmio.PWMOut(board.GP13)
import time
import board
import digitalio

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


def dance_move1():
    set_servo_angle(servo_right_foot, 125 )
    set_servo_angle(servo_left_foot, 125 )
    set_servo_angle(servo_right_thigh, 125)
    set_servo_angle(servo_left_thigh, 125)
    time.sleep(1)
    set_servo_angle(servo_right_foot, 30)
    set_servo_angle(servo_left_foot, 30)
    set_servo_angle(servo_right_thigh, 30)
    set_servo_angle(servo_left_thigh, 30)
    time.sleep(1)
def dance_move2():
    print("move2")
    set_servo_angle(servo_right_foot, 90)
    set_servo_angle(servo_left_foot, 80)
    set_servo_angle(servo_right_thigh, 100)
    set_servo_angle(servo_left_thigh, 50)
    time.sleep(0.5)
    set_servo_angle(servo_right_foot, 90)
    set_servo_angle(servo_left_foot, 80)
    set_servo_angle(servo_right_thigh, 50)
    set_servo_angle(servo_left_thigh, 100)
    time.sleep(0.5)


def dance_move3():
    i =0
    while (i<10):
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
        i +=1

def dance_move4():

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
        set_servo_angle(servo_right_thigh, 60)
        set_servo_angle(servo_left_thigh, 60)
        time.sleep(0.6)
        set_servo_angle(servo_right_foot, 90)
        set_servo_angle(servo_left_foot,90)
        set_servo_angle(servo_right_thigh, 140)
        set_servo_angle(servo_left_thigh, 140)
        time.sleep(0.6)
        i +=1
    set_servo_angle(servo_right_foot, 90)
    set_servo_angle(servo_left_foot,90)
    set_servo_angle(servo_right_thigh, 90)
    set_servo_angle(servo_left_thigh, 90)
    time.sleep(0.7)
def dance_move5():
    print("amin wuz here")
    set_servo_angle(servo_right_foot, 125 )
    set_servo_angle(servo_left_foot, 125 )
    set_servo_angle(servo_right_thigh, 125)
    set_servo_angle(servo_left_thigh, 125)
    time.sleep(1)
    set_servo_angle(servo_right_foot, 179)
    time.sleep(0.5)
    set_servo_angle(servo_right_foot, 60)
    time.sleep(0.5)
    set_servo_angle(servo_right_foot, 125)
    time.sleep(1)
    set_servo_angle(servo_right_foot, 30)
    set_servo_angle(servo_left_foot, 30)
    set_servo_angle(servo_right_thigh, 30)
    set_servo_angle(servo_left_thigh, 30)
    time.sleep(1)
    set_servo_angle(servo_left_foot, 179)
    time.sleep(0.5)
    set_servo_angle(servo_left_foot, 60)
    time.sleep(0.5)
    set_servo_angle(servo_left_foot, 125)
    time.sleep(1)


def dance_move6():

    set_servo_angle(servo_right_foot,90 )
    set_servo_angle(servo_left_foot, 90)
    set_servo_angle(servo_right_thigh, 100)
    set_servo_angle(servo_left_thigh, 100)
    time.sleep(0.05)
    set_servo_angle(servo_right_foot, 150)
    set_servo_angle(servo_left_foot, 150)
    set_servo_angle(servo_right_thigh, 100)
    set_servo_angle(servo_left_thigh, 100)
    time.sleep(0.05)
    set_servo_angle(servo_right_foot, 90)
    set_servo_angle(servo_left_foot, 90)
    set_servo_angle(servo_right_thigh, 100)
    set_servo_angle(servo_left_thigh, 100)
def all_dancemove():
    dance_move1()
    dance_move2()
    dance_move3()
    dance_move4()
    dance_move5()
    dance_move6()

dance_array = [None, dance_move1, dance_move2, dance_move3, dance_move4, dance_move5, dance_move6, all_dancemove]

while True:
    key = get_keypad_value()
    if key:
        function = dance_array[key]
        if function:
            function()
    time.sleep(0.1)

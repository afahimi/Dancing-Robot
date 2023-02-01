import board
import digitalio
import time
import pwmio
import microcontroller

# create a PWMOut object on pin D5
servo_right_foot = pwmio.PWMOut(board.GP2)
servo_left_foot = pwmio.PWMOut(board.GP12)
servo_right_thigh = pwmio.PWMOut(board.GP3)
servo_left_thigh = pwmio.PWMOut(board.GP13)


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
    set_servo_angle(servo_right_foot, 150)
    set_servo_angle(servo_left_foot, 30)
    set_servo_angle(servo_right_thigh, 90)
    set_servo_angle(servo_left_thigh, 90)
    time.sleep(0.5)
    set_servo_angle(servo_right_foot, 30)
    set_servo_angle(servo_left_foot, 150)
    set_servo_angle(servo_right_thigh, 90)
    set_servo_angle(servo_left_thigh, 90)
    time.sleep(0.5)




while True:
    #dance_move1();
    #dance_move2();
    #dance_move3();
    #dance_move4();
    time.sleep(0.01)



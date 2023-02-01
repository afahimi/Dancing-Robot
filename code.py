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




while True:
    #dance_move1();
    #dance_move2();
    #dance_move3();
    #dance_move4();
    time.sleep(0.01)



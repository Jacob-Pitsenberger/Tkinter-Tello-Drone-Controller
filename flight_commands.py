"""
-Adapted From-
Title: flydo - commands.py
Author: Charles Yuan
Date: 1-4-22
Code Version: N/A
Availability: https://github.com/Chubbyman2/flydo
"""

import threading
import time


def fly(direction, drone):
    """

    Send RC control via four channels:

           left_right_velocity (left/right),
           forward_backward_velocity (forward/backward)
           up_down_velocity (up/down)
           yaw_velocity (yaw)

           drone.send_rc_control(left/right, forward/backward, up/down, yaw left/right)

    """

    drone.send_rc_control(direction[0], direction[1], direction[2], direction[3])
    time.sleep(0.05)


def start_flying(event, direction, drone, speed):
    """Have the drone fly in a certain direction at a certain speed"""

    lr, fb, ud, yv = 0, 0, 0, 0

    if direction == "upward":
        print("Moving up")
        ud = speed
    elif direction == "downward":
        ud = -speed
        print("Moving down")
    elif direction == "forward":
        fb = speed
        print("Moving forward")
    elif direction == "backward":
        fb = -speed
        print("Moving backward")
    elif direction == "yaw_left":
        yv = -speed
        print("turning left")
    elif direction == "yaw_right":
        yv = speed
        print("turning right")
    elif direction == "left":
        lr = -speed
        print("Moving left")
    elif direction == "right":
        lr = speed
        print("Moving right")

    if [lr, fb, ud, yv] != [0, 0, 0, 0]:
        threading.Thread(target=lambda: fly([lr, fb, ud, yv], drone)).start()


def stop_flying(event, drone):
    """When user releases a movement key the drone stops performing that movement"""
    drone.send_rc_control(0, 0, 0, 0)


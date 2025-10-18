from time import sleep

import robot

arlo = robot.Robot()

print ("Running ...")

driving = True
while driving:
    print (arlo.go_diff(80, 80, 1, 1))  # Forward
    if arlo.read_front_ping_sensor() < 300:
        arlo.rotate_robot(180)
        sleep(0.5)
        arlo.go_diff(80, 80, 0, 1)
    elif arlo.read_left_ping_sensor() < 300:
        arlo.rotate_robot(-180)
        sleep(0.5)
        arlo.go_diff(80, 80, 0, 1)
    elif arlo.read_right_ping_sensor() < 300:
        arlo.rotate_robot(180)
        sleep(0.5)
        arlo.go_diff(80, 80, 1, 0)
        
        
print ("Finished")
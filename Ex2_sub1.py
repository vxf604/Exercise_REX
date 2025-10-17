from time import sleep

import robot

arlo = robot.Robot()

print ("Running ...")

driving = True
while driving:
    print (arlo.go_diff(80, 80, 1, 1))  # Forward
    if arlo.read_front_ping_sensor() < 300:
        arlo.rotate_robot(90)
        sleep(0.5)
        arlo.go_diff(80, 80, 1, 1)
    elif arlo.read_left_ping_sensor() < 300:
        arlo.rotate_robot(-90)
        arlo.go_diff(80, 80, 1, 1)  # Forward
    elif arlo.read_right_ping_sensor() < 300:
        arlo.rotate_robot(90)
        arlo.go_diff(80, 80, 1, 1)  # Forward
        
        
print ("Finished")
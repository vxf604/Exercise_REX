from time import sleep

import robot

arlo = robot.Robot()

print ("Running ...")

i = 0
while i < 5:
    if arlo.read_front_ping_sensor() < 20:
        arlo.rotate_robot(90)
        print(arlo.go_diff(80, 80, 1, 1))  # Forward
        i += 1
    elif arlo.read_left_ping_sensor() < 20:
        arlo.rotate_robot(-90)
        print(arlo.go_diff(80, 80, 1, 1))  # Forward
        i += 1
    elif arlo.read_right_ping_sensor() < 20:
        arlo.rotate_robot(90)
        print(arlo.go_diff(80, 80, 1, 1))  # Forward
        i
    else:
        print(arlo.go_diff(80, 80, 1, 1))  # Forward
        
        
print ("Finished")
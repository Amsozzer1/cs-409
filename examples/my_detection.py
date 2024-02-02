#Write a program that uses the ultrasonic sensor to detect
#obstacles that come within several centimeters of your car's front bumper. When your
#car gets within that obstacle, it should stop, choose another random direction, back up
#and turn, and then move forward in the new direction.

import picar_4wd as fc
import numpy as np
import time

speed = 30
obstacle_threshold = 15  # Distance in cm to consider as an obstacle

def operations(direction_number):
    # Define possible actions
    actions = {
        0: fc.turn_right,
        1: fc.turn_left,
        2: fc.backward,
        3: fc.forward
    }
    
    # Get the corresponding function and execute it
    action = actions.get(direction_number, fc.stop)
    action(speed)

def main():
    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        # Detect obstacles based on ultrasonic sensor readings
        min_distance = min(scan_list)
        if min_distance < obstacle_threshold:
            print(f"Obstacle detected at {min_distance} cm")
            fc.stop()
            time.sleep(1)
            
            # Choose a random action (turn right, turn left, backward, or forward)
            random_action = int(np.random.uniform(0, 4))
            operations(random_action)
            time.sleep(1)
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()

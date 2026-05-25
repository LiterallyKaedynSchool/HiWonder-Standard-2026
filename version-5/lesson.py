"""
AS91896: HiWonder Robot Manuevering 
By Kaedyn Eastall : Version 5 (I think)
"""

# Robot movement and sensors
from lesson_header import *

# Cup counter (starting at 0)
cups = 0

# Safe movement distance
SAFE_DIST = 15

# Define dict_logs as an empty dictionary
dict_logs = {}

# Import DateTime
from datetime import datetime as clock
now = clock.now()

# Importing core_actions page
from core_actions import *
from core_actions import dict_moves as d_m

# Print when starting movement
print("[DEBUG] Movement Starting")

# Print distance
distance_cm = sonar.get_distance_cm(filtered=True)

# Start while/if/elif statements for movement and decisions
while cups < 4:
    distance_cm = sonar.get_distance_cm(filtered=True)
    dict_logs["[DEBUG] Started"] = True
    if distance_cm < SAFE_DIST:
        if d_m[cups] == "right":
            # Move the bot
            moves.move_right(1.5)

            # Increase cup count
            cups += 1

            # Print that the cup was passed
            print(f"[INFO] Cup {cups} pass")

            # Add to logs dictionary
            dict_logs[f"move{cups}"] = "Success: Right"
        elif d_m[cups] == "left":
            # Move the bot
            moves.move_left(1.5)

            # Increase cup count
            cups += 1

            # Print that the cup was passed
            print(f"[INFO] Cup {cups} pass")

            # Add to logs dictionary
            dict_logs[f"move{cups}"] = "Success: Left"
    else:
        moves.forward(0.2)

# Move forward when cups == 5 to get out of the course
moves.forward(0.5)

# Print logs dictionary
print(dict_logs)

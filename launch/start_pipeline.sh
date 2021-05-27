#!/bin/bash
source devel/setup.sh

# start ROS Core
roscore &

# Start camera driver
roslaunch camera_launch_config pylon_camera_front.launch
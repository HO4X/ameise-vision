# ameise-vision
ROS System for the Ameise Vision PC

# Build dependencies

Ubuntu 20.04 
TensorRT 8.0
Cuda 11.1<

catkin build vision_all


# Starup 
´´´roscore´´´

## Camera 
roslaunch camera_launch_config pylon_camera_front.launch

## Start Lidar
roslaunch ouster_ros ouster.launch sensor_hostname:=169.254.112.236 udp_dest:=169.254.122.37 lidar_mode:=1024x20 viz:=true


### find LiDar IP Example 

ping os-122116000117.local

will give you the IP as follows: 

PING os-122116000117.local (169.254.112.236) 56(84) bytes of data.
64 bytes from os-122116000117.local (169.254.112.236): icmp_seq=1 ttl=64 time=0.177 ms
64 bytes from os-122116000117.local (169.254.112.236): icmp_seq=2 ttl=64 time=0.312 ms

-> 169.254.112.236

### Sample transform for "Lidar / Camera"

rosrun tf2_ros static_transform_publisher -0.025 0 -0.08 1.5 0.0 -1.65  os_lidar pylon_camera

## Run RViz with given config

rviz -d src/config/rviz/licam.rviz 


# OS0 - 122116000117
# OS1 - 992111000483
# OS2 - 992111000489

# Get IP address of Lidar
# ping os-122116000117.local -c 1 -q

# Host PC
udp_dest=192.168.42.98

# Lidar OS0 169.254.112.236
gnome-terminal --command="bash -c 'source ~/workspace/devel/setup.bash && \
roslaunch lidar_launch_config ouster.launch sensor_hostname:=169.254.112.236 \
udp_dest:=$udp_dest lidar_mode:=1024x20 viz:=false sensor_name:=OS0'"

# Lidar OS1 169.254.141.135
gnome-terminal --command="bash -c 'source ~/workspace/devel/setup.bash && \
roslaunch lidar_launch_config ouster.launch sensor_hostname:=169.254.141.135 \
udp_dest:=$udp_dest lidar_mode:=1024x20 viz:=false sensor_name:=OS1'"

# Lidar OS2 169.254.86.233
gnome-terminal --command="bash -c 'source ~/workspace/devel/setup.bash && \
roslaunch lidar_launch_config ouster.launch sensor_hostname:=169.254.86.233 \
udp_dest:=$udp_dest lidar_mode:=1024x10 viz:=false sensor_name:=OS2'"
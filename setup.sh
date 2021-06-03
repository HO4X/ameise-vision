cd ..
sudo apt-get install python3-catkin-tools
sudo apt install build-essential cmake libglfw3-dev libglew-dev libeigen3-dev libjsoncpp-dev libtclap-dev libtins-dev libpcap-dev
sudo rosdep init
sudo sh -c 'echo yaml https://raw.githubusercontent.com/basler/pylon-ros-camera/master/pylon_camera/rosdep/pylon_sdk.yaml > /etc/ros/rosdep/sources.list.d/30-pylon_camera.list' && rosdep update && sudo rosdep install --from-paths ./src/drivers/submodules --ignore-src --rosdistro=noetic -y
cd src && git submodule update --init --recursive && cd ..
catkin build vision_all

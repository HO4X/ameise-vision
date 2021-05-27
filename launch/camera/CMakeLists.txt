cmake_minimum_required(VERSION 3.0.2)
project(camera_launch_config)

find_package(catkin REQUIRED COMPONENTS roslaunch)
roslaunch_add_file_check(launch USE_TEST_DEPENDENCIES)
install(
    DIRECTORY
     launch/
    DESTINATION
     ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
    FILES_MATCHING PATTERN "*.launch"
)
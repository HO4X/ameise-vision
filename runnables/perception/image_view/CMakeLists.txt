cmake_minimum_required(VERSION 3.0.2)
project(image_view_dbg)

find_package(catkin REQUIRED COMPONENTS roscpp roscpp_serialization sensor_msgs)

catkin_package(INCLUDE_DIRS src
               LIBRARIES ${PROJECT_NAME}
               CATKIN_DEPENDS roscpp sensor_msgs
               )

include_directories(${catkin_INCLUDE_DIRS})

add_executable(image_view_dbg /home/ameise/workspace/src/runnables/perception/image_view/src/main.cpp)

target_link_libraries(image_view_dbg ${catkin_LIBRARIES})

install(TARGETS image_view_dbg
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
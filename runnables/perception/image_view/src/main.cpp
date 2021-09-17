#include "ros/ros.h"
#include "sensor_msgs/Image.h"

void chatterCallback(const sensor_msgs::Image::ConstPtr& msg)
{
  ROS_INFO("I heard: something lel");
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "image_view_dbg");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("/pylon_camera_node/image_rect", 1, chatterCallback);
  ros::spin();

  return 0;
}
cmake_minimum_required(VERSION 3.0.2)
project(pose_estimate_3d)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/pose_estimate_3d.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/scripts
)

install(DIRECTORY
  launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

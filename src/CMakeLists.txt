cmake_minimum_required(VERSION 2.8.3)
project(dynamic_tutorials)

find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  rospy
  std_msgs
  message_generation
)

generate_dynamic_reconfigure_options(
   cfg/Tutorials.cfg
 )





add_message_files(
    FILES
    Vel.msg
  )


generate_messages(
  DEPENDENCIES
  std_msgs
)


catkin_package(
  
  CATKIN_DEPENDS message_runtime 
  )


add_executable(dynamic_tutorials_server src/server.py)
add_executable(dynamic_tutorials_client src/client.py)
add_dependencies(dynamic_tutorials_server ${PROJECT_NAME}_gencfg)
add_dependencies(dynamic_tutorials_client ${PROJECT_NAME}_gencfg)

set_target_properties(dynamic_tutorials_server PROPERTIES LINKER_LANGUAGE CMAKE_py_LINK_EXECUTABLE)
set_target_properties(dynamic_tutorials_client PROPERTIES LINKER_LANGUAGE CMAKE_py_LINK_EXECUTABLE)

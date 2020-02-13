#!/usr/bin/env python
# -*- coding: ascii -*-

import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from dynamic_reconfigure.server import Server
# from rviz_pose_publisher.cfg import rviz_pose_publisherConfig

vel_command= Twist()



# def dn_callback(config, level):
#     rospy.loginfo("""Reconfigure Request: {int_param}, {double_param},\ 
#           {str_param}, {bool_param}, {size}""".format(**config))
#     return config


def callback(data):
    vel_command.linear.x=data.x
    vel_command.linear.y=data.y
    vel_command.angular.z=data.z
    saturation_x = rospy.get_param('~sat_x')
    saturation_y = rospy.get_param('~sat_y')
    saturation_rot = rospy.get_param('~sat_rot')

    if abs(vel_command.linear.x)>saturation_x:
        vel_command.linear.x=math.copysign(saturation_x, vel_command.linear.x)
    if abs(vel_command.linear.y)>saturation_y:
        vel_command.linear.y=math.copysign(saturation_y, vel_command.linear.y)
    if abs(vel_command.angular.z)>saturation_rot:
        vel_command.angular.z=math.copysign(saturation_rot, vel_command.angular.z)
    # rospy.loginfo('Sat Param is '+str(saturation_rot))

    
if __name__ == '__main__':
    try:
        rospy.init_node('command_publisher')
        rospy.Subscriber("vel_cmd", Point, callback)
        pub = rospy.Publisher('turtle1/cmd_vel', Twist)
        rate = rospy.Rate(10) # 10hz   
        # srv = Server(TutorialsConfig, callback)

        while not rospy.is_shutdown(): 

            pub.publish(vel_command)
            rate.sleep()  
            
    except rospy.ROSInterruptException:
        pass



# def translator():
#     rospy.init_node('turtlesim_to_rviz_translator')
#     rospy.Subscriber("turtle1/pose", Pose, callback)
#     pub = rospy.Publisher('turtlesim_rviz_pose', Pose, queue_size=10)
#     rate = rospy.Rate(10) # 10hz
    
# while not rospy.is_shutdown(): 

#     pub.publish(turtlesim_pose)
#     rate.sleep()
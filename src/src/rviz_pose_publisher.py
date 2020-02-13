#!/usr/bin/env python
# -*- coding: ascii -*-
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from turtlesim.msg import Pose

turtlesim_pose= PoseStamped()

X=0
Y=0
Theta=0

def callback(data):
    turtlesim_pose.header.stamp=rospy.Time.now()
    turtlesim_pose.pose.position.x=data.x
    turtlesim_pose.pose.position.y=data.y
    
    # turtlesim_pose.pose.position.=data.theta
    
# def translator():
#     rospy.init_node('turtlesim_to_rviz_translator')
#     rospy.Subscriber("turtle1/pose", Pose, callback)
#     pub = rospy.Publisher('turtlesim_rviz_pose', Pose, queue_size=10)
#     rate = rospy.Rate(10) # 10hz
        
    # while not rospy.is_shutdown(): 

    #     pub.publish(turtlesim_pose)
    #     rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_to_rviz_translator')
        rospy.Subscriber("turtle1/pose", Pose, callback)
        pub = rospy.Publisher('turtlesim_rviz_pose', PoseStamped, queue_size=10)
        rate = rospy.Rate(10) # 10hz   
        while not rospy.is_shutdown(): 
            pub.publish(turtlesim_pose)
            rate.sleep()  
            
    except rospy.ROSInterruptException:
        pass




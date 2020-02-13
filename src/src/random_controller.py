#!/usr/bin/env python
# -*- coding: ascii -*-

import sys
import rospy
import math
import random

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Turtle(object): 

    def __init__(self):
        
        self.sub=rospy.Subscriber("turtle1/pose", Pose, self.callback)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=0)
        
        self.rate = rospy.Rate(0.1) # hz
        
        self.vel_command= Twist()
        
        self.null_command=Twist()
        self.null_command.angular.z=0
        self.null_command.linear.x=0
        self.pose=Pose() 
        self.yf=5.5
   
    # Predict final Yf
    def sample(self):
        self.vel_command.linear.x=random.uniform(-3,3)
        self.vel_command.angular.z=random.uniform(-3,3)
        self.yf=self.pose.y+self.vel_command.linear.x/self.vel_command.angular.z*(math.cos(self.pose.theta)-math.cos(self.pose.theta+self.vel_command.angular.z))
 
    # Move if predicted yf is below 5.5
    
    def move(self):
        # rospy.loginfo('Vel commands are: %f,%f',vel_command.linear.x,vel_command.angular.z)
        rospy.loginfo('Initial Position is: %f',self.pose.y)
        self.sample()
        while (self.yf>=5):
            self.sample()
        rospy.loginfo('Predicted Position is: %f', self.yf)
        self.pub.publish(self.vel_command)
        rospy.sleep(1)
        self.pub.publish(self.null_command)
        rospy.loginfo('Final position is: %f',self.pose.y)            


    def callback(self,data):
        self.pose=data    

if __name__ == "__main__":
    rospy.init_node('random_command_publisher')   
    try:
        t=Turtle()
    except rospy.ROSInterruptException:
        pass
    while not rospy.is_shutdown():
        t.move()


    

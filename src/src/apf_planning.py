#!/usr/bin/env python3

import sys
import rospy
import math
import random
import time

from matplotlib import pyplot as plt
from matplotlib.patches import Circle

from turtlesim.srv import Spawn
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

vel_command= Twist()
turtle_1_pose=Pose()
turtle_2_pose=Pose()
turtle_3_pose=Pose()

def callback1(data):
    global turtle_1_pose
    turtle_1_pose.x=data.x
    turtle_1_pose.y=data.y
    turtle_1_pose.theta=data.theta
       
def respawn(x, y,theta,name):
    rospy.wait_for_service('/spawn')
    try:
        respawn = rospy.ServiceProxy('/spawn', Spawn)
        resp1 = respawn(x, y,theta,name)
    except rospy.ServiceException:
        print ("Service call failed")   
        
def compute_direction(pose,x,y):
    angle=math.atan2(y-pose.y, x-pose.x)
    return angle
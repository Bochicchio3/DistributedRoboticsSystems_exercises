#!/usr/bin/env python



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


if __name__ == "__main__":
    rospy.init_node('artificial_potential_field')
    rnd=[]
    for i in range(10):
        rnd.append(random.uniform(0,11))
    
    try:
        respawn(rnd[0], rnd[1],rnd[2],'turtle2')
        respawn(rnd[3], rnd[4],rnd[5],'turtle3')
    except:
        Print("Already spawned?")    

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(0.5) # 10hz   
    sub  = rospy.Subscriber("turtle1/pose", Pose, callback1)
    
    x_goal,y_goal=rnd[6:7]
    
    def compute_distance(x,y,x_goal,y_goal):
        return ((y-y_goal)**2+(x-x_goal)**2)**1/2

    
    """list of param"""
    k_goal=1
    k_t=1    
    potential_field_goal=-k_goal*compute_distance(x,y,x_g,y_g)
    potential_field_turtles=1/2*k_t*compute_distance(x,y)**2
        
    while not rospy.is_shutdown():         
            while (abs(turtle_1_pose.theta-compute_direction(turtle_1_pose,goal_x,goal_y))>0.15):
                vel_command.angular.z=1*(-turtle_1_pose.theta+compute_direction(turtle_1_pose,goal_x,goal_y))
                pub1.publish(vel_command)
                print(abs(turtle_1_pose.theta-compute_direction(turtle_1_pose,goal_x,goal_y)))


            while (  (math.sqrt (float((y[i]-turtle_1_pose.y) ** 2+ (x[i]-turtle_1_pose.x) ** 2)))<0.5):
                vel_command.linear.x=float(0.5*(math.sqrt (float((y[i]-turtle_1_pose.y) ** 2+ (x[i]-turtle_1_pose.x) ** 2))))
                vel_command.linear.y=0
                vel_command.angular.z=0 
                pub1.publish(vel_command) 
                time.sleep(0.3)
            vel_command.linear.x=0
            vel_command.linear.y=0
            vel_command.angular.z=0
            pub1.publish(vel_command)




        rate.sleep()  
    
#!/usr/bin/env python
# -*- coding: ascii -*-

import sys
import rospy
import math
import random
import time
import numpy as np

from libraries.pid_controller import TurtleBot
from turtlesim.srv import Spawn
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Turtle(object):
    
    def __init__(self,name):
        
        # Def required messages
        self.name=name
        self.pose=Pose()
        self.vel_command= Twist()

        # Defining Null Command
        self.null_command=Twist()
        self.null_command.angular.z=0
        self.null_command.linear.x=0
        self.angle=0
        
        # Spawn turtle if not already spawned
        try:
            self.respawn(random.uniform(0,11), random.uniform(0,11),0,name)
            
        except: 
            rospy.loginfo("Already Spawned")
            
        self.pub = rospy.Publisher('/'+name+'/cmd_vel', Twist, queue_size=10)

        self.sub = rospy.Subscriber('/'+name+'/pose', Pose, self.callback)
        self.rate = rospy.Rate(1)

        # self.sub_str=rospy.Subscriber("/boh", String, self.action())
       
    def callback(self,data):
        self.pose=data
        # print (data )
        
    def respawn(self,x,y,theta,name):
        rospy.wait_for_service('/spawn')
        try:
            self.respawn = rospy.ServiceProxy('/spawn', Spawn)
            self.resp1 = self.respawn(x, y,theta,name)
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def compute_direction(self,x_bar,y_bar):
        self.angle=math.atan2(y_bar-self.pose.y, x_bar-self.pose.x)
        # print(self.angle)
        return self.angle

    def orient(self,angle):
        
        while (abs(self.pose.theta-angle)>0.01):
            self.vel_command.angular.z=(-self.pose.theta+angle)
            self.pub.publish(self.vel_command)
        self.pub.publish(self.null_command)
    
    def approach(self,x_bar,y_bar):
        self.dist=self.compute_distance(x_bar,y_bar)
        while (self.dist>0.1):
            self.dist=self.compute_distance(x_bar,y_bar)
            print(self.dist)
        # print(math.pow(float(math.pow((y-pose[i].y),2)+math.pow((x-pose[i].x),2)),2),'Distance')
            self.vel_command=self.null_command
            self.vel_command.linear.x=self.dist
            self.pub.publish(self.vel_command)
        # rospy.sleep(0.3)
        self.pub.publish(self.null_command)

    def action(self,x_bar,y_bar):
        print("ACTION")
        angle=self.compute_direction(x_bar,y_bar)
        self.orient(angle)    
        self.approach(x_bar,y_bar)
      
    def compute_distance(self,x_bar,y_bar):
        
        dist= ((self.pose.y-y_bar)**2+(self.pose.x-x_bar)**2)**1/2
        return dist

class Turtle_baricenter():
    def __init__(self, number):
        rospy.init_node('turtlebot_controller')
        self.x_bar=0
        self.y_bar=0
        self.number=number
        self.turtles=[]
        for i in range (0, number):
            t1=Turtle('turtle'+ str(i))
            self.turtles.append(t1)
        self.rate = rospy.Rate(1)
 
    def compute_baricenter(self):
        rospy.wait_for_message('turtle0/pose',Pose)
        rospy.wait_for_message('turtle1/pose',Pose)
        rospy.wait_for_message('turtle2/pose',Pose)
        rospy.wait_for_message('turtle3/pose',Pose)
        
        self.x_bar=0
        self.y_bar=0
        for i in range (0,self.number):
            self.x_bar=self.x_bar+self.turtles[i].pose.x
            self.y_bar=self.y_bar+self.turtles[i].pose.y
            print(self.turtles[i].pose.x,self.turtles[i].pose.y)
        self.x_bar=self.x_bar/4
        self.y_bar=self.y_bar/4
        print("baricenter is:" ,self.x_bar,self.y_bar)

    def action(self):
        while not rospy.is_shutdown():
            for i in range (0,self.number):
                self.compute_baricenter()
                if (self.turtles[0].compute_distance(self.x_bar,self.y_bar)<0.1 and self.turtles[1].compute_distance(self.x_bar,self.y_bar) < 0.1 and self.turtles[2].compute_distance(self.x_bar,self.y_bar)< 0.1 and self.turtles[3].compute_distance(self.x_bar,self.y_bar)< 0.1 ):
                    break   
                self.turtles[i].action(self.x_bar,self.y_bar)
            self.rate.sleep()

# Main function.
if __name__ == '__main__':

    try:
        tt= Turtle_baricenter(4)
        tt.compute_baricenter()
        tt.action()
    except rospy.ROSInterruptException:
        pass
    

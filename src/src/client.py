#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Example Python node to publish on a specific topic."""

# Import required Python code.
import rospy
import math
# Give ourselves the ability to run a dynamic reconfigure server.
from dynamic_reconfigure.server import Server as DynamicReconfigureServer
# Import custom message data and dynamic reconfigure variables.
from dynamic_tutorials.cfg import TutorialsConfig as ConfigType

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point


class FirstExercise(object):
    """Node example class."""

    def __init__(self):
        
        # Initialize the node and name it.
        rospy.init_node('controller')

        # Define custom msg
        self.sat_x = rospy.get_param('~sat_x', 1.0)
        self.sat_rot = rospy.get_param('~sat_rot', 1.0)
        self.vel_command= Twist()

        # Create a dynamic reconfigure server.
        self.server = DynamicReconfigureServer(ConfigType, self.reconfigure_cb)

        # Create a publisher for our custom message.
        self.pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=25)
        self.sub=rospy.Subscriber("vel_cmd", Point, self.callback)


        # Create a timer to go to a callback at a specified interval.
        self.rate=rospy.Rate(10)

    def callback(self, data):
        self.vel_command.linear.x=data.x
        self.vel_command.linear.y=data.y
        self.vel_command.angular.z=data.z

        rospy.loginfo('%d, %d, %d',data.x, data.y, data.z)
        
        if abs(self.vel_command.linear.x)>self.sat_x:
            self.vel_command.linear.x=math.copysign(self.sat_x, self.vel_command.linear.x)
        if abs(self.vel_command.angular.z)>self.sat_rot:
            self.vel_command.angular.z=math.copysign(self.sat_rot, self.vel_command.angular.z)
        # rospy.loginfo('Sat Param is '+str(saturation_rot))
        self.pub.publish(self.vel_command)

    def reconfigure_cb(self, config, dummy):
        """Create a callback function for the dynamic reconfigure server."""
        # Fill in local variables with values received from dynamic reconfigure
        # clients (typically the GUI).
        self.sat_x = config["sat_x"]
        self.sat_rot = config["sat_rot"]
        return config


# Main function.
if __name__ == '__main__':
    # Go to class functions that do all the heavy lifting.
    try:
        FirstExercise()
    except rospy.ROSInterruptException:
        pass
    # Allow ROS to go to all callbacks.
    rospy.spin()
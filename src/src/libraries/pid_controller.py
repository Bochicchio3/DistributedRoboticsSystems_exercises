#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


class TurtleBot:

    def __init__(self):
        rospy.init_node('turtlebot_controller')
        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)
        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(50)
        self.vel_msg=Twist()
        
        
        
    def teleport(self):
        rospy.wait_for_service('/turtle1/teleport_absolute')
        try:
            self.teleport= rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
            self.telep=self.teleport(0,0,0)
        except:
            print ("Service call failed")

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self,path, tolerance):
        """Moves the turtle to the goal."""
        self.goal_pose = Pose()
        for K in path:
            
            # Get the input from the user.
            self.goal_pose.x = K[0]
            self.goal_pose.y = K[1]
            self.distance_tolerance =tolerance
    
            while self.euclidean_distance(self.goal_pose) >= self.distance_tolerance:

                # Linear velocity in the x-axis.
                self.vel_msg.linear.x = self.linear_vel(self.goal_pose)
                self.vel_msg.linear.y = 0
                self.vel_msg.linear.z = 0

                # Angular velocity in the z-axis.
                self.vel_msg.angular.x = 0
                self.vel_msg.angular.y = 0
                self.vel_msg.angular.z = self.angular_vel(self.goal_pose)

                # Publishing our vel_msg
                self.velocity_publisher.publish(self.vel_msg)

                # Publish at the desired rate.
                self.rate.sleep()

            # Stopping our robot after the movement is over.
            self.vel_msg.linear.x = 0
            self.vel_msg.angular.z = 0
            self.velocity_publisher.publish(self.vel_msg)

            # If we press control + C, the node will stop.
        rospy.spin()



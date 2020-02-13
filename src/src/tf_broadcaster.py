#!/usr/bin/env python  
# -*- coding: ascii -*-
import rospy
import tf
import turtlesim.msg

def handle_turtle_pose(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x-5.5, msg.y-5.5, 0),tf.transformations.quaternion_from_euler(0, 0, msg.theta),rospy.Time.now(),'/turtle1',"map")

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    rospy.Subscriber('/turtle1/pose',turtlesim.msg.Pose,handle_turtle_pose)
    rospy.spin()
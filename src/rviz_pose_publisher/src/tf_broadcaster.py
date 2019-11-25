#!/usr/bin/env python  
# -*- coding: ascii -*-

# import roslib
# import rospy
# import tf
# import turtlesim.msg

# def handle_turtle_pose(msg):
#     br = tf.TransformBroadcaster()
#     br.sendTransform((msg.x, msg.y, 0),
#                      tf.transformations.quaternion_from_euler(0, 0, msg.theta),
#                      rospy.Time.now(),
#                      'turtle1',
#                      "map")

# if __name__ == '__main__':
#     rospy.init_node('tf_broadcaster')
#     rospy.Subscriber('/%s/pose' % 'turtle1',turtlesim.msg.Pose,handle_turtle_pose)
#     rospy.spin()


import roslib
# roslib.load_manifest('learning_tf')
import rospy

import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "map")

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()
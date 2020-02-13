#!/usr/bin/env python3

import rospy
import random
import numpy as np
import math
import random
import time
from matplotlib import pyplot as plt
from matplotlib.patches import Circle

from libraries.apf import APF
from libraries.apf import Vector2d
from libraries.pid_controller import TurtleBot

from turtlesim.srv import Spawn
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import TeleportAbsolute


def sample_path():
    k_att, k_rep = 1.0, 100.0
    rr = 3
    step_size, max_iters, goal_threashold = .2, 500, .2 
    step_size_ = 2
    start, goal = (0, 0), (10,10)
    
    rd= 1+8*np.random.rand(12)

    obs = [[rd[0],rd[1]], [rd[2], rd[3]],[rd[4],rd[5]], [rd[6],rd[7]],[rd[8],rd[9]],[rd[10],rd[11]]]

    is_plot=True
    if is_plot:
        fig = plt.figure(figsize=(7, 7))
        subplot = fig.add_subplot(111)
        subplot.set_xlabel('X-distance: m')
        subplot.set_ylabel('Y-distance: m')
        subplot.plot(start[0], start[1], '*r')
        subplot.plot(goal[0], goal[1], '*r')
        
    if is_plot:
        for OB in obs:
            circle = Circle(xy=(OB[0], OB[1]), radius=rr, alpha=0.3)
            subplot.add_patch(circle)
            subplot.plot(OB[0], OB[1], 'xk')
        
    apf = APF(start, goal, obs, k_att, k_rep, rr, step_size, max_iters, goal_threashold, is_plot)
    apf.path_plan()
    if apf.is_path_plan_success:
        path = apf.path
        path_ = []
        i = int(step_size_ / step_size)
        while (i < len(path)):
            path_.append(path[i])
            i += int(step_size_ / step_size)

        if path_[-1] != path[-1]: 
            path_.append(path[-1])
        
        # for K in path:
        #     # print (K)
            
        if is_plot:
            px, py = [K[0] for K in path_], [K[1] for K in path_] 
            subplot.plot(px, py, '^k')
            plt.show()
    else:
        print('path plan failed')
        return sample_path()
    
    return path

# Main function.
if __name__ == '__main__':
    
    path= sample_path()
    try:
        tt=TurtleBot()
        tt.teleport()
        tt.move2goal(path,0.1)
    except rospy.ROSInterruptException:
        pass
#!/usr/bin/env python
import copy
from os import wait
from shutil import move 
import sys
import rospy
import moveit_commander
import geometry_msgs.msg
import moveit_msgs.msg
from std_msgs.msg import Int8
from math import pi

class trajectory :
    def __init__(self):
        #setup commander
        moveit_commander.roscpp_initialize(sys.argv)

        #setup scene for robot
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander('manipulator')
        
        #configuration setup
        self.group.set_goal_position_tolerance(0.05)

        #self.group.set_planner_id('RRTConnectkConfigDefault')

        self.group.set_planning_time(5)
        self.group.set_num_planning_attempts(5)

        #applying ready status
        self.status = 0
        
        scale =1

        waypoints = []

        wpose = self.group.get_current_pose().pose
        print(wpose.position.z)
        wpose.position.z -= scale * 0.5  # First move up (z)
    
        waypoints.append(copy.deepcopy(wpose))

        # wpose.position.y -= scale * 0.1  # Third move sideways (y)
        # waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0,
        # ignoring the check for infeasible jumps in joint space, which is sufficient
        # for this tutorial.
        (plan, fraction) = self.group.compute_cartesian_path(
            waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
        )  

       
        self.group.execute(plan, wait=True)


if __name__=='__main__':
    rospy.init_node('Trajecory_UR3')
    scale = 1
    trajectory ()
    
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
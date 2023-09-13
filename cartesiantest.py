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

scale = 1.0

import sys
import moveit_commander
from geometry_msgs.msg import Pose, Point, Quaternion

def main():
    # Initialize MoveIt
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    
    # Get user input for coordinates
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    z = float(input("Enter z coordinate: "))
    
    # Get user input for orientation (quaternion)
    qx = float(input("Enter quaternion x: "))
    qy = float(input("Enter quaternion y: "))
    qz = float(input("Enter quaternion z: "))
    qw = float(input("Enter quaternion w: "))
    
    # Create goal pose from user input
    goal_pose = geometry_msgs.msg.Pose()
    goal_pose.position.x = x
    goal_pose.position.y = y
    goal_pose.position.z = z
    goal_pose.orientation.x = qx
    goal_pose.orientation.y = qx
    goal_pose.orientation.z = qx
    goal_pose.orientation.w = qx
    
    # Set the goal pose as the target
    move_group.set_pose_target(goal_pose)

    # Plan and execute the motion
    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()

    # Clean up
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    main()  
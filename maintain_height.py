from ast import parse
import time
from sys import excepthook
import rospy
from std_msgs.msg import Int32
import serial
import copy
import sys
import rospy
import moveit_commander
from math import pi



def z_down(z_coor) :
    print(z_coor)
    # Setup commander
    moveit_commander.roscpp_initialize(sys.argv)
    # Setup scene for robot
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander('manipulator')
    # Configuration setup
    group.set_goal_position_tolerance(0.05)
    group.set_planning_time(5)
    group.set_num_planning_attempts(5)

    # Applying ready status
    status = 0
    waypoints = []
    wpose = group.get_current_pose().pose
    #move z backwards

    wpose.position.z = 0.214285714  # Move along Z axis
    waypoints.append(copy.deepcopy(wpose))
    (plan, fraction) = group.compute_cartesian_path(
        waypoints, 0.01, 0.0  # Waypoints to follow, eef_step
    )
    group.execute(plan, wait=True)
    group.stop()
    group.clear_pose_targets()
    quit()
    time.sleep(10)
    pass

def z_up(z_coor):
    print(z_coor)
    # Setup commander
    moveit_commander.roscpp_initialize(sys.argv)
    # Setup scene for robot
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander('manipulator')
    # Configuration setup
    group.set_goal_position_tolerance(0.05)
    group.set_planning_time(5)
    group.set_num_planning_attempts(5)


    # Applying ready status
    status = 0
    waypoints = []
    wpose = group.get_current_pose().pose
    #move z backwards

    wpose.position.z = 0.214285714  # Move along Z axis
    waypoints.append(copy.deepcopy(wpose))
    (plan, fraction) = group.compute_cartesian_path(
        waypoints, 0.01, 0.0  # Waypoints to follow, eef_step
    )
    group.execute(plan, wait=True)
    group.stop()
    group.clear_pose_targets()
    quit()
    time.sleep(10)
    pass 

def callback(data):
     x = data.data
     z_coor = (data.data/70)*0.5
     if x <=35 and x >=25:
            return
     elif x >=35:
          z_down(z_coor) 
          time.sleep(3)
          pass
     elif x <=25:
          z_up(z_coor)
          time.sleep(3)
          pass

def listener():
       rospy.init_node('height_control',anonymous =True)
   
       rospy.Subscriber("ultradata", Int32, callback)
   
       # spin() simply keeps python from exiting until this node is stopped
       rospy.spin()

if __name__ == '__main__':
    while not rospy.is_shutdown():
        listener()
        try:
            rospy.spin()
        except rospy.ROSInterruptException:
            pass

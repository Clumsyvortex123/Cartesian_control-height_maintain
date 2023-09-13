import copy
import sys
import rospy
import moveit_commander
from math import pi

class trajectory:
    def __init__(self):
        # Setup commander
        moveit_commander.roscpp_initialize(sys.argv)

        # Setup scene for robot
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander('manipulator')

        # Configuration setup
        self.group.set_goal_position_tolerance(0.05)
        self.group.set_planning_time(5)
        self.group.set_num_planning_attempts(5)

        # Applying ready status
        self.status = 0

        # Get user input for the axis, direction, and magnitude
        axis = input("Enter the axis to move along (X/Y/Z): ").upper()
        direction = input("Enter the direction (F for forward, B for backward): ").upper()
        magnitude = float(input("Enter the magnitude of movement: "))

        if axis not in ('X', 'Y', 'Z') or direction not in ('F', 'B') or magnitude <= 0:
            print("Invalid input. Please enter a valid axis (X, Y, Z), direction (F/B), and positive magnitude.")
            return

        scale = 1

        waypoints = []

        wpose = self.group.get_current_pose().pose

        if axis == 'X':
            if direction == 'F':
                wpose.position.x += scale * magnitude  # Move along X axis
            else:
                wpose.position.x -= scale * magnitude  # Move along X axis
        elif axis == 'Y':
            if direction == 'F':
                wpose.position.y += scale * magnitude  # Move along Y axis
            else:
                wpose.position.y -= scale * magnitude  # Move along Y axis
        elif axis == 'Z':
            if direction == 'F':
                wpose.position.z += scale * magnitude  # Move along Z axis
            else:
                wpose.position.z -= scale * magnitude  # Move along Z axis

        waypoints.append(copy.deepcopy(wpose))

        (plan, fraction) = self.group.compute_cartesian_path(
            waypoints, 0.01, 0.0  # Waypoints to follow, eef_step
        )

        self.group.execute(plan, wait=True)

if __name__ == '__main__':
    rospy.init_node('MnuaL_controlxyz')
    while True:

        trajectory()

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

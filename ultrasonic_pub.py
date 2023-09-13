from sys import excepthook
import rospy
from std_msgs.msg import Int32  # Import Int32 message type
import serial

ser = serial.Serial('/dev/ttyACM0', 57600)

def talker():
    pub = rospy.Publisher('ultradata', Int32, queue_size=10)  # Use Int32 message type
    rospy.init_node('ultra1', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            data = int(ser.readline().decode().strip())  # Convert the data to an integer
            rospy.loginfo(data)
            pub.publish(data)
        except ValueError:
            rospy.logwarn("Invalid data received from serial port")
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

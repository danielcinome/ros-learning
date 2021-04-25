#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import re


def publisher_msg_memory():
    rospy.init_node('pub_memory', anonymous=True)
    pub = rospy.Publisher('pub_msg_memory', Float64, queue_size=1000)
    hz = rospy.Rate(1) #1Hz
    msg = Float64(0.0)
    while not rospy.is_shutdown():
        get_free_memory(msg)
        rospy.loginfo("Sending free memory value: %f", msg.data)
        pub.publish(msg)
        hz.sleep()


def get_free_memory(msg):
    with open('/proc/meminfo') as fp:
        fp.readline()
        line = fp.readline()
        msg_line = re.split('[\t| ]+', line)
        msg.data = long(msg_line[1]) / 1024.0 # from kilobyte to megabyte


if __name__ == '__main__':
    try:
        publisher_msg_memory()
    except rospy.ROSInterruptException:
        pass
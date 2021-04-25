#!/usr/bin/env python
# Create Second subscriber
import rospy
from std_msgs.msg import Float64
import re


def name(msg):
    rospy.loginfo('This message of second subscriber %f', msg.data)

def subscriber2():
    rospy.init_node('subscriber2', anonymous=True)
    rospy.Subscriber('memory', Float64, name)
    rospy.spin()

if __name__ == '__main__':
    subscriber2()
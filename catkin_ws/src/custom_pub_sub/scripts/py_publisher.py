import rospy
from custom_pub_sub.msg import Memory
import re

def custom_msg():
    rospy.init_node('publisher_custom', anonymous=True)
    pub = rospy.Publisher('memory', Memory, queue_size=1000)
    rate = rospy.Rate(1)
    msg = Memory()
    counter = 0

    while not rospy.is_shutdown():
        msg.header.seq = counter
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = 0
        get_msg(msg)
        rospy.loginfo("Sending memory message of time: %d.%d", msg.header.stamp.secs, msg.header.stamp.nsecs)
        pub.publish(msg)
        rate.sleep()
        counter += 1

def get_msg(msg):
    with open('/proc/meminfo') as fp:
        str_line = fp.readline()
        msg.total.data = get_data(str_line) / 1024.0
        str_line = fp.readline()
        msg.available.data = get_data(str_line) / 1024.0
        str_line = fp.readline()
        msg.free.data = get_data(str_line) / 1024.0
        str_line = fp.readline()
        msg.buffer.data = get_data(str_line)

def get_data(str_line):
    str = re.split('[\t| ]+', str_line)
    return number = long(str[1])




if __name__ == '__main__':
    try:
        custom_msg()
    except rospy.ROSInterruptException:
        pass
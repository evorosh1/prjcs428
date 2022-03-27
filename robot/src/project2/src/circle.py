#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def main():
    pub = rospy.Publisher('simple_create/cmd_vel', Twist, queue_size=10)
    rospy.init_node('circler', anonymous=True)

    rate = rospy.Rate(2) # 2hz
    msg = Twist()
    msg.linear.x = 0
    msg.angular.y = 6

    while not rospy.is_shutdown():
        msg.linear.x += .4
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

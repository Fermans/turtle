#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class ROS:

    def move(self):
    # Starts a new node
        rospy.init_node('robot_cleaner', anonymous=True)
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        vel_msg = Twist()

    
    #Receiveing the user's input
        print("Let's move your robot")

        PI = 3.1415926535897


        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = PI

        self.velocity_publisher.publish(vel_msg)


        vel_msg = Twist()
        # vel_msg.angular.z = 1
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        # Testing our function
        x = ROS()
        x.move()
    except rospy.ROSInterruptException:
        pass
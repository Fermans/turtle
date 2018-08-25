#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class turtlesim_move:


    # rosservice call
    def move_ros(self):

        rospy.init_node('turtlesim_moveros', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        vel_msg = Twist()
        Pi = 3.141592657

        angular_z = [1,0,-2,0,-1.5,-2,0,2,0,1,0,1.6,0,-1.6,0]
        linear_x = [0,2,0,2,2,0,2,0,2,2,2,2,2,2,2]
        # time = [3.14,2.5,0.8,2,3.5,1.75,1.715,0.45,1,6.35,1.65,1.85,0.25,1.9,0.75]
        distance = []
        angle = []
        i = 0

        while i <len(angular_z):
            # vel_msg.angular.z = angular_z[i]
            # vel_msg.linear.x = linear_x[i]
            t0 = rospy.Time.now().to_sec()
            t1 = rospy.Time.now().to_sec()
            current_distance = (t1-t0)*linear_x
            current_angle = (t1-t0)*angular_z
            # print(t1-t0)
            while (t1 - t0) < time[i]:
                vel_msg.angular.z = angular_z[i]
                vel_msg.linear.x = linear_x[i]
                self.velocity_publisher.publish(vel_msg)
                t1 = rospy.Time.now().to_sec()
            print(vel_msg.)

            i = i + 1
        vel_msg = Twist()

        self.velocity_publisher.publish(vel_msg)

if __name__ == '__main__':

    try:
        x = turtlesim_move()
        x.move_ros()

    except rospy.ROSInterruptException:
        pass
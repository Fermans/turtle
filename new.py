#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class TurtleBot:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(1000)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def straight2goal(self):

        goal_pose = Pose()
        goal_pose.x = input("Set your x goal: ")
        goal_pose.y = input("Set your y goal: ")
        distance_tolerance = input("Set your tolerance: ")

        current_angle = input("radius after the last run")
        print(current_angle)

        vel_msg = Twist()
        PI = 3.1415926535897
        print(self.pose.x,self.pose.y)
        print(goal_pose.x,goal_pose.y)

        Ky = goal_pose.y - self.pose.y
        Kx = goal_pose.x - self.pose.x
        K = Ky / Kx

        if (goal_pose.x >= self.pose.x)and(goal_pose.y >= self.pose.y):
            Angle = math.atan(K)
            # print(Angle)
            vel_msg.angular.z = Angle/1
            vel_msg.angular.y = 0
            vel_msg.angular.x = 0
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            # print(self.pose.angular_velocity)


        elif (goal_pose.x < self.pose.x)and(goal_pose.y >= self.pose.y):
            Angle = PI + math.atan(K) - current_angle
            print(PI)
            print(math.atan(K))
            print(current_angle)
            vel_msg.angular.z = Angle / 1
            vel_msg.angular.y = 0
            vel_msg.angular.x = 0
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            # print(self.pose.angular_velocity)

        self.velocity_publisher.publish(vel_msg)

        # print(vel_msg.angular.z)
        time.sleep(1)
        # print(self.pose.angular_velocity)

        vel_msg.linear.x = 1
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.z = 0
        vel_msg.angular.y = 0
        vel_msg.angular.x = 0

        # current_distance = 0
        distance = self.euclidean_distance(goal_pose)
        current_distance = distance
        t0 = rospy.Time.now().to_sec()
        # print(distance)
        while current_distance > distance_tolerance:
            self.velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = distance - 1 * (t1 - t0)
        # print(self.pose.angular_velocity)
        # print(goal_pose.angular_velocity)
            # print(current_distance)
        # print(vel_msg.linear.x)
        # len(Posex)

        # self.velocity_publisher.publish(vel_msg)
        vel_msg = Twist()
        self.velocity_publisher.publish(vel_msg)
        print(Angle)
        print(self.pose.x,self.pose.y)


if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.straight2goal()

    except rospy.ROSInterruptException:
        pass
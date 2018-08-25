#!/usr/bin/env python
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

    def linear_vel(self, goal_pose, constant=1.5):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)


    def move2goal(self):
        i = 0
        for pose1 in Posex:
            goal_pose.x = pose1
            goal_pose.y = Posey[i]
            i = i + 1

            vel_msg = Twist()

            while self.euclidean_distance(goal_pose) >= distance_tolerance:

                # Porportional controller.
                # https://en.wikipedia.org/wiki/Proportional_control

                # Linear velocity in the x-axis.
                vel_msg.linear.x = self.linear_vel(goal_pose)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                # Angular velocity in the z-axis.
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel(goal_pose)

                # Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)

                # Publish at the desired rate.
                # self.rate.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        # If we press control + C, the node will stop.
        # rospy.spin()

    def straight2goal(self):
        vel_msg = Twist()
        PI = 3.1415926535897
        print(self.pose.x,self.pose.y)

        Ky = goal_pose.y - self.pose.y
        Kx = goal_pose.x - self.pose.x
        K = Ky / Kx
        # if K > 0:

        Angle = math.atan(K)
        # print(Angle)
        vel_msg.angular.z = Angle/1
        vel_msg.angular.y = 0
        vel_msg.angular.x = 0
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        self.velocity_publisher.publish(vel_msg)
        # print(vel_msg.angular.z)
        time.sleep(1)

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
        print(distance)
        while current_distance > distance_tolerance:
            self.velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = distance - 1 * (t1 - t0)
            print(current_distance)
        # print(vel_msg.linear.x)
        # len(Posex)

        # self.velocity_publisher.publish(vel_msg)
        vel_msg = Twist()
        self.velocity_publisher.publish(vel_msg)



if __name__ == '__main__':
    try:
        x = TurtleBot()

        goal_pose = Pose()
        i = 0
        # Get the input from the user.
        Posex = list(range(input("Set your x goal: ")))
        Posey = list(range(input("Set your y goal: ")))
        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        distance_tolerance = input("Set your tolerance: ")

        if int(input('Straight?')) == 1:
            x.straight2goal()
        else:
            x.move2goal()

    except rospy.ROSInterruptException:
        pass
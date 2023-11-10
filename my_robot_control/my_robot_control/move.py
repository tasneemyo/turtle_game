import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Bool
import math

class Turtle_GTG(Node):
    def __init__(self):
        super().__init__("Go_to_Goal_Node")
        self.flag=False
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.publisher=self.create_publisher( Bool,"kill_topic",10)
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.subscription=self.create_subscription(Pose,'pos_topic',self.listener,10)
        self.pose = Pose()
        self.goal=Pose()
    def pose_callback(self, data):
        self.pose = data
    def listener(self,msg:Pose):
        self.goal=msg
        self.timer = self.create_timer(0.1, self.go_to_goal)

    def go_to_goal(self):
        goal = Pose()
        goal=self.goal
        msg=Bool()
        self.flag=False
        new_vel = Twist()

        distance_to_goal = math.sqrt( (goal.x - self.pose.x)**2  + (goal.y - self.pose.y)**2 )
        
        angle_to_goal =math.atan2(goal.y - self.pose.y , goal.x - self.pose.x)

        distance_tolerance = 0.1
        angle_tolerance = 0.01

        angle_error = angle_to_goal - self.pose.theta
        kp = 10

        if abs(angle_error) > angle_tolerance:
            new_vel.angular.z = kp * angle_error
        else :
            if( distance_to_goal ) >= distance_tolerance:
                new_vel.linear.x = kp * distance_to_goal
            else :
                new_vel.linear.x= 0.0
                self.flag=True
                
        msg.data=self.flag
        self.publisher.publish(msg)

        self.cmd_vel_pub.publish(new_vel)


def main(args=None):
    rclpy.init(args=args)
    node= Turtle_GTG()
    rclpy.spin(node)
    rclpy.shutdown()





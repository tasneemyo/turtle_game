#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from random import Random
import math
class PoseSub(Node):
    def __init__(self):
        super().__init__("pose_sub")
        name1="turtle1" 
        position1='/'+name1+'/pose'
        name2='turtle2'#recieved from random
        position2='/'+name2+'/pose'
        self.x1=0
        self.x2=0
        self.y1=0
        self.y2=0


        self.pose_subscriber_=self.create_subscription(Pose,position1,self.pose_callback1,10)
        self.pose_subscriber_=self.create_subscription(Pose,position2,self.pose_callback2,10)
        self.timer = self.create_timer( 1.0, self.calculate_distance)
    def pose_callback1(self,msg:Pose):
        # self.get_logger().info("one")
        # self.get_logger().info(str(msg))
        self.x1=msg.x
        self.y1=msg.y
    def pose_callback2(self,msg:Pose):
        # self.get_logger().info(str(msg))
        self.x2=msg.x
        self.y2=msg.y
    def calculate_distance(self):
        distance = math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)
        self.get_logger().info(str(distance))
        if distance<1.0:
            self.get_logger().info("attack")
        else :
            pass


def main(args=None):
    
    rclpy.init(args=args)
    node=PoseSub()
    rclpy.spin(node)
    rclpy.shutdown()
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import random
from functools import partial
from std_msgs.msg import String
class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.get_logger().info("ggg")
        self.subscription=self.create_subscription(String,'new_topic',self.listeners,10)
      
    def listeners(self,msg):
        self.get_logger().info("here")
        self.get_logger().info(str(msg.data))
def main(args=None):
    rclpy.init(args=args)
    node=Listener()
    # node.get_logger().info(node.name())
    rclpy.spin(node)
    rclpy.shutdown()
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        
        self.publisher=self.create_publisher(String,'new_topic',10)
        
        self.timer=self.create_timer(0.5,self.timer_call_back)
        self.count=0
    def timer_call_back(self):
        msg=String()
        msg.data=str(self.count)
        self.publisher.publish(msg)
        self.count+=1
        self.get_logger().info(f"pub {msg.data}")
def main(args=None):
    rclpy.init(args=args)
    node=Talker()
    # node.get_logger().info(node.name())
    rclpy.spin(node)
    rclpy.shutdown()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        #self.get_logger().info("Hello tasneemo")
        self.counter=0
        self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):

        self.get_logger().info(f"Message : {self.counter}")
        self.counter+=1





def main (args=None):
    rclpy.init(args=None)
    node=MyNode()
    rclpy.spin(node)

    rclpy.shutdown() #destroys the node and shutdown the communication



if __name__=="__main__":
  
    main()
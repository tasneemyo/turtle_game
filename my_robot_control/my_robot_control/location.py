#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from turtlesim.srv import Spawn
import random
from functools import partial
class Location(Node):
    def __init__ (self):
        super().__init__("location")
        self.get_logger().info("fff")
        self.timer = self.create_timer( 3.0, self.call_set_pen)
 
    def call_set_pen(self):
        self.get_logger().info("here")
        client=self.create_client(Spawn,"/spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for service")
        request =Spawn.Request()
        #x=random.randint(0,11)
        x=random.uniform(0.0,11.0)
        #y=random.randint(0,11)
        y=random.uniform(0.0,11.0)
        
        request.x=float(x)
        request.y=float(y)
        request.theta=0.2
        #request.name="ff"
        
        future=client.call_async(request)
        #self.get_logger().info(request)
        
        future.add_done_callback(partial(self.call_back_set_pen))
        self.get_logger().info("lll")
    def call_back_set_pen(self,future):
        try:
            
            response =future.result()
           
           
            #self.get_logger().info(str(response))
            
        except Exception as e:
            self.get_logger().error("Service failed : %r" %(e,))



def main(args=None):
    rclpy.init(args=args)
    node=Location()
    # node.get_logger().info(node.name())
    rclpy.spin(node)
    rclpy.shutdown()
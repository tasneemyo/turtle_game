#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from turtlesim.srv import Kill

from functools import partial
from std_msgs.msg import Bool,String
class Killer(Node):
    def __init__ (self):
        super().__init__("kill")
        self.flag=False
        self.count=3
        self.subscription1=self.create_subscription(Bool,'kill_topic',self.listener,10)
    def listener(self,msg:Bool):
        if msg.data:
            self.publisher=self.create_publisher(Bool,"random_topic",10)
            name=String()
            name.data="turtle"+str(self.count)
            self.call_set_kill(name)
            self.count+=1


    def call_set_kill(self,msg:String):
        
        client=self.create_client(Kill,"/kill")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for service")

        request=Kill.Request()
        request.name=msg.data
        future=client.call_async(request)
        self.flag=False
        
        future.add_done_callback(partial(self.call_back_set_kill))
       
    def call_back_set_kill(self,future):
        try:
            
            response =future.result()
            self.flag=True
        except Exception as e:
            self.get_logger().error("Service failed : %r" %(e,))
        msg=Bool()
        msg.data=self.flag
        self.publisher.publish(msg)




def main(args=None):
    rclpy.init(args=args)
    node=Killer()
 
    rclpy.spin(node)
    rclpy.shutdown()


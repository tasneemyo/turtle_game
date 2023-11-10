#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
import random
from functools import partial
from std_msgs.msg import String,Bool
class Random(Node):
    def __init__ (self):
        super().__init__("random")
        me=Bool()
        self.publisher1=self.create_publisher(Pose,"pos_topic",10)
        self.call_set_spawn(me)
        
        self.subscriber=self.create_subscription(Bool,"random_topic",self.subscribe,10)
        self.count=0
        
        
    
    def subscribe(self,msg:Bool):
        
        if msg.data:
            
            self.call_set_spawn(msg)

    def call_set_spawn(self,msg):
        self.count+=1
        client=self.create_client(Spawn,"/spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for service")
        request =Spawn.Request()
        
        x=random.uniform(0.0,11.0)
        
        y=random.uniform(0.0,11.0)
        theta=random.uniform(-2.0,2.0)
        request.x=float(x)
        request.y=float(y)
        request.theta=theta 
        pose=Pose()
        pose.x=request.x
        pose.y=request.y
        pose.theta=theta
       
            
        self.publisher1.publish(pose)
        future=client.call_async(request) #-->send to controller
        future.add_done_callback(partial(self.call_back_set_spawn))
    def call_back_set_spawn(self,future):
        try:
            
            response =future.result()
        except Exception as e:
            self.get_logger().error("Service failed : %r" %(e,))


    




def main(args=None):
    rclpy.init(args=args)
    node=Random()
    rclpy.spin(node)
    rclpy.shutdown()


   

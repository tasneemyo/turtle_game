#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

from functools import partial
class turtle(Node):
    def __init__(self) :
        super().__init__("turtle_control")
        self.previousx=0
        self.cmd_vel_pub_=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.pose_subscriber=self.create_subscription(Pose,'/turtle1/pose',self.call_back,10)
        self.get_logger().info("TURTLE")
    def call_back(self,pose:Pose):
        cmd=Twist()
        if pose.x>=9.0 or pose.x<=2.0 or pose.y>=9.0 or pose.y<=2.0 :
          cmd.linear.x=  1.0
          cmd.angular.z=0.9 #<--
        else:

            cmd.linear.x=2.0
            cmd.angular.z=0.0
        self.cmd_vel_pub_.publish(cmd)
        if pose.x>5.5 and self.previousx<=5.5: 
            self.previousx=pose.x  #<--
            self.get_logger().info("Red")
            self.call_set_pen(255,0,0,5,0)
        elif pose.x<=5.5 and self.previousx>5.5: 
            self.previousx=pose.x
            self.get_logger().info("Blue")
            self.call_set_pen(0,0,255,5,0)

    def call_set_pen(self,r,g,b,width,off):
        client=self.create_client(SetPen,"/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for service")
        request =SetPen.Request()
        request.r=r
        request.g=g
        request.b=b
        request.off=off
        request.width=width
        future=client.call_async(request)
        future.add_done_callback(partial(self.call_back_set_pen))
    def call_back_set_pen(self,future):
        try:
            response =future.result()
        except Exception as e:
            self.get_logger().error("Service failed : %r" %(e,))

def main(args=None):
    rclpy.init(args=args)
    node =turtle()
    rclpy.spin(node)
    rclpy.shutdown()

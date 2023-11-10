#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist,Pose

class DrawCircle(Node):
    def __init__ (self):
        super().__init__("draw_circle")
        self.cmd_vel_pub_=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        #self.pose_subscriber=self.create_subscription(Pose,'/turtle1/pose',self.distance,10)

        self.get_logger().info("Draw circle !!")
        self.x=0
        self.y=0
        self.pose_subscriber_=self.create_subscription(Pose,'/turtle1/pose',self.pose_callback1,10)
    def pose_callback1(self,msg:Pose):
        # self.get_logger().info("one")
        # self.get_logger().info(str(msg))
        self.x1=msg.x
        self.y1=msg.y
    def distance(self,position:Pose):
        cmd=Twist()
        cmd.linear.x=2.0
        cmd.angular.z=1.0
        self.x=position.x
        self.y=position.y

        if self.x<=1.0 and self.x>=2:
            if self.y<=1.0 and self.y>=2:
                self.get_logger().info("Attack")
        self.cmd_vel_pub_.publish(cmd)





def main(args=None):
    rclpy.init(args=args)
    node=DrawCircle()
    rclpy.spin(node)
    rclpy.shutdown()
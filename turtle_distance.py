#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import math

class TurtleDistanceNode(Node):

    def __init__(self):
        super().__init__("turtle_distance")
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.publisher_ = self.create_publisher(Float32, "/turtle1/distance_from_origin", 10 )
    def pose_callback(self, msg):
        distance_from_origin = math.sqrt(msg.x ** 2 + msg.y ** 2)

        distance_from_origin_ = Float32()
        distance_from_origin_.data = distance_from_origin

        self.publisher_.publish(distance_from_origin_)

        self.get_logger().info(f"Pose heard - x: {msg.x:.2f}, y: {msg.y:.2f}, distance of the turtle from origin is:{distance_from_origin:.2f}")

    
        

def main(args=None):
    rclpy.init(args=args)
    node = TurtleDistanceNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()





































#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HardwareStatusPublisherNode(Node):
    def __init__(self):
        super().__init__("hardware_status_publisher") 
        self.hw_status_pub_ = self.create_publisher(HardwareStatus, "hardware_status", 10)
        self.timer_ = self.create_timer(1.0, self.publish_hardware_status)
        self.get_logger().info("Hardware Status Publisher Node has been started.")


    def publish_hardware_status(self):
        msg = HardwareStatus()
        msg.temperature = 43.7  # Example temperature
        msg.are_motors_ready = True  # Example motor readiness status
        msg.debug_message = "Nothing Special"  # Example debug message
        self.hw_status_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()